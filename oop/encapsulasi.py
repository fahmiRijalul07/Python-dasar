class Hero :
    def __init__(self,name,attackPower,health):
        self.__name = name,
        self.__attackPower = attackPower,
        self.__health = health

    # getter
    def getname (self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def getAttack(self):
        return self.__attackPower
    
    # setter

    def diserang(self,serangPower):
        self.__health -= serangPower

    def hasclau(self,attackDiberi):
        self.__attackPower = attackDiberi

agus = Hero("agus",60,80)

print(agus.__dict__)
print(agus.getname())
print(agus.getHealth())
agus.diserang(5)
print(agus.getHealth())
agus.hasclau(10)
print(agus.getHealth())