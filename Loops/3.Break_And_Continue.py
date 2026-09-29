"""
- break: Menghentikan dan keluar dar iloop sepenuhnya, meskipun kondisi masih bernilai True.
- continue: Melewati sisa blokk kode pada iterasi saat ini, dan langsung melompat ke iterasi berikutnya.
"""

# Contoh break dan continue:

for angka in range(1, 10):
    if angka == 3:
        continue    # Lewati angka 3, jangan dicetak
    if angka == 7:
        break       # Hentikan loop sepenuhnya saat mencapai 7

    print(angka)
# Output: 1, 2, 4, 5, 6