import os
print("\e[0;35mУстановка зависимостей...")
os.popen("pip install -r requirements.txt")
print("\e[0;35mЗависимости установлены. Запуск скрипта.\nСейчас вам потребуется ввести свой номер и код.\e[0;0m")
os.system("cd dist; python3 main.py")
