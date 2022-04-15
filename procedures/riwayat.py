from rich import print
from procedures.interface import displaytable
from functions.arraytools import *


def riwayat(userindex, history):
    # I.S. userindex dan history sudah terdefinisi
    # F.S. Menampilkan tabel riwayat user

    # KAMUS LOKAL
    # userhistory, found : array of array
    # temp, header : array
    # title : string

    # ALGORITMA
    if history:
        userhistory = search_by(str(userindex + 1), 3, history)  # Mencari daftar riwayat yang dimiliki user pada array riwayat

        found = []
        for historyid in userhistory:                          # Array yang akan berisi data riwayat yang dimiliki user
            temp = search_by(historyid[0], 0, history)[0]      # Pencarian data riwayat berdasarkan game ID
            found += [popped(temp, 3)]                         # Menambahkan array data history (tanpa data user_id)

        title = "Daftar Game"
        header = ["ID", "NAMA GAME", "HARGA", "TAHUN BELI"]

        displaytable(header, found, title=title)
    else :
        print("\n[red]Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah [bold]beli_game[/bold] untuk membeli.")

    return
