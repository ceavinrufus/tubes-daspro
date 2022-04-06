# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# F10-Mencari Game yang Dimiliki dari ID dan Tahun Rilis
from F09 import ListGameMilikUser
from ParsingConverting import convertCSVtoArr, Parsing

# Parsing Data Game CSV to Array
data_game="D:\.data\[] DATA HUSNIA\[1] KAMPUS\SEMESTER 2\DASAR PEMROGRAMAN\[] TUGAS BESAR\DATA\game.csv"
baris_game = convertCSVtoArr(Parsing(data_game))[0]
kolom_game = convertCSVtoArr(Parsing(data_game))[1]
arrGame = convertCSVtoArr(Parsing(data_game))[2]

# Parsing Data Kepemilikan CSV to Array
data_milik="D:\.data\[] DATA HUSNIA\[1] KAMPUS\SEMESTER 2\DASAR PEMROGRAMAN\[] TUGAS BESAR\DATA\kepemilikan.csv"
baris_milik = convertCSVtoArr(Parsing(data_milik))[0]
kolom_milik = convertCSVtoArr(Parsing(data_milik))[1]
arrMilik = convertCSVtoArr(Parsing(data_milik))[2]

def searchData(array, col, elmt) :
    found = False
    searchResult = ['' for i in range (baris_milik)]
    idx = 0
    for i in array :
        for j in range (1,baris_game) :
            if i == arrGame[j][0] :
                if col == "tahun" and arrGame[j][3] == elmt :
                    searchResult[idx] = i
                    found = True
                    idx += 1
                elif col == "idGame" and arrGame[j][0] == elmt :
                    searchResult[idx] = i
                    found = True
                    idx += 1
    return (searchResult, found)

# List Data Game yang dimiliki
User = "US003"
UserGame = ListGameMilikUser(User)

# Input informasi yang dibutuhkan
print("Masukkan ID Game: ", end='')
idGame = input()
print("Masukkan Tahun Rilis Game:", end='')
tahun = input()

# Searching
print("Daftar game pada inventory yang memenuhi kriteria:")
if idGame == "" :       # IDGame tidak diisi
    if tahun == "" :    # Tahun tidak diisi
        outputList = UserGame
    else :              # Pencarian berdasarkan tahun saja
        outputList = searchData(UserGame,"tahun", tahun )[0]
        found = searchData(UserGame,"tahun", tahun )[1]
else :                  # IDGame diisi
    if tahun == "" :    # Pencarian berdasarkan ID Game saja
        outputList = searchData(UserGame,"idGame", idGame)[0]
        found = searchData(UserGame,"idGame", idGame)[1]
    else :              # Pencarian berdasarkan tahun dan ID Game
        outputList = searchData(searchData(UserGame, "idGame", idGame)[0], "tahun", tahun)[0]
        found = searchData(searchData(UserGame, "idGame", idGame)[0], "tahun", tahun)[1]
        
# output
if found :
    list = 1
    for i in outputList :
        for j in range (1,baris_game) :
            if i == arrGame[j][0] :
                print(str(list) + ("."), end=' ')
                for k in range (kolom_game-1) :
                    print(arrGame[j][k], end='')
                    if (k < kolom_game-2) :
                        print(" | ", end='')
                    else :
                        print()
        list += 1
else :
    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")