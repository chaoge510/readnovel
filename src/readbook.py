import pyttsx3


f = open("/Users/leon/Downloads/novel.txt")
try:
    for lin in f:
        pyttsx3.speak(lin)
finally:
    f.close()