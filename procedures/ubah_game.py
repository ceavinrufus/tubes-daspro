from rich import print
from functions.arraytools import find_index_matriks, update_data


def ubah_game(game):
    # I.S. Array game terdefinisi
    # F.S. Data pada game ada/tidak ada yang diubah

    # KAMUS LOKA
    # gameID, nama_game, kategori, tahun_rilis, harga : string
    # indeks : integer

    # ALGORITMA
    gameID = input("\nMasukkan ID game: ")
    indeks = find_index_matriks(gameID, game, 0)      # Indeks game pada array. Jika tidak ditemukan, indeksnya -999

    if indeks >= 0:
        # Mengubah data pada array game sesuai input
        nama_game = update_data(input("Masukkan nama game: "), game[indeks][1])
        kategori = update_data(input("Masukkan kategori: "), game[indeks][2])
        try:
            tahun_rilis = update_data(int(input("Masukkan tahun rilis: ")), game[indeks][3])
            harga = update_data(int(input("Masukkan harga: ")), game[indeks][4])
        except ValueError:
            print("[red]Input harus berupa integer!")
            return

        game[indeks] = [gameID, nama_game, kategori, tahun_rilis, harga, game[indeks][5]]

        print("\n[green]Data berhasil diubah!")
    else:  # indeks < 0
        print("[red]ID game tidak valid.")

    return