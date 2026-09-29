"""
Typecasting
proses mengubah nilai dari satu tipe data menjadi tipe data lain. Proses ini 
sangat pentign ketika Anda ingin melakukan operasi yang melibatkan dua tipe data yg berbeda
"""


"""
Konversi Tipe Data Implisit (Otomatis)

Python secara otomatis mengubah tipe data yang lebi redah/kecil ke 
tipe data yang lebih tinggi/besar tanpa instruksi khusus dari programmer.

Tujuan utamanya adalah untuk mencegah hilangnya presis atau informasi data (data loss)
"""

angka_int = 10      # Integer
angak_float = 2.5   # Float

# Python otomatis mengubah hasil menjadi Flaot agar desimalnya tidak hilang
hasil = angka_int + angak_float

print(hasil)        # Otuput: 12.5
print(type(hasil))  # Output: <class 'float'>


"""
Konversi Tipe Data Eksplisit (Manual)
Progammer secara paksa mengubah tipe data menggunakan fungsi bawaan (built-in functions).

Berikut adalah fungsi knversi utama di Python:
- int()
- float()
- str()
- bool()
- lsit(), tuple(), set()
"""

# 1. String ke Angka 
umur_teks = "25"
umur_angka = int(umur_teks)     # Berubah menjadi Integer 25

harga_teks = "99.5"
harga_angka = float(harga_teks) # Berubah menjadi Float 99.5

# 2. Float ke Integer
berat = 65.8
berat_int = int(berat)  # Output: 65 (Nilai desimal langsung dibuang)

# 3. Angka ke String
tahun = 2026
pesan = "Tahun ini adalah " + str(tahun)
print(pesan)

# 4. List ke Set
id_banyak = [1, 1, 2, 3, 3, 3]
id_unik = list(set(id_banyak))  # Output: [1, 2, 3]
print(id_unik)