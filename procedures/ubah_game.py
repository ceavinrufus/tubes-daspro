from functions.arraytools import *
from rich import print


def validId(gameID, game):
    # Fungsi yang mereturn indeks pertama kali ditemukan pada array game.
    # Jika tidak ditemukan, maka fungsi mereturn -999

    # KAMUS LOKAL

    # ALGORITMA
    for i in range(panjang(game)):
        if gameID == game[i][0]:
            return i

    return -999


def update_data(update, data):
    # Fungsi yang mengembalikan data terbaru setelah diupdate

    # KAMUS LOKAL
    # data = string

    # ALGORITMA
    if update == '':        # Jika update kosong, data tetap sama
        data = data
    else:                   # Jika update tidak kosong, data diganti dengan update terbaru
        data = update

    return data


def ubah_game(game):
    # I.S. Array game terdefinisi
    # F.S. Data pada game ada/tidak ada yang diubah

    # KAMUS LOKA
    # gameID, nama_game, kategori, tahun_rilis, harga : string
    # indeks : integer

    # ALGORITMA
    gameID = input("Masukkan ID game: ")
    indeks = validId(gameID, game)      # Indeks game pada array. Jika tidak ditemukan, indeksnya -999

    if indeks < 0:
        print("[red]ID game tidak valid.")
    else:
        nama_game = update_data(input("Masukkan nama game: "), game[indeks][1])
        kategori = update_data(input("Masukkan kategori: "), game[indeks][2])
        tahun_rilis = update_data(input("Masukkan tahun rilis: "), game[indeks][3])
        harga = update_data(input("Masukkan harga: "), game[indeks][4])

        game[indeks] = [gameID, nama_game, kategori, tahun_rilis, harga, game[indeks][5]]

        print("\n[green]Data berhasil diubah!")
