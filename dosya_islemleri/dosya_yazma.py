
if __name__ == '__main__':
    file = open("test.txt", "w", encoding="utf-8")
    file.write("user1 - Büşra")
    file.close()

    file2 = open("test2.txt", "a", encoding="utf-8")
    file2.write("user2 - büşra2")
    file2.close()

    file3 = open("test2.txt", "a", encoding="utf-8")
    file3.write("\n user3 - büşra2")
    file3.close()


