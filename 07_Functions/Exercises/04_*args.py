def hitung_total(*angka):
    total = 0
    for n in angka:
        total += n
    return total

print(hitung_total(2, 6, 34))
print(hitung_total(5, 5))