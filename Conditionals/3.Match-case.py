"""
Metode ini sangat berguna saat Anda ingin emncocokkan satu nilai variabel
dengan banyak pilihan nilai/pola(pattern)
"""

# Contoh Dasar
perintah = "start"

match perintah:
    case "start":
        print("Sistem mulai berjalan...")
            # Menggunakan operator OR (|) untuk beberapa pilihan
    case "stop" | "pause":
        print("Sistem dihentkan atau ditangguhkan.")
            # Simbol underscore (_) bertindak sebagai wildcard / default case
    case _:
        print("Perintah tidak dikenali.")


# Contoh Guard
status_code = 404

match status_code:
    case 200:
        print("OK / Berhasil")
    case code if code >= 400 and code < 500:
        print(f"Client Error dengan kode: {code}")
    case code if code >= 500:
        print(f"Sever Error dengan kode: {code}")
    case _:
        print("Kode status tidak diketahui.")