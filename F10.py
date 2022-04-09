# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# F10-Mencari Game yang Dimiliki dari ID dan Tahun Rilis

# Program Searching User Game
# Input     : ID User dan Keyword Pencarian
# Output    : Menampilkan data game yang dimiliki oleh User sesuai keyword,
#             Jika tidak ada, tampilkan pesan

# KAMUS
# Deklarasi Variabel
#   data_game, data_milik :
#   baris_game, kolom_game : Integer
#   baris_milik, kolom_milik : Integer
#   i, j, k, list : Integer
#   arrGame, arrMilik, UserGame, searchBy : Array of String
#   User, idGame, tahun, by : String
#   foundVal : boolean

# ALGORITMA PROGRAM UTAMA
from ListGameUser import ListGameMilikUser
from ParsingConverting import convertCSVtoArr, TakeDataFrom
from SearchBy import searchData

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

# List Data Game yang dimiliki
User = "US003"
UserGame = ListGameMilikUser(User)[0]

# Input informasi yang dibutuhkan
searchBy = ["" for i in range(2)]
print("Masukkan ID Game: ", end='')
idGame = input()
searchBy[0] = idGame
print("Masukkan Tahun Rilis Game: ", end='')
tahun = input()
searchBy[1] = tahun

# Searching
print("Daftar game pada inventory yang memenuhi kriteria:")
i = 0
foundVal = True
while i < 2 and foundVal:
    if searchBy[i] == "" :
        i += 1
    else :
        if i == 0 : by = "idGame"
        else : by = "tahun"
        foundVal = searchData(UserGame, by , searchBy[i])[1]
        UserGame = searchData(UserGame, by, searchBy[i])[0]
        i += 1

# output
if foundVal :
    list = 1
    for i in UserGame :
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
