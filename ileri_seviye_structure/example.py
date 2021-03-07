if __name__ == '__main__':

    "1"
    s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
    frekans = dict()

    for karakter in s:
        if (karakter in frekans):
            frekans[karakter] += 1
        else:
            frekans[karakter] = 1
    for i, j in frekans.items():
        print(i, ":", j)


    "2"
    bas_harfler = ""

    with open("şiir.txt","r",encoding="utf-8") as file:
        for satır in file:
            bas_harfler += satır[0]
    print(bas_harfler)

    "3"
    with open("mailler.txt", "r", encoding="utf-8") as file:
        for satır in file:
            satır = satır[:-1]
            if (satır.endswith(".com") and satır.find("@") != -1):
                print(satır)

    "4"
    isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
    soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
    liste = list(zip(isim,soyisim))
    liste.sort()
    for i,j in liste:
        print(i,j)