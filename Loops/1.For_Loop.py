"""
for loop digunakan ketika anda sudah mengetahui jumlah perulangan yang akan dilakukan.
atau ketika anda ingin menelusuri isi dari sebuah 
koleksi data (list, tuple, dictionary, atau string)
"""

# Sintaks Dasar:
"""
for elemen in urutan:
"""
    # Blok kode yang dijalankan


# Contoh Menelusuri List
buah = ["Apel", "Pisang", "Jeruk"]

for b in buah:
    print(f"Saya suka makan {b}")

# Contoh Menggunakan range():

# Mencetak angka 0 sampai 4 (5 tidak termasuk)
for i in range(5):
    print(f"Perulangan ke-{i}")

# Mengatur titik mulai, titik akhir, dan interval (step)
for i in range(2, 11, 2):
    print(f"Angka genap: {i}")  # Output: 2, 4, 6, 8, 10