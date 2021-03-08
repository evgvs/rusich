from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode
from random import randint
from time import sleep
import time
import datetime
import urllib.request
import xml.etree.ElementTree as ET
markov = MarkovText()
import os
import psutil
import subprocess
version = '1.4.8.7'

ANSI_COLOR_RED      = "\x1b[31m"
ANSI_COLOR_GREEN    = "\x1b[32m"
ANSI_COLOR_YELLOW   = "\x1b[33m"
ANSI_COLOR_BLUE     = "\x1b[34m"
ANSI_COLOR_MAGENTA  = "\x1b[35m"
ANSI_COLOR_CYAN     = "\x1b[36m"
ANSI_COLOR_RESET    = "\x1b[0m"
ANSI_COLOR_UNDERLINE= "\x1b[4m"
ANSI_COLOR_BOLD     = "\x1b[1m"
pendos = ["a","b","c","d","e","f","g" ,"h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w" ,"x" ,"y","z","A","B","C","D","E","F" ,"G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W" ,"X" ,"Y","Z"]
rusacok =["а","б","ц","д","е","ф","дж","х","и","й","к","л","м","н","о","п","к","р","с","т","ю","в","вь","кс","ы","з","А","Б","Ц","Д","Е","Ф","ДЖ","Х","И","Й","К","Л","М","Н","О","П","К","Р","С","Т","Ю","В","ВЬ","КС","Ы","З"]
def localize_EN_to_RU(text):
    for i in range(len(pendos)):
        text = text.replace(pendos[i], rusacok[i])
    return text

def localize_RU_to_EN(text):
    for i in range(len(pendos)):
        text = text.replace(rusacok[i], pendos[i])
    text = text.replace("ч", "ch")
    text = text.replace("ш", "csh")
    text = text.replace("щ", "tcsh")
    text = text.replace("ж", "g")

    text = text.replace("Ч", "CH")
    text = text.replace("Ш", "CSH")
    text = text.replace("Щ", "TCSH")
    text = text.replace("Ж", "G")

    return text
    
def calculateDebt():
    startYear=2020
    startMonth=11
    startDay=19
    baseDebt=27248063291167
    perSecondDebt=42635
    today = time.mktime(datetime.datetime.today().timetuple())
    togda = time.mktime(datetime.date(startYear, startMonth, startDay).timetuple())

    secs = today - togda
    curdeb=(secs*perSecondDebt)+baseDebt

    return curdeb

os.system("clear")

print("УМНАЯ КОМАНДНАЯ ОБОЛОЧКА \"РУСИЧ\" АО \"В. Т. СОФТ\"")
sleep(randint(1,3)/2)
print(f"Версия{ANSI_COLOR_GREEN} {version} {ANSI_COLOR_RESET}является крайней, спасибо за своевременную установку обновлений лицензионного программного обеспечения АО \"В. Т. СОФТ\" - официального партнера Фирмы \"1C\"")
sleep(randint(1,3)/3)
print("Начинаю инициализацию 1С:Предприятие 8 для оболочки коммандного интерпретатора \"РУСИЧ\"...")
sleep(randint(4,9)/3)
print(f"{ANSI_COLOR_GREEN}Успешно!{ANSI_COLOR_RESET}")
print("Коммандный интерпретатор \"РУСИЧ\" в ипостаси \"РАБОЧАЯ ЭЛЕКТРОННО-ВЫЧИСЛИТЕЛЬНАЯ СТАНЦИЯ\" не поддерживает некоторые возможности. В случае появления затруднений в его работе, обратитесь к системному администратору предприятия.")
print(f"РЕЖИМ ЛОКАЛИЗАЦИИ [{ANSI_COLOR_GREEN}ВКЛЮЧЕНО{ANSI_COLOR_RESET}]")

print("Напечатайте ИНТЕРАКТИВНЫЙ-СПРАВОЧНИК дабы перейти в режим получения справочной информации про команды ЖНЮ/Линюкс")

with open('content') as fp:
    markov.data(fp.read())

contents = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?").read()
tree = ET.fromstring(contents)
date_CBR = time.time()

markov.save('markov.json')
while True:
    if time.time() - date_CBR > 1000:
        contents = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?").read()
        tree = ET.fromstring(contents)
        date_CBR = time.time()

    print(f"ТЕКУЩЕЕ МЕСТОПОЛОЖЕНИЕ: {ANSI_COLOR_YELLOW}" + localize_EN_to_RU(os.getcwd()) + 
    f"{ANSI_COLOR_RESET} | ОПЕРАТИВНОЙ ПАМЯТИ ИСПОЛЬЗОВАНО: " + str(psutil.virtual_memory().percent) + "%" + 
    "\nГрошы братняга народа: " + tree[4][4].text + " Российских Рублей " + 
    "| 兄弟人民的货币: " + tree[16][4].text + " Российских Рублей" + 
    f"\n{ANSI_COLOR_BOLD}Госдолг США: " + str(calculateDebt()) + f" долларов{ANSI_COLOR_BOLD}" 
    "\nРУСИЧ =>> ", end="")
    rplt = localize_RU_to_EN(input())
    
    #print("Примечание - переведенная строка: " + rplt)
    argv = rplt.split(" ")
    if argv[0] == "cd":
        print(f"{ANSI_COLOR_RED}КОМАНДА ЦД - ПЛОД АМЕРИКАНСКОГО ИМПЕРИАЛИЗМА, ИСПОЛЬЗУЙТЕ КОМАНДУ СМЕНИТЬ-ТЕКУЩУЮ-ДИРЕКТОРИЮ{ANSI_COLOR_RESET}")
        continue

    if argv[0] == localize_RU_to_EN("СМЕНИТЬ-ТЕКУЩУЮ-ДИРЕКТОРИЮ"):
        try:
            os.chdir(argv[1])
        except:
            print(f"{ANSI_COLOR_RED}УКАЗАННАЯ ВАМИ ДИРЕКТОРИЯ НЕ ЭКЗИСТЕНЦИРУЕТ НА ВАШЕМ ЗАПОМИНАЮЩЕМ УСТРОЙСТВЕ{ANSI_COLOR_RESET}")
        continue

    if argv[0] == localize_RU_to_EN("ИНТЕРАКТИВНЫЙ-СПРАВОЧНИК"):
        print(f"{ANSI_COLOR_YELLOW}Вызываю справочную службу села Бухалово, Ярославская область...{ANSI_COLOR_RESET}")
        sleep(randint(4,16)|4)
        print(f"{ANSI_COLOR_GREEN}Село Бухалово на связи. Напечатайте 'СПАСИБО, МУДРЕЦ, ПРОЩАЙ!' для отключения.{ANSI_COLOR_RESET}")
        while True:
            print(f"РУСИЧ {ANSI_COLOR_GREEN}СПРАШИВАЕТ У МУДРЕЦА{ANSI_COLOR_RESET} =>? ", end="")
            rplt = input()
            if rplt == "'СПАСИБО, МУДРЕЦ, ПРОЩАЙ!'":
                print(f"{ANSI_COLOR_RED}БЕЗ КАВЫЧЕК БЛЯТЬ{ANSI_COLOR_RESET}")
            elif rplt == "СПАСИБО, МУДРЕЦ, ПРОЩАЙ!":
                print(f"{ANSI_COLOR_YELLOW}Связь разорвана.{ANSI_COLOR_RESET}")
                break
            else:
                print(markov(max_length=randint(10, 30), reply_to=rplt, reply_mode=ReplyMode))
        continue


    try:
        out = subprocess.check_output(argv).decode("utf-8")
        ruout = ""
        for line in out.split("\n"):
            ruout += localize_EN_to_RU(line) + "\n"
        ruout = ruout[:-2]
        print(ruout)
    except FileNotFoundError:
        print(f"{ANSI_COLOR_RED}КОМАНДА НЕ ЭКЗИСТЕНЦИРУЕТ НА ВАШЕМ ЗАПОМИНАЮЩЕМ УСТРОЙСТВЕ{ANSI_COLOR_RESET}")
    except:
        print(f"{ANSI_COLOR_RED}ВО ВРЕМЯ ЭКЗЕКУЦИИ ПРОГРАММЫ ПРОИЗОШЛА КРИТИЧЕСКАЯ ОШИБКА{ANSI_COLOR_RESET}")
    