def safe_divide(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print(f"Angka tidak boleh nol")
    else:
        print(f"Hasil dari pembagian adalah: {hasil}")

safe_divide(54, 6)