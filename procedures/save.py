import os
from functions.arraytools import *
from interface import saving_animation
from rich import print


def save_file(data, filename, savedir):
    # I.S. data dan savedir (direktori tempat menyimpan) terdefinisi
    # F.S. data tersimpan ke dalam file csv

    # KAMUS LOKAL
    # path : string
    # ada : boolean

    # ALGORITMA
    saving_animation(filename)

    thisdir = os.getcwd()
    path = os.path.join(thisdir, "savedata", savedir)
    ada = False

    # Mengecek apakah folder save yang dipilih user sudah ada
    for dirs, subdirs, files in os.walk(os.path.join(thisdir, "savedata")):
        if is_subset([savedir], subdirs):
            ada = True
            break

    if not ada:
        os.mkdir(path)  # Membuat folder yang diinput pengguna jika belum ada foldernya

    directory = os.path.join(path, filename)  # Direktori tempat menyimpan file
    f = open(directory, "w")

    for row in data:  # Menuliskan tiap baris pada array ke dalam file
        f.writelines(joining(row) + "\n")

    f.close()

    return


def save(header, user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. array user, game, riwayat, dan kepemilikan disimpan ke dalam file

    # KAMUS LOKAL
    # savedir : string

    # ALGORITMA
    savedir = input("\nMasukkan nama folder penyimpanan: ")

    while panjang(savedir) <= 0:
        os.system("cls")
        print("\n[red]Nama folder tidak boleh kosong!")
        savedir = input("\nMasukkan nama folder penyimpanan: ")

    print()
    save_file([header[0]] + user, "user.csv", savedir)
    save_file([header[1]] + game, "game.csv", savedir)
    save_file([header[2]] + riwayat, "riwayat.csv", savedir)
    save_file([header[3]] + kepemilikan, "kepemilikan.csv", savedir)

    return
