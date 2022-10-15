x,y,z = 2,5,107
numbers = 1,5,7,10,6

#1- Kullanıcıdan Aldığınız 2 Sayının Çarpımı İle x,y,z Toplamının Farkı Nedir?
a = int(input('1. Sayı: '))
b = int(input('2. Sayı: '))

result = a*b - x+y+z
print(result)

#2- y Değişkenin x e Kalansız Bölümünü Hesaplayınız

result = int(x//y) # Float olarak da yazabilirsiniz.

#3- x,y,z toplamının mod(Yüzde) 3 ü nedir?
toplam = x+y+z
result = toplam % 3


#4- y nin x. kuvvetini hesapla
result= y ** x 

#5- x,*y,z = numbers işlemine göre z nin küpü kaçtır
x,*y,z = numbers
z ** 3






