# Python programlarımızda geçici olarak veri saklamak için oluşturduğumuz alanlara değişken denir.

# x = 10
# y = 20
# z = x + y
# k

# print(x)  # 10
# print(y)  # 20
# print(z)  # 30
# print(k)  # NameError: name 'k' is not defined
# Tanımlamış olduğumuz x,y ve z değişkenleri bellekte tanımlanan geçici alanlardır.

# k değişkenine bir değer ataması yapmadığımızdan dolayı "NameError: name 'k' is not defined" şeklinde bir hata alırız. Çünkü pythonda tanımlanan her bir değişkene değer ataması yapmak zorundayız.

# Örneğin;

# name = "Çınar"
# Değişkenlere sözel bir atama (string) işlemi yaparken tek tırnak ya da çift tırnak kullanabiliriz.

# name = "Çınar"
# surname = 'Turan'
# Değişkenlere sayısal bir atama yaparken tırnak kullanmamamız gerekiyor. Aksi halde string bir değişken tanımlaması yapmış oluruz.

# a = '50'           # sözel olarak 50 değeri tanımladık
# b = "50"           # sözel (string) olarak 50 değeri tanımladık.
# toplam = a + b     # a + b' nin sonucu 5050 olur.
# eğer ki; a + b' nin sonucunun 100 olmasını istiyorsak bu durumda b değişkenini de sayısal olarak tanımlamamız gerekiyor yani tırnak kullanmadan değişken tanımlamamız lazım.

# a = 50
# b = 50
# toplam = a + b 
# Bu durumda toplam değişkeninin içeriği 100 olur.

# Değişken içerisinde var olan bir değeri yeni bir atamayla değiştirebiliriz.

# x = 10   # x içinde 10 değeri var.
# y = 20   # y içinde 20 değeri var.
# x = 30   # x içinde bulunan 10 değeri silinir ve 30 değeri aktarılır.
# x += 10  # x değişkeni üzerine 10 değerini eklemiş oluruz ve 40 olur.
# Değişken isimlerini seçerken belli kurallara uymamız gerekiyor;

# * Değişken isimleri rakam ile başlayamaz.   

# 1yas => hatalı
# yas1 => geçerli
# _yas => geçerli
# * Komut isimleriyle tanımlama yapılamaz. 

# Örneğin if ya da for kelimesi değişken ismi olamaz.

# * Büyük küçük harf duyarlılığı vardır.

# firstName = 'Sadık'
# FirstName = 'Çınar'
# Burada tanımlanan 2 farklı değişken vardır. Yani bellekte tutulan farklı adreslerdeki farklı değişkenlerdir.

# * Değişken isimlerinde türkçe karakter kullanmamalıyız. Python açısıdan türkçe karakter kullanımında sıkıntı yok ancak bu alışkanlığı edinmemenizi tavsiye ederim.

# Aşağıda ise farklı veri tipleri kullanılmaktadır;

# x = 1             # int
# y = 2.3           # float
# name = 'Çınar'    # string
# isStudent = True  # bool
# x bir sayısal değişkendir ve tam sayı tanımlaması (int) yapılmıştır.

# y bir sayısal değişken ancak ondalıklı yani float değer tipindedir.

# name bir karakter dizisidir. Yani karakter topluluğudur.

# isStudent boolean tipinde bir değişken türüdür ve bir durumun doğru (True: 1) ya da yanlışlığı (False: 0) ile alakalı bilgi tutar.

# Eğer ki tanımlanan bu değişkenlerin veri tiplerini kontrol etmek istersek type() fonksiyonunu kullanarak aşağıdaki şekilde bir çıktı alırız.

# print(type(x))         # <class 'int'>
# print(type(y))         # <class 'float'>
# print(type(name))      # <class 'string'> 
# print(type(isStudent)) # <class 'bool'>
# Pythonda ayrı satırlarda yapılan değişken tanımlaması aynı satırda da yapılabilir;

# x, y, name, isStudent = 1, 2.3, 'Çınar', True
# Son olarak python değişken tanımlamaları ile alakalı bir örnek yapalım;

# maasAli = 3000
# maasAhmet = 5000 
# vergi = 0.25

# print(maasAli - (maasAli * vergi ))     # ali maaşı
# print(maasAhmet - (maasAhmet * vergi )) # ahmet maaşı
# Burada değişken kullanarak daha sağlıklı ve güvenilir kod yazmış oluruz. Örneğin vergi değişkeni yerine tüm kod satırlarında 0.27 oranını kullansaydık hata yapma ihtimalimiz çok yüksek olurdu ki; ileride vergi oranı 0.27 den 0.25 e düştüğü anda bir çok yerde bu değişikliği yapmamız gerekirdi ancak değişken kullanımıyla sadece vergi = 0.25 güncellemesini yapmanız yeterli olur.

# Aynı şekilde Ali' nin maaşına yüzde 10 zam yapmak için her yerdeki 3000 değerini değiştirmek yerine sadece maasAli = 3000 * 1.1 güncellemesini yapmamız yeterli olacaktır.

 