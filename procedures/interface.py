import time
from functions.arraytools import panjang
from rich.progress import track
from rich.console import Console
from rich import print


def menu(commands, role):
    # I.S. command dan role sudah terdefinisi
    # F.S. Menampilkan menu sesuai role

    # KAMUS LOKAL
    # commands_user, commands_admin, commands_guest, printed : array
    # idx : integer

    # ALGORITMA
    commands_user = ["buy_game", "list_game", "search_my_game", "riwayat", "kerangajaib", "tictactoe"]
    commands_admin = ["register", "tambah_game", "ubah_game", "ubah_stok", "topup"]
    commands_guest = ["login", "help"]

    printed = []
    idx = 1

    print()
    # Mencetak menu yang bisa diakses oleh role tersebut
    for i in range(panjang(commands)):
        if role == "admin":
            if commands[i] not in commands_user:
                if commands[i] == "login":          # Tidak mencetak menu login jika sudah login
                    continue
                else:
                    print("{}. {}".format(idx, commands[i]))
                    printed += [commands[i]]
                    idx += 1
        elif role == "user":
            if commands[i] not in commands_admin:
                if commands[i] == "login":          # Tidak mencetak menu login jika sudah login
                    continue
                else:
                    print("{}. {}".format(idx, commands[i]))
                    printed += [commands[i]]
                    idx += 1
        else:
            if commands[i] in commands_guest:
                print("{}. {}".format(idx, commands[i]))
                printed += [commands[i]]
                idx += 1

    # Mencetak menu yang tidak bisa diakses role tersebut
    for i in range(panjang(commands)):
        if commands[i] not in printed:
            print("[dim]{}. {}[/dim]".format(idx, commands[i]))
            idx += 1


def loading_animation(filename):
    # I.S. nama file yang ingin diload ada
    # F.S. Menampilkan animasi loading dan nama file yang sedang diload

    # KAMUS LOKAL

    # ALGORITMA
    with Console().status('Loading [blue]{}[/blue]'.format(filename)):
        time.sleep(1)
        print('\n[blue]{}[/blue] loaded'.format(filename))


def saving_animation(filename):
    # I.S. nama file yang ingin disave ada
    # F.S. Menampilkan animasi loading dan nama file yang sedang disave

    # KAMUS LOKAL

    # ALGORITMA
    for i in track(range(10), description='Saving [blue]{}[/blue]'.format(filename)):
        time.sleep(0.1)

    print('[blue]{}[/blue] saved'.format(filename))
