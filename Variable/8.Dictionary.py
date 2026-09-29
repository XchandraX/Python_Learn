"""
Dictionary: Kumpulan data tak terurut yang menyimpan informasi
dalam bentuk pasangan Key: Value (Kunci: Nilai)
Didefinisikan menggunakan kurung kurawal {}
"""


# Membuat dictionary
profil_user = {
    "username": "budi_99",
    "email": "budi@mail.com",
    "umur": 24,
    "is_active": True
}

print(profil_user)      # Output: semua profil_user

# Mengakses dan mengubah value berdasarkan Key
print(profil_user["email"])         # Output: budi@mail.com
profil_user["umur"] = 25            # Memperbarui nilai umur
profil_user["kota"] = "Kuningan"    # Menambahkan key-value baru

print(profil_user)
print(type(profil_user))    # Output: <class 'dict'>