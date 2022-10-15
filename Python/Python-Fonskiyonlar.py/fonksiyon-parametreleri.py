'''Fonksiyona Parametre Gönderme
Fonksiyonlara dışarıdan bilgi gönderip fonksiyon içerisinde kullanabiliriz.

Örnek
def hello(name):
    print("Merhaba "+ name)

hello("Arda") # Merhaba Arda
Örnekte olduğu gibi dışarıdan name parametresini fonksiyona gönderip kullanabiliriz.

Örnek
def yazdir(ad,soyad,yas):
    return f"ad: {ad} soyad: {soyad} yaş: {yas}"

sonuc = yazdir("ali","aksoy",20)
yazdir() fonksiyonuna gönderdiğimiz parametrelerin sırası önemlidir. Eğer ki parametreleri yanlış sırada gönderirsek istemediğimiz bir sonuç alırız.

Dolayısıyla parametre isimlerini belirterek fonksiyona bilgi gönderebiliriz bu durumda parametre sırasına uymak zorunda kalmayız.

sonuc = yazdir(soyad="aksoy",ad="ali",yas=20)
Bu durumda gene aynı sonucu alırız çünkü parametreleri key, value şeklinde gönderiyoruz.

Fonksiyonlarda Default Parametreler
Bazen fonksiyonlara gönderdiğimiz parametreler yerine varsayılan değerleri kullanmak isteyebiliriz.

Örnek
def my_function(country = "Turkey"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
country parametresinin varsayılan değeri Turkey' dir. Dolayısıyla fonksiyona bir parametre göndermediğimiz durumda Turkey geçerli olacaktır diğer durumlarda gönderilen parametre geçirli olur.

Değişken Sayıda Parametre Gönderme
Kendisine gönderilen değişken sayıdaki sayıları toplayan bir fonksiyon yazmak istediğimizde *params keyword' üni kullanabiliriz.

Örnek
def toplama(a,b):
    return a+b
Bu şekilde 2 sayıyı toplayabiliriz ya da 3 sayı istiyorsak 3 parametre bekleriz ?

def toplama(a,b,c):
    return a+b+c
Peki 4,5,6 ...?

Bu durumda *params ile parametre tanımlamasını aşağıdaki gibi yapabiliriz.

Örnek
def toplama(*params):
    print(type(params))  # <class 'tuple'>
    sum = 0
    for n in params:
        sum = sum + n
    return sum

print(toplama(10, 20, 50))
print(toplama(10, 20, 30))
print(toplama(10, 20, 30,50,60,10,20))
Gördüğünüz gibi istediğiniz sayıda parametre gönderin sorun değil gelen her parametre bir tuple listesi içine alınıp fonksiyona gönderilir ve bu tuple listesi üzerinde for döngüsü ile dolaşıp gönderilen her değeri alıp toplayabiliriz.

Fonksiyona Key-Value Bilgisi Gönderme
Eğer ki **args şeklinde parametre belirtirsek bu durumda key-value şeklinde istediğimiz sayıda bilgiyi fonksiyona gönderebiliriz.

Örnek
def displayUser(**args):
    print(type(args))  # <class 'dict'>
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name= 'Çınar', age = 2, city = 'istanbul')
displayUser(name= 'Ada', age = 12, city = 'kocaeli', phone = '123132')
displayUser(name= 'Yiğit', age = 14, city = 'ankara', phone = '123132', email= 'yigit@gmail.com')
Bu durumda bir kullanıcının istediğimiz kadar özelliğini fonksiyona key-value şeklinde gönderebiliriz ve gönderdiğimiz farklı sayıdaki bilgiyi for döngüsü ile ekrana yazdırabiliyoruz. Gelen veri tipinin <class 'dict'> yani dictionary olduğuna dikkat ediniz.

Ekran çıktısı;

<class 'dict'>
name is Çınar
age is 2
city is istanbul

<class 'dict'>
name is Ada
age is 12
city is kocaeli
phone is 123132

<class 'dict'>
name is Yiğit
age is 14
city is ankara
phone is 123132
email is yigit@gmail.com
Örnek
def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')
Ekran çıktısı;

10
20
30
(40, 50, 60, 70)
{'key1': 'value 1', 'key2': 'value 2'}
Burada ise ilk 3 parametre sırasıyla a,b ve c yerine geçer. Sonraki 4 bilgi (40,50,60,70) bir tuple bilgisi olur ve en sondaki key-value bilgisi ise dictionary veri tipinde alınır.

Örnek
Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

def listeyeCevir(*params):
    liste = []

    for param in params:
         liste.append(param)
    return liste

result = listeyeCevir(10,20,30,'Merhaba')
print(result)
'''

