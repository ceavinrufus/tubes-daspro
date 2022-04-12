# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# F09-Melihat Game yang dimiliki

# Program Listing User Game
# Input     : ID User terdefinisi
# Output    : Menampilkan data game yang dimiliki oleh User,
#             Jika tidak ada, tampilkan pesan

# KAMUS
# Deklarasi Variabel
#   data_game, data_milik :
#   baris_game, kolom_game : Integer
#   baris_milik, kolom_milik : Integer
#   banyakGame, i, j, k, list : Integer
#   arrGame, arrMilik, UserPunya : Array of String
#   User, sortby : String

# ALGORITMA PROGRAM UTAMA
from ParsingConverting import convertCSVtoArr, TakeDataFrom
from ListGameUser import ListGameMilikUser

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

# LISTING KEPEMILIKAN GAME
User = "US003"
# Skema Searching
UserPunya = ListGameMilikUser(User)[0]
banyakGame = ListGameMilikUser(User)[1]
if banyakGame == 0 :
    print("Maaf kamu belum membeli game. Ketik perintah beli_game untuk beli.")
else :
    print("Daftar game:")
    list = 1        # Penomoran output
    for i in UserPunya :
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