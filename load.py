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

def dir_path(string):
    # Validasi apakah argumen yang diberikan saat menjalankan program sesuai atau tidak

    # ALGORITMA
    if os.path.isdir(string):   # Jika argumen sesuai dengan path yang ada, maka program akan lanjut
        print("Loading...")
        return string
    elif string == " ":         # Jika argumen (nama folder) tidak diberikan saat menjalankan program
        print("Tidak ada nama folder yang diberikan!")
        sys.exit("Usage: python program_binomo.py <nama_folder>")
    else:                       # Jika argumen (nama folder) tidak ditemukan
        sys.exit("Folder ”{}” tidak ditemukan.".format(string))

def open_file(filename):
    # I.S. Data mentah tersedia
    # F.S. Data mentah diubah menjadi data yang dapat diolah (dalam bentuk list)

    # ALGORITMA
    data = []

    # Open file user.csv, game.csv, riwayat.csv, dan kepemilikan.csv
    raw = open(folder + "/" + filename, 'r')

    # Membaca data mentah dan memasukkan ke dalam list
    for row in raw:
        data += [delimiter(row)]

    return data

# Parser untuk membaca argumen sehingga bisa membaca argumen sebagai folder yang akan dibaca
parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs="?", type=dir_path, help='Input folder name', default=' ')
args = parser.parse_args()
folder = "./" + args.folder         # Direktori folder

# Menyimpan isi file eksternal ke dalam variabel (berupa array)
user = open_file("user.csv")
game = open_file("game.csv")
riwayat = open_file("riwayat.csv")
kepemilikan = open_file("kepemilikan.csv")