class Hero : #template
    pass


hero1 = Hero(); #object / instance
hero2 = Hero();
hero3 = Hero();

hero1.nama = "sniper"
hero1.health = 100

hero2.nama = "sven"
hero2.health = 200

hero3.nama = "usyupss"
hero3.health = 1000


print(hero1.__dict__)
print(hero1.nama)
print(hero1)

print(hex(id(hero1.nama)))
print(hex(id(hero1)))