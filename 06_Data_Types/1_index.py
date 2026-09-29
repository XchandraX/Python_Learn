"""
Harus di awalin huruf / _
nama = "Budi"
_total = 100
1nama = "budi" (salah)

hanya karakter alfanumerik dan garis bawah
Karakter A-Z, a-z, 0-9 dan _ 

Case-Sensitive
umur, Umur, dan UMUR adalah 3 variable yg berbeda

Naming Style (Snake Case)
gunakan huruf kecil dan pisahkan dengan _ (nama_lengkap)

Jangan gunakan kata kunci bawaan Python
"""

# # # #
# Deklarsi Dasar
# # # #

# Membuat variabel dan memasukan nilai
nama_lengkap = "Budi"   # String (Teks, diapit kutip tunggal ' atau ganda ")
umur = 18               # Integer (Bilangan bualt)
berat_badan = 65.3      # Float (Bilangan desimal, gunakan titik bukan kome)
sudah_lulus = True      # Boolean (Wajib diawali huruf kapital: True atua False)

print("Namaku",nama_lengkap, "Umurku", umur,"tahun", "\nBerat badanku", berat_badan)

# # # #
# Multiple Assignment 
# # # #

# Memberikan nilai berbeda ke beberapa variabel
x, y, z = "Apel", "Pisang", "Jeruk"

# Memberikan nilai yang sama ke beberapa variabel
a = b = c = 0 

print(x, b, z, a)

# # # #
# Dynamic Typing
# # # #

x = 10          # x saat ini bertipe Integer
print(type(x))  # Output: <class 'int'>

x = "Python"    # x diubah nilainya menjadi String 
print(type(x))  # Output: <class 'str'>

# # # #
# Combation  
# # # #

nama = "Andi"
umur = 25

# 1. Menggunakan F-String (Sangat direkomendasikan karena paling bersih)
print(f"Nama saya {nama} dan umur saya {umur} tahun.")

# 2. Menggunakan Koma (Otomatis memberi spasi antar argumen)
print("Nama saya", nama, "dan umur saya", umur, "tahun.")

# 3. Menggunakan Konkatenasi String (+)
# Catatan: Variabel non-string harus diubah ke string dengan str() terlebih dahulu
print("Nama saya " + nama + " dan umur saya " + str(umur) + " tahun.")