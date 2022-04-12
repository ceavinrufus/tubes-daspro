import argparse
import os
import sys
from functions.arraytools import *
from procedures.interface import loading_animation

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
        sys.exit("Folder ”{}” tidak ditemukan.".format(folder))


def load_file(data, filename, args):
    # I.S. data dan filename (nama file yang ingin dibuka) sudah terdefinisi
    # F.S. Data dari file dimasukkan ke dalam array data

    # KAMUS LOKAL
    # data : array
    # directory : string
    # f : TextIOWrapper

    # ALGORITMA
    loading_animation(filename)

    directory = os.path.join(args.folder, filename)  # Direktori file yang ingin dibuka
    f = open(directory, 'r')  # Membuka file yang ingin dibuka

    # Membaca data mentah dan memasukkan ke dalam list
    for row in f:
        data += [splitting(row)]


def load(user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. Data dari file di-load ke dalam array user, game, riwayat, dan kepemilikan

    # KAMUS LOKAL
    # parser : ArgumentParser

    # ALGORTIMA
    print()

    # Membaca argumen saat menjalankan file
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", nargs="?", type=dir_path, help='Input folder name', default=' ')
    args = parser.parse_args()

    # Load file user, game, riwayat, kepemilikan ke dalam array masing-masing
    load_file(user, "user.csv", args)
    load_file(game, "game.csv", args)
    load_file(riwayat, "riwayat.csv", args)
    load_file(kepemilikan, "kepemilikan.csv", args)
