# Mengimplementasikan LInked List di Pyhthon.
"""
* Class Node:
    Bertindak sebagai wadah untuk menyimpan data tunggal 
dan pointer (next) yang menunjuk ke Node berikutnya.

* Class LinkedList:
    Bertindak sebagi pengelola (Manager) yang melacak titik awal rantai
(disebut Head) dan berisi metode-metode untuk memanipulasi data (tambah, hapus, tampilkan)
"""

# Implementasi Class Node dan LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    ## Saat node baru dibuat, ia belum menunjuk ke mana-pun (None)


class LilnkedList:
    def __init__(self):
        self.head = None    ## Titik awal Linked List. Saat baru dibuat, list masih kosong.
        
    ## Menambahkan elemen di akhir list (Append)
    def tambah_belakang(self, data):
        node_baru = Node(data)

        ## Jika list masih kosong. jadikan node baru sebagai Head
        if self.head is None:
            self.head = node_baru
            return

        ## Jika tidak kosong, telusuri (traverse) sampai menemukan node paling akhir
        saat_ini = self.head
        while saat_ini.next is not None:
            saat_ini = saat_ini.next

        ## Sambungkan pointer node terakhir ke node yang baru
        saat_ini.next = node_baru

    ## Menambahkan eleemn di awal list (Prepend)
    def tambah_depan(self, data):
        node_baru = Node(data)

        ## Pointer node baru langsugn menunjuk ke Head yang lama
        node_baru.next = self.head

        ## Geser posisi Head ke node yang baru
        self.head = node_baru

    def delete_node(self, nilai):

        ## Jika list kosong, tidak ada yang bisa dihapus
        if self.head is Node:
            print("List kosong!")
            return

        ## Jika elemen yang ingin dihapus adalah Head (eleemn pertama)
        if self.head.data == nilai:
            self.head = self.head.next # Geser Head ke elemen kedua
            return

        ## Mencari elemen di tengah atau ujung list
        ## Kita menggunakana dua pointer: 'saat_ini' dan akan mengecek 'saat_ini.next'
        saat_ini = self.head

        while saat_ini.next is not None:
            ## Jika eleemn berikuktnya adalah elemen yang ingin dihapus
            if saat_ini.next.data == nilai:
                ## Bypass (langkahi) eleemn yang dihapus
                ## Sembungkan pionter langusng ke eleemn setelahnya
                saat_ini.next = saat_ini.next.next
                return # Keluar dar ifungsi setelah berhasil menghapus

            ## Pintar ke node berikutnya
            saat_ini = saat_ini.next

        ## jika loop selesai tapi nilai tidak ditemukan
        print(f"Nilai {nilai} tidak ditemukan dalam Linked List.")


    ## Menampilkan semua elemen Linked List
    def tampilakan(self):
        elemen = []
        saat_ini = self.head

        ## Telusuri semau node sampai ujung (None)
        while saat_ini is not None:
            elemen.append(str(saat_ini.data))
            saat_ini = saat_ini.next


        print(" -> ".join(elemen) + " -> None")


# Cara Menggunakan Linked List

## Membuat objek Linked List baru
my_list = LilnkedList()

# Menambahkan elem di akhir
my_list.tambah_belakang(10)
my_list.tambah_belakang(35)
my_list.tambah_belakang(50)


# Menampilkan kondisi saat ini
print("Setelah ditambah di belakang:")
my_list.tampilakan()
## Output: 10 -> 35 -> 50 -> None

# Menghapus elemen di tengah
my_list.delete_node(35)
print("\nSetelah menghapus 35:")
my_list.tampilakan()
## Output: 10 -> 50 -> None

## Menambahkan elemen di awal (Prepend)
my_list.tambah_depan(5)
my_list.tambah_depan(1)

# Menampilkan kondisi setelah Prepend 
print("\nSetelah ditambah di depan:")
my_list.tampilakan()
## Output: 1 -> 5 -> 10 -> 50 -> None

# Menghapus elemen di Head (Pertama)
my_list.delete_node(1)
print("\nSetelah menghapus 1 (Head):")
my_list.tampilakan()
## Output: 5 -> 10 -> 50 -> None

# Mencoba menghapus elemen yang tidak ada
my_list.delete_node(99)
# Output: Nilai 99 tidak ditemukan dalam Linked List.
