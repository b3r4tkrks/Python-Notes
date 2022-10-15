# İlk Örnek
def hello():
    print("Merhaba")


# Fonksiyon Çağırma
hello() # Merhaba



# Fonksiyona Parametre Göndermek
def hello(name):
    print("Merhaba "+ name)

hello("Berat") # Merhaba Arda


# Fonksiyondan Geriye Bilgi Göndermek
def hello(name):
    return "Merhaba "+ name

print(hello("Arda")) # Merhaba Arda


# Fonksiyondan Geriye Bilgi Göndermek Örnek : 2
def toplama(a,b):
    return False

sonuc = toplama(10,20)
print(sonuc) # 30




# Fonksiyondan Fonksiyon Çağırma

def yasHesapla(dogumYili): # Fonksiyon
    return 2019 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageCinar, ageAda, ageSena)

def EmekliligeKacYilKaldi(int(dogumYili), isim):    # Fonksiyon 2
    yas = yasHesapla(dogumYili) # Fonksiyon Çağırdık
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Yağmur')


