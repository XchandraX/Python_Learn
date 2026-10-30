# Paradigms

class Burung:
    def suara(self):
        return "Cuit cuit!"
    
class Bebek:
    def suara(self):
        return "Kwek kwek!"
    
class Kucing:
    def suara(self):
        return "Meow!"

# POLYMORPHISM IN ACTION:
# Fungsi ini tidak peduli objek apa yg dilemparkan kepadanya.
# Selama objek tersebut memiliki metode 'suara()', fugsi ini akan bekerja.
# Kita tidak perlu membuat if-else yang panjang untuk mengecek tipe hewannya
def konser_hewan(hewan_apapun):
    print(f"Hewan ini bersuara: {hewan_apapun.suara()}")

# --- CARA MENGGUNAKAN ---
burung_gereja = Burung()
bebek_karet = Bebek()
kucing_oren = Kucing()

# Memanggil fungsi yang sama, dengan object yang berbeda
konser_hewan(burung_gereja) # Output: Cuit cuit!
konser_hewan(bebek_karet)   # Output: Kwek kwek!
konser_hewan(kucing_oren)   # Output: Meow!
    