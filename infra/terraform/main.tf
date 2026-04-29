provider "aws" {
  region = var.aws_region
}

# Шукаємо останню версію чистої Ubuntu 22.04
data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
  owners = ["099720109477"] # Canonical
}

# Створюємо файрвол
resource "aws_security_group" "web_sg" {
  name        = "web_sg_lab"
  description = "Allow SSH and HTTP"

  # Відкриваємо порт 22 для доступу через термінал (за потреби)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Відкриваємо порт 8000 для вашого веб-інтерфейсу
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Дозволяємо серверу виходити в Інтернет (щоб він міг скачати Docker і ваш код)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Створюємо сам сервер (віртуальну машину)
resource "aws_instance" "web_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.micro" # Безкоштовний рівень
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  # Передаємо наш скрипт налаштування!
  user_data              = file("cloud-init.yaml")

  tags = {
    Name = "OpenData-Docker-VM"
  }
}