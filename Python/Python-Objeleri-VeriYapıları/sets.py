# Python Set
# Pythonda set listeleri, list' e benzer ancak fark olarak set içindeki elemanlar sıralanamaz (sort) ve indekslenemez yani set elemanlarına 0,1 şeklinde indeks numaraları ile ulaşamayız. Dolayısıyla set 'e eklediğimiz bir elemanın set listesi içinde hangi sırada olacağını bilemeyiz. Ayrıca set içerisindeki elemanlar tekrarlayamaz, her bir elemandan sadece bir tane olmalıdır, tekrarlayanlar silinir.

# Pythonda set oluşturmak için süslü parantezler kullanırız. 

# Örnek
# fruits = {"banana", "grape", "cherry"}
# print(fruits)  # {"grape", "banana", "cherry"}
# Gördüğünüz gibi listeyi ekrana yazdırdığımızda liste elemanlarının yeri karışık geliyor. Hatta uygulamayı her çalıştırdığınızda bu sıra değişecektir.

# Set Elemanlarına Erişim
# Set elemanlarına indeks numarası verilmediğinden dolayı indeks numarasına göre elemanlara ulaşamayız. Ancak bir döngü yardımıyla ulaşabiliriz. 

# Örnek
# fruits = {"banana", "grape", "cherry"}
# for fruit in fruits:
#     print(fruit)

# Çıktı: 
# grape
# banana
# cherry
# Ya da bir elemanın set listesinin bir elemanı olup olmadığını kontrol etmek için in operatörü kullanabiliriz.

# Örnek
# fruits = {"banana", "grape", "cherry"}
# print("banana" in fruits) # True
# "banana" fruits listesinin bir elemanı olduğundan ekrana True değeri gelir.

# Set Elemanlarını Güncelleme
# Set listesi oluşturulduktan sonra her hangi bir elemanını güncelleyemeyiz ancak liste üzerine yeni eleman ekleyebiliriz.

# Set' e Yeni Eleman Ekleme
# Set listesine tek bir eleman eklemek için add() metodunu, birden fazla eleman eklemek için ise update() metodunu kullanabiliriz.

# Örnek
# fruits = {"banana", "grape", "cherry"}
# fruits.add("orange")  # {"grape", "banana","orange","cherry"}
# Set' e birden fazla eleman eklemek için ise;

# Örnek
# fruits = {"banana", "grape", "cherry"}
# fruits.update(["orange", "mango"])  # {"orange", "banana", "mango", "grape", "cherry"}
# Set Elemanlarını Silme
# Set' den bir eleman silmek için remove() ya da discard() metodu kullanılabilir.

# Örnek
# fruits = {"banana", "grape", "cherry"}
# fruits.remove("grape")  # {"banana","cherry"}
# ** Eğer ki silmek istediğimiz eleman set içerisinde yok ise bu durumda geriye bir exception yani hata objesi döndürülür. 

# Örnek
# fruits = {"banana", "grape", "cherry"}
# fruits.discard("grape")  # {"banana","cherry"}
# remove() metodundan farklı olarak discard() metodu ile silmek istediğimiz değer set içerisinde yoksa bir exception yani hata objesi döndürülmez.

# ** Exception için Error Handling dersine bakınız.

# Bir eleman silmek için ayrıca pop() metodunuda kullanabiliriz ancak set listeleri indekslenmediğinden dolayı pop() ile sildiğimiz bir elemanın hangisi olacağını bilemeyiz. Dolayısıyla uygulamayı her çalıştırdığımızda set listesinin son elemanı silinir ancak hangi eleman olacağını bilemeyiz.

# Örnek
# fruits = {"banana", "grape", "cherry"}
# fruits.pop()  # {"banana","cherry"}
# clear() metodu ile set elemanlarının hepsini silebiliriz.

# Örnek
# fruits = {"banana", "grape", "cherry"}
# fruits.clear()  # { }
# del komutu ile set listesinin referansını sileriz dolayısıyla set ' e tekrar ulaşmak istediğimizde hata alırız.

# Örnek
# fruits= ["banana", "grape", "cherry"] 
# del fruits
# print(fruits) # NameError: name 'fruits' is not defined
# Birden Fazla Set Listesini Birleştirme
# Birden fazla set listesini birleştirmek için kullanabileceğimiz union() ve update() metotları vardır.

# Örnek
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)  # {"a",1,3,2,"b","c"}
# union() metodu ile birleştirilen set' ler yeni bir set objesiyle geri döner. (set3)

# Örnek
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1) # {"a",1,3,2,"b","c"}
# update() metodu ile bir set'i diğer set içerisine eklemiş oluyoruz yeni bir set objesi oluşturulmaz. (set1)

