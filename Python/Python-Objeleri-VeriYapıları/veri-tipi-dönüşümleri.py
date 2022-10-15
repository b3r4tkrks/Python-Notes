# Pythonda tanımlanan bir veri tipini bazen başka bir veri tipine dönüştürme ihtiyacı duyarız.

# Örneğin;

# x = input('1.sayı: ')
# y = input('2.sayı: ')
# şeklinde kullanıcıdan aldığımız 2 sayıyı x, y değişkenleri içerisine attıktan sonra 2 sayıyı aşağıdaki gibi toplarsak,

# toplam = x + y
# print(toplam)
# sonuç beklediğimiz gibi olmaz. Örneğin x için 10 ve y için 20 değerlerini girersek toplam = 1020 şeklinde olur. Çünkü python input() fonksiyonu ile satırdan okuduğumuz değer her ne kadar sayısal bir değer olsada python açısından string bir veri tipi olarak algılanır ve toplama işlemide string birleştirme işlemi ile 1020 sonucunu verir.

# Eğer girilen değerlerin tipini kontrol edersek str tipini yani string veri tipini görürüz.

# print(type(x))    # <class 'str'>
# print(type(y))    # <class 'str'>
# Burada string birleştirme değil de sayısal bir toplama işlemi yapmak istiyorsak bu durumda toplama işlemine girmeden önce x ve y değişkenlerini number veri türüne çevirmemiz gerekir.

# toplam = int(x) + int(y)
# print(toplam)
# Bu durumda sonuç x için 10 ve y için 20 değerlerini girersek toplam = 30 olur.

# Aynı işlemi eğer ki ondalıklı olarak yapmak istersek int() fonksiyonu yerine float() fonksiyonunu kullanarak değerleri float veri tipine çevirebiliriz.

# toplam = float(x) + float(y)
# print(toplam)
# Eğer ki; float() ya da int() fonksiyonu ile bir dönüştürme işlemi yaparken ilgili veri tipine uymayacak bir değer girersek ValueError alırız.

# float('a12')
# Burada a12 değeri float veri tipine çevrilemediğinden dolayı "ValueError: could not convert string to float: 'a12' şeklinde string' den float veri tipine dönüştürme hatasını alırız.

# Pythondaki diğer veri tipi dönüşüm metotları,

# x = 10 
# y = 20.5
# isOnline = True
# ** int veri türünden float veri türüne,

# x = float(x)     # int to float
# print(x)         # 10.0 
# print(type(x))   # <class 'float'>
# ** float veri türünden int veri türüne,

# y = int(y)     # float to int 
# print(y)       # 20 
# print(type(y)) # <class 'int'> 
# ** int veri türünden string veri türüne,

# result = str(x) + str(y)   # int to string
# print(result)              # 1020.5
# print(type(result))        # <class 'str'>
# ** bool veri türünden string veri türüne,

# isOnline = str(isOnline)   # bool to str
# print(isOnline)            # True (string bir kelime)
# print(type(isOnline))      # <class 'str'>
# ** bool veri türünden int veri türüne,

# isOnline = int(isOnline)   # bool to int
# print(isOnline)            # 1 (True için 1, False için 0)
# print(type(isOnline))      # <class 'int'> 
# Uygulama: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.

# Daire Alanı : πr² 

# Daire Çevresi : 2πr 

# r: 3.14
 

# pi = 3.14
# r = float(input("yarı çap: "))

# alan = pi * (r ** 2)
# print(type(alan))

# cevre = 2 * pi * r
# print(type(cevre))

# print("alan: "+ str(alan) + " çevre: "+ str(cevre))
# Kullanıcıdan aldığımız değerler bize string veri tipinde gelir. Gelen ondalıklı değerleri float() metodu ile float değerlere dönüştürmemiz lazım. Hesaplama işlemi bittikten sonra da ekranda sonucu string şeklinde göstermeliyiz çünkü string birleştirme işlemine sadece string değerler girer.

