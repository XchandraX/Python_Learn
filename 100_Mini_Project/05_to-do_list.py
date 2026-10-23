# To-Do List

Catatan = []

print("1. Tambah Tugas")
print("2. Lihat Tugas")
print("3. Tandai Selesai")
print("4. Hapus Tugas")
print("5. Keluar")

while True:
    pilihan = input("\nMasukkan Menu(1-5): ").lower()

    match pilihan:
        case "Menu":
            print("1. Tambah Tugas")
            print("2. Lihat Tugas")
            print("3. Tandai Selesai")
            print("4. Hapus Tugas")
            print("5. Keluar")


        case "1":
            print("\n--- TAMBAH TUGAS ---\n")
            nama_tugas = input("Masukkan nama tugas: ")
            Catatan.append(nama_tugas)
            print(f"--- Catatan berhasil ditambahkan ---")


        case "2":
            print("\n--- DAFTAR TUGAS ---\n")
            if not Catatan:
                print("Belum ada tugas.")
            else:
                for i, t in enumerate(Catatan, 1):
                    print(f"{i}, {t}")


        case "3":
            print("\n--- Tandai selesai ---\n")
            if not Catatan:
                print("Daftar Catatan kosong.")
            else:
                for i, t in enumerate(Catatan, 1):
                    print(f"{i}, {t}")

                print("\nStatus pilihan: Selesai | Pending | Gagal")
                pilihan = input("Pilih status baru: ").title()

                if pilihan in ["Keluar", "Exit"]:
                    break

                if pilihan in ["Selesai", "Pending", "Gagal"]:
                    try:
                        index = int(input(f"Pilihan nomor Catatan yang akan [{pilihan.upper()}]: ")) - 1

                        if 0 <= index < len(Catatan):
                            teks_asli = Catatan[index]
                            for status_lama in ["[SELESAI]", "[PENDING]", "[GAGAL]"]:
                                if teks_asli.startswith(status_lama):
                                    teks_asli = teks_asli.replace(status_lama, "")

                            Catatan[index] = f"[{pilihan.upper()}] " + teks_asli
                            print(f"Catatan berhasil ditandai sebagai {pilihan}")
                        else:
                            print("Nomor Catatan tidak valid.")
                    except ValueError:
                        print("Masukkan harus berupa angka nomor catatan.")
                else:
                    print("Pilihan status tidak valid. Pilih antara Selesai, Pending, Gagal")

                            
        case "4":
            print("\n--- HAPUS TUGAS ---\n")
            if not Catatan:
                print("Daftar Catatan kosong.")
            else:
                for i, t in enumerate(Catatan, 1):
                    print(f"{i}, {t}")

                pilihan = input("Pilih nomor Catatan yang akan dihapus: ").lower()

                if pilihan in ['exit']:
                    print("Penghapusan dibatalkan")
                    continue 
                try:
                    index = int(pilihan) - 1
                    if 0 <= index < len(Catatan):
                        dihapus = Catatan.pop(index)
                        print(f"Catatan '{dihapus}' berhasil dihapus!")
                    else:
                        print("Nomor Catatan tidak valid.")
                except ValueError:
                    print("Input tidak valid! Harap masukkan angka atau ketik 'exit'")

        case "5" | "exit":
            print("Keluar dari program. Sampai jumpa!")
            break

        case _:
            print("Pilihan tidak valid. Ketik 'menu' untuk melihat daftar")
        