import numpy as np
import random


def sayiyiBulmayaCalis(baslangic,bitis):
    tahmin=int(input(f"{baslangic} sayisi ile {bitis} sayilari arasindan sayi tahmin ediniz."))
    try:
        if(tahmin>=baslangic and tahmin<=bitis):
            return tahmin
        else:
            print(f"Lutfen {baslangic} ve {bitis} degerleri arasindan bir deger giriniz.")

    except ValueError:
        print("Lutfen tam sayi giriniz")

def randomSayiyiAl(baslangic,bitis):
    return np.random.randint(baslangic,bitis)

def tabloyuGoster():
    arrTable=np.random.randint(0,9,size=9).reshape=(3,3)
    print(arrTable)

def oyunuOyna():
    print("Oyuna hosgeldnizi!")
    print("Oyun 3'e 3'luk bir matris tablosundaki elemanlardan sayi tahmin etme oyunudur.")
    print("Sayilar her seferinde yer degistiriyor.")
    
    baslangic=0
    bitis=9
    tahminEtmeHakki=10
    tahminSayisi=0
    randomSayi=randomSayiyiAl(baslangic,bitis)
    

    while(tahminSayisi<tahminEtmeHakki):
        tahmin=sayiyiBulmayaCalis(baslangic,bitis)
        if(tahmin<randomSayi):
            print("Tahmininizi yukseltin.")
            tahminSayisi+=1
        elif(tahmin==randomSayi):
            print(f"Tahmininz dogru,tebrikler! {tahminSayisi}.denemede buldunuz.")
            break
        else:
            print("Tahmininizi dusurun")
            tahminSayisi+=1

        if(tahminSayisi==tahminEtmeHakki):
            print(f"Tahmin hakkiniz doldu.Oyunu kaybettiniz.Dogru tahmin edilecek sayi {randomSayi} idi. ")


oyunuOyna()
        

        

        

        

