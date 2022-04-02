# Kamus
#   function helpuser() -> string
#   {menampilkan instruksi dalam pemakaian perintah untuk User}
#   function helpadmin() -> string
#   {menampilkan instruksi dalam pemakaian perintah untuk Admin}
# Algoritma :
def helpuser() :    
    print("============ HELP ============")
    print("1. login - Untuk melakukan login ke dalam sistem")
    print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
    print("3. buy_game - Untuk membeli game yang diinginkan")
    print("4. search_my_game - Untuk mencari game yang dimiliki oleh User")
    print("5. search_game_at_store - Untuk mencari game yang ada di toko berdasarkan ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
    print("6. riwayat - Untuk melihat riwayat pembelian User")
    print("7. save - Untuk menyimpan data User")
def helpadmin():
    print("============ HELP ============")
    print("1. register - Untuk mendaftarkan pengguna baru ke program")
    print("2. login - Untuk melakukan login ke dalam sistem")
    print("3. tambah_game - Untuk menambahkan game ke toko")
    print("4. ubah_game - Untuk melakukan pengubahan pada informasi game")
    print("5. ubah_stok - mengubah stok game yang ada di toko")
    print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
    print("7. search_game_at_store - Untuk mencari game yang ada di toko berdasarkan ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
    print("8. topup - mengisi saldo kepada User")
    print("9. save - Untuk menyimpan data User")

