# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# Program Parsing Data
# Input     : File CSV
# Output    : Mengakses file CSV dan mengubah data format CSV menjadi Array untuk dapat diolah

# ALGORITMA FUNGSI/PROSEDUR
# Ambil Data CSV to Array
def TakeDataFrom(data) :
# Menghasilkan data yang diambil dari file 

# KAMUS LOKAL
#   importCSV, data :

# ALGORITMA FUNGSI/PROSEDUR
    importCSV = open(data, "r")
    data = importCSV.read()
    return data

# Mengubah Format data CSV menjadi Array
def convertCSVtoArr(DataCSV) :
# Menghasilkan tuple yang terdiri dari jumlah baris, jumlah kolom, dan
# data dalam bentuk Array untuk diproses selanjutnya

# KAMUS LOKAL
#   baris, kolom, i : Integer
#   arrData : Array of String
#   row. column : Integer

# ALGORITMA FUNGSI/PROSEDUR
    # Menemukan banyak baris dan kolom array
    baris = 0
    kolom = 0
    for i in (DataCSV) :
        if i == "\n" :
            baris += 1
            kolom += 1
        elif i == ';' :
            kolom += 1
    kolom = int(kolom/baris)

    # Masukan data ke Array
    arrData = [['' for j in range (kolom) ] for i in range (baris)]
    column = 0
    row = 0
    for i in (DataCSV) :
        if i == ';' :
            column += 1
        elif i == '\n' :
            row += 1
            column = 0
        elif i != '"' :
            arrData[row][column] += str(i)
    
    return (baris, kolom, arrData)
