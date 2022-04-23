import argparse
import os
import sys
from functions.arraytools import *
from interface import loading_animation


def dir_path(folder):
    # Validasi apakah argumen yang diberikan saat menjalankan program sesuai atau tidak

    # KAMUS LOKAL
    # path : string

    # ALGORITMA
    thisdir = os.getcwd()
    path = os.path.join(thisdir, "savedata", folder)  # Direktori folder

    if os.path.isdir(path):  # Jika argumen sesuai dengan path yang ada, maka program akan lanjut
        if folder == ' ':  # Jika argumen (nama folder) tidak diberikan saat menjalankan program
            print("Tidak ada nama folder yang diberikan!")
            sys.exit("Usage: python program_binomo.py <nama_folder>")
        else:
            return path
    else:  # Jika argumen (nama folder) tidak ditemukan
        sys.exit("Folder ”{}” tidak ditemukan pada folder savedata.".format(folder))


def load_file(data, filename, folder):
    # I.S. data dan filename (nama file yang ingin dibuka) sudah terdefinisi
    # F.S. Data dari file dimasukkan ke dalam array data

    # KAMUS LOKAL
    # directory : string
    # f : TextIOWrapper

    # ALGORITMA
    loading_animation(filename)

    directory = os.path.join(folder, filename)  # Direktori file yang ingin dibuka
    f = open(directory, 'r')  # Membuka file yang ingin dibuka

    # Membaca data mentah dan memasukkan ke dalam list
    lines = f.readlines()

    for line in lines:
        data += [splitting(line)]

    f.close()

    return


def load(user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. Data dari file di-load ke dalam array user, game, riwayat, dan kepemilikan

    # KAMUS LOKAL
    # parser : ArgumentParser
    # foldername : string

    # ALGORTIMA
    print()

    # Membaca argumen saat menjalankan file
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", nargs="?", type=dir_path, help='Input folder name', default=' ')
    foldername = parser.parse_args().folder

    # Load file user, game, riwayat, kepemilikan ke dalam array masing-masing
    load_file(user, "user.csv", foldername)
    load_file(game, "game.csv", foldername)
    load_file(riwayat, "riwayat.csv", foldername)
    load_file(kepemilikan, "kepemilikan.csv", foldername)

    return
