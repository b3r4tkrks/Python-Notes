import os
import colorama 
from colorama import Fore,Style,Back


while True:
    try:
        print(Fore.RED + Style.BRIGHT)
        print(Fore.RED + Style.BRIGHT)
        print('''

         /$$      /$$   /$$    /$$$$$$   /$$$$$$   /$$$$$$ 
        | $$$    /$$$ /$$$$   /$$$_  $$ /$$$_  $$ /$$$_  $$
        | $$$$  /$$$$|_  $$  | $$$$\ $$| $$$$\ $$| $$$$\ $$
        | $$ $$/$$ $$  | $$  | $$ $$ $$| $$ $$ $$| $$ $$ $$
        | $$  $$$| $$  | $$  | $$\ $$$$| $$\ $$$$| $$\ $$$$
        | $$\  $ | $$  | $$  | $$ \ $$$| $$ \ $$$| $$ \ $$$
        | $$ \/  | $$ /$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$/
        |__/     |__/|______/ \______/  \______/  \______/ 

        PYTHON KÜTÜPHANE İNDİRİCİ by m1000

''')
        login = input('Hangi Kütüphaneyi İndirmek İstersiniz (Büyük Küçük Harf Duyarlı Değildir!!!) ? :  ')
        print('Kütüphane İndiriliyor...')
        os.system('pip install ' + str(login))
    except:
           print('Sanırım Bir Hata Oluştu Lütfen Yazdığınız Kütüphanenin Var Olup Olmadığını Kontrol Edin Veya Pythonı Silip Tekrar Yükleyin Yüklerken PATH a Ekleyi Seçin')
           





