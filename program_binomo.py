import os
import interface
from procedures import *
from rich import print
from rich.markdown import Markdown
from functions.arraytools import *

# PROGRAM BNMO
# SPESIFIKASI: Program yang mensimulasikan cara kerja BNMO sesuai spesifikasi pada
#              https://docs.google.com/document/d/1mqODeKIMLjvRmoUb_XQPK7pOifJb-rma83bMuqE9C1s/edit
#              User Interface pada terminal dihias dengan menggunakan module rich. Agar bisa berjalan dengan optimal,
#              gunakan Windows Terminal

# KAMUS
# idx : integer
# commands, user, game, history, kepemilikan : array of array of string
# header : array of string
# choose : string
# logged_on : boolean

# ALGORITMA
commands = ["login", "register", "tambah_game", "ubah_game", "ubah_stok", "list_game_toko",
            "buy_game", "list_game", "search_my_game", "search_game_at_store", "topup",
            "riwayat", "help", "save", "kerangajaib", "tictactoe", "logout", "exit"]

user = [] ; game = [] ; history = [] ; kepemilikan = []     # Inisiasi array

load(user, game, history, kepemilikan)                      # Load file ke dalam array

header = [user[0], game[0], history[0], kepemilikan[0]]

# Menghilangkan header pada array
user = popped(user, 0)
game = popped(game, 0)
history = popped(history, 0)
kepemilikan = popped(kepemilikan, 0)

while True:                             # Looping selagi belum login
    os.system("cls")

    print(Markdown('''\n# Selamat datang di antarmuka "Binomo"'''))
    interface.gambar_BNMO()

    interface.menu(commands, "guest")
    choose = stripping(input(">>> ").lower())

    os.system("cls")
    if choose == "login":
        idx, logged_on = login(user)     # Indeks user pada array. Jika tidak berhasil login, indeks user -999

        while logged_on:                 # Looping selagi masih logged in
            os.system("cls")
            print('\nHalo [blue]{}[/blue]!'.format(user[idx][2]))
            interface.menu(commands, user[idx][4])

            choose = stripping(input(">>> ").lower())
            if find_index_array(choose, commands) >= 0:
                os.system("cls")
                if user[idx][4] == "admin":             # Menu yang dapat dijalankan oleh admin
                    if choose == "login":
                        print("\nAnda sudah login dengan akun [blue]{}[/blue]".format(user[idx][1]))
                    elif choose == "register":          # Hanya admin
                        register(user)
                    elif choose == "tambah_game":       # Hanya admin
                        tambah_game(game)
                    elif choose == "ubah_game":         # Hanya admin
                        ubah_game(game)
                    elif choose == "ubah_stok":         # Hanya admin
                        ubah_stok(game)
                    elif choose == "topup":             # Hanya admin
                        topup(user)
                    elif choose == "list_game_toko":
                        list_game_toko(game)
                    elif choose == "search_game_at_store":
                        search_game_at_store(game)
                    elif choose == "help":
                        help("admin")
                    elif choose == "save":
                        save(header, user, game, history, kepemilikan)
                    elif choose == "logout":
                        break
                    elif choose == "exit":
                        exit(header, user, game, history, kepemilikan)
                    else:
                        print("\n[red]Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                elif user[idx][4] == "user":            # Menu yang dapat dijalankan oleh user
                    if choose == "login":
                        print("\nAnda sudah login dengan akun [blue]{}[/blue]".format(user[idx][1]))
                    elif choose == "buy_game":          # Hanya user
                        buy_game(idx, user, game, history, kepemilikan)
                    elif choose == "list_game":         # Hanya user
                        list_game(kepemilikan, game, idx)
                    elif choose == "search_my_game":    # Hanya user
                        search_my_game(kepemilikan, game, idx)
                    elif choose == "riwayat":           # Hanya user
                        riwayat(idx, history)
                    elif choose == "kerangajaib":       # Hanya user
                        kerangajaib()
                    elif choose == "tictactoe":         # Hanya user
                        tictactoe()
                    elif choose == "list_game_toko":
                        list_game_toko(game)
                    elif choose == "search_game_at_store":
                        search_game_at_store(game)
                    elif choose == "help":
                        help("user")
                    elif choose == "save":
                        save(header, user, game, history, kepemilikan)
                    elif choose == "logout":
                        break
                    elif choose == "exit":
                        exit(header, user, game, history, kepemilikan)
                    else:
                        print("\n[red]Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            else:
                print('[red]Tidak ada menu "{}"'.format(choose))
            input("\nPress enter to continue..")
    elif choose == "help":
        help()
    else:
        print('\n[red]Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login" dan "help"')
    input("\nPress enter to continue..")
