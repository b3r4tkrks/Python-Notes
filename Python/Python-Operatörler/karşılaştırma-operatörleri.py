"""
Operatör	Açıklama	
Kullanım

Sonuç
==	eşit mi ?	
10 == 10

True
 	5 == 4	False
 	
x = 5 y = 5

x == y

True
!=	eşit değil mi?	
10 != 9

True
 	10 != 10	False
>	Büyük mü ?	10 > 5	True
<	Küçük mü ?	10 < 5	False
>=	Büyük eşit mi ?	5 >= 5	True
<=	Küçük eşit mi ?	5 <= 5	True
Örnek
a = 10
b = 20
sonuc = (a<b) # True
a, b' den küçük mü diye sorduğumuzda geriye doğruysa True yanlış ise False değeri gelir. Burada a, b' den küçük olduğundan dolayı True bilgisi gelir.

Örnek
a = 20
b = 20
sonuc = (a!=b) # False
Burada ise; a, b'ye eşit değil mi diye soruyoruz ve eşit olduğundan dolayı False bilgisi gelir.

Örnek
a = 20
b = 20
sonuc = (a=<b) # True
Burada ise; a, b' den küçük ya da eşit mi diye soruyoruz ve küçük değil ancak eşit olduğundan dolayı True bilgisi gelir.

Örnek
Doğum yılına göre yaşı 18 ve üstü olan bir kişi ehliyet alabilir. Dolayısıyla doğum yılına göre yaşını hesapladığımız bir kişinin ehliyet alıp alamayacağını (>=) büyük eşit operatörü ile kontrol edebiliriz.

dogumYili = 1999
yas = 2020 - dogumYili # 21
ehliyet = (yas >= 18)
ehliyet değişkeninin değeri True olacağından dolayı kişi ehliyet alabilir. Çünkü (2020 - 1999) bize 21 yaşını verir ve (21>=18) karşılaştırması bize True değerini döndürür.

Python Karşılaştırma Operatör Örnekleri
1- Girilen 2 sayıdan hangisi büyüktür ?

a = int(input('a: '))
b = int(input('b: '))
result = (a > b)
print(f'a: {a} b: {b} den büyüktür: {result}')
2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 = float(input('1. vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final : '))
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')
3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

sayi = int(input('sayı: '))
tekcift = (sayi % 2 == 0)
print(f'girilen sayı çift olma durumu: {tekcift}')
4- Girilen bir sayının negatif pozitif durumunu yazdırın.

sayi = int(input('sayı: '))
pozitifmi = (sayi > 0)
print(f'girilen sayının pozitif olma durumu: {pozitifmi}')
5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz. (email: email@sadikturan.com parola:abc123)

email = 'email@sadikturan.com'
password = 'abc123'
girilenEmail = input('email: ')
girilenPassword = input('parola: ')
isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())
print(f'Email bilgisi doğrumu: {isEmail} ve Parola doğru mu: {isPassword}')
"""
