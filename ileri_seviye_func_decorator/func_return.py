def fonksiyon(işlem_adı):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım

    if işlem_adı == "toplama":
        return toplama
    else:
        return çarpma


deneme = fonksiyon("toplama")

print(deneme(2, 69, 5, 74, 5))
deneme2 = fonksiyon("çarpma")
print(deneme(2 * 2 * 2 * 22 * 2))


def toplama(a, b):
    return a + b


def çıkarma(a, b):
    return a - b


def çarpma(a, b):
    return a * b


def bölme(a, b):
    return a / b


def anafonksiyon(func1, func2, func3, func4, işlem_adı):  # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (işlem_adı == "toplama"):
        print(func1(3, 4))
    elif (işlem_adı == "çıkarma"):
        print(func2(10, 3))
    elif (işlem_adı == "çarpma"):
        print(func3(10, 3))
    elif (işlem_adı == "bölme"):
        print(func4(10, 4))
    else:
        print("Geçersiz işlem adı...")


anafonksiyon(toplama, çıkarma, çarpma, bölme, "toplama")

anafonksiyon(toplama, çıkarma, çarpma, bölme, "bölme")
