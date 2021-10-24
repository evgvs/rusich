#!/usr/bin/env python3

from random import randint
from time import sleep
from pathlib import Path
import time
import datetime
import urllib.request
import xml.etree.ElementTree as ET
import os
import psutil
import subprocess
from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode
import loading
version = '1.4.8.8'
import sys
import localizer
import helper
import warnings
import getpass
import glob

engine = "vtsoft"
from pygments.lexers import BashLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter

f = open(os.path.expanduser('~') + '/.rysich_history', "w+")
f.write("")
promptsession = PromptSession(history=FileHistory((os.path.expanduser('~') + '/.rysich_history')))


warnings.simplefilter(action='ignore', category=FutureWarning)
ANSI_COLOR_RED      = "\x1b[31m"
ANSI_COLOR_GREEN    = "\x1b[32m"
ANSI_COLOR_YELLOW   = "\x1b[33m"
ANSI_COLOR_BLUE     = "\x1b[34m"
ANSI_COLOR_MAGENTA  = "\x1b[35m"
ANSI_COLOR_CYAN     = "\x1b[36m"
ANSI_COLOR_RESET    = "\x1b[0m"

ANSI_COLOR_BOLD     = "\x1b[1m"
ANSI_COLOR_DIM      = "\x1b[2m"
ANSI_COLOR_UNDERLINE= "\x1b[4m"
ANSI_COLOR_REVERSE  = "\x1b[7m"

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

doleep = True
try:
    if sys.argv[1] == "--под_спидами":
        doleep = False
except:
    pass

def sleepsex(tme):
    if doleep:
        sleep(tme)
def splash(count):
    if doleep:
        loading.splash(count)
os.system("clear")



print("УМНАЯ КОМАНДНАЯ ОБОЛОЧКА \"РУСИЧ\" АО \"В. Т. СОФТ\"")
print(" ")
splash(1)
os.system('clear')

print(f"{ANSI_COLOR_BOLD}УМНАЯ КОМАНДНАЯ ОБОЛОЧКА \"РУСИЧ\" АО \"В. Т. СОФТ\"{ANSI_COLOR_RESET}")
print("Инициализация 1С:Предприятие 9 для оболочки коммандного интерпретатора \"РУСИЧ\"...")
splash(4)
os.system('clear')

markov = MarkovText()
markov = MarkovText.from_file(os.path.dirname(os.path.realpath(__file__)) + "/markov.json")
f = open(os.path.dirname(os.path.realpath(__file__)) + "/help.txt", "r")
normalhelp = f.read() 



print(f"{ANSI_COLOR_BOLD}УМНАЯ КОМАНДНАЯ ОБОЛОЧКА \"РУСИЧ\" АО \"В. Т. СОФТ\"{ANSI_COLOR_RESET}")
print("Проверка лицензии на коммандный интерпретатор \"РУСИЧ\" в ипостаси \"РАБОЧАЯ ЭЛЕКТРОННО-ВЫЧИСЛИТЕЛЬНАЯ СТАНЦИЯ\"...")
splash(4)
os.system('clear')



print(f"{ANSI_COLOR_BOLD}УМНАЯ КОМАНДНАЯ ОБОЛОЧКА \"РУСИЧ\" АО \"В. Т. СОФТ\"{ANSI_COLOR_RESET}")
print("Получаю актуальную информацию о курсах валют...")

date_CBR = time.time()
byn="ОШИБКА"
kit="ОШИБКА"
try:
    assert doleep == True
    contents = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?", timeout=6).read()
    tree = ET.fromstring(contents)
    byn=tree[4][4].text
    kit=tree[16][4].text
except:
    byn="ОШИБКА"
    kit="ОШИБКА"

splash(3)
os.system('clear')


fls2 = ["ЗАДАТЬ-ДВИГАТЕЛЬ-ПЕРЕВОДА", "ИНТЕРАКТИВНЫЙ-СПРАВОЧНИК"]
for e in os.environ["PATH"].split(":"):
    fls1 = glob.glob(e + "/*")
    for fi in fls1:
        fls2.append(localizer.localize_EN_to_RU(fi.split("/")[-1]))
completer = WordCompleter(list(set(fls2)))

if not doleep:
    print(f"{ANSI_COLOR_DIM}Русич объебошился клеем, занюхал дорожку, наелся таблеток - ебанутый на голову, самый прикольный среди шеллов. Будте аккуратны с этим режимом.{ANSI_COLOR_RESET}")

print(f"{ANSI_COLOR_BOLD}УМНАЯ КОМАНДНАЯ ОБОЛОЧКА \"РУСИЧ\" АО \"В. Т. СОФТ\" ВЕРСИЯ {ANSI_COLOR_GREEN}{version}{ANSI_COLOR_RESET}")
splash(1)
print(f"РЕЖИМ ЛОКАЛИЗАЦИИ [{ANSI_COLOR_GREEN}ГООГЛЕ{ANSI_COLOR_RESET}]")
splash(1)
print("Напечатайте ИНТЕРАКТИВНЫЙ-СПРАВОЧНИК дабы перейти в режим получения справочной информации про команды ДЖНЮ/Линюкс")
splash(1)
print("\r ", end="")

f = open(os.path.dirname(os.path.realpath(__file__)) + "/motds.txt", "r")
motd = f.read()
motd = motd.split("===\n")
motd1 = motd[randint(0, len(motd)-1)]
print(f"\n{motd1}")

splash(2)
print("\r", end="")
def parse(inputstr):
    out = []
    buf = ""
    inbr = False
    for letter in inputstr:
        if letter == " " and not inbr:
            out.append(localizer.localize_RU_to_EN(buf))
            buf = ""
        elif letter == "'" and not inbr:
            inbr = True
        elif letter == "'" and inbr:
            inbr = False
            out.append(buf)
            buf = ""
        else:
            buf = buf + letter
    out.append(localizer.localize_RU_to_EN(buf))
    for elem in out:
        if elem == "":
            out.remove(elem)    
    return out

def fetchval(date_CBR):
    if time.time() - date_CBR > 1000:
        try:
            assert doleep == True
            contents = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?", timeout=6).read()
            tree = ET.fromstring(contents)
            byn=tree[4][4].text
            kit=tree[16][4].text
        except:
            byn="0"
            kit="0"

        date_CBR = time.time()

while True:
    try:
        fetchval(date_CBR)


        print(f"ТЕКУЩЕЕ МЕСТОПОЛОЖЕНИЕ: {ANSI_COLOR_YELLOW}" + localizer.localize_EN_to_RU(os.getcwd()) + 
        f"{ANSI_COLOR_RESET} | ОПЕРАТИВНОЙ ПАМЯТИ ИСПОЛЬЗОВАНО: " + str(psutil.virtual_memory().percent) + "%")
        if byn != "ОШИБКА" and kit != "ОШИБКА":
            print("Грошы братняга народа (BYN): " + byn + " Российских Рублей " + 
            "| 兄弟人民的货币 (CNY): " + kit + " Российских Рублей")

        print("Госдолг США: " + str(calculateDebt()) + f" долларов")





        rplt=promptsession.prompt("[" + localizer.localize_EN_to_RU(engine) + "] РУСИЧ (" + localizer.localize_EN_to_RU(getpass.getuser()) + ") =>> ", lexer=PygmentsLexer(BashLexer), auto_suggest=AutoSuggestFromHistory(), completer=completer) 






        argv = parse(rplt)
        #if argv[0] == localizer.localize_RU_to_EN(""):
        #print(argv)
        if argv[0] == localizer.localize_RU_to_EN("ЗАДАТЬ-ДВИГАТЕЛЬ-ПЕРЕВОДА"):
            if argv[1] == "google":
                
                try:
                    localizer.localize_EN_to_RU("test", "google")
                    print(f"{ANSI_COLOR_DIM}Двигателем перевода установлен гугле.{ANSI_COLOR_RESET}")
                except Exception as E:
                    print(f"{ANSI_COLOR_RED}Двигателем перевода не удалось установить гугле. Учтите, что для работы с Гугле нужен высокоскоростной доступ к широкополосному подключению к глобальной сети \"Интернет\". Ошибка: " + localizer.localize_EN_to_RU(str(E)) + f"{ANSI_COLOR_RESET}")
                
                engine = "google"
            elif argv[1] == "vtsoft":
                print(f"{ANSI_COLOR_DIM}Двигателем перевода установлен переводчик АО В. Т. СОФТ.{ANSI_COLOR_RESET}")
                engine = "vtsoft"
            else:
                print(f"{ANSI_COLOR_RED}УКАЗАННЫЙ ДВИГАТЕЛЬ ПЕРЕВОДА НЕ ЭКЗИСТЕНЦИИРУЕТ В ДАННОМ КОМПЛЕКТЕ ПОСТАВКИ РУСИЧ{ANSI_COLOR_RESET}")
            continue
        if argv[0] == "cd":
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

        if argv[0] == localizer.localize_RU_to_EN("ИНТЕРАКТИВНЫЙ-СПРАВОЧНИК"):
            print(f"{ANSI_COLOR_YELLOW}Вызываю справочную службу села Бухалово, Ярославская область...{ANSI_COLOR_RESET}")
            splash(randint(3,7))
            print(f"{ANSI_COLOR_GREEN}Село Бухалово на связи. Напечатайте 'СПАСИБО, МУДРЕЦ, ПРОЩАЙ!' для отключения.{ANSI_COLOR_RESET}")
            while True:
                rplt = prompt(f"РУСИЧ {ANSI_COLOR_GREEN}СПРАШИВАЕТ У МУДРЕЦА{ANSI_COLOR_RESET} =>? ")
                if rplt == "'СПАСИБО, МУДРЕЦ, ПРОЩАЙ!'":
                    print(f"{ANSI_COLOR_RED}БЕЗ КАВЫЧЕК БЛЯТЬ{ANSI_COLOR_RESET}")
                elif rplt == "СПАСИБО, МУДРЕЦ, ПРОЩАЙ!":
                    print(f"{ANSI_COLOR_YELLOW}Связь разорвана.{ANSI_COLOR_RESET}")
                    break
                else:
                    splash(randint(1,3))
                    print(helper.help(rplt, markov, normalhelp))
            continue
        
        
        
        try:
            process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if engine == "google":
                buf = ""
                for c in iter(lambda: process.stdout.read(1), b''): 
                    try:
                        a = str(c.decode("utf-8"))
                        if a != "\0" and a != "\n" and a != "\r" and a != "\b" and a != "\a":
                            buf += str(c.decode("utf-8"))
                        if str(c.decode("utf-8")) == '\n':
                            print(localizer.localize_EN_to_RU(str(buf), engine), end="\n")
                            buf = ""
                    except:
                        pass
            else:
                for c in iter(lambda: process.stdout.read(1), b''): 
                    print(localizer.localize_EN_to_RU(str(c.decode("utf-8")), engine), end="")
            
        except FileNotFoundError:
            print(f"{ANSI_COLOR_RED}{ANSI_COLOR_RED}КОМАНДА НЕ ЭКЗИСТЕНЦИРУЕТ НА ВАШЕМ ЗАПОМИНАЮЩЕМ УСТРОЙСТВЕ{ANSI_COLOR_RESET}")
        except Exception as E:
            print(f"{ANSI_COLOR_RED}{ANSI_COLOR_RED}ВО ВРЕМЯ ЭКЗЕКУЦИИ ПРОГРАММЫ ПРОИЗОШЛА КРИТИЧЕСКАЯ ОШИБКА{ANSI_COLOR_RESET}")
            print(E)
    except Exception as ex:
        print(f"{ANSI_COLOR_RED}{ANSI_COLOR_BOLD}ПРОИЗОШЛА ФАТАЛЬНАЯ ОШИБКА, ДЛЯ КОТОРОЙ НЕ СУЩЕСТВУЕТ ПОВЕДЕНИЙ СТАБИЛИЗАЦИИ: {localizer.localize_EN_to_RU(repr(ex))}{ANSI_COLOR_RESET}")

   