class Hero :
    # private class  variable
    __jumlah = 0

    def __init__(self,name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar =attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar*self.__level
        self.__attPower = self.__attPowerStandar*self.__level
        self.__armor = self.__armorStandar*self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return"{} level {}:\n\thealth : {}/{}\n\tattack : {}\n\tarmor  : {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)
    
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

        self.__healthMax = self.__healthStandar*self.__level
        self.__attPower = self.__attPowerStandar*self.__level
        self.__armor = self.__armorStandar*self.__level

    def attack(self,musuh):
        self.gainExp = 50
        
ultra = Hero("ultra",100,80,40)
max = Hero("max",100,60,70)

print(ultra.info)
ultra.gainExp = 80
ultra.gainExp = 80
print(ultra.info)
ultra.gainExp = 100


ultra.attack(max)
ultra.attack(max)
ultra.attack(max)
print(ultra.info)
print(ultra.__dict__)