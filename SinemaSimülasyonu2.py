import numpy as np

class SinemaSalonu:
    def __init__(self):
        self.sinemaSalonu=np.zeros(30).reshape(6,5)
    
    def koltukRezerveEt(self,satir,sutun):
        self.koltukDurumu()
        if(self.sinemaSalonu[satir-1,sutun-1]==0):
            self.sinemaSalonu[satir-1,sutun-1]=1
        else:
            print(f"{self.sinemaSalonu[satir-1][sutun-1]} koltugu dolu.")
    
    def koltukDurumu(self):
        print(f"{self.sinemaSalonu}")
    
    def koltukSil(self,satir,sutun):
            if(self.sinemaSalonu[satir-1][sutun-1]==1):
                self.sinemaSalonu[satir-1][sutun-1]=0
            else:
                print("Koltuk zaten bos.")
                
    def bosKoltuklar(self):
        bosKoltuk=[]
        for i in range(6):
            for j in range(5):
                if(self.sinemaSalonu[i][j]==0):
                    bosKoltuk.append(self.sinemaSalonu[i][j])
        print(bosKoltuk)


sinema=SinemaSalonu()

main=True
while(1):
    if(main):
        print("""SINEMAYA HOSGELDINIZ.
              1-Sinema Salonunun Simulasyonunu Goster
              2-Koltuk Rezerve Et
              3-Koltuk Sil
              4-Menuye Tekrar Gel
              5-Cikis""")
        secim=int(input("1-5 arasinda secim yapiniz."))
        if(secim==1):
            sinema.koltukDurumu()
            main=True
        elif(secim==2):
            satir=int(input("Hangi satiri istiyorsunuz?"))
            sutun=int(input("Hangi sutunu istiyorsunuz?"))
            sinema.koltukRezerveEt(satir,sutun)
            main=True
        elif(secim==3):
            satir=int(input("Hangi satiri istiyorsunuz?"))
            sutun=int(input("Hangi sutunu istiyorsunuz?"))
            sinema.koltukSil(satir,sutun)
            main=True
        elif(secim==4):
            main=True
        elif(secim==5):
            break
        else:
            print("1-5 arasinda secim yapiniz.")
            main=True
        


        




    
    






