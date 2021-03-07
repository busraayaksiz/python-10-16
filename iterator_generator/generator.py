#pythonda iterable objeler oluşturmak için kullanılan objelerdir ve bellekte yer kaplamazlar
#değerler istenildiği anda üretilir ve saklanmaz
#GENERATORLARIN ASIL AMACI BELLEK TASARRUFU
def kareal():
    for i in range(1,5):
        yield i**2 #yield kelimesi generatorun değer üretmesi için kullanılıyor

generator = kareal()
print(generator)
iterator = iter(generator)
print(next(iterator))
print(next(iterator))

liste = [i * 3 for i in range(5)]
print(liste)

generator = (i * 3 for i in range(5))
iterator = iter(generator)
print(next(iterator))

def carpim_tablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} * {} = {}".format(i,j,i*j)

for i in carpim_tablosu():
    print(i)