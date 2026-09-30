# 2. Buat program konversi suhu dari Celsius ke Fahrenheit 
# (F = C * 9/5 + 32), input dari user

"""
Pertama, kita bikin input untuk mengambil data celsius 

kedua, bikin variable untuk konversi dari nilai C ke F

ketiga, tampilan hasi nila knonversi ini ke user
"""

print("Program konversi suhu dari C ke F\n")

celsius = input("Masukkan input dari Celsius = ")

konversi = float(celsius) * 9/5 + 32

print(f"Hasil dari konversi dari C {celsius} ke fahrenheit adalah {konversi}")

