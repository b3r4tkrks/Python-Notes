numbers = []
# Boş bir numbers dizisi oluşturduk
for x in range(10):
    numbers.append(x)
# range Methodundaki karakterleri append komutu ile boş dizine aktardık.




numbers = [x for x in range(10)]
# Böylece range methodundaki karakterleri x listesinin içine aktarmış olduk.
print(numbers)





for x in range(10):
    print(x**2)


numbers = [x**2 for x in range(10)]
print(numbers)



numbers = [x**x for x in range(10) if x%3 == 0]
print(numbers)
# Sadece 3 e bölünebilen sayıları karesi ile (kendisiyle çarpımı ) ile almış olduk

myString = 'Hello World'
myList = []

for  i in myString:
    myList.append(i)
print(myList)


myList = [i for i in myString]
print(myList)


year= [2007,2008,2011,2001,]
ages = [2021 - i for i in year]
print(ages)



