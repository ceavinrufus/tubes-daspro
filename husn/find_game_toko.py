# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 7 April 2022

# F11-Mencari Game di Toko dari ID, Nama Game, Harga, Kategori, dan Tahun Rilis

# Program Searching Game di Toko
# Input     : Keyword Pencarian
# Output    : Menampilkan data game pada toko sesuai kategori,
#             Jika tidak ada, tampilkan pesan

# KAMUS
# Deklarasi Variabel
#   data_game :
#   baris_game, kolom_game : Integer
#   i, j, k, list : Integer
#   arrGame, searchBy, outputArr : Array of String
#   User, idGame, nama, harga, kategori, tahun, by : String
#   foundVal : boolean

# ALGORITMA PROGRAM UTAMA
from ParsingConverting import convertCSVtoArr, TakeDataFrom
from SearchBy import searchData

# Parsing Data Game CSV to Array
data_game="D:\.data\[] DATA HUSNIA\[1] KAMPUS\SEMESTER 2\DASAR PEMROGRAMAN\[] TUGAS BESAR\DATA\game.csv"
baris_game = convertCSVtoArr(TakeDataFrom(data_game))[0]
kolom_game = convertCSVtoArr(TakeDataFrom(data_game))[1]
arrGame = convertCSVtoArr(TakeDataFrom(data_game))[2]

# Input informasi yang dibutuhkan
searchBy = ["" for i in range(5)]
print("Masukkan ID Game: ", end='')
idGame = input()
searchBy[0] = idGame
print("Masukkan Nama Game: ", end='')
nama = input()
searchBy[1] = nama
print("Masukkan Harga Game: ", end='')
harga = input()
searchBy[2] = harga
print("Masukkan Kategori Game: ", end='')
kategori = input()
searchBy[3] = kategori
print("Masukkan Tahun Rilis Game: ", end='')
tahun = input()
searchBy[4] = tahun

# Searching
print("Daftar game pada toko yang memenuhi kriteria:")
outputArr = ["" for i in range(baris_game-1)]
for i in range (1, baris_game) :
    outputArr[i-1] = arrGame[i][0]

foundVal = True
i = 0
while i < 5 and foundVal :
    if searchBy[i] == "" :
        i += 1
    else :
        if i == 0 : by = "idGame" 
        elif i == 1 : by = "nama"
        elif i == 2 : by = "harga"
        elif i == 3 : by = "kategori"
        else : by = "tahun"
        foundVal = searchData(outputArr, by , searchBy[i])[1]
        outputArr = searchData(outputArr, by, searchBy[i])[0]
        i += 1
        
# output
if foundVal :
    list = 1        # Penomoran output
    for i in outputArr :
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