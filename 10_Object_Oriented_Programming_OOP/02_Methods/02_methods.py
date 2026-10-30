# Methods
class Karyawan:
    # Class Attribute: Data yang dimiliki berasam oleh seluruh ojek Karyawan
    tarif_kenaikan_gaji = 1.05  # Kenaikan 5%
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        # Mengubah class attribute setiap kali objek baru dibuat
        Karyawan.jumlah_karyawan += 1

    # 1. INSTANCE METHOD (Paling Umum)
    def naikkan_gaji(self):
        # menggunakan class attribute untuk menghiutng gaji baru objek ini
        self.gaji = int(self.gaji * self.tarif_kenaikan_gaji)
        return self.gaji

    # 2. CLASS METHOD (Ditandai dengan dekorator @classmethod)
    # Parameter pertamanya adalah 'cls' (Class), bukan 'self'
    @classmethod
    def ubah_tarif_kenaikan(cls, tarif_baru):
        cls.tarif_kenaikan_gaji = tarif_baru
        print(f"Tarif kenaikan global diubah manjadi {tarif_baru}")

    # 3. STATIC METHOD (Ditandai dengan dekorator @staticemthod)
    # Tidak menerima 'self' atau 'cls'. Hanya fugnsi utilitas biasa.
    @staticmethod
    def cek_hari_kerja(hari):
        if hari.lower() in ['sabtu', 'minggu']:
            return "Tidak, Hari ini Libur"
        return "Ya, Hari Kerja"
    
# --- CARA MENGGUNAKAN ---

pegawai_1 = Karyawan("Andi", 5000000)
pegawai_2 = Karyawan("Budi", 6000000)

# Memanggil Instance Method (Berdamapk hanya pada pengawai_1)
pegawai_1.naikkan_gaji()
print(f"Gaji Andi sekarang: {pegawai_1.gaji}")

# Memaanggil Class Method (Berdampak pada seluruh sistem)
Karyawan.ubah_tarif_kenaikan(1.10)  # Diubah ke 10%
pegawai_2.naikkan_gaji()    # Budi menikmati kenaikan 10%
print(f"Gaji Budi sekarang: {pegawai_2}")

# Memanggil Static Method (Dipanggi langsung dari Class, tanpa perlu objek)
print(f"Apakah Seni hari kerja? {Karyawan.cek_hari_kerja('Senin')}")