"""
Function
fondasi untuk meluis kode yang bershi, terstruktur, dan tidak berulang (Don't Repeat Yourself / DRY)

Dengan membungkus seubah blok kode ke dalam fungsi, Kita daapt menjalankan tugas yang sama berkali-kali
dari berbagai bagian program hanya dengan "memanggil" nama fungsi tersebut
"""

# Global 

def space():
    print("\n--------------------\n")

# Membuat dan Memanggil Fungsi Dasar
"""
function dideklarasikan menggunakaan kata kunci `def` diikuti dengan nama fungsi
(menggunakan format snak_case), tanda kurung (), dan titik dua :
"""

## Mendefinisikan fungsi
def sapa_pengguna():
    print("Halo! Selamat datang di program Python.")

## Memanggil fungsi
sapa_pengguna()


space()

# Parameter dan Argumen (Memberikan Input ke Fungsi)
"""
Variable di dalam tanda kurung saat fungsi dibuat disebut Parameter,
sedangkan data akrual yg dimasukkan saat fungsi dipanggil disebut Argumen.
"""
def perkenalan(nama, umur):
    print(f"Nama saya {nama} dan saya berumur {umur} tahun.")

# Memanggil fungsi dengan argumen
perkenalan("Budi", 25)
perkenalan("Siti", 22)


space()

# Mengembalikan Nilai (return)
"""
function sering kali digunakan untuk melakukan perhitungan dan mengembalikan hasil akhir ke program utama.
Kata kunci return digunakan untuk mengirim nilai kembali, sekaligus menghentikan eksekusi fungsi tersebut.
"""

def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas # print("Teks ini tidak akan pernah dieksekkusi karena berada setelah return")

# Menyimpan hasil funsi ke dalam variable
hasil_luas = hitung_luas_persegi(39)
print(f"Luas persegi adalah {hasil_luas}")


space()

# Paremeter Default (Default Arguments)
"""
Memberikan nilai bawaan (default) pada parameter. Jika argumen tidak diberikan saat fungsi
"""

def sapa(nama, ucapan="Selamat Pagi"):
    print(f"{ucapan}, {nama}!")

sapa("Andi")                    # Output: Selamat Pagi, Andi!
sapa("Andi", "Selamat Malam")   # Output: Selamat Malam, Andi!


space()

# Argumen Fleksibel (*args dan **kwargs)
"""
Tidak tahu pasti berapa banyak argumen yang akan dikirimkan ke dalam fungsi.
Pyhton memiliki solusi elegan untuk ini:

*args (Arbirary Positional Arguments)   : Menerima banyak argumen tanpa nama sebagai sebuah Tuple.
**kwargs (Arbirary Keyword Arguments)   : Menerima banyak arumen dengan nama (key-value) sebagai sebuah Dictionary.
"""

## Contoh menggunakan *args
def hitung_total(*angka):
    total = 0
    for n in angka:
        total += n
    return total

print(hitung_total(10, 20, 30)) # Output: 60
print(hitung_total(5, 5))       # Output: 10

## Contoh menggunakan **kwargs
def data_karyawan(**info):
    for kunci, nilai in info.items():
        print(f"{kunci.capitalize()}: {nilai}")

data_karyawan(nama="Andi", divisi="Keuangan", lokasi="Jakarta")
