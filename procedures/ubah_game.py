from rich import print
from functions.arraytools import find_index_matriks, update_data


def ubah_game(game):
    # I.S. Array game terdefinisi
    # F.S. Data pada game ada/tidak ada yang diubah

    # KAMUS LOKAL
    # gameID, nama_game, kategori, tahun_rilis, harga : string
    # indeks : integer

    # ALGORITMA
    gameID = input("\nMasukkan ID game: ")
    indeks = find_index_matriks(gameID, game, 0)      # Indeks game pada array. Jika tidak ditemukan, indeksnya -999

    if indeks >= 0:
        # Mengubah data pada array game sesuai input
        game[indeks][1] = update_data(input("Masukkan nama game: "), game[indeks][1])
        game[indeks][2] = update_data(input("Masukkan kategori: "), game[indeks][2])
        game[indeks][3] = update_data(input("Masukkan tahun rilis: "), game[indeks][3])
        game[indeks][4] = update_data(input("Masukkan harga: "), game[indeks][4])

        print("\n[green]Data berhasil diubah!")
    else:  # indeks < 0
        print("[red]ID game tidak valid.")

    return