# IDENTITAS
# Nama  :
# NIM   :
# Tanggal : 7 April 2022

# Program Mencari Game
# Input     : array data asal, jenis kategori, dan keyword terdefinisi
# Output    : Mencari data berdasarkan keyword

# KAMUS GLOBAL
# Deklarasi Variabel
#   data_game, data_milik :
#   baris_game, kolom_game : Integer
#   baris_milik, kolom_milik : Integer
#   arrGame, arrMilik : Array of String

# Parsing Data CSV to Array
from ParsingConverting import convertCSVtoArr, TakeDataFrom

# Parsing Data Game CSV to Array
data_game="game.csv"
baris_game = convertCSVtoArr(TakeDataFrom(data_game))[0]
kolom_game = convertCSVtoArr(TakeDataFrom(data_game))[1]
arrGame = convertCSVtoArr(TakeDataFrom(data_game))[2]

# Parsing Data Kepemilikan CSV to Array
data_milik="kepemilikan.csv"
baris_milik = convertCSVtoArr(TakeDataFrom(data_milik))[0]
kolom_milik = convertCSVtoArr(TakeDataFrom(data_milik))[1]
arrMilik = convertCSVtoArr(TakeDataFrom(data_milik))[2]

def searchData(array, col, elmt) :
# Menghasilkan tuple yang terdiri dari daftar game yang memenuhi kriteria
# dan found, bernilai True jika ada game yang ditemukan, False jika tidak

# KAMUS LOKAL
#   found : Boolean
#   searchResult : Array of String
#   idx, i, j : Integer

# ALGORITMA FUNGSI/PROSEDUR
    found = False
    searchResult = ['' for i in range (baris_milik)]
    idx = 0
    for i in array :
        for j in range (1,baris_game) :
            if i == arrGame[j][0] :
                if (col == "idGame" and arrGame[j][0] == elmt) or (col == "nama" and arrGame[j][1] == elmt) or (col == "harga" and arrGame[j][4] == elmt) or (col == "kategori" and arrGame[j][2] == elmt) or (col == "tahun" and arrGame[j][3] == elmt) :
                    searchResult[idx] = i
                    found = True
                    idx += 1
    return (searchResult, found)
