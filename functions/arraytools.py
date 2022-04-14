alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialchar = ['_', '-', ' ', '@', '%', '+', '/', '!', '#', '$', '?', ':', '.', '(',
               ')', '~', '^', '&', '*', '=', '{', '[', '}', ']', '|', '<', '>']


def panjang(arr):
    # Fungsi yang menerima sebuah array dan menghitung panjang array tersebut

    # KAMUS LOKAL
    # pjg : integer

    # ALGORITMA
    pjg = 0

    for _ in arr:       # Setiap membaca ada sebuah elemen dalam array, nilai pjg bertambah 1
        pjg += 1

    return pjg


def splitting(string, delimiter=";"):
    # Memisahkan delimiter dari string

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
        data += [temp]      # Menambahkan sisa string ke dalam list data dalam bentuk integer

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


def find_index_matriks(element, arr, idx):
    # Mencari indeks pertama ditemukan element dalam sebuah array dalam sebuah matriks.
    # Jika tidak ditemukan, maka fungsi mereturn -999

    # KAMUS LOKAL

    # ALGORITMA
    for i in range(panjang(arr)):
        if element == arr[i][idx]:
            return i
    return -999


def find_index_array(element, arr):
    # Mencari indeks pertama ditemukan element dalam sebuah array.
    # Jika tidak ditemukan, maka fungsi mereturn -999

    # KAMUS LOKAL

    # ALGORITMA
    for i in range(panjang(arr)):
        if element == arr[i]:
            return i
    return -999


def update_data(new, old):
    # Fungsi untuk mengupdate data pada indeks suatu array

    # KAMUS LOKAL

    # ALGORITMA
    if new == '':        # Jika update kosong, data tetap sama
        return old
    else:                   # Jika update tidak kosong, data diganti dengan update terbaru
        return new


def is_subset(arr1, arr2):
    # Fungsi yang mereturn True jika arr1 merupakan subset dari arr2
    # elemen pada list allowed

    # KAMUS LOKAL
    # count : integer

    # ALGORITMA
    count = 0

    # Mengecek apakah setiap karakter pada username valid (terdapat pada list allowed)
    for i in range(panjang(arr1)):
        if arr1[i] in arr2:
            count += 1

    return count == panjang(arr1)
