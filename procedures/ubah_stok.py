from functions.arraytools import *
from functions.formulas import absolute as abso


def ubah_stok(game):
    # I.S. Array game sudah terdefinisi
    # F.S. Stok ditambah/dikurang sesuai masukan admin

    # KAMUS LOKAL
    # gameid : string
    # jumlah, stok : integer

    # ALGORITMA
    gameid = input("\nMasukkan ID game: ")
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("[red]Jumlah stok harus berupa angka!")
        return

    idx = find_index_matriks(gameid, game, 0)      # Indeks ID game yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0:
        stok = int(game[idx][5]) + jumlah                   # Nilai stok setelah diubah
        if jumlah < 0:
            if stok >= 0:                                   # Jika stok mencukupi, stok diubah
                game[idx][5] = stok
                print("Stok game {} berhasil dikurangi. Stok sekarang: {}".format(game[idx][1], stok))
            else:  # stok < 0
                print("Stok game {} gagal dikurangi. Stok sekarang: {} (< {})".format(game[idx][1], stok, abso(jumlah)))
        else:  # jumlah >= 0
            game[idx][5] = stok                             # Mengubah stok pada array
            print("Stok game {} berhasil ditambahkan. Stok sekarang: {}".format(game[idx][1], stok))
    else:  # idx < 0
        print("Tidak ada game dengan ID tersebut!")

    return
