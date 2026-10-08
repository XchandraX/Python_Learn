# Rekursi tidak selalu harus mengembalikan nilai matematika. Ia juga bis digunakan untuk mengeksekusi aksi yang berulang, seperti hitung mundur roket.

def hitung_mundur(angka):
    # Base Case
    if angka <= 0:
        print("Roket meluncur! 🚀🚀")
        return  # Menghentikan fungsi

    # Recursive Case
    print(angka)
    hitung_mundur(angka - 1)    # Memanggil dirinya sendiri dengan angka yang dikurangi

hitung_mundur(5)