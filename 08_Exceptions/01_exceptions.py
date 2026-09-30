"""
Exception
error yang terjadi ketika program sedang berjalan(runtime), misalnya saat membagi angka dengan nol,
membuka file yg tidak ada, atau memasukkan huruf saat program meminta angka.
"""

"""
Jika exception tidak ditangani, program akan langsung terhenti(crash) dan menampilkan pesan error merah/kuning.
Untuk mencegah hal ini dan membuat program gagal secara anggun(fail gracefully),
Python menggunakan struktur blok `try`, `except`, `else` dan `finally`.
"""

# Komponen Utama Exception Handling
"""
*try: Blok yang berisi kode utama kita. Python akan "mencoba" menjalankan kode ini.
    Jika terjadi error, eksekusi di blok ini langsung dihentikan dan dilempar ke blok except.

*except: Blok yang berfungsi sebagai "jaring pengaman". 
    Kode di sini hanya akan dijalankan jika terjadi error di dalam blok try.    

*else: Blok opsional yang hanya dijalankan jika kode di block try 
    berhasil dieksekusi tanpa ada error sama sekali

*finally: Blok opsional yang selalu dieksekusi pada akhir proses, tidak peduli apakah 
    terjadi error atau tidak. Ini sangat berguna untuk "bersih-bersih"
    (misalnya menutup file atau memutuskan koneksi database).
"""

# Contoh Penggunaan Lengkap

try:
    # Meminta input dari pengguna dan mencoba melakukan pembagian
    angka = input("Masukkan angka pembagi untuk 100: ")
    pembagi = int(angka)
    hasil = 100 / pembagi

# Menangkap error spesifik jika input bukan angka (misal huruf "A")
except ValueError:
    print("Error: Input tidak valid. Anda harus memasukkan angka!")

# Menangkap error spesifik jika pengguna memassukkan angka 0
except ZeroDivisionError:
    print("Error: Tidak bisa melakukan pembagian dengan angka nol!")

# Menangkap semua error lain yang tidak terduga
except Exception as e:
    print(f"Terjadi erro yang tidak diketahui: {e}")

# Dieksekusi hanya jika TIDAK ADA error di blok try
else:
    print(f"Perhitungan sukses! Hasilnya adalah {hasil}")

# Selalu dieksekusi di akhir proses
finally:
    print("Selesai: Blok finally dieksekusi.")