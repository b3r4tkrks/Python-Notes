import os
import random
import string
import colorama
from colorama import Fore,Style,Back


login = input('''Hoşgeldiniz Yapmak İstediğiniz İşlemi Seçiniz;
                 (1):Random Sayı Oyunu
                 (2):İstediğin Süre İçinde Biligsayarı Kapatma
                 (3):Random İsim Soyisim Eşleştirme
                 (4):Framework (Kütüphane) İndirici
                 (5):Program Başlatıcı (Bilgisayarında Olan Programalardan İstediğini Başlatmaya Yarar
                 (6):Taş, Kağıt, Makas Oyunu 
                 (7):Random Password (Rastgele Şifre Koyma)
                 ''')


def sayı_tahmin():
    sayı = random.randint(1,50)
    hak =  input('Kaç Hakkınız Olsun İstersiniz : ')
    while hak > 0:
        hak - 1
        tahmin = input('Tahmininiz Nedir?')
        if int(tahmin) == sayı:
            print(f'Helal Olsun {hak}. da Bildin')







