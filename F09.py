# IDENTITAS
# Nama  : 
# NIM   : 
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
data_game="game.csv"
baris_game = convertCSVtoArr(TakeDataFrom(data_game))[0]
kolom_game = convertCSVtoArr(TakeDataFrom(data_game))[1]
arrGame = convertCSVtoArr(TakeDataFrom(data_game))[2]

# Parsing Data Kepemilikan CSV to Array
data_milik="kepemilikan.csv"
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
    list = 1    # Untuk penomoran pada output
    print("Daftar game:")
    for i in UserPunya :
        for j in range (1,baris_game) :
            if i == arrGame[j][0] :
                # output
                print(str(list) + ("."), end=' ')
                for k in range (kolom_game-1) :
                    print(arrGame[j][k], end='')
                    if (k < kolom_game-2) :
                        print(" | ", end='')
                    else :
                        print()
            
        list += 1
