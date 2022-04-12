from functions.arraytools import *
from functions.formulas import absolute

def ubah_stok(game):
    # I.S. Array game sudah terdefinisi
    # F.S. Elemen stok ([5]) ditambahi/dikurangi sesuai masukan admin

    # KAMUS LOKAL
    # id : string
    # jumlah, stok : integer
    # found : boolean

    # ALGORITMA
    id = input("Masukkan ID game: ")
    jumlah = int(input("Masukkan jumlah: "))

    # Pencarian ID game sesuai input pada array game
    found = False
    i = 0
    while i < panjang(game) and not found:
        if game[i][0] == id:
            found = True
        else:
            i += 1

    if found:
        stok = int(game[i][5])      # Variabel sementara untuk menampung nilai integer dari stok pada array
        if jumlah < 0 and stok >= absolute(jumlah):     # Jika stok dikurangi dan stok mencukupi
            stok += jumlah
            print("Stok game {} berhasil dikurangi. Stok sekarang: {}".format(game[i][1], stok))
        elif jumlah < 0 and stok < absolute(jumlah):    # Jika stok dikurangi tetapi stok tidak mencukupi
            print("Stok game {} gagal dikurangi karena stok kurang. Stok sekarang: {} (< {})".format(game[i][1], stok,
                                                                                                      absolute(jumlah)))
        else: # jumlah >= 0
            stok += jumlah
            print("Stok game {} berhasil ditambahkan. Stok sekarang: {}".format(game[i][1], stok))
        game[i][5] = str(stok)      # Mengembalikan nilai stok pada array dalam bentuk string
    else:
        print("Tidak ada game dengan ID tersebut!")
