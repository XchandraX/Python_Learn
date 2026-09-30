# 1. FizBuzz - Cetak angka 1 sampai 20. Tapi kalau kelipatan 
# 3 cetak "Fizz", kelipatan 5 cetak "Buzz",
# kelipatan 3 dan 5 cetak "FizzBuzz."

"""
Pertama, Tentukan mengunakan Sintax yg digunakan

Kedua, bikin logika agar setiap kelipatan 3, 5 dan 3 and 5

Ketiga, pake for if dan range(1, 21)
""" 

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print(garis)