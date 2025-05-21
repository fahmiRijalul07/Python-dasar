class Master :

    jumlah = 0
    def __init__(self,inputNama,inputAttack,inputHealth,inputShield):
        self.nama = inputNama;
        self.attack = inputAttack;
        self.health = inputHealth;
        self.shield = inputShield;
        Master.jumlah += 1
        print(f"selamat karakter utama hero telah ditambah dengan nama {inputNama}")

hero1 = Master("tobrut sakti", 85, 80, 50 )
print(hero1.jumlah)
hero2 = Master("sarutobu", 70, 60, 50 )
print(hero2.jumlah)
hero3 = Master("kasteing", 89, 40, 70 )
print(hero3.jumlah,"\n")



print(hero1.__dict__)
print(hero1.__dict__)
print(hero1.__dict__)
