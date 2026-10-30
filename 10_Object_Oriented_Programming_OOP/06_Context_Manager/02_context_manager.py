# Context Manager
class KoneksiDatabase:
    def __init__(self, nama_db):
        self.nama_db = nama_db
        self.terhubung = False

    # 1. Method yang dieksekuksi SAAT MEMASUKI blok 'with'
    def __enter__(self):
        print(f"[SETUP] Membuka koneksi ke database: {self.nama_db}...")
        self.terhubung = True
        # Nilai yang di-return di sini akan masuk ke variabel setelah kata 'as'
        return self

    # 2. Method yang dieksekusi SAAT KELUAR dari blok 'with' (Apapun yang terjadi)
    def __exit__(self, exc_type, exc_value, traceback):
        # exc_type, exc_value, traceback digunakan untuk menangkap informasi error
        print(f"[TEARDOWN] Menutup koneksi database {self.nama_db} dengan aman.")
        self.terhubung = False

        # Jika terjadi error di dalam blok with, kita tangkap di sini
        if exc_type is not None:
            print(f"[WARNING] Terjadi error: {exc_value}")

        # Return True jika kita ingin 'menelan' error agar program tidak crash
        # Return False (default) jika kita ingin error tetap dilempar (raise)
        return True

    def eksekusi_query(self, query):
        if not self.terhubung:
            raise Exception("Koneksi belum dibuka!")
        print(f"[QUERY] Mengeksekusi: {query}")

# --- CARA MENGGUNAKAN ---

print("--- Skenario 1: Berjalan Normal ---")
# 'db' menampung objek yang di-return oelh __enter__
with KoneksiDatabase("Server_Produksi") as db:
    db.eksekusi_query("SELECT * FROM users")
    db.eksekusi_query("UPDATE users SET status = 'Aktif'")
# Begitu keluar dari indentasi blok with, __exit__, OTOMATIS dieksekusi

print("\n--- Skenario 2: Terjadi Error (Koneksi tetap ditutup dengan aman) ---")
with KoneksiDatabase("Server_Testing") as db_test:
    db_test.eksekusi_query("SELECT * FROM produk")
    # Mensimulasikan error yang tidak terduga
    hasil = 10 / 0
    # Baris ini tidak akan pernah dijalankan
    db_test.eksekusi_query("DELETE FROM produk")

print("\nProgram selesai tanpa crash berkat __exit__!")