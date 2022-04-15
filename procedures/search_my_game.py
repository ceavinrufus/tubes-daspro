import os
from functions.arraytools import *
from procedures.interface import displaytable
from procedures.list_game import search_by_id


def search_my_game(kepemilikan, game, userindex):
    # I.S. Array kepemilikan, game, dan integer userindex terdefinisi
    # F.S. Menampilkan tabel hasil filtering search pada game yang dimiliki user

    # KAMUS LOKAL
    # result : array of array
    # search, header : array
    # title : string

    # ALGORITMA
    search = ['', '', '', '', '']                   # Array untuk menyimpan filter yang diinput pengguna
    search[0] = stripping(input("\nMasukkan ID game: ").upper())
    search[3] = stripping(input("Masukkan tahun rilis game: "))

    result = search_by_id(kepemilikan, game, userindex)     # Hasil pencarian data game yang dimiliki user
    for by in range(panjang(search)):                       # Looping array search untuk memfilter array result
        result = search_by(search[by], by, result)          # Hasil filtering terus diupdate selagi looping

    title = "Daftar Game pada Inventori yang Memenuhi Kriteria"
    header = ["GAME ID", "NAMA", "KATEGORI", "TAHUN RILIS", "HARGA"]

    os.system("cls")
    displaytable(header, result, title=title)       # Menampilkan tabel
