

import time
import os
basa = {}
pul = 100000
class Dori:
        def __init__(self):
            self.dori_royxat = basa
        
        def dorilar(self):
            for i in range(int(input("Nechta dori qo'shasiz: "))):
                kasallik = input(f"{i+1}-Dori qanday kasallik uchun: ")
                soz = {
                    "Nomi: ": "Nomini kiriting: ",
                    "Tan narxi: ": "Tan narxini kiriting: ",
                    "Narxi: ": "Aniqlik uchun qayta kiriting: ",
                    "Muddati: ": "Muddati (yyyy) faqat yil kiriting: ",
                    "Kompaniyasi: ": "Kompaniyani kiriting: ",
                    "Tasir: ": "Tasirini kiriting: "
                }
                temp = {}
                for k, v in soz.items():
                    temp[k] = input(v)
                temp["Narxi: "] = int(temp["Tan narxi: "]) * 1.2
                self.dori_royxat[kasallik] = temp
            time.sleep(1)
            os.system("cls")
        
        def dori_ochirish(self, nomi):
            for i, v in self.dori_royxat.items():
                if v['Nomi: '].lower() == nomi.lower():
                    del self.dori_royxat[i]
                    print(f"{nomi} dorisi o'chirildi.")
                    return
            print(f"{nomi} dorisi topilmadi.")

        def muddati_tekshir(self):
            hozirgi_sana = 2024
            for kasallik, malumot in list(self.dori_royxat.items()):
                muddat = int(malumot["Muddati: "])
                if hozirgi_sana - muddat > 1:
                    del self.dori_royxat[kasallik]
                    print(f"{malumot['Nomi: ']} dorisi muddati o'tganligi sababli o'chirildi.")

class Apteka:
        def __init__(self, nomi, sotuvchi, obj: Dori):
            self.nomi = nomi
            self.sotuvchi = sotuvchi
            self.tzm = obj
            self.kassa = pul
        
        def dor_add(self):
            self.tzm.dorilar()
        
        def dor_sotish(self):
            while True:
                print("Sizga nima kasallik uchun dori kerak?")
                kasal = input("Qayeringiz og'riyapti >>> ")
                print("")
                for ky, vu in self.tzm.dori_royxat.items():
                    if ky.lower() == kasal.lower():
                        vu: dict
                        print(f"Kasallik turi: {ky}")
                        for key, vel in vu.items():
                            print(key, vel)
                        self.kassa += int(vu['Narxi: '])
                        print("")
                        print(f"Dori sotildi\nKassaga {int(vu['Narxi: '])} so'm qo'shildi")
                        return 
                else:
                    print("Bunday dori mavjud emas\n0.Asosiy menyuga o'tish")
                    asf = int(input(">>> "))
                    if asf == 0:
                        return

        
        def dor_delete(self):
            print("Qaysi dorini o'chirmoqchisiz?")
            nom = input("Nomini kiriting: ")
            self.tzm.dori_ochirish(nom)
            time.sleep(1)
            os.system("cls")
        
        def dor_korish(self):
            self.tzm.muddati_tekshir()
            os.system("cls")  
            for i, j in self.tzm.dori_royxat.items():
                j: dict
                print(f"Kasallik turi: {i}")
                for d, s in j.items():
                    print(d, s)
                print("")
        
        def kassa_k(self):
            print("")
            print(f"Jami summa {self.kassa}")

    
dori_obj = Dori()
apteka_obj = Apteka("Hayot Farm", "Ali", dori_obj)
while 1:
    print("________________________________")
    print("---------- Hayot Farm ----------")
    print("********************************")
    print("1.Dori qo'shish\n2.Dori o'chirish\n3.Dorilarni ko'rish\n4.Dori sotish\n5.Kassani ko'rish\n0.Exit")
    
    n = int(input(">>> "))
    if n == 1:
        apteka_obj.dor_add()
    elif n == 2:
        apteka_obj.dor_delete()
    elif n == 3:
        apteka_obj.dor_korish()
    elif n == 4:
        apteka_obj.dor_sotish()
    elif n == 5:
        apteka_obj.kassa_k()
    elif n == 0:
        break
    else:
        print("????? Xato raqam ?????\nQayta kiriting")
        time.sleep(1)
        os.system("cls")
print("Dastur tugatildi")