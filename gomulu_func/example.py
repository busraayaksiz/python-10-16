if __name__ == '__main__':
    """1"""
    liste = [(3,4),(10,3),(5,6),(1,9)]
    def dikdortgen_alan(cift):
        return cift[0] * cift[1]

    print(list(map(dikdortgen_alan, liste)))


    """2"""
    liste1 = [(3,4,5),(6,8,10),(3,10,7)]
    def üçgen_mi(demet):

        if (abs(demet[0] + demet[1]) > demet[2] and abs(demet[0] + demet[2]) > demet[1] and abs(demet[1] + demet[2]) >
                demet[0]):
            return True
        else:
            return False

    print(list(filter(üçgen_mi, liste1)))

    """3"""
    isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
    soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]
    for i, j in zip(isimler, soyisimler):
        print(i, j)