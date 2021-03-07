if __name__ == '__main__':
    string = "busra ZEYNEP Ayaksız"
    print(string.upper())#bütün harfleri büyük yapıyor
    print(string.lower())#bütün harfler küçük yapıyor
    print(string.replace("a","o"))#ilk paramatre olan yerleri ikinci parametre ile değiştiriliyor
    print(string.startswith("b"))#verilen parametre ile başlıyorsa true başlamıyorsa false
    print(string.endswith("z"))#verilen parametre ile bitiyorsa true bitmiyorsa false
    liste = string.split(" ")#verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.
    print(liste)
    string2 = "      deneme        "
    print(string2.strip())#Stringin başında ve sonunda bulunan x değerlerini siler.
    print(string2.lstrip())#Stringin sadece başında bulunan x değerlerini siler.
    print(string2.rstrip())#Stringin sadece sonunda bulunan x değerlerini siler.
    liste1 = ["23","01","1997"]
    print("/".join(liste1))#Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.
    print(string.count("a"))#Stringin içindeki x değerlerini sayar.
    print(string.count("a", 6))#Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.
    print(string.find("a"))#x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür.
    # Bulamazsa "-1" değerini verir.
    print(string.rfind("a"))#x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür.
    # Bulamazsa "-1" değerini verir.