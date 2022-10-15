# range() METHODU
for i in range(10):
    print(i)
# Başlangıcı 0 Olan 10 'a Kadar Devam Eden ( 10 Dahil Değil ) Döngü İçinde Bir Liste Oluşturur



for i in range(2,10):
    print(i)
# 2 'den Başla 10 'a Kadar Devam Et

for i in range(50,100,10):
    print(i)
# 50 'den Başla 100 'e Kadar 10 'ar 10'ar  Devam Et

# "enumerate" METHODU
strings = 'Hello World'

for i in enumerate(strings):
    print(i)
# İndex Numarasını Yazdırmamıza Yarar Bu 2 Şekilde Çalışır 1. Si "enumerate"


for index,i in enumerate(strings):
    print(index) # İndex Adlı Karakterleri Belirleyecek Bir Değişken Atadık , Yazdırdık Ve Enumerate Sayesinde Etkin Hale Getirdik Bu Da 2. Hali


# zip METHODU

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c','d','e','f','g','ğ','h'],
list3 = [100,200,300,400,500,600,700,800,900,1000]

new_list = zip(list1,list2)
# zip methodu sayesinde 2 listeyi birbiriyle eşleştirdik her harfe başka bir sayı denk geldi

