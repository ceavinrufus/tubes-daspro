# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
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

def searchData(array, col, elmt) :
    # Menghasilkan tuple yang terdiri dari daftar game yang memenuhi kriteria
    # dan found, bernilai True jika ada game yang ditemukan, False jika tidak

    # KAMUS LOKAL
    # found : boolean
    # searchResult : array of string
    # idx, i, j : integer

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
