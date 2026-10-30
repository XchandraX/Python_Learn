# Inheritance

# 1. Parent Class (Class Induk)
class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def bersuara(self):
        # Metode ini sengaja dikosongkan agar ditimpa (override) oleh Child
        pass

# 2. Child class (Class Anak) mewarisi dari Hewan
class Kucing(Hewan):
    def __init__(self, nama, warna_bulu):
        super().__init__(nama, spesies="Feline")

        self.warna_bulu = warna_bulu

    def bersuara(self):
        print(f"{self.nama} Mengeong: Meow!")

class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama, spesies="Canine")

        self.ras = ras

    def bersuara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# --- CARA MENGGUNKAN ---

cat = Kucing("Milo", "Oren")
dog = Anjing("Rex", "Golden Retriever")

# Kucing dan Anjing otomatis memiliki metode makan() dari class Hewan!
cat.makan()
dog.makan()

# Masing-masing memiliki suara yang berbeda karena Overrding
cat.bersuara()
dog.bersuara()

# Melihat MRO (Urutan pencarian metode jika terjadi Multiple Inheritance)
print("\nMRO dari class Kucing:")
print(Kucing.mro())
# Output: [<class '__main__.Kucing'>, <class '__main__.Hewan'>, <class 'object'>]