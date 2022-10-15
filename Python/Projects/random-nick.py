import random


def generate_name():
    name = ['Berat','Akif','Albert',]
    last_name = ['Laçinkaya','Karakuş','Einstein']
    print('İsminiz: ',random.choice(name),' Soy İsminiz: ',random.choice(last_name))


generate_name()