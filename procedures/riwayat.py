from rich import print
from interface import displaytable
from functions.arraytools import *


def riwayat(userindex, history):
    # I.S. userindex dan history sudah terdefinisi
    # F.S. Menampilkan tabel riwayat user

    # KAMUS LOKAL
    # userhistory : array of array of string
    # temp, header, found : array
    # title : string

    # ALGORITMA
    if panjang(history) > 0:
        userhistory = filtering(str(userindex + 1), 3, history)  # Mencari daftar riwayat yang dimiliki user pada array riwayat

        found = []
        for historyid in userhistory:                          # Array yang akan berisi data riwayat yang dimiliki user
            temp = filtering(historyid[0], 0, history)[0]      # Pencarian data riwayat berdasarkan game ID
            found += [popped(temp, 3)]                         # Menambahkan array data history (tanpa data user_id)

        title = "Daftar Game"
        header = ["ID", "NAMA GAME", "HARGA", "TAHUN BELI"]

        displaytable(header, found, title)
    else:   # panjang(riwayat) <= 0
        print("\n[red]Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah [bold]beli_game[/bold] untuk membeli.")

    return
