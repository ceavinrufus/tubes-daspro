# IDENTITAS
# Nama  : Husnia Munzayana
# NIM   : 16521313
# Tanggal : 6 April 2022

# Parsing dan mengubah format data CSV ke Array
# Parsing Data CSV to Array
def Parsing(data) :
    importCSV = open(data, "r")
    data = importCSV.read()
    return data

# Mengubah Format data CSV menjadi Array
def convertCSVtoArr(DataCSV) :
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
