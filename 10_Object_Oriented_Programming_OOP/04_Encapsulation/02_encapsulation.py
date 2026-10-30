# Encapsulation

class AkunBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik      # Public attribute
        self._jenis = "Tabungan"    # Protected attribute (Konvensi)
        self.__saldo = saldo_awal   # Private attribute (Sangat rahasia)
        
    @property
    def saldo(self):
        # Di sini kita bisa menambahkan log atau format khusus
        return self.__saldo

    # 2. SETTER: Cara aman untuk memodifikasi data Private
    # Nama fungsi harus sama dengan fungsi @property di atas
    @saldo.setter
    def saldo(self, nilai_baru):
        # Keuntungan Setter: Kita bisa melakukan validasi data!
        if nilai_baru < 0:
            print("Error: Saldo tidak boleh negatif!")
        else:
            self.__saldo = nilai_baru
            print(f"Saldo berhasil diupdate menjadi: {self.__saldo}")

# --- CARA MENGGUNAKAN ---
rekening = AkunBank("Budi", 1000000)

# Mengakses data Public dan Protected
print(f"Pemilik: {rekening.pemilik}")
print(f"Jenis: {rekening._jenis}")  # Bisa diakses, tapi tidak disarankan

# MENGAKSES DATA PRIVATE SECARA LANGUSNG AKAN ERROR
# print(rekeinig.__saldo) # AttributteError: 'AkunBank' object has no attribute

# Membaca saldo dengan aman melalui Getter(Perhatikan: dipanggil tanpa kurung())
print(f"Saldo awal: {rekening.saldo}")

# memodifikasi saldo melalui Setter (Tampak seperti assignment biasa)
rekening.saldo = 1500000 # Sukses
rekening.saldo = -50000 # Gagal karena terhalang validasi Setter!