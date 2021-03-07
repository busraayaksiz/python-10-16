from functools import reduce


if __name__ == '__main__':
# reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve
# daha sonra çıkan sonucu listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döner.
   print(reduce(lambda x,y : x+y , [12,18,20]))