import os
from procedures import *
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from functions.arraytools import popped

# KAMUS
# idx : integer
# commands, user, game, history, kepemilikan : array
# choose : string

# ALGORITMA
commands = ["login", "register", "tambah_game", "ubah_game", "ubah_stok", "list_game_toko",
            "buy_game", "list_game", "search_my_game", "search_game_at_store",
            "topup", "riwayat", "help", "save", "kerangajaib", "tictactoe", "exit"]

user = [] ; game = [] ; history = [] ; kepemilikan = []     # Inisiasi array

load(user, game, history, kepemilikan)                      # Load file ke dalam array

header = [user[0], game[0], history[0], kepemilikan[0]]

user = popped(user, 0)
game = popped(game, 0)
history = popped(history, 0)
kepemilikan = popped(kepemilikan, 0)

while True:
    os.system("cls")
    Console().print(Markdown('''\n# Selamat datang di antarmuka "Binomo"'''))
    menu(commands, "guest")
    choose = input(">>> ")
    os.system("cls")
    if choose == "login":
        idx = login(user)     # Indeks user pada array. Jika tidak berhasil login, indeks user -999

        while idx >= 0:
            os.system("cls")
            print('\nHalo [blue]{}[/blue]!'.format(user[idx][2]))
            menu(commands, user[idx][4])

            choose = input(">>> ")
            if choose in commands:
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
                        help_admin()
                    elif choose == "save":
                        save(header, user, game, history, kepemilikan)
                    elif choose == "exit":
                        exit(header, user, game, history, kepemilikan)
                    else:
                        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
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
                        help_user()
                    elif choose == "save":
                        save(header, user, game, history, kepemilikan)
                    elif choose == "exit":
                        exit(header, user, game, history, kepemilikan)
                    else:
                        print("\nMaaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            else:
                print('Tidak ada menu "{}"'.format(choose))
            input("\nPress enter to continue..")
    elif choose == "help":
        help_guest()
    else:
        print('\nMaaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login" dan "help"')
    input("\nPress enter to continue..")
