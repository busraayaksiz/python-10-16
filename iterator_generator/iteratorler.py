#en genel anlamı üzerinde gezinilebilecek bir objedir ve bu obje her seferinde bir tane eleman döner
#kendisinden iterator oluşturabileceğinmiz her obje iterable bir objedir
#bir objenin iterable olması için hazır metodlardan olan __iter()__ ve __next()__ methodlarının tanımlanması gerekli

liste = [1,2,3,4,5,6]
iterator = iter(liste)
print(iterator)
#for i in liste:
    #print(next(iterator))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class Kumanda():
    def __init__(self, kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration


kumanda = Kumanda(["Atv", "Show", "Kanald", "NTV"])
iterator = iter(kumanda)
print(next(iterator))