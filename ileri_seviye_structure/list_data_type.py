if __name__ == '__main__':
    liste1 = [0,1,2,3,4,5,6,7]
    liste1.append(9)
    #listeye eleman ekleme
    liste1.append("Busra")

    liste2 = [1,2,3,4,5,6,7,8]
    liste2.extend([6,7,9])
    #listenin sonuna başka bir liste eklenir
    for i in liste2:
        print(i)


    liste2.insert(0,"Busra") #listenin belli bir indeksine eleman eklenir

    liste3 = [0,10,11,12,13]
    liste3.pop()#içine hiçbir değer vermezsek listenin son elemanını silerek ekrana basar.
    #İçine belli bir indeks değeri verirsek o indeksi siler ve ekrana basar.
    liste3.pop(1)
    for i in liste3:
        print(i)

    liste4 = ["a","b","c","d"]
    liste4.remove("d")
    #verdiğimiz değeri listeden çıkarmamızı sağlar.
    for i in liste4:
        print(i)

    liste = [1, 2, 3, 4, 3, 3, 5, 6, 7, 8, 9]
    liste.index(3)#index() metodu verilen bir değerin baştan başlayarak hangi indekste olduğunu söyler. Değer listede yoksa hata döner.
    # Eğer ekstra index değeri belirtilirse, index metodu() değeri bu indeksten itibaren aramaya çalışır.

    liste = [1,2,3,4,5,6,1,1,1,1,1,1,1,1,8]
    liste.count(10)#verilen bir değerin listede kaç defa geçtiğini sayar.

    liste = [12, -2, 3, 1, 34, 100] #bir listenin elemanlarını sayıysa küçükten büyüğe , string ise alfabetik olarak sıralar.
    # Eğer özellikle içine reverse = True değeri verilirse elemanları büyükten küçüğe sıralar.
    liste.sort()
    for i in liste:
        print(i)

    liste2 = ["Python", "Php", "C", "Java"]
    liste2.sort()
    for i in liste2:
        print(i)

    liste = [12, -2, 3, 1, 34, 100]
    liste.sort(reverse=True)
    for i in liste:
        print(i)

    liste2 = ["Python", "Php", "C", "Java"]
    liste2.sort(reverse=True)
    for i in liste2:
        print(i)

