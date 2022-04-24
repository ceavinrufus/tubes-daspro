def help(role = "guest"):
    # I.S. role terdefinisi
    # F.S. Menampilkan instruksi pemakaian perintah

    # KAMUS LOKAL

    # ALGORITMA
    print("\n============ HELP ============")

    if role == "user":
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("3. buy_game - Untuk membeli game yang diinginkan")
        print("2. list_game - Untuk melihat list game yang dimiliki pengguna")
        print("4. search_my_game - Untuk mencari game yang dimiliki oleh user")
        print("5. search_game_at_store - Untuk mencari game yang ada di toko berdasarkan ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("6. riwayat - Untuk melihat riwayat pembelian user")
        print("7. help - Untuk menampilkan instruksi pemakaian perintah untuk user")
        print("8. save - Untuk menyimpan data")
        print("9. exit - Untuk keluar dari program")
    elif role == "admin":
        print("1. register - Untuk mendaftarkan pengguna baru ke program")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. tambah_game - Untuk menambahkan game ke toko")
        print("4. ubah_game - Untuk melakukan pengubahan pada informasi game")
        print("5. ubah_stok - mengubah stok game yang ada di toko")
        print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("7. search_game_at_store - Untuk mencari game yang ada di toko berdasarkan ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("8. topup - mengisi saldo kepada user")
        print("9. help - Untuk menampilkan instruksi pemakaian perintah untuk admin")
        print("10. save - Untuk menyimpan data")
        print("11. exit - Untuk keluar dari program")
    else:
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. help - Untuk menampilkan instruksi pemakaian perintah untuk guest")

    return
