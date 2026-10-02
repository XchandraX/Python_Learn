print("""Perintah untuk Note :
1. Tambah
2. Kurang
3. Keluar
""")

perintah = input("Masukkan printah: ")

match perintah:
    case "tambah" | "Tambah":
        print("Tambah Note")
    case "Kurang" | "kurang":
        print("Kurang Note")
    case "Keluar" | "keluar":
        print("Keluar")
