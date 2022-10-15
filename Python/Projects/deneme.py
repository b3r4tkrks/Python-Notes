import os
import colorama
from colorama import Fore,Back,Style

print(Fore.GREEN)
print(Style.BRIGHT)
print(Back.BLACK)

login = input('Bilgisayarınız Kaç Saniye içinde Kapansın İstersiniz : ')


os.system(f'shutdown -s -f -t {int(login)}')
