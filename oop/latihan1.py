class Hero :
    def __init__(self,inputName,inputHealth,inputAttack, inputArmor):
        self.nama = inputName;
        self.health = inputHealth;
        self.attack = inputAttack;
        self.armor = inputArmor;

    def Menyerang (self, Musuh):
        print(self.nama + " menyerang " + Musuh.nama)
        Musuh.Diserang(self, self.attack)

    def Diserang (self,Musuh,attackPowerLawan):
        print(self.nama + " diserang "+ Musuh.nama)
        attack_diterima = attackPowerLawan /self.armor
        print("serangan terasa "+ str(attack_diterima))
        self.health -=  attack_diterima
        print(f"darah {self.nama} tersisa {str(self.health)}")
        
        

player1 = Hero("dangding", 100, 70, 80)
player2 = Hero("kastil", 100, 90, 40)



player1.Menyerang(player2)