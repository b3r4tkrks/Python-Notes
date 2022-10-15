'''Nesne Tabanlı Programlama-Kalıtım Nedir?
Nesne tabanlı programlamada kalıtım (inheritance) ile bir sınıf (Parent Class) içerisindeki tüm özellik ve metotları başka bir sınıfa (Child Class) aktarabiliriz. 

Person sınıfı için tanımladığımız name,lastname,age özellikleri ve eat(),run(),drink() metotlarını Student ve Teacher sınıfları için de tekrar tekrar tanımlamamıza gerek yok çünkü Student ve Teacher zaten Person sınıfının barındırdığı özellik ve yeteneklere de sahip birer sınıftır. Dolayısıyla Person sınıfını Parent Class olarak tanımlayıp Student ve Teacher sınıflarını Child Class olarak tanımlayıp Parent Class' ın tüm özellik ve yeteneklerini Child Class' lara kalıtım yoluyla aktarabiliriz.

Parent Class Tanımlama
Parent bir sınıf yani base sınıf tanımlarken o sınıfa ait temel özellik ve yetenek tanımlaması yapıyoruz. Örneğin Person sınıfı için bir insanın temel özellikleri ya da bir araç için aracın temel özellik tanımlaması yapmamız gerekiyor.

Örnek
class Person:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastName = lastname
        self.age = age

    def eat(self):
        print('I am eating')

    def drink(self):
        print('I am drinking')

    def run(self):
        print('I am running')
Child (Base) Class Tanımlama
Temel sınıftaki özelliklere sahip olacak ancak ekstra üzerine özellik yada yetenek ekleyecek olduğumuz sınıflar child yani base class olarak tanımlanır.

Person sınıfı için olan özellik ve yetenekler Student ve Teacher sınıfları için de geçerlidir dolayısıyla Person sınıfı, Student ve Teacher sınıfı için Parent Class ya da diğer adıyla Base Class 'dır.

Student ve Teacher sınıfları ise Person sınıfına göre Child Class' dır.

Örnek
class Student(Person):
  pass

class Teacher(Person):
  pass
Base sınıfı Child sınıflarda parametre olarak almamız gerekiyor bu durumda Student ve Teacher sınıfları Person sınıfının sahip olduğu tüm özellik ve yeteneklere sahiptir.

Örnek
p1 = Person("Çınar","Turan",3)
s1 = Student("Yiğit","Bilgi",12)
t1 = Teacher("Sadık","turan",36)

print(p1.name+' '+p1.lastname+' '+str(p1.age))  # Çınar Turan 3
print(s1.name+' '+s1.lastname+' '+str(s1.age))  # Yiğit Bilgi 12
print(t1.name+' '+t1.lastname+' '+str(t1.age))  # Sadık turan 36
s1 ve t1 nesneleri türetilirken sınıfa gönderdiğimiz parametreler aslında Person sınıfının yapıcı metodu tarafından ele alınıyor. Sonuçta tanımlayacağımız her Student ve Teacher nesnesi birer Person nesnesi oluyor. Hatta sq ve t1 nesneleri üzerinden Person da tanımlanan metotlara da ulaşabiliriz.

Örnek
s1.eat()   # I am eating
t1.run()   # I am running
Child Class' ın Genişletilmesi
Child sınıflar her ne kadar base sınıfın özelliklerini kullansalarda miras aldığı tüm özelliklerin üstüne kendilerine özgü özelliklere ihtiyaç duyarlar. Çünkü bir student nesnesi her ne kadar run(), eat() yeneklerine sahip olsa da study() özelliğine de sahip olmalıdır yani ders çalışma eylemini de yapabiliyor olmalıdır. Peki neden study() yeteneğini Person sınıfına eklemedik ? Çünkü her person örneğin emekli bir kişi ders çalışma eyleminde bulunmaz, bu durum öğrenciyi ilgilendirir. Ya da Student sınıfına özel bir öğrenci numarası olabilir.

Örnek
class Student(Person):
    def __init__(self,name,lastname,age,number):
        Person.__init__(self, name, lastname, age)
        self.number = number
Student sınıfına ekstra olarak number bilgisi gönderiyoruz. İlk 3 parametreyi Person sınıfının yapıcı metoduna gönderiyoruz ve number bilgisini ise Student sınıfının yapıcı metodu ele alıyor.

Person__init__() ile base sınıfın yapıcı metodunu çağırıyoruz aynı şekilde super().__init__() şeklinde de kullanabiliriz.

Örnek
Aynı şekilde Teacher sınıfı için de öğretmen branş bilgisini ekleyelim.

class Teacher(Person):
    def __init__(self,name,lastname,age,branch):
        super().__init__(name,lastname,age)
        self.branch = branch
Peki Student() ve Teacher() sınıfından nesne türetelim.

Örnek
p1 = Person('Ali','Yılmaz')
s1 = Student('Çınar','Turan', 1256)
t1 = Teacher('Serkan','Yılmaz','Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName+ ' '+ str(s1.studentNumber))
print(t1.firstName + ' ' + t1.lastName+ ' '+ t1.branch)
Ekran çıktısı;

Ali Yılmaz
Çınar Turan 1256
Serkan Yılmaz Math
Gördüğünüz gibi Student' ın bir öğrenci numara bilgisi ve Teacher' ın ise branş bilgisi mevcut.

Base Sınıf Metodunu Ezme (Method Override)
Base sınıf için yeni bir metot ekleyelim.

class Person:

    # Diğer tanımlamalar...

    def who(self):
        print('I am a person')

class Student(Person):
  pass

class Teacher(Person):
  pass
Bu durumda 3 sınıf üzerinden de who() metodu ekrana 'I am a person' yazar. Ancak ben Student üzerinden 'I am a student' ve Teacher üzerinden ise 'I am a teacher yazdırmak istiyorum'. Bu durumda base sınıfın who() metodunu ezmemiz gerekiyor.

class Student(Person):
  def who(self):
      print("I am a student")

class Teacher(Person):
   def who(self):
      print("I am a teacher")
Aynı isimle eklediğimiz metotlar temel sınıftaki metodu ezmiş olur ve artık student ve teacher nesneleri üzerinden çağırdığımız who() metodu farklı mesajları ekrana yazar.



 
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