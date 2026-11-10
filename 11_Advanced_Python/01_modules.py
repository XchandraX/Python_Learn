# 1. Import keseluruhan modul (membutuhkan prefix nama modul saat dipakai)
import math

# 2. Import spesifik (hanya mengambil fungsi tertentu, lebih hemat memori)
from datetime import datetime

# 3. Import dengan alias (berguna untuk nama modul yang panjang atau standar industrsi)
# import matematika_kompleks as mk # Asumi ini custom module

def sapa(nama):
    return f"Halo, {nama}! Selamat datang di Advanced Python."

# Eksekusi fungsi built-in
akar_kuadrat = math.sqrt(64)
waktu_sekarang = datetime.now()

# =====================================================================
# SANGAT PENTING (Pythonic Way)
# Kode di bawah ini TIDAK AKAN berjalan jika file 01_modules.py ini 
# di-import oleh file lain (misalnya main.py). 
# Ini sangat berguna untuk melakukan 'testing' di dalam modul itu sendiri.
# =====================================================================
if __name__ == "__main__":
    print("File ini dijalankan secara langsung")
    print(sapa("Chx"))
    print(f"Akar 64 adalah {akar_kuadrat}")