"""
Type Annotations (Type Hints)
cara untuk menambahkan informasi(metadata) mengenai tipe data apa yg diharapkan dari sebuah variabel,
parametner fungsi, atau nilai kembalian (return value).
"""

# Anotasi pada Fungsi

## Fungsi ini mengharapkan dua parameter berjenis integer 
## dan berjanji akan mengembalikan nilai berjenis integer

def tambah(a: int, b: int) -> int:
    return a + b

# Memanggil fungsi
hasil = tambah(10, 5)
print(hasil)

## Jika Anda melakukan ini Python TETAP akan menjalankannya tanpa error saat runtime,
## teatpi IDE atau linter (seperti mypy) akan memberi garis bawah merah/peringatan.
hasil_salah = tambah("10", "5")
print(hasil)


# Anotasi pada Variable Dasar
umur: int = 25
nama: str = "Budi Santoso"
is_aktif: bool = True
harga: float = 99.99



# Anotasi untuk Struktur Data Koleksi

## List yang HANYA berisi string
nama_siswa: list[str] = ["Andi", "Siti", "Budi"]

## Dictionary dengan key berupa string dna Value berupa integer
nilai_ujian: dict[str, int] = {"Matematika": 90, "Fisika": 85}

## Tuple yang secara berurutan berisi (string, integer, float)
koordinat_lokasi: tuple[str, int, float] = ("Jakarta", 101, -6.2)


# Tipe Fleksibel (Union dan Opsional)
"""
fungsi bisa menerima lebih dari satu tipe data atau bisa menerima nilai kosong (None).
Kita bisa menggunakan operator pemisah | (OR) untuk menanganis hal ini.
"""
# Parameter 'data' bisa berupa integer ATAU float
def hitung_diskon(harga: int | float, diskon: float) -> float:
    return harga - (harga / diskon)

print(hitung_diskon(50000, 10))

# Parameter 'nama' bisa berupa string, atau bisa juga None (kosong)
def sapa_user (nama: str | None = None) -> str:
    if nama is None:
        return "Halo, Tamu!"
    return f"Halo, {nama}!"

print(sapa_user("Budi"))
print(sapa_user())