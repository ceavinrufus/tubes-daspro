import os
from functions.arraytools import *
from interface import displaytable
from rich import print


def search_my_game(kepemilikan, game, userindex):
    # I.S. Array kepemilikan, game, dan integer userindex terdefinisi
    # F.S. Menampilkan tabel hasil filtering search pada game yang dimiliki user

    # KAMUS LOKAL
    # result : array of array string
    # search, header : array of string
    # title : string

    # ALGORITMA
    if panjang(game) > 0:
        search = ['', '', '', '', '']                   # Array untuk menyimpan filter yang diinput pengguna
        search[0] = stripping(input("\nMasukkan ID game: ").upper())
        search[3] = stripping(input("Masukkan tahun rilis game: "))

        result = search_user_game(kepemilikan, game, userindex)     # Hasil pencarian data game yang dimiliki user

        for by in range(panjang(search)):                       # Looping array search untuk memfilter array result
            result = filtering(search[by], by, result)          # Hasil filtering terus diupdate selagi looping

        title = "Daftar Game pada Inventori yang Memenuhi Kriteria"
        header = ["GAME ID", "NAMA", "KATEGORI", "TAHUN RILIS", "HARGA"]

        if panjang(result) == 0:
            print("\n{}".format(title))
            print("[red]Tidak ada game pada inventorimu yang memenuhi kriteria.")
            return

        os.system("cls")
        displaytable(header, result, title)       # Menampilkan tabel
    else:   # panjang(game) <= 0
        print("\n[red]Maaf, kamu belum membeli game. Ketik [bold]buy_game[/bold] untuk beli!")

    return
