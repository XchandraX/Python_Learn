data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# --- Cara Kuno (Non-Pythonic) ---
angka_genap = []
for x in data_angka:
    if x % 2 == 0:
        angka_genap.append(x * 2)# Dikalian 2

# --- Cara Pythonic ---
# Sintaks: [hasil_operasi for item in data if kondisi]
angka_genap_pythonic = [x * 2 for x in data_angka if x % 2 == 0]

print(f"Hasil List Comprehension: {angka_genap_pythonic}")
# Output: [4, 8, 16, 28]

# Conoth Nyata: Membersihkan data teks dari spasi kosong
karyawan = ["   Andi", " Budi  ", "Citra"]
# Memberiskan spasi dan mengubha jadi huruf besar semua dalam 1 baris
karyawan_berish = [nama.strip().upper() for nama in karyawan]
print(karyawan_berish) # Output: ["ANDI", "BUDI", "CITRA"]