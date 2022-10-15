'''Nesne Tabanlı Programlama-Method Oluşturma
Nesne tabanlı programlamada sınıftan türetilmiş her bir nesneye  hizmet eden ve belli bir görevi yerine getiren fonksiyona method diyoruz. Her bir nesne derken burada bahsettiğimiz instance metottur ve instance metotlar ilk parametre olarak self parametresini almak zorundadırlar ki hizmet ettiği nesnenin diğer elemanlarına ulaşabilsin.

class Person:      
   def __init__(self, name, year):       
      self.name = name
      self.year = year

   # instance methods
    def intro(self):
         print('Hello There. I am '+ self.name )

   # instance methods
    def calculateAge(self):
        return 2020 - self.year
Person sınıfı için tanımlanan intro() ve calculateAge() metotları birer instance metotlardır çünkü türetildiği nesnelere hizmet ederler ve ilk parametre olarak self alırlar.

 # object (instance)
 p1 = Person(name='ali', year= 1990) 
 p2 = Person(name ='yağmur', year = 1995)

 p1.intro() # Hello There. I am ali
 p2.intro() # Hello There. I am yağmur
Gördüğünüz gibi intro() her çağrıldığı nesnenin name özelliğindeki değeri kullanır.

print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')
Burada ise p1 ve p2, name ve year bilgilerini kullanarak ekrana aşağıdaki mesajları yazdırır.

'adım ali ve yaşım 30' 
'adım yağmur ve yaşım 25' 
Şimdi ise Circle isminde bir class tanımlaması yapalım.

class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap 

Circle sınıfından türetilecek her bir nesne pi değerine sahip olması gerektiğinden pi özelliğini class seviyesinde tanımlıyoruz. 

Yapıcı metod dışarıdan sadece yaricap bilgisini alıyor çünkü Circle dan türetilcek nesnelerin her bir tanesinde yaricap bilgisi farklı olabilir ancak dikkat edersiniz ki; yaricap bilgisi için varsayılan bir değer ataması yaptık. Eğer ki nesne oluşturma aşamasında nesneye yaricap bilgisi verilmezse yaricap bilgisi 1 olur.

Circle sınıfından aşağıdaki gibi nesneler türetebiliriz.

c1 = Circle() 
c2 = Circle(5)
c1 ve c2 nesnelerinin yaricap bilgileri sırasıyla 1 ve 5' dir. 

Peki sınıfa 2 tane daha metod ekleyelim,

def cevre_hesapla(self):
     return 2 * self.pi * self.yaricap

def alan_hesapla(self):
     return self.pi * (self.yaricap**2)
Bu durumda c1 ve c2 nesneleri üzerinden cevre_hesapla() ve alan_hesapla() metotları nesnelerin bilgilerine göre hesaplama işlemlerini yapar.

c1 = Circle() 
c2 = Circle(5)

print(f'c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')
** pi özelliğinin class seviyesinde tanımladığı ve c1 ve c2 nesneleri için ortak özellik olduğuna dikkat ediniz. Her nesne için tekrar tekrar pi değeri belirtmemize gerek kalmadı.

Ekran çıktısı;

c1 : alan = 3.14 çevre = 6.28
c2 : alan = 78.5 çevre = 31.400000000000002
'''