# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# F07-Listing Harga Berdasarkan ID, Tahun Rilis, Harga  
from ParsingConverting import convertCSVtoArr, Parsing

# PROGRAM UTAMA
data = "D:\.data\[] DATA HUSNIA\[1] KAMPUS\SEMESTER 2\DASAR PEMROGRAMAN\[] TUGAS BESAR\DATA\game.csv"
baris = convertCSVtoArr(Parsing(data))[0]
kolom = convertCSVtoArr(Parsing(data))[1]
arrDataGame = convertCSVtoArr(Parsing(data))[2]

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