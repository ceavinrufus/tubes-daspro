from functions.arraytools import *
from rich import print
from datetime import date


def buy_game(userindex, user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. Melakukan pembelian game dan kemudian mengupdate data user, game, kepemilikan, dan riwayat

    # KAMUS LOKAL
    # gameID, nama, tahun : string
    # idx, stok, harga, saldo : integer
    # punya : boolean

    # ALGORITMA
    gameID = input("\nMasukkan ID Game: ")
    idx = find_index_matriks(gameID.upper(), game, 0)   # Indeks game pada array. Jika tidak ditemukan, indeks game -999

    if idx >= 0:
        nama = game[idx][1]
        stok = int(game[idx][5])
        tahun = str(date.today().year)
        harga = int(game[idx][4])
        saldo = int(user[userindex][5])

        punya = is_subset([[gameID.upper(), str(userindex+1)]], kepemilikan)       # True jika user sudah punya game yang diinput, False jika sebaliknya

        if not punya:       # Jika user belum punya gamenya
            if stok > 0:            # Jika stok game masih ada
                if saldo < harga:           # Jika saldonya tidak cukup untuk membeli game
                    print('\n[red]Saldo anda tidak cukup untuk membeli game "{}"!'.format(nama))
                else:
                    game[idx][5] = stok - 1             # Mengurangi stok game terkait
                    user[userindex][5] = saldo - harga  # Mengurangi saldo user

                    kepemilikan += [[gameID, str(userindex+1)]]                        # Mengupdate data kepemilikan
                    riwayat += [[gameID, nama, str(harga), str(userindex+1), tahun]]   # Mengupdate data riwayat

                    print('\n[green]Game "{}" berhasil dibeli!'.format(nama))
            else:
                print('\n[red]Stok game "{}" sedang habis!'.format(nama))
        else:
            print('\n[red]Anda sudah memiliki game "{}"!'.format(nama))
    else:
        print('\n[red]Tidak ada game dengan ID "{}"!'.format(gameID))

    return
