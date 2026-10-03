
try:
    angka = int(input("Masukkan Angka: "))
    hasil = 100 / angka

except ValueError:
    print("Masukkan angka")
except ZeroDivisionError:
    print("Angka jangan nol")
else:
    print(f"Perhitungan sukses! Hasilnya adalah {hasil}")
finally:
    print("HAI")