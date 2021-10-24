pendos = ["a","b","c","d","e","f","g" ,"h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w" ,"x" ,"y","z","A","B","C","D","E","F" ,"G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W" ,"X" ,"Y","Z"]
rusacok =["а","б","ц","д","е","ф","дж","х","и","й","к","л","м","н","о","п","к","р","с","т","ю","в","вь","кс","ы","з","А","Б","Ц","Д","Е","Ф","ДЖ","Х","И","Й","К","Л","М","Н","О","П","К","Р","С","Т","Ю","В","ВЬ","КС","Ы","З"]

rusacok1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я',     'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',   'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я']

pendos1  = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'gh', 'z', 'iy', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch','sh','tcsh', '', 'y', '', 'e', 'u', 'ja', 'A', 'B', 'V', 'G','D', 'E', 'E', 'GH', 'Z', 'I', 'IY','K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'H', 'C', 'CH','SH','TSCH', '', 'Y',  '', 'E', 'U','JA']



def localize_EN_to_RU(text, mode="vtsoft"):
    if mode == "vtsoft":
        text = text.replace("oo", "у")
        text = text.replace("ch", "ч")
        text = text.replace("ja", "я")
        text = text.replace("sh", "ш")
        text = text.replace("csh", "щ")
        text = text.replace("g", "г")
        text = text.replace("gh", "Ж")

        text = text.replace("CH", "Ч")
        text = text.replace("JA", "Я")
        text = text.replace("SH", "Ш")
        text = text.replace("TCSH", "Щ")
        text = text.replace("G", "Г")
        text = text.replace("GH", "Ж")
        text = text.replace("OO", "У")
        for i in range(len(pendos)):
            text = text.replace(pendos[i], rusacok[i])

        return text
    elif mode == "google":

        from googletrans import Translator
        translator = Translator()
        return localize_EN_to_RU(translator.translate(text, src='en', dest='ru').text)


def localize_RU_to_EN(text):
    text = text.replace("OO", "Ы")
    text = text.replace("oo", "ы")
    for i in range(len(pendos)):
        text = text.replace(rusacok1[i], pendos1[i])
    return text