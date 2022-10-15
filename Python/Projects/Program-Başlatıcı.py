import os
import colorama
from colorama import Fore,Back,Style


print(Fore.RED)
login = input('''Hoşgeldiniz , Berat Karakuş Çalıştırmak İstediğiniz Program Nedir (1:Firefox),(2:Chrome),(3:Discord):  ''')
print(Fore.GREEN)


if login == '1':
    print(Fore.LIGHTBLACK_EX)
    print('Firefox Çalıştırılıyor...')
    os.startfile('firefox.exe')
    print(Fore.LIGHTGREEN_EX)
    print('Firefox Çalıştırıldı.')
elif login == '2':
    print(Fore.LIGHTBLACK_EX)
    print('Chrome Çalıştırılıyor...')
    os.startfile('chrome.exe')
    print(Fore.LIGHTGREEN_EX)
    print('Chrome Çalıştırıldı.')

elif login ==  '3':
    print(Fore.LIGHTBLACK_EX)
    print('Discord Çalıştırılıyor')
    os.startfile('discord.exe')
    print(Fore.LIGHTGREEN_EX)
    print('Discord Çalıştırıldı')




