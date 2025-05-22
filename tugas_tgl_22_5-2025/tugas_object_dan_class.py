class Rambut:
    def __init__(self, bentuk, warna):
        self.bentuk = bentuk
        self.warna = warna

    def tampilkan(self, nama):
        print(f"{nama} details:")
        print(f"Rambut:  {self.bentuk}")
        print(f"Warna Rambut:  {self.warna}\n")

# Membuat object untuk Budi dan Michael
budi = Rambut("Ikal", "Hitam")
michael = Rambut("Lurus", "Pirang")

# Menampilkan data masing-masing
budi.tampilkan("Budi")
michael.tampilkan("Michael")
