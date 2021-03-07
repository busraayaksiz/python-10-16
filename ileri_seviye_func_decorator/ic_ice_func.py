if __name__ == '__main__':
    def fonksiyon(*args):  # İstediğimiz sayıda argüman gönderebiliyoruz.
        print(args)
        for i in args:
            print(i)

    fonksiyon(1, 2, 3, 4, 5)


    def fonksiyon(isim, *args):
        print("İsim:", isim)
        for i in args:
            print(i)


    fonksiyon("Murat", 1, 2, 3, 4, 5, 6, 7, 8)

    def fonksiyon(**kwargs):
        print(kwargs)

    # 2 yıldız koyarak keyword argümanlar ile (anahtar kelimeli argümanlar) fonksiyonumuzu tanımladık ve
    # argümanlara isim vererek fonksiyonumuzu çağırdığımızda isimleri anahtar kelime ,
    # argüman değerlerini değer olarak alarak fonksiyonumuz sözlük oluşturdu.
    # İşte keyword argümanlar bu şekilde kullanılabiliyor.
    fonksiyon(isim="Murat", soyisim="Coşkun", numara=12345)


    def fonksiyon(**kwargs):
        for i, j in kwargs.items():
            print("Argüman İsmi:", i, "Argüman Değeri:", j)

    fonksiyon(isim="Murat", soyisim="Coşkun", numara=12345)


    def fonksiyon(*args, **kwargs):
        for i in args:
            print("Argümanlar:", i)
        print("------------------------------")
        for i, j in kwargs.items():
            print("Argüman İsmi:", i, "Argüman Değeri:", j)


    fonksiyon(1, 2, 3, 4, 5, 6, 7, isim="Murat", soyisim="Coşkun", numara=12345)


    def selamla(isim):
        print("Selam", isim)


    selamla("Büşra")
    merhaba = selamla
    merhaba("ayaksız")
