# IDENTITAS
# Nama  : 
# NIM   : 
# Tanggal : 7 April 2022

# Program Sorting Game
# Input     : ID User terdefinisi
# Output    : Mengumpulkan data yang dimiliki oleh seorang user sesuai ID User

# KAMUS GLOBAL
# Deklarasi Variabel
#   data_game, data_milik :
#   baris_game, kolom_game : Integer
#   baris_milik, kolom_milik : Integer
#   arrGame, arrMilik : Array of String


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


def ListGameMilikUser (User) :
# Menghasilkan tuple yang terdiri dari daftar game yang dimiliki oleh seorang User
# berdasarkan ID User dan banyak game yang dimiliki

# KAMUS LOKAL
#   gameUser : Array of String
#   n, i : Integer
# ALGORITMA FUNGSI/PROSEDUR
    gameUser = ['' for i in range (baris_milik)]
    n = 0 # Jumlah game yang dimiliki user
    for i in range(1, baris_milik):
        if arrMilik[i][1] == User :
            gameUser[n] = arrMilik[i][0]
            n += 1
    return (gameUser, n)
