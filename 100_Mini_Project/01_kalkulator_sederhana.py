# !TODO
# Project pertamaku Membuat Kalkulator Sederhana

print("==============================")
print("     KALKULATOR SEDERHANA     ")
print("==============================")

print("""
Operator yang ada:
Tambah          : +
Kurang          : -
Kali            : *
Bagi            : /
Sisa Bagi       : %
Semua Operasi   : All
""")


#########################
# PENGULANGAN INPUT
#########################

print("==============================")
print("    Masukkan Angka Pertama:   ")
print("==============================")
while True:
    try:
        angka_A = float(input(""))
        break
    except ValueError:
        print('"Masukkan Angka yang Valid untuk angka pertama!!"')


print("\n==============================")
print("      Masukkan Operator:      ")
print("==============================")
while True:
    operasi = input("")
    if operasi not in ["+", "-", "*", "/", "%", "All"]:
        print('"Masukkan Operasi angka yg benar"')
    else:
        print('"Operasi benar"')
        break


print("\n==============================")
print("     Masukkan Angka Kedua:    ")
print("==============================")
while True:
    try:
        angka_B = float(input(""))
        break
    except ValueError:
        print('"Masukkan Angka yang Valid untuk angka kedua!!"')

#########################
# PENGULANGAN INPUT (END)
#########################


#########################
# FUNGSI OPERASI
#########################

def tambah(a, b):
    hasil = a + b
    return hasil

def kurang(a, b):
    hasil = a - b
    return hasil

def kali(a, b):
    hasil = a * b
    return hasil

def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError: 
        return ("Angka Nol Tidak bisa bagi")
    else:
        return hasil
    
def sisa_bagi(a, b):
    try:
        hasil = a % b
    except ZeroDivisionError: 
        return ("Angka Nol Tidak bisa bagi")
    else:
        return hasil

#########################
# FUNGSI OPERASI (END)
#########################


#########################
# HASIL
#########################

if operasi not in ["All"]:
    print("\n==============================")
    print(f"        HASIL OPERATOR:      ")
    print("==============================")
    if operasi == "+":
        print(f"Tambah    : {tambah(angka_A, angka_B)}")
    elif operasi == "-":
        print(f"Kurang    : {kurang(angka_A, angka_B)}")
    elif operasi == "*":
        print(f"Kali      : {kali(angka_A, angka_B)}")
    elif operasi == "/":
        print(f"Bagi      : {bagi(angka_A, angka_B)}")
    elif operasi == "%":
        print(f"Sisa Bagi : {sisa_bagi(angka_A, angka_B)}")

else:
    print("\n==============================")
    print("     HASIL SEMUA OPERATOR:    ")
    print("==============================")
    print(
f"""Hasil Tambah adalah: {tambah(angka_A, angka_B)}
Hasil Kurang : {kurang(angka_A, angka_B)}
Hasil Kali   : {kali(angka_A, angka_B)}
Hasil Bagi   : {bagi(angka_A, angka_B)}
Sisa  Bagi   : {sisa_bagi(angka_A, angka_B)}""")

#########################
# HASIL (END)
#########################