# Dari sebuah list angka [12, 45, 3, 67, 23, 89, 5], 
# buat list comprehension baru yang isinya cuma angka yang lebih besar dari 20.

angka = [12, 45, 3, 67, 23, 89, 5]

angka_besar = [x for x in angka if x > 20]
print(angka_besar)