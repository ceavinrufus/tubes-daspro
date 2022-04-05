import os
from bnmo_function import *

def save_file(data, filename):
    # Fungsi yang menulis data dari array ke dalam file csv

    # KAMUS LOKAL
    # path : string
    # ada : boolean

    # ALGORITMA
    path = os.path.join("./savedata", savedir)
    ada = False

    # Mengecek apakah folder save yang dipilih user sudah ada
    for dir, subdir, files in os.walk("./savedata"):
        if savedir in subdir:
            ada = True
            break

    if not ada:
        os.mkdir(path)  # Membuat folder yang diinput pengguna jika belum ada foldernya

    directory = os.path.join(path, filename)
    f = open(directory, "w")

    for row in data:
        f.writelines(joining(row) + "\n")

savedir = input("Masukkan nama folder penyimpanan: ")

print("Saving...")