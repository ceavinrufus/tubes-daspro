from functions.arraytools import *
from rich import print


def ubah_stok(game):
    # I.S. Array game sudah terdefinisi
    # F.S. Stok ditambah/dikurang sesuai masukan admin

    # KAMUS LOKAL
    # gameid : string
    # jumlah, stok : integer

    # ALGORITMA
    gameid = input("\nMasukkan ID game: ")

    idx = find_index_matriks(gameid.upper(), game, 0)      # Indeks ID game yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0:
        jumlah = input("Masukkan jumlah: ")
        if not is_numeric(jumlah):
            print("\n[red]Jumlah stok harus berupa angka!")
            return
        else:
            jumlah = int(jumlah)

        stok = int(game[idx][5]) + jumlah                   # Nilai stok setelah diubah
        if jumlah < 0:
            if stok >= 0:                                   # Jika stok mencukupi, stok diubah
                game[idx][5] = stok
                print("\n[green]Stok game {} berhasil dikurangi.".format(game[idx][1]))
                print("Stok sekarang: {}".format(stok))
            else:  # stok < 0
                print("\n[red]Stok game {} gagal dikurangi.".format(game[idx][1]))
                print("Stok sekarang: {} (< {})".format(game[idx][5], abs(jumlah)))
        else:  # jumlah >= 0
            game[idx][5] = stok                             # Mengubah stok pada array
            print("\n[green]Stok game {} berhasil ditambahkan.".format(game[idx][1]))
            print("Stok sekarang: {}".format(stok))
    else:  # idx < 0
        print('\n[red]Tidak ada game dengan ID "{}".'.format(gameid))

    return
