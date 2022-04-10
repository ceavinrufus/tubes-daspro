def panjang(arr):
    # Fungsi yang menerima sebuah array dan menghitung panjang array tersebut

    # KAMUS LOKAL
    # pjg : integer

    # ALGORITMA
    pjg = 0

    for i in arr:       # Setiap membaca ada sebuah elemen dalam array, nilai pjg bertambah 1
        pjg += 1

    return pjg

def splitting(string, delimiter=";"):
    # Memisahkan delimiter dari string.
    # Syaratnya elemen setelah delimiter terakhir harus integer

    # KAMUS LOKAL
    # temp : string
    # data : array

    # ALGORITMA
    temp = ""           # Variabel sementara untuk menampung anggota list
    data = []           # List untuk menampung data

    for char in string:     # Looping setiap huruf yang ada pada string
        if char == "\n":
            data += [temp]
            temp = ""
        elif char == delimiter:
            data += [temp]  # Menambahkan variabel sementara ke dalam list data
            temp = ""       # Mengosongkan variabel sementara
        else:
            temp += char    # Menambahkan huruf ke dalam variabel sementara
    if temp:
        data += [temp] # Menambahkan sisa string ke dalam list data dalam bentuk integer

    return data

def joining(arr, delimiter=";"):
    # Menggabungkan anggota dalam list menjadi sebuah string dengan delimiter tertentu

    # KAMUS LOKAL
    # string : str

    # Menambahkan string dan delimiter secara bergantian ke dalam string
    string = str(arr[0])
    for i in range(1, panjang(arr)):
        string += delimiter
        string += str(arr[i])

    return string
