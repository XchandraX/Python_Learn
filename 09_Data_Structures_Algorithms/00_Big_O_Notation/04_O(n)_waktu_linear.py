# O(n) - Waktu Linear (Fair)
"""
Waktu eksekusi meningkat lurus sebanding dengan jumlah data.
Jika data bertambah 10 kali lipat, waktu eksekusinya juga bartambah 10 kali lipat.
Ini terjadi setiap Kita menelusuri data dari ujung ke ujung
"""

data_angka = [4, 2, 7, 1, 9]

# O(n) - Looping satu kali melintasi seluruh elemen
for angka in data_angka:
    if angka == 9:
        print("Ketemu!")

# Fungsi bawaan seperti min(), max(), sum() di list juga berjalan dalam O(n)