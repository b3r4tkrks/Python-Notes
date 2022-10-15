# Soru 1 : Seçtiniz Bir Kelimeyi İstediğiniz Defa Ekrana Yazdırın.
from typing import List, Any


def yazdir(a,b):
    print( a * b)


yazdir('Merhaba\n',5)



# Soru 2 : Kendine Gönderilen Sınırsız Sayıdaki Parametreyi Listeye Çeviren Bir Fonksiyon Yazın.

def  listeyeCevir(*params):
    liste = []

    for i in params:
        liste.append(i)


    return liste

result = listeyeCevir(10,20,30,40,50,'Salam')
print(result)




# Soru 3 : Gönderilen 2 Sayı Arasındaki Tüm Asal Sayıları Bul

def AsalSayıBulma(a,b):
    for sayi in range(a,b+1):
        if  sayi > 1:
            for i in range(2,sayi):
                if (sayi % i == 0):
                    break
                    print('bitti')
            else:
                print(i)


sayi1 = int(input('1. Sayınız : '))
sayi2 = int(input('2. Sayınız : '))
AsalSayıBulma(sayi1,sayi2)




# Soru 4 : Kendisine Gönderilen Sayının Tam Bölenleri Ayırıp Bir Liste Yapacak Fonksiyon Yaz

def SayıBul(a):

    for i in range(2,a):
        if a % i  == 0:
            tamBolen.append(i)
    return tamBolen


tamBolen = []
deneme = int(input('Sayı : '))
SayıBul(deneme)
print(tamBolen)