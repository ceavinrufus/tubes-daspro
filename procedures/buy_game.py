from functions.arraytools import *
from rich import print
from datetime import date


def buy_game(userindex, user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. Melakukan pembelian game dan kemudian mengupdate data game, kepemilikan, dan riwayat

    # KAMUS LOKAL
    # gameID : string
    # idx, stok, harga, saldo : integer
    # punya : boolean

    # ALGORITMA
    gameID = input("\nMasukkan ID Game: ").upper()
    idx = find_index_matriks(gameID, game, 0)   # Indeks user pada array. Jika tidak berhasil login, indeks user -999

    if idx >= 0:
        stok = int(game[idx][5])
        harga = int(game[idx][4])
        saldo = int(user[userindex][5])

        punya = [gameID, str(userindex+1)] in kepemilikan       # True jika user sudah punya game yang diinput, False jika sebaliknya

        if not punya:       # Jika user belum punya gamenya
            if stok > 0:            # Jika stok game masih ada
                if saldo < harga:           # Jika saldonya tidak cukup untuk membeli game
                    print('\n[red]Saldo anda tidak cukup untuk membeli game "{}"!'.format(game[idx][1]))
                else:
                    print('\n[green]Game "{}" berhasil dibeli!'.format(game[idx][1]))

                    game[idx][5] = stok - 1             # Mengurangi stok game terkait
                    user[userindex][5] = saldo - harga  # Mengurangi saldo user

                    kepemilikan += [[gameID, userindex+1]]                                        # Mengupdate data kepemilikan
                    riwayat += [[gameID, game[idx][1], harga, userindex+1, date.today().year]]    # Mengupdate data riwayat
            else:
                print('\n[red]Stok game "{}" sedang habis!'.format(game[idx][1]))
        else:
            print('\n[red]Anda sudah memiliki game "{}"!'.format(game[idx][1]))
    else:
        print('\n[red]Tidak ada game dengan ID "{}"!'.format(gameID))

    return
