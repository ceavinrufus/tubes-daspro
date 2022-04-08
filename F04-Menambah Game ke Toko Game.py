allowednum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def IntValid(x) :
    valid = True
    counter = 0
    for i in (x) :
        if i not in allowednum :
           counter += 1
    if counter == 0 :
        valid = True
    else :
        valid = False
    return valid
while True: #validasi input data game yang didaftarkan
    nama_game = input("Masukkan nama game : ")
    kategori = input("Masukkan kategori : ")
    tahun_rilis = input("Masukkan tahun rilis : ")
    harga = input("Masukkan harga : ")
    stok_awal = input("Masukkan stok awal : ")
    if nama_game == "" or kategori == "" or stok_awal == "" or harga == "" or tahun_rilis == "" or not IntValid(tahun_rilis) or not IntValid(harga) or not IntValid(stok_awal):
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.") 
    else :
        print("Selamat! Berhasil menambahkan game", nama_game, ".")
        break
Datagame = [nama_game, kategori, tahun_rilis, harga, stok_awal]
    