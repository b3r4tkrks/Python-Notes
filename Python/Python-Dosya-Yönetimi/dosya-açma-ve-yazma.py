# Herhangi Bir Konuda (Türde) Dosya Açmak İçin open() Fonksiyonunu Kullanırız.
# Kullanımı : open(dosya_adı,dosya_erişim_modu)
# dosya_modu => Dosyayı Hangi Amaçla Açtığımızı Belirtir

# w : Write Yazma Methodudur, Dosyayı Konumda Oluşturur.
# w : Dosya İçeriğini Siler Ve Yeniden Yükler

# file = open('file.txt','w')
# file.close()

# file = open('C:/users/m1000/Desktop/dosyayı_buraya_açıyoruz.txt','w')
hakaretler = ['mal','salak','aptal']
file = open('new_file.txt','w',encoding = 'utf-8')
isim = input('Kullanıcı Adınız : ')
file.write(isim)
# r : Read Okuma Methodur, Dosya Konumda Yoksa Hata Verir.
# Var Olan Bir Dosyayı Okursun
file2 = open('PYTHON_ORİGİNAL','r')
file.read()
# a : Append Ekleme Methodudur, Dosya Konumda Yoksa Oluşturur.
# x : Create Dosya Oluşturma Methodudur, Dosya Varsa Hata Verir.

