from procedures import *
from rich import print

# KAMUS
# idx : integer
# commands, user, game, riwayat, kepemilikan : array
# choose : string

# ALGORITMA
commands = ["login", "register", "tambah_game", "ubah_game", "ubah_stok", "list_game_toko",
            "buy_game", "list_game", "search_my_game", "search_game_at_store",
            "topup", "riwayat", "help", "save", "kerangajaib", "tictactoe", "exit"]

user = [] ; game = [] ; riwayat = [] ; kepemilikan = []     # Inisiasi array

load(user, game, riwayat, kepemilikan)                      # Load file ke dalam array


while True:
    os.system("cls")
    print('\nSelamat datang di antarmuka "Binomo"')
    menu(commands, "guest")
    choose = input(">>> ")
    if choose == "login":
        idx = login(user)     # Indeks user pada array. Jika tidak berhasil login, indeks user -999

        while idx >= 0:
            os.system("cls")
            print('\nHalo [red]{}[/red]!'.format(user[idx][2]))
            menu(commands, user[idx][4])

            choose = input(">>> ")
            if choose in commands:
                if user[idx][4] == "admin":             # Menu yang dapat dijalankan oleh admin
                    if choose == "login":
                        temp = idx
                        idx = login(user)
                        if idx < 0:
                            idx = temp
                        elif idx == temp:
                            print("Anda sudah login dengan akun [red]{}[/red]".format(user[idx][1]))
                        else:
                            continue
                    elif choose == "register":          # Hanya admin
                        register(user)
                    elif choose == "tambah_game":       # Hanya admin
                        pass
                    elif choose == "ubah_game":         # Hanya admin
                        pass
                    elif choose == "ubah_stok":         # Hanya admin
                        ubah_stok(game)
                    elif choose == "topup":             # Hanya admin
                        pass
                    elif choose == "list_game_toko":
                        pass
                    elif choose == "search_game_at_store":
                        pass
                    elif choose == "help":
                        help_admin()
                    elif choose == "save":
                        save(user, game, riwayat, kepemilikan)
                    elif choose == "exit":
                        exit(user, game, riwayat, kepemilikan)
                    else:
                        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                elif user[idx][4] == "user":            # Menu yang dapat dijalankan oleh user
                    if choose == "login":
                        temp = idx
                        idx = login(user)
                        if idx < 0:
                            idx = temp
                        elif idx == temp:
                            print("Anda sudah login dengan akun [red]{}[/red]".format(user[idx][1]))
                        else:
                            continue
                    elif choose == "buy_game":          # Hanya user
                        pass
                    elif choose == "list_game":         # Hanya user
                        pass
                    elif choose == "search_my_game":    # Hanya user
                        pass
                    elif choose == "riwayat":           # Hanya user
                        pass
                    elif choose == "kerangajaib":       # Hanya user
                        kerangajaib()
                    elif choose == "tictactoe":         # Hanya user
                        tictactoe()
                    elif choose == "list_game_toko":
                        pass
                    elif choose == "search_game_at_store":
                        pass
                    elif choose == "help":
                        help_user()
                    elif choose == "save":
                        save(user, game, riwayat, kepemilikan)
                    elif choose == "exit":
                        exit(user, game, riwayat, kepemilikan)
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            else:
                print('Tidak ada menu "{}"'.format(choose))
            input("\nPress enter to continue..")
    elif choose == "help":
        help_guest()
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    input("\nPress enter to continue..")