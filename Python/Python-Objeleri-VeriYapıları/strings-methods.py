# Split Metodu
# Split metodu, karakter dizisinde belirtilen bir karaktere göre parçalama işlemi yapar. 

# Örnek
# message = 'Hello, There.'
# message = message.split(',')   # ['Hello',' There']
# Karakter dizisini ',' karakterinden parçalara ayırır ve bize bir liste gönderir.

# Split metoduna bir parametre göndermediğimizde ise, boşluk karakterinden parçalama yapılır.

# Örnek
# message = 'Hello, There.'
# message = message.split()   # ['Hello,', 'There.']
# Upper Metodu
# Upper metodu, karakterleri büyük harfe çevirir.

# Örnek
# message = 'Hello There.'
# message = message.upper()  # HELLO THERE.
# Lower Metodu
# Lower metodu, karakterleri büyük harfe çevirir.

# Örnek
# message = 'HELLO THERE.'
# message = message.upper()  # Hello There.
# ** title() metodu, karakter dizisindeki her kelimenin baş harfini büyük harfe çevirir.
# ** capitalize(), karakter dizisindeki sadece ilk kelimenin baş harfini büyük harfe çevirir.

# Strip Metodu
# Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler. 

# Örnek
# username = "     sadikturan     "
# x = username.strip()
# print("my username is +  x")  # my username is sadikturan
# Eğer strip() metodunun belirttiğimiz karakterleri silmesini istersek bu karakteri parametre olarak göndermemiz gerekir.

# Örnek
# username = ",,,,...!!sadikturan***"
# x = username.strip(',.!*')
# print("my username is +  x")  # my username is sadikturan
# Replace Metodu
# Replace metodu karakter güncellemesi için kullanılır. 

# Örnek
# message = 'My name is Sadık Turan'
# message = message.replace('Sadık','Çınar')  # My name is Çınar Turan
# replace() metotlarını ard arda kullanabiliriz. 

# Örnek
# url = url.replace(' ','-')
#          .replace('@','')             
#          .replace('ö','o')
#          .replace('ü','u')
#          .replace('ş,'s')
#          .replace('ü','u')
# şeklinde türkçe karakterleri, boşluk karakterlerini ve '@' işaretini url içinde güncelleyebiliriz. 

# Find Metodu
# Find metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa exception döndürür.

# Örnek
# txt = "My name is Sadık Turan."
# x = txt.find("name")
# print(x)  # x = 3
# name string içerisinde 3.indeks numarasından itibaren başladığından dolayı 3 değeri yazdırılır.

# Index Metodu
# index metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa find metodundan farklı olarak geriye -1 değerini döndürür.

# Örnek
# txt = "My name is Sadık Turan."
# x = txt.index("name")
# print(x)  # x = 3
# Eğer ki string içinde olmayan bir ifadeyi aratırsak geriye -1 döner.

# Örnek
# txt = "My name is Sadık Turan."
# x = txt.index("old")
# print(x)  # x = -1
# old, string içinde bulunmadığından dolayı -1 döner.

# ** Ayrıca index ve find metodu için bir arama kapsamı belirtebiliriz.

# index("aranılacak ifade", "başlangıç indeksi","bitiş indeksi")
# Örnek
# txt = "My name is Sadık Turan."
# x = txt.index("name",0,10)
# print(x)  # x = 3
# 0 ile 10. indeks arasında bir arama yapılır.

# String Metot Uygulamaları
# website = "http://www.sadikturan.com"
# course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

# result = ' Hello World '.strip()     # baş ve sondaki boşluk karakterleri silinir.
# result = ' Hello World '.lstrip()    # baştaki boşluk karakterleri silinir.
# result = ' Hello World '.rstrip()    # sondaki boşluk karakterleri silinir.
# result =   website.lstrip('/:pth')   # baştan itibaren '/:pth' karakteri silinir. result "www.sadikturan.com" değerini alır.
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

# result = 'www.sadikturan.com'.strip('w.moc')
# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

# result = course.lower() # küçük harfe çevrilir.
# result = course.upper() # büyük harfe çevrilir.
# result = course.title() # her kelimenin baş harfe büyük harfe çevrilir.
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

# result = website.count('a')         # a karakteri sayılır.
# result = website.count('www')       # www karakterleri sayılır. 
# result = website.count('www',0,10)  # 0 ile 10. indeks arasında www ifadesi sayılır.
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

# result = website.startswith('www')    # website www ile başlıyor mu ? False
# result = website.startswith('http')   # website http ile başlıyor mu ? True
# result = website.endswith('com')      # website com ile bitiyor mu ? True
# 6- 'website' içinde 'com' ifadesi var mı?

# result = website.find('com')          # website içerisinde 'com' ifadesini arar ve geriye 22 döner.
# result = website.find('com',0,10)     # 0 ile 10 arasında com ifadesini bulamaz ve exception döndürür.
# result = course.find('Python')        # 0.indeksten itibaren bulduğu ilk Python için 0 değeri döner.
# result = course.rfind('Python')       # Aramaya sağdan başlayacağından dolayı 2. Python' i 26. indekste bulur.
# result = website.index('com')         # website içerisinde 'com' ifadesini arar ve geriye 22 döner.
# result = website.rindex('com')        # website içerisinde 'com' ifadesini arar ve geriye 22 döner.
# result = website.rindex('comm')       # comm bulunamadığından "ValueError: substring not found" hatası gelir.
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

# result = course.isalpha()   # tüm karakterler alfabetik mi diye sorar ve False gelir.
# result = 'Hello'.isalpha()  # tüm karakterler alfabetik olduğundan True gelir.
# result = course.isdigit()   # tüm karakterler rakam mı diye sorar ve False gelir.
# result = '123'.isdigit()    # tüm karakterler rakam mı diye sorar ve True gelir.
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

# result = 'Contents'.center(50, '*')    # **** Contents **** şeklinde toplam 50 karakter olur.
# result = 'Contents'.ljust(50, '*')     # Contents ********* şeklinde toplam 50 karakter olur.
# result = 'Contents'.rjust(50, '*')     # ********* Contents şeklinde toplam 50 karakter olur.
# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

# result = course.replace(' ', '-')    # tüm boşluk karakterleri '-' ile değiştirilir.
# result = course.replace(' ', '-',5)  # ilk 5 boşluk karakterleri '-' ile değiştirilir.
# result = course.replace(' ', '')     # tüm boşluk karakteri silinir.
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

# result = 'Hello World'.replace('World','There')
# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

# result = course.split(' ')  # ['Python', 'Kursu:', 'Baştan', 'Sona', 'Python', 'Programlama', 'Rehberiniz', '(40', 'saat)']
# result = result[2]          # 'Baştan'
# result = result[5]          # 'Programlama'
# split metodu ile string ifadeyi her boşluk karakterinden ayırıp bir listeye çevirmiş oluruz ve her bir liste elemanına indeks numarası ile ulaşabiliriz.


