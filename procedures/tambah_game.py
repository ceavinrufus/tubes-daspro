import os
from rich import print
from functions.arraytools import *


def tambah_game(game):
    # I.S. Matriks game terdefinisi
    # F.S. Array game ditambahkan dengan data baru berupa array

    # KAMUS LOKAL
    # new : array of string
    # last_gameid : integer

    # ALGORITMA
    def input_game():
        # I.S. Array new terdefinisi
        # F.S. Array new diisi dengan data sesuai input

        # KAMUS LOKAL

        # ALGORITMA
        new[0] = "GAME{:03d}".format(last_gameid + 1)
        new[1] = stripping(input("\nMasukkan nama game: "))
        new[2] = stripping(input("Masukkan kategori: "))
        new[3] = stripping(input("Masukkan tahun rilis: "))
        new[4] = stripping(input("Masukkan harga: "))
        new[5] = stripping(input("Masukkan stok awal: "))

    if panjang(game) > 0:                                   # Memastikan apakah array game ada isinya
        last_gameid = extract_integer(game[-1][0])          # Menyimpan nilai game ID elemen game terakhir
    else:  # panjang(game) <= 0
        last_gameid = 0

    new = ['','','','','','']               # Inisialisasi array new

    input_game()
    while is_subset([''], new):             # Looping terus berjalan hingga semua input terisi
        os.system("cls")
        print("\n[red]Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        input_game()

    game += [new]           # Menambahkan array new ke dalam game
    print('\n[green]Selamat! Berhasil menambahkan game "{}"'.format(new[1]))

    return
