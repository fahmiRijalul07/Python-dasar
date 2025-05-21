class Hero:
    jumlah = 0

    def __init__(self,name,health):
        self.name = name;
        self.health = health;

        self.__private = "janji"
        self._gasmine = "oke"
        
dadang = Hero("dadang",100)
dadang.__private = "akanji"
print(dadang.__private)
print(dadang.__dict__)

print("\n")

dadang._gasmine = "yah kok min"
print(dadang._gasmine)
print(dadang.__dict__)