try:
    umur = int(input("Masukkan umur: "))
except ValueError:
    print("Umur harus angka!")
else:
    print(f"Umur mu adalah {umur}")