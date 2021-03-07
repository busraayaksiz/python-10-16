if __name__ == '__main__':

    #dic şeklinde numaralandırma yapıyor
    liste = ["Elma", "Armut", "Muz", "Kiraz"]
    print(list(enumerate(liste)))

    liste = ["a", "b", "c", "d", "e", "f", "g"]

    for index, eleman in enumerate(liste):
        if (index % 2 == 0):
            print("Eleman: ", eleman)