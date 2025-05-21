class Hero:
    __jumlah = 0
    def __init__(self,name):
        self.__nama = name;
        Hero.__jumlah += 1

    def getNamaJumlah(self):
        return Hero.__jumlah
    
    def getNamaJumlah1():
        return Hero.__jumlah
    
    def getNamaJumlah2():
        return Hero.__jumlah
    @staticmethod
    def getNamaJumlah3():
        return Hero.__jumlah
    @classmethod
    def getNamaJumlah4(cls):
        return cls.__jumlah
    

sniper = Hero("sniper")
print(sniper.getNamaJumlah3())
gading = Hero('gading')
print(gading.getNamaJumlah4())
pasar = Hero('pasar')
print(Hero.getNamaJumlah4())
