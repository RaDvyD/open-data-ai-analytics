У ході виконання роботи було створено локальний Git-репозиторій open-data-ai-analytics. 
Налаштовано структуру папок для проєкту та файл .gitignore.
Було відпрацьовано створення feature-гілок, їх злиття у гілку main (у тому числі з використанням прапорця --no-ff). 
Штучно створено та успішно розв'язано merge-конфлікт у файлі README.md. 
Проєкту присвоєно початковий тег v0.1.0.


* f861e56 (HEAD -> main, tag: v0.1.0) docs: add CHANGELOG for v0.1.0
* 5e023b4 (feature/visualization) feat: add visual data analysis script
* 12ae15e fix: resolve merge conflict in README.md
|\  
| * 13a6761 (conflict-b) docs: update README from branch B
* | cc66f1c (conflict-a) docs: update README from branch A
|/  
* e28c03d Merge: додано код для аналізу даних та побудови базових моделей
|\  
| * b4c7bcd (feature/data_research) feat: add research logic and modeling
|/  
* b822850 Merge: додано скрипт для перевірки якості даних на пропуски та дублікати
|\  
| * 427ac58 (feature/data_quality_analysis) feat: add data quality checks
|/  
* cf80cce (feature/data_load) feat: add script to load data
* b8bc01f docs: add project description and hypotheses
* 5731b8d chore: add project structure and .gitignore

# Звіт з лабораторної роботи №2 (DevOps)
**Тема:** Побудова CI/CD конвеєрів за допомогою GitHub Actions
**Виконав:** Семенов Олександр Володимирович, Національний університет «Львівська політехніка»

## Частина A — CI для кожного модуля
1. У директорії `.github/workflows/` створено файл конфігурації `ci.yml`.
2. **Тригери запуску:** - Автоматично при `push` та `pull_request` у гілку `main`.
   - Вручну через `workflow_dispatch` з можливістю вибору конкретного модуля (`load_data`, `data_quality`, `research`, `visualize`) або запуск усіх одразу.
3. **Паралелізм:** Використано стратегію `matrix`, що дозволяє запускати всі модулі проєкту одночасно на різних віртуальних машинах GitHub (ubuntu-latest).
4. **Кроки виконання:** Встановлення Python 3.12, запуск скриптів та логування виводу у файли.

## Частина B — CD/Публікація результатів
1. Налаштовано автоматичне завантаження результатів роботи (логів виконання) як **GitHub Actions Artifacts**.
2. Після кожного успішного прогону в розділі "Summary" доступні для завантаження 4 архіви (по одному на кожен модуль), що містять звіти про виконання.

## Частина C — Self-hosted runner (локальний агент)
1. На власному ПК підключено та активовано локальний агент (Self-hosted runner).
2. Створено workflow `ci-selfhosted.yml`, який використовує тег `runs-on: self-hosted` для виконання модуля візуалізації локально.

### Порівняння ранерів:

| Критерій | GitHub-hosted (Cloud) | Self-hosted (Local Mac) |
| :--- | :--- | :--- |
| **Швидкість** | Витрачається час на ініціалізацію ВМ (Spin-up). | Майже миттєвий запуск, оскільки середовище вже готове. |
| **Доступ до ресурсів** | Обмежений ізольованою ВМ. | Прямий доступ до локального диска та великих датасетів без копіювання. |
| **Ризики** | Обмеження безкоштовних хвилин. | Потреба в самостійній підтримці стабільності та ризики безпеки локальної системи. |

## Посилання на репозиторій з виконаним CI:
[https://github.com/RaDvyD/open-data-ai-analytics](https://github.com/RaDvyD/open-data-ai-analytics)