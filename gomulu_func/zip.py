if __name__ == '__main__':
    # zip fonksiyonu listelerin elemanları sırasıyla demet şeklinde gruplayarak bir tane liste oluşturuyor.
    liste1 = [1, 2, 3, 4, 5]
    liste2 = [6, 7, 8, 9, 10, 11]

    i = 0
    sonuç = list()
    while (i < len(liste1) and i < len(liste2)):
        sonuç.append((liste1[i], liste2[i]))

        i += 1
    print(sonuç)

    print(list(zip(liste1,liste2)))

    liste1 = [1, 2, 3, 4]
    liste2 = [5, 6, 7, 8]
    liste3 = ["Python", "Php", "Java", "Javascript", "C"]
    liste4 = ["birinci", "ikinci", "üçüncü", "dördüncü", "beşinci"]

    print(list(zip(liste1,liste2,liste3,liste4)))

    sözlük1 = {"Elma": 1, "Armut": 2, "Kiraz": 3}
    sözlük2 = {"Sıfır": 0, "Bir": 1, "İki": 2}
    print(list(zip(sözlük1,sözlük2)))
    print(list(zip(sözlük1.values(),sözlük2.values())))