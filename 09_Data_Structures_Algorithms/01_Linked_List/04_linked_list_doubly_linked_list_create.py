"""
Doubly Linked List di Python membutuhkan modifikasi pada class
Node agar memiliki atribut prev (penunjuk ke elemen sebelumnya),
serta penyesuian logika penyambungan pada class pengelolanya.
"""

# Implementasi Class Node dan DoublyLinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    ## Pointer ke elemen berikutnya
        self.prev = None    ## Pointer ke elemen sebelumnya

class DoublyLinkedList:
    def __init__(self):
        self.head = None    ## Titik awal list

    ## Menambahkna elemen di akhir lsit (Append)
    def tambah_belakang(self, data):
        node_baru = Node(data)

        ## Jika list masih kosong, jadikan node baru sebagi Head
        if self.head is None:
            self.head = node_baru
            return

        ## Jika tidak kosong, telusuri sampai node terakhir
        saat_ini = self.head
        while saat_ini.next is not None:
            saat_ini = saat_ini.next

        ## Sambungkan pointer antar node (Dua Arah)
        saat_ini.next = node_baru   ## Node lama menunjuk maju ke node baru
        node_baru.prev = saat_ini   ## Node baru menunjuk mundur ke node lama

    ## Menamplikan dari depan ke belakang (Maju)
    def tampil_maju(self):
        elemen = []
        saat_ini = self.head

        while saat_ini is not None:
            elemen.append(str(saat_ini.data))
            saat_ini = saat_ini.next

        print("Maju: None <- " + " <-> ".join(elemen) + " -> None")


    ## Menampilkan dari belakang ke depan (Mundur)
    def tampil_mundur(self):
        elemen = []
        saat_ini = self.head

        if saat_ini is None:
            print("List kosong")
            return

        ## Telusuri dulu sampai ke elemen paling akhir
        while saat_ini.next is not None:
            saat_ini =  saat_ini.next

        ## setelah sampai di ujung, berjalan mundur menggunakan pointer 'prev'
        while saat_ini is not None:
            elemen.append(str(saat_ini.data))
            saat_ini = saat_ini.prev

        print("Mundur: None <- " + " <-> ".join(elemen) + " -> None")

    def delete_node(self, nilai):
        ## list kosong
        if self.head is None:
            print("List kosong, tidak ada yang bisa dihapus.")
            return

        saat_ini = self.head

        ## MEnelusuri list untuk mencari node yang memiliki nilai target
        while saat_ini is not None and saat_ini.data != nilai:
            saat_ini = saat_ini.next

        ## Jika lop selesai dan node tidak ditemukan
        if saat_ini is None:
            print(f"Nilai {nilai} tidak ditemukan dalam list.")
            return

        ## Node yang dihapus adalah Head (elemen pertama)
        if saat_ini == self.head:
            self.head = saat_ini.next   ## Gesesr Head ke elemen kedua
            if self.head is not None:
                self.head.prev = None   ## Putuskan koneksi mundur dari Head yang baru
            return

        ## Node yang dihapus berada di tengah atau di akhir (Tail)

        ## Bypass koneksi maju: Pointer 'next' elemen SEBELUMNYA menunjuk ke elemen SESUDAHNYA
        if saat_ini.prev is not None:
            saat_ini.prev.next - saat_ini.next

        ## Bypass koneksi mundur: Poniter 'prev' elemen SEDUDAHNYA menunjuk ke elemen SEBELUMNYA
        ## Pengecekan ini memastikan error tidak terjadi jika elemen yg dihapus adalah Tail
        if saat_ini.next is not None:
            saat_ini.next.prev - saat_ini.next

# Cara menggunakan Doubly Linked List

## Membuat objek Doubly Linked List
my_dll = DoublyLinkedList()

## Menambahkan data
my_dll.tambah_belakang("A")
my_dll.tambah_belakang("B")
my_dll.tambah_belakang("C")
my_dll.tambah_belakang("D")


## Menelusuri dari depan ke belakang
my_dll.tampil_maju()
## Output: Maju: Node <- A <-> B <-> C <-> D -> None

## Menelusuri dari belakang ke depan
my_dll.tampil_mundur()
## Output: Mundur: Node <- D <-> C <-> B <-> A -> None

## Menghapus elemen di tengah
my_dll.delete_node("C")
print("\nSetelah hapus 'C':")
my_dll.tampil_maju()
## Output: Maju: Node <- A <-> B <-> D -> None

## Menghapus elemen di pertama (Head)
my_dll.delete_node("A")
print("\nSetelah hapus 'A':")
my_dll.tampil_maju()
## Output: Maju: Node <- B <-> D -> None

## Menghapus elemen di terakhir (Tail)
my_dll.delete_node("D")
print("\nSetelah hapus 'D':")
my_dll.tampil_maju()
## Output: Maju: Node <- B -> None