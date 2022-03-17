from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode
from random import randint

import os

def help(request, markov, normalhelp):
    answ = ""
    for line in normalhelp.split("\n"):
        if ((request in line.split("—")[0]) and (request[-1] == " ")) or (((request + " ") in line.split("—")[0]) and (request[-1] != " ")):
            answ += line + "\n"
    if answ != "":
        return answ
    else:
        m = markov(max_length=randint(10, 130), reply_to=request, reply_mode=ReplyMode.END)
        if (len(m) < len(request) + 5):
            return markov(max_length=randint(10, 130))
        return m