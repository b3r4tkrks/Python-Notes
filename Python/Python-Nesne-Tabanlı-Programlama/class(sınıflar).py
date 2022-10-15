'''Nesne Tabanlı Programlama-Class Nedir?
Gerçek hayattaki bir nesneyi yazılım dünyasında temsil edecek olan yapıya class denir. Peki örnek bir class tanımlaması yapalım.

Örnek
class Person:
    pass

p1 = Person()
p2 = Person()
Person isminde bir class tanımlaması yaptık ve Person sınıfını kullanarak 2 tane nesne türettik. Ancak şu anda Person sınıfı içinde özellik ve metod tanımlaması yok. Özellik ataması yapabilmek için sınıf içerine bir özellik ve özelliğe değer ataması yapabileceğimiz bir constructor (yapıcı metod) eklememiz gerekir.

Constructor (Yapıcı) Metod
Class bünyesinde tanımlanan bir özellik (attribute) bilgisine değer ataması yapabilmek için yapıcı metod tanımlaması yapmalıyız. Instance metodlar için yapıcı metod tanımlaması yapmamız gerekiyor.

Örnek

class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
Yapıcı metod ismi __init__() olarak tanımlanmalıdır. Başta ve sonda 2 alt çizgi ile oluşturulan __init__() metodu sınıf için özel bir metottur. İlk parametre olarak self parametresi ve özellik parametrelerini alır.

self parametresi sınıftan türetilecek olan nesneleri (p1, p2) temsil eder. Yani Person sınıfından türetilecek olan p1 ve p2 nesneleri sınıf tanımlama aşamasında bilinmediğinden dolayı self ile temsil edilir ve yapıcı metoda gönderilen name ve year parametreleri p1 ve p2 nesneleri içerisine yani self içerisine kopyalanır.

p1 = Person("ahmet", 1986)
p2 = Person("deniz", 1989)
Burada 2 tane Person nesnesi türettik ve nesne içerisine gönderdiğimiz ad ve yıl bilgileri ilgili nesnelerin name ve year alanları içerisine kopyalandı.

** Her bir nesne türetme aşamasında ekrana 'init metodu çalıştı.' şeklinde mesaj yazdırıldığına dikkat ediniz. Çünkü her nesne türetme aşamasında Person() 'a gönderdiğimiz parametreler ilgili nesnenin (p1 ya da p2) içerisinde tanımlanan name ve year bilgilerine self aracılığıyla kopyalanmış olur ve bu aşamada ise her bir nesne için ekrana 'init metodu çalıştı.' mesajı yazdırılır.

Özellik (Attributes) Tanımlama
Sınıflar içerisinde class attributes yani özellikleri class seviyesinde ya da nesne seviyesinde tanımlayabiliriz.

Örnek
class Person:
     # class attributes
     address = 'no information'

     # constructor (yapıcı metod)
     def __init__(self, name, year):

         # object attributes
         self.name = name
         self.year = year
constructor içerisinde tanımlanan özellikler nesne seviyesindedir ve değer atamaları nesne üzerinden yapılır. Ancak bazen sınıf seviyesinde de özellik tanımlaması yapmak isteyebiliriz. Örneğin Person sınıfının address özelliği sınıf seviyesindedir.

Person' dan türetilecek her bir nesne için ortak olarak address alanına 'no information' bilgisini sınıf seviyesinde yapacağımız özellik ataması ile yapabilirsiniz. Yani üretilecek her bir Person nesnesinin address alanı olacak ve içerisinde ise 'no information' yazacak ancak nesne içerisinden bu değeri istersek değiştirebileceğiz ancak değiştirmezsek bu bilgi her nesne için geçerli olacak. Dikkat ederseniz address bilgisi constructor metodu içinden alınmıyor çünkü nesneye özel instance bir özellik değil.

p1 = Person(name='ali', year= 1990) 
p2 = Person(name ='yağmur', year = 1995)

p1.name = 'ahmet'
p1.address = 'kocaeli' 

print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')

Ekran çıktısı;

p1 :name: ahmet year: 1990 address: kocaeli
p2 :name: yağmur year: 1995 address: no information
** Burada dikkat edersiniz ki; sadece p1 nesnesinin address alanını güncelliyoruz.

Metod Tanımlama
Sınıflar içerisinde tanımlanan ve sınıfın yeteneklerini yapmak için görevlendirilen fonksiyonlara metod denir.

Örnek
class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def calculateAge(self):
         return 2020 - self.year
Person sınıfı içerisinde calculateAge() isminde bir metod tanımladık ve metod nesne için bir yaş hesaplaması yapar. Peki yıl bilgisi bize nereden geliyor ?

calculateAge() metodu bir instance metodudur ve her nesnenin özelliklerine self üzerinden ulaşabilir. 

p1 = Person('ali', 1990) 
p2 = Person('yağmur', 1995)

print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}') # adım: ali ve yaşım: 30
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}') # adım: yağmur ve yaşım: 25
p1.name, ali ve p1.year 1990 bilgisini verir. Bu bilgilere aynı nesne üzerinden çağrılan metod da ulaşabilir. Dolayısıyla p1.calculateAge()  p1 nesnesinin year bilgisini alıp 2020 yılından çıkabilir.

Attributes Güncelleme
Nesne özelliklerini aşağıdaki gibi güncelleyebiliriz.

p1 = Person('ali', 1990) 
p1.name = 'ahmet';
print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}') # adım: ahmet ve yaşım: 30


 
 Python
 Python Geliştirme Ortamı
 Python Objeleri ve Veri Yapıları
 Python Operatörler
 Python Koşul İfadeleri
 Python Döngüler
 Python Fonksiyonlar
 Python Nesne Tabanlı Programlama
 OOP Nedir?
 Class
 Method
 Kalıtım
 Quiz Uygulaması
 Django
Paylaş
0
'''