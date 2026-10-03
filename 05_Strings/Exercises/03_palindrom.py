kata = input("Masukkan kata: ")

kata_bersih = kata.lower()
kata_terbalik = kata_bersih[::-1]

if kata_bersih == kata_terbalik:
    print(f'"{kata}" adalah palindrom.')
else:
    print(f'"{kata}" bukan palindrom.')