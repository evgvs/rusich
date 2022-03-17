from localizer import localize_EN_to_RU

f = open("content", "r")
t = f.read()
s = open("content", "w")
s.write(localize_EN_to_RU(t))