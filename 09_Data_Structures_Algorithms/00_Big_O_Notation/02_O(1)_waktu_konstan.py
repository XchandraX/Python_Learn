# Excellent
# Waktu eksekusi algoritma selalu sama dan instan, terlepas dari apakah Kita berjumlah 
# 10 atau 10 juta. algoritma ini langsung menuju target tanpa perlu mencari.

data_karyawan = ["Andi", "Budi", "Citra", "Dewi"]

# O(1) - Mengambil data berdasarkan indeks array
karyawan_pertama = data_karyawan[0]

# O(1) -Mengecek key dalam Dictionary (HashMap)
tabel_gaji = {"Andi": 5000, "Budi": 6000}
gaji_budi = tabel_gaji["Budi"]

print(gaji_budi)