# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# F09-Melihat Game yang dimiliki
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

def ListGameMilikUser (User) :
    gameUser = ['' for i in range (baris_milik)]
    n = 0 # (Jumlah game -1) yang dimiliki user
    for i in range(1, baris_milik):
        if arrMilik[i][1] == User :
            gameUser[n] = arrMilik[i][0]
            n += 1
    return gameUser

# LISTING KEPEMILIKAN GAME
User = "US003"
# Skema Searching
UserPunya = ListGameMilikUser (User)
if len(UserPunya) == 0 :
    print("Maaf kamu belum membeli game. Ketik perintah beli_game untuk beli.")
else : 
    list = 1
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