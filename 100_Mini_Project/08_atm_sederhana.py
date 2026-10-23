# ATM Sederhana

saldo = 500000

while True:
    print("\n=== ATM SEDERHANA ===")
    print("1. Cek saldo")
    print("2. Tarik saldo")
    print("3. Setor saldo")
    print("4. Keluar")
    pilihan = input("\nMasukkan Opsi Menu(1-4): ")
    print("-" * 25)

    match pilihan:
        case "1":
            print("Lihat Saldo Yang Tersisa")
            print(f"Saldo: {saldo:,}")

        case "2":
            try:
                print("Tarik Uang dari Saldo")
                tarik = int(input("Masukkan Jumlah Yang Ingin Di Tarik: "))
                if tarik > saldo:
                    print("Saldo tidak cukup untuk ditarik! Kurangin nominal penarikan")
                    continue
                if tarik <= 0:
                    print("Tidak Boleh Bawah angka 0!!")
                    continue
                
                saldo = saldo - tarik 
                print(f"Hasil Saldo: {saldo:,}")

            except ValueError:
                print("Hanya Angka!!")
                continue

        case "3":
            try:
                print("Setor Uang ke Dalam Saldo")
                setor = int(input("Masukkan Jumlah Yang Ingin di Setorkan: "))        
                saldo = saldo + setor
                print(f"Hasil Setor Saldo: {saldo:,}")
                if setor <= 0:
                    print("Tidak Boleh Bawah angka 0!!")
                    continue
            except ValueError:
                print("Hanya Angka!!")
                continue

        case "4":
            print("Keluar dari Aplikasi")
            break

        case _:
            print("Tidak Valid!!")