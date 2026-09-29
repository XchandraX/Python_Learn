"""
Dictionaries
    struktur data yang menyimpan informasi dalam bentuk pasangan
Kunci-Nilai (Key-Value paris).
"""

## Membuat Diconary

karyawan = {
    "id": 100,
    "nama": "Budi Santoso",
    "departemen": "IT",
    "gaji": 7500000,
    "aktif": True
}

## Mengakses Nilai

# 1. Menggunakan kurung siku (berisiko erro jika key tidak ada)
print(karyawan["nama"]) # Output: Budi Santoso

# 2. Menggunakan .get() (lebih aman, tidak error jika key tidak ditemukan)
print(karyawan.get("departemen"))   # Output: IT

# Anda bisa memberikan nilai default pada .get() jika key tidak ada
print(karyawan.get("alamat", "Alamat tidak ditemukan")) # Output: Alamat tidak ditmeukan

## Menambah dna Mengubah Data

print(karyawan["gaji"]) # Output: 7500000

# Mengubah nilai dari key yang sudah ada
karyawan["gaji"] = 8000000
print(karyawan["gaji"]) # Output: 8000000

# Menambahkan pasangan key-value baru
karyawan["kota"] = "Jakarta"

print(karyawan.get("kota", "Kota tidak ditemukan")) # Output: Jakarta

## Menghapus Data

# Menghapus key "aktif" dan mengambil nilainya
status = karyawan.pop("aktif")

# Menghapus key "departemen"
del karyawan["departemen"]

# Menghapus elemen terakhir yang dimasukkan (Python 3.7+)
karyawan.popitem()

## Menelusuri Dictionary (Iterasi/ Looping)

# 1. Menelusuri hanya Kunci (Keys)
for kunci in karyawan.keys():
    print(kunci)

# 2. Menelusuri hanya nilai (Values)
for nilai in karyawan.values():
    print(nilai)

# 3. Menelusuri Kunci dna Nilai sekaligus (paling sering digunakan)
for kunci, nilai in karyawan.items():
    print(f"{kunci.capitalize()}: {nilai}")