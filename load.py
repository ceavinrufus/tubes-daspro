import argparse, os, sys

def delimiter(string):
    # SPESIFIKASI: Memisahkan delimiter dari string

    # KAMUS LOKAL:
    # temp : string
    # data : array

    # ALGORITMA
    temp = ""           # Variabel sementara untuk menampung anggota list
    data = []           # List untuk menampung data

    for char in string:     # Looping setiap huruf yang ada pada string
        if char != ';':
            temp += char    # Menambahkan huruf ke dalam variabel sementara
        elif char == ';':
            data += [temp]  # Menambahkan variabel sementara ke dalam list data
            temp = ""       # Mengosongkan variabel sementara
    if temp:
        data += [int(temp)] # Menambahkan sisa string ke dalam list data dalam bentuk integer

    return data

def load_data(data, rawData):
    # I.S: Data mentah tersedia, list data terdefinisi secara sembarang
    # F.S: Data mentah dibaca dan dimasukkan ke dalam list

    # ALGORITMA
    for row in rawData:
        data += [delimiter(row)]

    return

def dir_path(string):
    # SPESIFIKASI: Validasi apakah argumen yang diberikan saat menjalankan program sesuai atau tidak

    # ALGORITMA
    if os.path.isdir(string):   # Jika argumen sesuai dengan path yang ada, maka program akan lanjut
        print("Loading...")
        return string
    elif string == " ":         # Jika argumen (nama folder) tidak diberikan saat menjalankan program
        print("Tidak ada nama folder yang diberikan!")
        sys.exit("Usage: python program_binomo.py <nama_folder>")
    else:                       # Jika argumen (nama folder) tidak ditemukan
        sys.exit('Folder "{}" tidak ditemukan.'.format(string))

def open_file():
    # I.S: Data mentah tersedia
    # F.S: Data mentah diubah menjadi data yang dapat diolah (dalam bentuk list)

    # ALGORITMA
    user = []; game = []; riwayat = []; kepemilikan = []
    
    # Open file user.csv, game.csv, riwayat.csv, dan kepemilikan.csv
    f_user = open(folder + "/user.csv", 'r')
    f_game = open(folder + "/game.csv", 'r')
    f_riwayat = open(folder + "/riwayat.csv", 'r')
    f_kepemilikan = open(folder + "/kepemilikan.csv", 'r')

    # Membaca data mentah dan memasukkan ke dalam list
    load_data(user, f_user)
    load_data(game, f_game)
    load_data(riwayat, f_riwayat)
    load_data(kepemilikan, f_kepemilikan)

# Parser untuk membaca argumen sehingga bisa membaca argumen sebagai folder yang akan dibaca
parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs="?", type=dir_path, help='Input folder name', default=' ')
args = parser.parse_args()
folder = "./" + args.folder         # Direktori folder

open_file()