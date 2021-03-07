if __name__ == '__main__':
    #filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False) bir fonksiyon alır ve
    # liste gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular.
    # filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner. Hemen örneklerimize bakalım.
    def asal_mi(x):
        i = 2
        if (x == 1):
            return False  # Asal değil
        elif (x == 2):
            return True  # Asal sayı
        else:
            while (i < x):
                if (x % i == 0):
                    return False  # Asal Değil
                i += 1
        return True
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print(list(filter(asal_mi, range(1, 100))))