# Inheritance (Pewarisan)
Inheritance memungkinkan sebuiah Class baru (Child) mengambil seluruh atribut dan metode dari Class yang sudah ada (Parent), ini mewujudkan prinsip DRY (Don't Repeat Yourself).
Fungsi super() digunakan oleh Child untuk memanggil metode (terutama __init__) milik Parent agar kita tidak perlu menulis ulang kodenya 

Multiple Inheritance & MRO:
Python mendukung sebuah Class memiliki lebih dar isatu Parent. Jika terjadi konflik nama metode antar Parent, Python menggunakan MRO (Method Resolution Order) -- algoritma perncarian dari kiri ke kanan, lalu dari bawah ke atas -- untuk menentukan metode nama yang akan dieksekusi duluan. Kita bisa melihatnya dengan perintah Class.mro()