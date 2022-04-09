# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# F07-Listing Game di Toko Berdasarkan ID, Tahun Rilis, Harga  

# Program Sorting Game
# Input     : Menerima Pilihan Skema Sorting berdasarkan ID secara ascending,
#             Tahun Rilis (tahun- untuk descending dan tahun+ untuk ascending), dan
#             Harga (harga- untuk descending dan harga+ untuk ascending)
# Output    : Menampilkan data game yang tersedia di toko terurut sesuai masukan skema sorting

# KAMUS
# Deklarasi Variabel
#   data :
#   baris, kolom, Pass, Idx, i, j    : Integer
#   arrDataGame, Temp : Array of String
#   sortby : String

# ALGORITMA PROGRAM UTAMA
from ParsingConverting import convertCSVtoArr, TakeDataFrom

data = "D:\.data\[] DATA HUSNIA\[1] KAMPUS\SEMESTER 2\DASAR PEMROGRAMAN\[] TUGAS BESAR\DATA\game.csv"
baris = convertCSVtoArr(TakeDataFrom(data))[0]
kolom = convertCSVtoArr(TakeDataFrom(data))[1]
arrDataGame = convertCSVtoArr(TakeDataFrom(data))[2]

# LISTING GAME
print("Skema sorting :", end=' ')
sortby = input()

if (sortby == '' or sortby == 'tahun+' or sortby == 'tahun-' or sortby == 'harga+' or sortby == 'harga-') :
    # Proses dilakukan
    if baris > 2 :
            for Pass in range (1,baris-1) :
                # Tentukan tahun maksimum
                Idx = Pass
                for i in range (Pass+1, baris) :
                    if sortby == "tahun-" and (int(arrDataGame[Idx][3]) < int(arrDataGame[i][3])) :
                        Idx = i 
                    elif sortby == "tahun+" and (int(arrDataGame[Idx][3]) > int(arrDataGame[i][3])) :
                        Idx = i
                    elif sortby == "harga-" and (int(arrDataGame[Idx][4]) < int(arrDataGame[i][4])) :
                        Idx = i
                    elif sortby == "harga+" and (int(arrDataGame[Idx][4]) > int(arrDataGame[i][4])) :
                        Idx = i 

                # Didapatkan nilai paling maksimum
                # Tukar data dengan Pass
                Temp = arrDataGame[Idx]
                arrDataGame[Idx] = arrDataGame[Pass]
                arrDataGame[Pass] = Temp

    # Jika masukan kosong, sorting ID ascending
    # Karena pada data sudah pasti IDGame terurut menaik, maka langsung output   
    # Output
    for i in range (1,baris) :
        for j in range (kolom) :
            print(arrDataGame[i][j], end='')
            if (j < kolom-1) :
                print(" | ", end='')
            else :
                print()

else :      # Proses tidak dilakukan
    print("Skema sorting tidak valid!")