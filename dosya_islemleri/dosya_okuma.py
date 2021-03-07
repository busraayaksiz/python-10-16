if __name__ == '__main__':
    try:
        file = open("test2.txt", "r", encoding="utf-8")
        for i in file:
            print(i, end="")
        file.close()
    except FileNotFoundError:
        print("dosya bulunamadı.")

    file = open("test2.txt", "r", encoding="utf-8")
    icerik = file.read()
    print("dosyanın içeriği:")
    print(icerik)
    file.close()

    file = open("test2.txt", "r", encoding="utf-8")
    print(file.readline())
    print(file.readline())
    file.close()

    file = open("test2.txt", "r", encoding="utf-8")
    liste = file.readlines()
    print(liste)
    file.close()