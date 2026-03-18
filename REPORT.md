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