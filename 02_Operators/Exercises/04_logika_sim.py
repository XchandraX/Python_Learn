umur = int(input("Masukkan umur: "))
punya_ktp = umur >= 17

if punya_ktp:
    print(f"Memiliki KTP")
else:
    print("Belum dewasa")