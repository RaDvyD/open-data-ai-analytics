output "public_ip" {
  value       = aws_instance.web_server.public_ip
  description = "Публічна IP-адреса сервера"
}

output "website_url" {
  value       = "http://${aws_instance.web_server.public_ip}:8000"
  description = "Готове посилання на ваш веб-інтерфейс"
}