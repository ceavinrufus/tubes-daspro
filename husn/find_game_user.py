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
data_game="D:\.data\[] DATA HUSNIA\[1] KAMPUS\SEMESTER 2\DASAR PEMROGRAMAN\[] TUGAS BESAR\DATA\game.csv"
baris_game = convertCSVtoArr(TakeDataFrom(data_game))[0]
kolom_game = convertCSVtoArr(TakeDataFrom(data_game))[1]
arrGame = convertCSVtoArr(TakeDataFrom(data_game))[2]

# Parsing Data Kepemilikan CSV to Array
data_milik="D:\.data\[] DATA HUSNIA\[1] KAMPUS\SEMESTER 2\DASAR PEMROGRAMAN\[] TUGAS BESAR\DATA\kepemilikan.csv"
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
    list = 1        # Penomoran output
    for i in UserGame :
        for j in range (1,baris_game) :
            if i == arrGame[j][0] :
                # output
                print(str(list), end = ". ") 
                print(arrGame[j][0], end = " | ")
                print("{:21.20}|".format(arrGame[j][1]), end=" ")
                print("{:13.12}|".format(arrGame[j][2]), end=" ")
                print("{:5.4}|".format(arrGame[j][3]), end=" ")
                print("{:7.6}|".format(arrGame[j][4]), end=" ")
                print(arrGame[j][5])
        list += 1
    
else :
    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")