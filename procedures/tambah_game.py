import os
from rich import print
from functions.arraytools import *


def extract_integer(string):
    # Mengambil elemen bilangan dari string dengan format GAMEXXX

    # KAMUS LOKAL
    # ratusan, puluhan, satuan : integer

    # ALGORITMA
    ratusan = int(string[-3]) * 100
    puluhan = int(string[-2]) * 10
    satuan = int(string[-1])

    return ratusan + puluhan + satuan


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

    last_gameid = extract_integer(game[-1][0])
    new = ['','','','','','']               # Inisialisasi array new

    input_game()
    while is_subset([''], new):
        os.system("cls")
        print("\n[red]Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        input_game()
    game += [new]           # Menambahkan array new ke dalam game

    return
