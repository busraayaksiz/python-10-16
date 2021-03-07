if __name__ == '__main__':
    with open("test2.txt", "r", encoding="utf-8") as file:
        for i in file:
            print(i)

    with open("test2.txt", "r", encoding="utf-8") as file:
        print(file.tell())
        file.seek(5)
        print(file.tell())

    with open("test2.txt", "r", encoding="utf-8") as file:
        file.seek(2)
        icerik = file.read(100)
        print(file.tell())
        print(icerik)
