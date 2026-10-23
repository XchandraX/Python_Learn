# Analaisis Teks

kalimat = input("Masukkan Kata: ")
kata_real = kalimat.lower()

daftar_kata = kata_real.split()
jumlah_kata =  len(daftar_kata)

vokal = "aiueo"
jumlah_vokal = 0
for huruf in kata_real:
    if huruf in vokal:
        jumlah_vokal += 1

kata_terbalik = kata_real[::-1]
palindrom = kata_real == kata_terbalik

print(f"\nInput: {kalimat}")
print(f"Jumlah Kata: {jumlah_kata}")
print(f"Jumlah Vokal: {jumlah_vokal}")
print(f"Dibalik: {kata_terbalik}")
print(f"Palindrom: {palindrom}")