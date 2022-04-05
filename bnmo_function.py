allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '_', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def input_username(msg):
    while True:
        username = input(msg)
        count = 0

        for i in range(panjang(username)):
            if username[i] in allowed:
                count += 1
        if count == panjang(username):
            break
        else:
            print("Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")

    return username

def is_ada(username, datasource):
    # Validasi apakah username sudah ada yang menggunakan. Username diasumsikan tidak case sensitive

    # ALGORITMA
    ada = False
    uname = ''
    for data in datasource:
        if data[1].upper() == username.upper():
            ada = True
            uname = data[1]
            break

    return ada, uname

def panjang(arr):
    pjg = 0
    for i in arr:
        pjg += 1

    return pjg