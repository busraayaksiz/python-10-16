import os
from datetime import datetime


for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("/home/busra-ayaksiz"):
    for i in klasör_isimleri:
        if (i.startswith("kr")):
            print(i)


#from datetime import datetime

# print(dir(os)) #os modülü fonksiyonları

print(os.getcwd()) #os.modülünün dizini

#os.chdir("/home/busra-ayaksiz/opt-segment") #gitmek istenilen dizin veriliyor

#print(os.listdir()) #bulunulan dizinin içindeki dosya veya klasörler sıralanır

#os.mkdir("Deneme1") #os modülün altında klasör oluşturulur

#os.makedirs("Deneme2/Deneme3") #os modülünün altında iç içe klasör oluşturulur.

#os.rmdir("Deneme2/Deneme3") #denem2 içindeki deneme3 silinir

#os.rename("Deneme1","Deneme2") #değiştirilmek istenen dosya, yeni isim
#os.removedirs("Deneme2/Deneme3") #bütün alt klasörler silinir

#os.rename("test.txt","test2.txt")

#print(os.stat("test2.txt")) #dosyanın tüm özelliklerini gösterir - history

#degistirilme = os.stat("test2.txt").st_mtime

#print(datetime.fromtimestamp(degistirilme))


"""for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/user/Desktop"):  #
    print("Current Path",klasör_yolu)
    print("Directories",klasör_isimleri)
    print("Dosyalar",dosya_isimleri)
    print("**********************************")"""





