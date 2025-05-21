class Heroes:
    def __init__(self, name,health,armor):
        self.name = name ,
        self.__health = health,
        self.__armor = armor
        
    @property
    def info(self):
        return "name {} : \n\thealth: {} \n\tarmor : {}".format(self.name,self.__health,self.__armor)
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor (self):
        print("sudah di hapus ya bro")
        self.__armor = None

print("merubah info")
sniper = Heroes('sniper',100,20)
print(sniper.info)
sniper.name = "maskur"
print(sniper.info)


print("getter dan setter untuk armor ")
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)
print(sniper.info)
del sniper.armor
print(sniper.info)



