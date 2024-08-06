import numpy as np
import random

def sayiTahminOyunu(zorluk):
    if(zorluk==1):
        aralik=(1,50)
        tahminHakki=10
    elif(zorluk==2):
        aralik=(1,100)
        tahminHakki=8
    elif(zorluk==3):
        aralik=(1,200)
        tahminHakki=6
    else:
        print("Lutfen dogru zorluk seviyesini seciniz.")
        return None

    tahminler=[]
    hedefSayi=np.random.randint(aralik[0],aralik[1] + 1)

    for i in range(tahminHakki):
        tahmin=int(input(f"Tahmin:{i+1}: "))
        tahminler.append(tahmin)
        if(tahmin<hedefSayi):
            print("Daha yuksek bir sayi soyleyin.")
        elif(tahmin>hedefSayi):
            print("Daha dusuk bir sayi soyleyin.")
        else:
            print(f"Tebrikler {i+1}.tahminde dogru sayiyi buldunuz")
            
        if(i<tahminHakki):
            print(f"{tahminHakki - i + 1} hakkiniz kaldi.")
        if(i==tahminHakki):
            print(f"Tahmin hakkiniz kalmadi.Oyunu Kaybettiniz.Dogru sayi {hedefSayi} idi.")

    tahminSayisi=i+1
    return tahminSayisi

def performansPuaniHesapla(zorluk,tahminSayisi):
    puan=zorluk*100
    toplamPuan=puan - (tahminSayisi*50)
    return toplamPuan

def oyunIstatistikleri(zorluk,tahminSayisi,puan):
    ortalamaTahmin=np.mean(tahminSayisi)
    ortalamaPuan=np.mean(puan)

    print(f"Ortalama tahmin sayisi: {ortalamaTahmin}")
    print(f"Ortalama puan : {ortalamaPuan}")

def anaMenu():
    print("Sayi tahmin oyununa hosgeldiniz.")
    print("Zorluk Seviyeleri:")
    print("1 - Kolay (1-50 arasi, 10 tahmin hakki)")
    print("2 - Orta (1-100 arasi, 8 tahmin hakki)")
    print("3 - Zor (1-200 arasi, 6 tahmin hakki)")
    
    zorluk = int(input("Zorluk seviyesini seçin (1-3): "))
    oyunSayisi = int(input("Kaç kez oynamak istersiniz? "))
    sonuclar=[]
    for i in range(oyunSayisi):
        print(f"Oyun : {i+1} ")
        tahminSayisi=sayiTahminOyunu(zorluk)
        puan=performansPuaniHesapla(zorluk,tahminSayisi)
        sonuclar.append((zorluk,tahminSayisi,puan))
        print(f"Bu oyun icin puaniniz {puan}")


anaMenu()






    
        



        