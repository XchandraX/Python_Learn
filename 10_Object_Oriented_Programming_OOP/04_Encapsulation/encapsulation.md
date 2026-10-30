# Encapsulation (Enkapsulasi & Pelindung Data)

Enkapsulasi adalah proses penyembunyikan detail internal objek dan melindunginya dari modifikasi langsung oleh pihak luar. Di Python, kita membedakan tingkat akses menggunakan garis bawah (underscore):
- Public (nama): Bisa diakses dan diubah dari mana saja.
- Protected(_gaji): Diberi satu garis bawah. Ini hanuya konvensi (kesepakatan antar programmer) yang berarti "tolong jangan akses ini dari luar, kecuali oleh class turunannya." Pyhton tidak memblokirnya secara paksa.
- Private (__pin): Diberi dua garis bawah. Python akan melakukan Name Mangling (mengubah nama variable di balik layar) sehingga benar-benar sulit diakses dari luar objek untuk mencegah modifikasi tidak sengaja.

Untuk membaca dan mengubah data Private, Kita menggunakan Getter dan Setter (di Python sangat elegan menggunakan dekorator @property).