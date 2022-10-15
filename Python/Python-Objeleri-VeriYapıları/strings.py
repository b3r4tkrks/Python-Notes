# Pythonda String Tanımlama
# Pythonda Karakter Dizileri yani string veri tipleri tek tırnak (' ') ya da çift tırnak (" ") ile oluşturulur.

# 'Hello World' ile "Hello World" tanımlaması aynıdır. Ancak bazen karakter dizileri içerisinde tek tırnak karakterini karakter dizisinin bir elemanı gibi göstermek isteriz.

# Örnek
# "I'm from Turkey" şeklinde tek tırnak karakterini tanımlayabilmek için mecburen çift tırnak kullanmamız gerekir çünkü 'I'm from Turkey' bu şekilde bir kullanım hata verecektir.

# Birden Fazla Satırda String Tanımlama
# 3 tırnak ile birden fazla satırda string tanımlaması yapabilirsiniz. 3 tane tek tırnak ya da 3 tane çift tırnak kullanabilirsiniz.

# Örnek
# text = """Lorem ipsum dolor sit amet, 
# consectetur adipiscing elit, sed do eiusmod 
# tempor incididunt ut labore et dolore magna aliqua."""
# print(text)
# String Birleştirme (String Concatenation)
# Tanımladığımız string ifadeleri '+' operatörü ile birleştirebiliriz. Ancak string birleştirmede number değişkenleri str() ile string'e çevirmemiz gerekiyor.

# Örnek
# name = 'Sadık'
# surname = 'Turan'
# age = 36

# greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old.'
# print(greeting)  # My name is Sadık turan and I am 36 years old.
# Bu şekilde değişken içeriklerine göre bir string ifadeyi + operatörü ile oluşturmuş olduk ve age değişkeni number türünde olduğundan dolayı str(age) şeklinde string' e çevirdik.

# String Formatlama
# '+' operatörünü kullanarak string birleştirme işlemi bazen zor olabiliyor. Dolayısıyla kullanabileceğimiz format() metodu ile f-string isminde iki farklı alternatifimiz mevcut.

# String format() Metodu
# name = 'Çınar'
# surname = 'Turan'
# age = 36
# .format() metoduna vereceğimiz her parametre sırasıyla { }' lerin yerine kopyalanır. 

# print('My name is {} {}'.format(name, surname)) # My name is Çınar Turan
# Gördüğünüz gibi birinci { }' in yerine Çınar ikinci { }' in yerine ise Turan yazdırılır.

# print('My name is {1} {0}'.format(name, surname))  # My name is Turan Çınar 
# { }' ler için indeks numarası da verebiliriz. Yani format metodu içindeki name, 0 ve surname, 1 değerlerini alır. 

# print('My name is {s} {n}'.format(n=name, s=surname))  # My name is Turan Çınar 
# format() metodu içindeki değişkenlere takma isim de verebiliriz.

# print("My name is {} {} and I'm {} years old.".format(name, surname, age))
# age 3. süslü parantezin yerine gelir ayrıca age number olduğundan dolayı format() metodunda str() fonksiyonunu kullanmamız gerekmez.

# print("My name is {} {} and I'm {} years old.".format(name, name, name)) # My name is Çınar Çınar Çınar 
# forma içine eklediğimiz 3 tane name değişkeni sırasıya süslü parantezler yerine gelir. Eğer ki tek name değerini 3 kere yazdırmak istersek, {0} şeklinde kullanabiliriz.

# print("My name is {0} {0} and I'm {0} years old.".format(name)) # My name is Çınar Çınar Çınar 
# f-String ile String Formatlama
# f-string ile kolaylıkla string birleştirme işlemi yapabiliriz. Çünkü string ifadenin içinde süslü parantezler içinde değişkenleri yazabiliriz.

# print(f"My name is {name} {surname} and I'm {age} years old.")
# String Parçalama (String Slicing)
# String veri tipleri bir karakter dizisi olarak anılır yani bir karakter listesi olarak tanımlanırlar. Dizilerin her bir karakterine soldan 0' dan başlayarak bir indeks numarası atanır. Atanan indeks numaraları dizi içerisindeki her bir elemana ulaşırken kullanılır.

# Örnek
# result = greeting[0] 
# print(result)  # M    
# gördüğünüz gibi greeting karakter dizisinin ilk elemanı soldan sağa doğru 0 indeks numarası ile başlar ve greeting[0] dediğimizde bize 0.indeksteki M karakteri gelir.

# Örnek
# result = greeting[3] 
# print(result)  # n  
# Pozitif indeks numarası soldan sağa 0'dan başlar negatif indeks numarası ise -1 ile sağdan başlar.

# Örnek
# result = greeting[-1] 
# print(result)  # . 
# greeting karakter dizisinin son elemanı "." karakteridir.

# Karakter dizilerinin daha doğrusu dizilerin eleman sayısını len() metodu ile bulabiliriz.

# Örnek
# result = len(greeting)
# print(result)  # 44
# Dolayısıyla son elemanın indeks numarası toplam karakter sayısından 1 eksik olur. 

# Örnek
# result = greeting[len(greeting)-1] 
# print(result)  # .
# Bir karakter dizisini başlangıç ve bitiş aralığında istediğimiz şekilde bölebiliriz.

# Örnek
# result = greeting[3:7] 
# print(result)  # name
# Örnek
# 3. indeksden başlayarak 7. indekse kadar olan karakterleri alıyoruz. Son indeks işin içine katılmıyor.

# Örnek
# result = greeting[:7] 
# print(result)  # My name
# Burada ise başlangıç indeksini belirtmediğimizden dolayı en başta başlar ve 7. indekse kadar gider.

# Örnek
# result = greeting[3:] 
# print(result)  # name is Çınar Turan and I'm 25 years old.
# Örnek
# Burada ise başlangıç indeksi 3 ve bitiş indeksi belirtilmediğinden dolayı en sona kadar alınır.

# result = greeting[0:10:2]
# print(result) # M aei
# Burada ise 0. indeksten 10. indekse kadar alınır ancak adım sayısı 2 olarak belirtildiğinden dolayı bir karakter alınır bir diğeri alınmaz.

# ** Adım sayısını soldan sağa doğru olduğuna dikkat ediniz.

# Örnek
# result = greeting[0:10:1]
# print(result)  # My name is 
# Adım sayısı 1 olduğundan dolayı [0:10] ile gene aynı sonucu verir. Ancak adım sayısına pozitif değer yerine negatif değer verirsek bu durumda sağdan sola doğru ilerleriz.

# Dolayısıyla karakterleri tersten yazdırmak istediğimizde aşağıdaki gibi sonuç alırız. [::] ile tüm karakter dizisini al ancak adım sayısı negatif olduğundan sağdan sola doğru birer birer ilerle. Dolayısıyla yazı tersten yazdırılmış olur.

# Örnek
# result = greeting[::-1]
# print(result)   # .dlo sraey 52 m'I dna naruT ranıÇ si eman yM
# Python String Uygulamaları
# website = "http://www.sadikturan.com"
# course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

# length = len(course)
# length = len(website)
# 2- 'website' içinden www karakterlerini alın.

# result = website[7:10]
# 3- 'website' içinden com karakterlerini alın.

# result = website[22:25]
# result = website[length-3:length]
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

# result = course[0:15]
# result = course[:15]
# result = course[-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

# result = course[::-1]
# name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis'
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.

# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

# result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job
# result = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job)
# result = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.'
# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

# s = 'Hello world'
# s = s[0:6] + 'W'+ s[-4:]
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

# result = 'abc ' * 3
