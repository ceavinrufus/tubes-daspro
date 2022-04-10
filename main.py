import argparse
from load import *
from save import *
from register import register
from login import login
from exit import exit

# Parser untuk membaca argumen sehingga bisa membaca argumen sebagai folder yang akan dibaca
parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs="?", type=dir_path, help='Input folder name', default=' ')
args = parser.parse_args()

print('Selamat datang di antarmuka "Binomo"')

# Menyimpan isi file eksternal ke dalam variabel (berupa array)
user = open_file(args.folder, "user.csv")
game = open_file(args.folder, "game.csv")
riwayat = open_file(args.folder, "riwayat.csv")
kepemilikan = open_file(args.folder, "kepemilikan.csv")

loggedOn = False
while True:
    if input(">>> ") == "login":
        (id, username, nama, password, role, saldo), loggedOn = login(user)

        while loggedOn:
            choose = input(">>> ")
            if choose == "save":
                save_all(user, game, riwayat, kepemilikan)
            elif choose == "register":
                register(user)
            elif choose == "tambah_game":     # Hanya admin
                    pass
            elif choose == "ubah_game":       # Hanya admin
                    pass
            elif choose == "ubah_stok":       # Hanya admin
                    pass
            elif choose == "list_game_toko":
                    pass
            elif choose == "buy_game":        # Hanya user
                    pass
            elif choose == "list_game":       # Hanya user
                    pass
            elif choose == "search_my_game":  # Hanya user
                    pass
            elif choose == "search_game_at_store":
                    pass
            elif choose == "topup":           # Hanya admin
                    pass
            elif choose == "riwayat":         # Hanya user
                    pass
            elif choose == "help":         # Hanya user
                    pass
            elif choose == "exit":
                    exit(user, game, riwayat, kepemilikan)
            elif choose == "help":         # Hanya user
                    pass
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')