import os
from functions.unamecheck import *
from procedures.interface import saving_animation

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
        if savedir in subdirs:
            ada = True
            break

    if not ada:
        os.mkdir(path)  # Membuat folder yang diinput pengguna jika belum ada foldernya

    directory = os.path.join(path, filename)  # Direktori tempat menyimpan file
    f = open(directory, "w")

    for row in data:  # Menuliskan tiap baris pada array ke dalam file
        f.writelines(joining(row) + "\n")


def save(user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. array user, game, riwayat, dan kepemilikan disimpan ke dalam file

    # KAMUS LOKAL
    # savedir : string

    # ALGORITMA
    savedir = input("Masukkan nama folder penyimpanan: ")

    save_file(user, "user.csv", savedir)
    save_file(game, "game.csv", savedir)
    save_file(riwayat, "riwayat.csv", savedir)
    save_file(kepemilikan, "kepemilikan.csv", savedir)
