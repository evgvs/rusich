#!/usr/bin/env python3
from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode
from random import randint
from time import sleep
from pathlib import Path
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
    text = text.replace("оо", "у")
    return text

def localize_RU_to_EN(text):
    for i in range(len(pendos)):
        text = text.replace(rusacok[i], pendos[i])
    text = text.replace("ч", "ch")
    text = text.replace("я", "ja")
    text = text.replace("ш", "csh")
    text = text.replace("щ", "tcsh")
    text = text.replace("ж", "g")
    text = text.replace("Г", "gh")

    text = text.replace("Ч", "CH")
    text = text.replace("Я", "JA")
    text = text.replace("Ш", "CSH")
    text = text.replace("Щ", "TCSH")
    text = text.replace("Ж", "G")
    text = text.replace("Г", "GH")
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

    return int(curdeb)




os.system("clear")

print("УМНАЯ КОМАНДНАЯ ОБОЛОЧКА \"РУСИЧ\" АО \"В. Т. СОФТ\"")
sleep(randint(1,3)/2.9)
print(f"Версия{ANSI_COLOR_GREEN} {version} {ANSI_COLOR_RESET}является крайней, спасибо за своевременную установку обновлений лицензионного программного обеспечения АО \"В. Т. СОФТ\" - официального партнера Фирмы \"1C\"")
sleep(randint(1,3)/3.9)
print("Начинаю инициализацию 1С:Предприятие 8 для оболочки коммандного интерпретатора \"РУСИЧ\"...")
sleep(randint(4,9)/4.7)
print(f"{ANSI_COLOR_GREEN}Успешно!{ANSI_COLOR_RESET}")
print("Коммандный интерпретатор \"РУСИЧ\" в ипостаси \"РАБОЧАЯ ЭЛЕКТРОННО-ВЫЧИСЛИТЕЛЬНАЯ СТАНЦИЯ\" не поддерживает некоторые возможности. В случае появления затруднений в его работе, обратитесь к системному администратору предприятия.")
print(f"РЕЖИМ ЛОКАЛИЗАЦИИ [{ANSI_COLOR_GREEN}ВКЛЮЧЕНО{ANSI_COLOR_RESET}]")
markov = MarkovText.from_file(os.path.dirname(os.path.realpath(__file__)) + "/markov.json")
print("Напечатайте ИНТЕРАКТИВНЫЙ-СПРАВОЧНИК дабы перейти в режим получения справочной информации про команды ДЖНЮ/Линюкс")
print("Получаю актуальную информацию о курсах валют...")
date_CBR = time.time()
byn="0"
kit="0"
try:
    contents = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?", timeout=6).read()
    tree = ET.fromstring(contents)
    byn=tree[4][4].text
    kit=tree[16][4].text
except:
    byn="0"
    kit="0"

def parse(inputstr):
    out = []
    buf = ""
    inbr = False
    for letter in inputstr:
        if letter == " " and not inbr:
            out.append(localize_RU_to_EN(buf))
            buf = ""
        elif letter == "'" and not inbr:
            inbr = True
        elif letter == "'" and inbr:
            inbr = False
            out.append(buf)
            buf = ""
        else:
            buf = buf + letter
    out.append(localize_RU_to_EN(buf))
    for elem in out:
        if elem == "":
            out.remove(elem)    
    return out

def fetchval(date_CBR):
    if time.time() - date_CBR > 1000:
        try:
            contents = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?", timeout=6).read()
            tree = ET.fromstring(contents)
            byn=tree[4][4].text
            kit=tree[16][4].text
        except:
            byn="0"
            kit="0"

        date_CBR = time.time()


markov.save('markov.json')
while True:
    try:
        fetchval(date_CBR)

        print(f"ТЕКУЩЕЕ МЕСТОПОЛОЖЕНИЕ: {ANSI_COLOR_YELLOW}" + localize_EN_to_RU(os.getcwd()) + 
        f"{ANSI_COLOR_RESET} | ОПЕРАТИВНОЙ ПАМЯТИ ИСПОЛЬЗОВАНО: " + str(psutil.virtual_memory().percent) + "%" + 
        "\nГрошы братняга народа: " + byn + " Российских Рублей " + 
        "| 兄弟人民的货币: " + kit + " Российских Рублей" + 
        f"\nГосдолг США: " + str(calculateDebt()) + f" долларов" 
        "\nРУСИЧ =>> ", end="")
        rplt = input()
        argv = parse(rplt)
        if argv[0] == "cd":
            print(f"{ANSI_COLOR_RED}КОМАНДА ЦД - ПЛОД АМЕРИКАНСКОГО ИМПЕРИАЛИЗМА, ИСПОЛЬЗУЙТЕ КОМАНДУ \"стд\"{ANSI_COLOR_RESET}")
            continue

        if argv[0] == localize_RU_to_EN("стд"):
            try:
                if '/' == argv[1][0]:
                    os.chdir(argv[1])
                elif '..' in argv[1]:
                    path = Path(os.getcwd())
                    os.chdir(path.parent)
                else:
                    os.chdir(os.getcwd() + "/" + argv[1])
            except:
                print(f"{ANSI_COLOR_RED}УКАЗАННАЯ ВАМИ ДИРЕКТОРИЯ НЕ ЭКЗИСТЕНЦИРУЕТ НА ВАШЕМ ЗАПОМИНАЮЩЕМ УСТРОЙСТВЕ{ANSI_COLOR_RESET}")
            continue

        if argv[0] == localize_RU_to_EN("ИНТЕРАКТИВНЫЙ-СПРАВОЧНИК"):
            print(f"{ANSI_COLOR_YELLOW}Вызываю справочную службу села Бухалово, Ярославская область...{ANSI_COLOR_RESET}")
            sleep(randint(4,16)|12)
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
    except Exception as ex:
        print(f"{ANSI_COLOR_RED}ПРОИЗОШЛА ФАТАЛЬНАЯ ОШИБКА, ДЛЯ КОТОРОЙ НЕ СУЩЕСТВУЕТ ПОВЕДЕНИЙ СТАБИЛИЗАЦИИ: {ex}{ANSI_COLOR_RESET}")