# Classes Objects

# 1. Mendefiniskan Class (Gunakan penulisan PascalCase untuk nama Class)
class Mobil:
    # 2. Constructor (__init__) dijalankan otomatis saat objek dibuat
    # 'self' EAJIB menajadi parameter pertama
    def __init__(self, merk, warna, tahun):
        # Menyimpan nilai dari parameter ke dalam atribut milik objek (self)
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        self.mesin_menyala = False

    # 3. Instance Method: Perilaku yang bisa dilakukan oleh objek
    def nyalakan_mesin(self):
        if not self.mesin_menyala:
            self.mesin_menyala = True
            print(f"Mesin {self.merk} ({self.warna}) telah dinyalakan. Vroom!")
        else:
            print(f"Mesin {self.merk} sudah menyala.")

    def matikan_mesin(self):
        self.mesin_menyala = False
        print(f"Msin {self.merk} dimatikan.")

# --- CARA MENGGUNAKAN (INSTANTIATION) ---

# Membuat wujud nyata (Objek) dari cetak biru Mobil
avanza_saya = Mobil("Toyota Avanza", "Hitam", 2020)
brio_kamu = Mobil("Honda Brio", "Kuning", 2022)

# Mengakses atribut objek 
print(f'Mobil saya adalah {avanza_saya.merk} ekluaran tahun {avanza_saya.tahun}')

# Memanggil metod objek
avanza_saya.nyalakan_mesin()
brio_kamu.nyalakan_mesin()

# Perhatikan bahwa state (kondisi) masing-masing objek saling independen!
print(f"Avanza menyala? {avanza_saya.mesin_menyala}")   # True
print(f"Brio menyala? {brio_kamu.mesin_menyala}")       # True