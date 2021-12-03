# -*- coding:utf-8 -*-
# Hoşgeldiniz Bu Program rusy4 Adlı GitHub Kullanıcısı Tarafından Kodlanmıştır!
# Password-Generator V1
import time
import string
from random import *
import os

print("""------------------------------------------------
=#######################=
=#                     #=
=#  Password Generator #=
=#                     #=
=#   ={ Rusy4 }=       #=
=#                     #=
=#######################=
------------------------------------------------""")


def parolaolusturucu():
    olustur = (string.ascii_letters + string.punctuation + string.digits)
    parola = "".join(choice(olustur) for x in range(randint(15, 31)))
    return parola


print("""
#NOT:
------------------------------------------------------------------------------
Selam dostum bu tool'u sadece size özgü ve güçlü şifre oluştursun diye yaptım!
------------------------------------------------------------------------------""")


print("Wordlistmi oluşturmak istiyorsun [E],[H]")
sorgu = input("->> ")

if "E" == sorgu:
    a = 0
    s = int(input("Kaç tane parola oluşturmak istiyorsunuz: "))
    os.remove("words.txt")
    while a < s:

        file = open("words.txt", "a", encoding='utf-8')
        file.write(parolaolusturucu() + "\n")
        file.close()
        a += 1
        continue
    print("Şifre Şu Dizine words.txt Olarak Kaydedildi!")
    print("words dosyasını açmak istermisiniz [E],[H]")
    sorbakam = str(input("->> "))
    if "E" in sorbakam:
        os.startfile("words.txt")
        time.sleep(3)
        os.system(exit())
    else:
        os.system(exit())

elif "H" == sorgu:
    s = int(input("Kaç tane parola oluşturmak istiyorsunuz: "))
    a = 0
    while a < s:
        print(parolaolusturucu())
        a += 1
        continue
    for i in range(100):
        time.sleep(100)
    print("")
else:
    print("[E]= evet,[H]= hayır")
