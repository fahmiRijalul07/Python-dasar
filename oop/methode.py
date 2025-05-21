class Super :
    #class variable
    jumlahPlayer = 0
    def __init__(self,inputNama,inputHealth,inputAttack,inputShield):
        # instace variable
        self.nama = inputNama;
        self.health = inputHealth;
        self.attack = inputAttack;
        self.shield = inputShield;
        Super.jumlahPlayer += 1
    
    def Siapa (self):
        print("nama saya adalah : "+ self.nama)

    def HealthUp(self, Up:int):
        self.health += Up
        
    def getHealth(self):
        return self.health

pemain1 = Super("mii", 80, 54, 75);
pemain2 = Super("jirr", 40, 34, 90);
pemain3 = Super("jkc", 60, 54, 88);
pemain4 = Super("cuss", 90, 84, 55);

pemain1.Siapa()
pemain1.HealthUp(10)
print(pemain1.getHealth())
