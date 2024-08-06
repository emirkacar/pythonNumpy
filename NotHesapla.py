import numpy as np

# Öğrenci not bilgilerini tanımla
notlar = np.array([
    ["Ali", "Matematik", "85"],
    ["Ayşe", "Matematik", "90"],
    ["Ahmet", "Fizik", "78"],
    ["Mehmet", "Fizik", "82"],
    ["Fatma", "Kimya", "88"],
    ["Emre", "Kimya", "91"]
])

isimler=notlar[:,0]
dersler=notlar[:,1]
puanlar=notlar[:,2].astype(int)

enYuksekAlanKisininIndeksi=np.argmax(puanlar)
enYuksekAlanKisininAdi=isimler[enYuksekAlanKisininIndeksi]
enYuksekAlanKisininDersi=dersler[enYuksekAlanKisininIndeksi]
enYuksekAlanKisiniPuani=puanlar[enYuksekAlanKisininIndeksi]

print(f"En yüksek puan, alan kişi: {enYuksekAlanKisininAdi}")
print(f"Ders: {enYuksekAlanKisininDersi}")
print(f"Puan: {enYuksekAlanKisiniPuani}")
print()
#Her dersin en yuksek ve en dusuk notunu bul

uniqueDers=np.unique(dersler)
for i in uniqueDers:
    dersNotlari=puanlar[i==dersler]
    maksimumPuan=dersNotlari.max()
    minimumPuan=dersNotlari.min()
    print(f"{i} dersinden en yuksek puan {maksimumPuan}")
    print(f"{i} dersinden en minimum puan {minimumPuan}")



    
    






