import time


def zaman_hesapla(func):
    def wrapper(sayılar):
        baslama = time.time()
        sonuc = func(sayılar)
        bitis = time.time()
        print(func.__name__ + " " + str(bitis - baslama) + "  saniye sürdü.")
        return sonuc
    return wrapper


@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuc = list()
    for i in sayılar:
        sonuc.append(i ** 2)
    return sonuc


@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuc = list()
    for i in sayılar:
        sonuc.append(i ** 3)
    return sonuc


print(kareleri_hesapla(range(10)))
print(küpleri_hesapla(range(10)))
