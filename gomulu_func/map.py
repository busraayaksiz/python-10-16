def dobule(x):
    return x * 2


if __name__ == '__main__':
    liste1 = list(map(dobule, [1,2,3,4,5,6,7]))
    print(liste1)

    liste2 = list(map(lambda x : x ** 2,(1,2,3,4,5,6,7,8,9,10)))
    print(liste2)

    liste3 = list(map(lambda x,y : x*y, liste1, liste2))
    print(liste3)