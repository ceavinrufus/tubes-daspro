allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '_', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def username_valid(username):
    # Fungsi yang menerima masukan username dan mengembalikan nilai apakah username hanya berisi
    # elemen pada list allowed

    # KAMUS LOKAL
    # count : integer

    # ALGORITMA
    count = 0

    # Mengecek apakah setiap karakter pada username valid (terdapat pada list allowed)
    for i in range(panjang(username)):
        if username[i] in allowed:
            count += 1

    return count == panjang(username)

def isuname_ada(username, datasource):
    # Fungsi yang mereturn apakah username sudah ada dan username yang sudah disimpan tersebut.
    # Username diasumsikan tidak case sensitive.

    # KAMUS LOKAL
    # ada : boolean
    # uname : string

    # ALGORITMA
    i = 0
    ada = datasource[i][1].upper() == username.upper()

    # Mengecek apakah username ada pada array of array of user data
    while i < panjang(datasource)-1 and not ada:
        i += 1
        ada = datasource[i][1].upper() == username.upper()

    return ada, i

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

    # KAMUS LOKAL:
    # temp : string
    # data : array

    # ALGORITMA
    temp = ""           # Variabel sementara untuk menampung anggota list
    data = []           # List untuk menampung data

    for char in string:     # Looping setiap huruf yang ada pada string
        if char != delimiter:
            temp += char    # Menambahkan huruf ke dalam variabel sementara
        elif char == delimiter:
            data += [temp]  # Menambahkan variabel sementara ke dalam list data
            temp = ""       # Mengosongkan variabel sementara
    if temp:
        data += [int(temp)] # Menambahkan sisa string ke dalam list data dalam bentuk integer

    return data


def joining(arr, delimiter=";"):
    string = str(arr[0])

    for i in range(1, panjang(arr)):
        string += delimiter
        string += str(arr[i])

    return string
