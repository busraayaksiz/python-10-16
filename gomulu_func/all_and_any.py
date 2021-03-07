if __name__ == '__main__':
    def hepsi(liste):
        for i in liste:
            if not i:
                return False
        return True


    # Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
    liste = [True, True, False, True, True]
    print(hepsi(liste))
    
    #all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
    print(all(liste))

    #any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
    print(any(liste))
