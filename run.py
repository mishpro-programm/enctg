import os
print("\033[33mУстановка зависимостей...")
os.popen("pip install -r requirements.txt")
print("\033[33mЗависимости установлены. Запуск скрипта.\nСейчас вам потребуется ввести свой номер и код.\033[0m")
os.system("cd dist; python3 main.py")
