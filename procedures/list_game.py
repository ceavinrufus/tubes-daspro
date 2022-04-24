import os
from functions.arraytools import *
from interface import displaytable
from rich import print


def list_game(kepemilikan, game, userindex):
    # I.S. Array kepemilikan, game, dan integer userindex terdefinisi
    # F.S. Menampilkan tabel hasil filtering search pada game yang dimiliki user

    # KAMUS LOKAL
    # result : array of array of string
    # header : array of string
    # title : string

    # ALGORITMA
    result = search_user_game(kepemilikan, game, userindex)     # Hasil pencarian data game yang dimiliki user

    title = "Daftar Game pada Inventori"
    header = ["GAME ID", "NAMA", "KATEGORI", "TAHUN RILIS", "HARGA"]

    if panjang(result) == 0:
        print("\n[red]Maaf, kamu belum membeli game. Ketik [bold]buy_game[/bold] untuk beli!")
        return

    os.system("cls")
    displaytable(header, result, title)               # Menampilkan tabel

    return
