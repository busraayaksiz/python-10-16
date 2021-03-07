if __name__ == '__main__':
    with open("test2.txt", "r+", encoding="utf-8") as file:
        print(file.read())

    with open("test2.txt", "r+", encoding="utf-8") as file:
        file.seek(10)
        file.write("BUSRA")

    with open("test2.txt", "r+", encoding="utf-8") as file:
        print(file.read())

    with open("test.txt", "r+", encoding="utf-8") as file:
        file.write(
            "BUSRA AYAKSIZ \n")  # "append" metoduyla açılan bir dosyanın imleci direk dosyanın sonunda olduğu için sadece write

    with open("test.txt", "r+", encoding="utf-8") as file:
        print(file.read())

    with open("test.txt", "r+", encoding="utf-8") as file:
        icerik = file.read()
        icerik = "Busra TEST\n" + icerik
        file.seek(0)
        file.write(icerik)
    with open("test.txt", "r+", encoding="utf-8") as file:
        print(file.read())

    with open("test.txt", "r+", encoding="utf-8") as file:
        liste = file.readlines()
        print(liste)

    with open("test.txt", "r+", encoding="utf-8") as file:
        liste = file.readlines()
        liste.insert(3,"test test1\n")
        file.seek(0)
        for i in liste:
            file.write(i)
    with open("test.txt", "r+", encoding="utf-8") as file:
        print(file.read())