import os, sys
from arraytools import *

def dir_path(folder):
    # Validasi apakah argumen yang diberikan saat menjalankan program sesuai atau tidak

    # KAMUS LOKAL
    # path : string

    # ALGORITMA
    path = os.path.join("./savedata", folder)       # Direktori folder

    if os.path.isdir(path):   # Jika argumen sesuai dengan path yang ada, maka program akan lanjut
        if folder == ' ':  # Jika argumen (nama folder) tidak diberikan saat menjalankan program
            print("Tidak ada nama folder yang diberikan!")
            sys.exit("Usage: python program_binomo.py <nama_folder>")
        else:
            print("Loading...")
            return path
    else:                       # Jika argumen (nama folder) tidak ditemukan
        sys.exit("Folder ”{}” tidak ditemukan.".format(folder))

def open_file(foldername, filename):
    # Fungsi yang memasukan data dari file ke data yang dapat diolah (dalam bentuk list)

    # KAMUS LOKAL
    # data : array
    # directory : string

    # ALGORITMA
    data = []

    directory = os.path.join(foldername, filename)   # Direktori file yang ingin dibuka
    f = open(directory, 'r')                                # Membuka file yang ingin dibuka

    # Membaca data mentah dan memasukkan ke dalam list
    for row in f:
        data += [splitting(row)]

    return data

if __name__ == "__main__":
    exec(open("main.py").read())