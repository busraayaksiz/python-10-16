if __name__ == '__main__':
    x = set()
    liste = [1, 2, 3, 3, 1, 1, 2, 2, 2]
    x = set(liste) #aynı elemanın kümede bi defa bulunabilmesi
    print(x)
    x = {"Python", "Php", "Java", "C", "Javascript"}
    for i in x:
        print(i)
    liste1 = list(x)
    print(liste1[0])
    #küme elemanlarına dizi gibi direkt ulaşılmaz
    y ={1,2,3,4,5}
    x.add(7)
    x.add(1)
    z={123,4,5,10}
    print(y.difference(z))#2 kümenin farkı
    y.difference_update(z)#birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.
    print(z)
    z.discard(10)#İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa, bu metod hiçbir şey yapmaz(Hata vermez).
    for i in z:
        print(i)

    küme1 = {1, 2, 3, 10, 34, 100, -2}
    küme2 = {1, 2, 23, 34, -1}
    küme1.intersection(küme2) #iki kümenin kesişimleri bulmamızı sağlar
    for i in küme1:
        print(i)

    küme1.intersection_update(küme2) #birinci kümeyle ikinci kümenin kesişimlerini bulur ve birinci kümeyi bu kesişime göre günceller.
    for i in küme1:
        print(i)

    küme1 = {1, 2, 3, 10, 34, 100, -2}
    küme2 = {1, 2, 23, 34, -1}
    küme3 = {30, 40, 50}
    print(küme1.isdisjoint(küme2)) #eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.
    print(küme1.isdisjoint(küme3))

    küme1 = {1, 2, 3}
    küme2 = {1, 2, 3, 4}
    küme3 = {5, 6, 7}
    print(küme1.issubset(küme2)) #birinci küme ikinci kümenin alt kümesiyse True, değilse False döner.

    küme1 = {1, 2, 3, 10, 34, 100, -2}
    küme2 = {1, 2, 23, 34, -1}
    küme1.union(küme2)
    for i in küme1:
        print(i)

    küme1 = {1, 2, 3, 10, 34, 100, -2}
    küme2 = {1, 2, 23, 34, -1}
    küme1.update(küme2) #birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.
    for i in küme1:
        print(i)


