# Manajemen Kontak Sederhana

Akun_Game = {}

print("\n--- Akun Game MLBB ---")
print("1. Tambah Akun Game")
print("2. Lihat Semau Akun Game")
print("3. Cari Nama atau Id Game")
print("4. Hapus Akun Game")
print("5. Keluar")

while True:


    pilihan = input("\nMasukkan Menu (1-5): ").lower()

    match pilihan:
        case "menu":
            print("\n--- Akun Game MLBB ---")
            print("1. Tambah Akun Game")
            print("2. Lihat Semau Akun Game")
            print("3. Cari Nama atau Id Game")
            print("4. Hapus Akun Game")
            print("5. Keluar")

        case "1":
            while True:
                try:
                    print("\n--- Tambah Akun Game ---")
                    nama = input("Masukkan Nama Akun: ").strip().title()

                    if nama in ["Exit", "Keluar"]:   
                        break

                    id = input("Masukkan ID Akun: ")

                    if nama == "" and id == "":
                        print("Nama dan ID Akun tidak boleh kosong!!")
                        continue
                    elif nama == "":
                        print("Nama Akun tidak boleh kosong!!")
                        continue
                    elif id == "":
                        print("ID Akun tidak boleh kosong!!")
                        continue
                    

                    id_angka = int(id)

                    if nama in Akun_Game:
                        print(f"{nama} sudah ada di Akun Game!")
                    else:
                        Akun_Game[nama] = id_angka
                        print(f"Akun {nama} dengan ID {id_angka} berhasil ditambahkan")

                except ValueError:
                    print("Masukkan angka yg valid")

        case "2":
            print("\n--- Daftar Akun Game ---")
            
            if len(Akun_Game) == 0:
                print("Akun Game masih kosong!")
            else:
                for nama, id in Akun_Game.items():
                    print(f"{nama} : {id}")

        case "3":
            print("\n--- Cari Akun Game ---\n")
            if len(Akun_Game) == 0:
                print("Akun Game masih kosong!")
                continue
            while True:
                cari = input("\nMasukkan Nama atau ID yang dicari: ").strip()
                ketemu = False

                if cari.lower() in ['keluar', 'exit']:
                    break

                for nama, id_game in Akun_Game.items():
                    if cari.lower() in nama.lower() or cari == str(id_game):
                        print(f"Ditemukan -> Nama: {nama} | ID: {id_game}")
                        ketemu = True

                if not ketemu:
                    print(f"Data '{cari}' tidak ditemukan.")

        case "4":
            print("\n--- Hapus Akun Game ---\n")
            nama = input("Cari Nama Akun Game: ").strip().title()

            if nama in Akun_Game:
                yakin = input(f"Yakin Hapus {nama}? (y/n): ").lower()
                if yakin == "y":
                    del Akun_Game[nama]
                    print(f"{nama} berhasil dihapus")
                else: 
                    print("Batal.")
            else:
                print(f"{nama} Tidak ditemukan.")

        case "5" | "exit":
            print("\n--- Keluar ---")
            break

        case _:
            print("Perintah menu tidak valid! Ketik 'menu' untuk melihat daftar opsi....")