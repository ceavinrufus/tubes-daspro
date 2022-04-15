import os
from functions.arraytools import *
from procedures.interface import displaytable
from rich import print


def search_game_at_store(game):
    # I.S. Array game terdefinisi
    # F.S. Menampilkan tabel hasil filtering search pada game pada toko

    # KAMUS LOKAL
    # result : array of array
    # search, header : array
    # title : string

    # ALGORITMA
    if game:
        search = ['', '', '', '', '']                       # Array untuk menyimpan filter yang diinput pengguna
        search[0] = stripping(input("\nMasukkan ID game: ").upper())
        search[1] = stripping(input("Masukkan nama game: "))
        search[2] = stripping(input("Masukkan kategori game: "))
        search[3] = stripping(input("Masukkan tahun rilis game: "))
        search[4] = stripping(input("Masukkan harga game: "))

        result = game
        for by in range(panjang(search)):                   # Looping array search untuk memfilter array game
            result = search_by(search[by], by, result)      # Hasil filtering disimpan pada array result

        title = "Daftar Game pada Toko yang Memenuhi Kriteria"
        header = ["GAME ID", "NAMA", "KATEGORI", "TAHUN RILIS", "HARGA", "STOK"]

        if not result:
            print("\n{}".format(title))
            print("[red]Tidak ada game pada toko yang memenuhi kriteria.")
            return

        os.system("cls")
        displaytable(header, result, title=title)           # Menampilkan tabel
    else:
        print("\n[red]Tidak ada game pada toko.")

    return
