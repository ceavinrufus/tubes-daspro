import os
from functions.arraytools import *
from interface import displaytable
from rich import print


def search_user_game(kepemilikan, game, userindex):
    # Fungsi yang mereturn data game yang dimiliki user

    # KAMUS LOKAL
    # usergame, game_found : array of array
    # temp : array

    # ALGORITMA
    usergame = filtering(str(userindex + 1), 1, kepemilikan)    # Mencari daftar game yang dimiliki user pada array kepemilikan

    game_found = []
    for gameid in usergame:                                     # Array yang akan berisi data game yang dimiliki user
        temp = filtering(gameid[0], 0, game)[0]                 # Pencarian data game berdasarkan ID game
        game_found += [popped(temp, -1)]                        # Menambahkan array data game (tanpa data stok)

    return game_found


def list_game(kepemilikan, game, userindex):
    # I.S. Array kepemilikan, game, dan integer userindex terdefinisi
    # F.S. Menampilkan tabel hasil filtering search pada game yang dimiliki user

    # KAMUS LOKAL
    # result : array of array
    # header : array
    # title : string

    # ALGORITMA
    result = search_user_game(kepemilikan, game, userindex)     # Hasil pencarian data game yang dimiliki user

    title = "Daftar Game pada Inventori"
    header = ["GAME ID", "NAMA", "KATEGORI", "TAHUN RILIS", "HARGA"]

    if panjang(result) == 0:
        print("\n[red]Maaf, kamu belum membeli game. Ketik [bold]buy_game[/bold] untuk beli!")
        return

    os.system("cls")
    displaytable(header, result, title=title)               # Menampilkan tabel

    return
