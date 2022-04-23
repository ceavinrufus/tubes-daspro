from functions.arraytools import *
from interface import displaytable, sorting_menu
from rich import print


def list_game_toko(game):
    # Menuliskan daftar game di toko dengan sorting tahun secara menurun atau menaik sesuai input

    # KAMUS LOKAL
    # skema, sortby : string

    # ALGORITMA
    if panjang(game) > 0:
        sorting_menu()
        skema = input("\nSkema sorting: ")

        # Sorting sesuai skema sorting yang diinput
        if skema == "harga+":
            result = selection_sorted(game, 4)
        elif skema == "harga-":
            result = selection_sorted(game, 4, ascending=False)
        elif skema == "tahun+":
            result = selection_sorted(game, 3)
        elif skema == "tahun-":
            result = selection_sorted(game, 3, ascending=False)
        elif not skema:
            result = []
            for i in range(panjang(game)):
                result += [game[i] + [extract_integer(game[i][0])]]    # Menambahkan game ID dalam bentuk integer pada array
            result = selection_sorted(result, 6)                       # Sorting naik berdasarkan game ID

            for i in range(panjang(result)):
                result[i] = popped(result[i], -1)                 # Menghilangkan kembali game ID yang baru ditambahkan
        else:
            print("[red]Skema sorting tidak valid!")
            return

        title = "Daftar Game pada Toko"
        header = ["GAME ID", "NAMA", "KATEGORI", "TAHUN RILIS", "HARGA", "STOK"]

        displaytable(header, result, title)
    else:
        print("\n[red]Tidak ada game pada toko.")

    return
