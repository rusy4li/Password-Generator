# -*- coding:utf-8 -*-
# Hoşgeldiniz Bu Program rusy4 Adlı GitHub Kullanıcısı Tarafından Kodlanmıştır!
# Password-Generator V1
import time
import string
from random import *

print("""================================
##############################
#    Password Generator      #
#                            #
#   ===[ Rusy4 ]===          #
##############################
=================================""")


def parolaolusturucu():
    olustur = (string.ascii_letters + string.punctuation + string.digits)
    parola = "".join(choice(olustur) for x in range(randint(15, 31)))
    return parola


print("""
#NOT:
------------------------------------------------------------------------------
Selam dostum bu tool'u sadece size özgü ve güçlü şifre oluştursun diye yaptım!
------------------------------------------------------------------------------""")

a = 0
s = int(input("Kaç tane parola oluşturmak istiyorsunuz: "))
while a < s:
    print(parolaolusturucu())
    a += 1
    continue

for i in range(100):
    time.sleep(100)
    print("")
