from rich import print
from functions.arraytools import *


def ubah_game(game):
    # I.S. Array game terdefinisi
    # F.S. Data pada game ada/tidak ada yang diubah

    # KAMUS LOKAL
    # gameID, nama, kategori, tahun, harga : string
    # indeks : integer

    # ALGORITMA
    gameID = input("\nMasukkan ID game: ")
    indeks = find_index_matriks(gameID.upper(), game, 0)      # Indeks game pada array. Jika tidak ditemukan, indeksnya -999

    if indeks >= 0:
        # Mengubah data pada array game sesuai input
        nama = update_data(stripping(input("Masukkan nama game: ")), game[indeks][1])
        kategori = update_data(stripping(input("Masukkan kategori: ")), game[indeks][2])
        tahun = update_data(stripping(input("Masukkan tahun rilis: ")), game[indeks][3])
        harga = update_data(stripping(input("Masukkan harga: ")), game[indeks][4])

        if is_subset(tahun+harga, numeric):
            game[indeks] = [game[indeks][0], nama, kategori, tahun, harga, game[indeks][5]]
            print("\n[green]Data berhasil diubah!")
        else:
            print("\n[red]Data tidak valid.")
    else:  # indeks < 0
        print('[red]Tidak ada game dengan ID "{}".'.format(gameID))

    return
