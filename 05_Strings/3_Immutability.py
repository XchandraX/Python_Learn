# Anda akan mendapatkan error jika mencoba mengubah karakter tertentu secara langsung.

bahasa = "Python"
print(bahasa)
# bahasa[0] = "J" <-- TypeError: 'str' object does not support item assignment

print("\nImmutability: ")
# Cara yang benar: Buat string baru
bahasa_baru = "J" + bahasa[1:]
print(bahasa_baru)  # Output: Jython