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
        angka_A = int(input(""))
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
        angka_B = int(input(""))
        break
    except ValueError:
        print('"Masukkan Angka yang Valid untuk angka kedua!!"')

#########################
# PENGULANGAN INPUT (END)
#########################


#########################
# FUNGSI OPERASI
#########################

def tambah():
    hasil = angka_A + angka_B
    return hasil

def kurang():
    hasil = angka_A - angka_B
    return hasil

def kali():
    hasil = angka_A * angka_B
    return hasil

def bagi():
    try:
        hasil = angka_A / angka_B
    except ZeroDivisionError: 
        return ("Angka Nol Tidak bisa bagi")
    else:
        return hasil
    
def sisa_bagi():
    try:
        hasil = angka_A % angka_B
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
        print(f"Tambah    : {tambah()}")
    elif operasi == "-":
        print(f"Kurang    : {kurang()}")
    elif operasi == "*":
        print(f"Kali      : {kali()}")
    elif operasi == "/":
        print(f"Bagi      : {bagi()}")
    elif operasi == "%":
        print(f"Sisa Bagi : {sisa_bagi()}")

else:
    print("\n==============================")
    print("     HASIL SEMUA OPERATOR:    ")
    print("==============================")
    print(
f"""Hasil Tambah adalah: {tambah()}
Hasil Kurang : {kurang()}
Hasil Kali   : {kali()}
Hasil Bagi   : {bagi()}
Sisa  Bagi   : {sisa_bagi()}""")

#########################
# HASIL (END)
#########################