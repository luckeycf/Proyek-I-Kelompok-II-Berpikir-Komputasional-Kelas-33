# Tugas Besar Mata Kuliah Berpikir Komputasional
# Institut Teknologi Bandung
# WI1102 Berpikir Komputasional — Kelas 33 — Semester 1 2026/2027 — Dosen: Dody Dharma, Ph.D.

# Anggota Kelompok:
# 16526115	Raffalian Abrari Yusuf
# 16526223	Mitchell Theodore A. T. Noya
# 16526157	Mahmud Adam Mukarim
# 19626085	Lucky Lukman Zhamil
 
# PROGRAM PENGATURAN KAPASITAS MAKSIMAL JEMBATAN
# Program memperhitungkan luas dan berat kendaraan serta memberi peringatan jika kapasitas dilampaui.

# KAMUS
# Jenis kendaraan disimpan dalam dictionary dengan jenis kendaraan sebagai kunci dan data kendaraan sebagai nilai

# ALGORITMA

# data setiap jenis kendaraan berisi berat rata-rata, panjang, dan lebar
# nilai yg terdapat dalam data ini merupakan rata-rata panjang dan lebar kendaraan yang kami (kelompok 2) tentukan
jenis_kendaraan ={
    "Motor": {
        "beratrata": 100,
        "panjang": 1.5,
        "lebar": 0.7
    },
    "Mobil": {
        "beratrata": 1000,
        "panjang": 4,
        "lebar": 1.8
    },
    "Truk": {
        "beratrata": 3000,
        "panjang": 5,
        "lebar": 2.2
    }
}

# FUNGSI
# terdapat 2 fungsi utama dalam program ini, yaitu fungsi untuk meminta input angka yang harus lebih besar dari batas minimum dan fungsi untuk menampilkan status kendaraan di jembatan.

# fungsi untuk meminta input angka yang harus lebih besar dari batas minimum
def angka_yang_diinput (pertanyaan, minimum):
    while True:
        try: # berfungsi untuk mencoba menjalankan kode di dalamnya. Jika terjadi kesalahan, akan masuk ke blok except
            angka = float(input(pertanyaan))

            if angka > minimum: # berfungsi untuk memeriksa apakah angka yang diinput lebih besar dari minimum
                return angka # jika angka lebih besar dari minimum, akan mengembalikan angka tersebut
            print("Nilai harus lebih besar dari", minimum) # jika angka tidak lebih besar dari minimum, akan mencetak pesan kesalahan dan meminta input lagi

        except ValueError: # berfungsi untuk menangkap kesalahan ValueError yang terjadi saat mencoba mengubah input menjadi float
            print("Masukkan angka yang valid.")

# fungsi untuk menampilkan status kendaraan di jembatan. fungsi ini akan menghitung luas dan berat kendaraan di jembatan, serta menampilkan peringatan jika kapasitas jembatan dilampaui.
def tampilkan_status():
    luas_terpakai = 0
    total_berat = 0

    print("\n--- Kendaraan di jembatan ---")

# memerik jumlah kendaraan di jembatan. jika tidak ada kendaraan, akan menampilkan pesan "Belum ada kendaraan"
    if len(kendaraan_di_jembatan) == 0:
        print("Belum ada kendaraan.")

# jika ada kendaraan, akan menampilkan daftar kendaraan beserta luas dan beratnya
    for kendaraan in kendaraan_di_jembatan:
        print(
            "#" + str(kendaraan["nomor"]), kendaraan["jenis"],
            "// Luas", round(kendaraan["luas"], 2), "m²",
            "// Beban", round(kendaraan["beban"], 2), "kg"
        )

        luas_terpakai += kendaraan["luas"]
        total_berat += kendaraan["beban"]

    # menampilkan luas jembatan, luas terpakai, total beban gabungan, dan batas berat jembatan
    # dibulatkan hingga 2 angka di belakang koma menggunakan fungsi round
    print("\nLuas jembatan:", round(luas_jembatan, 2), "m²")
    print("Luas terpakai:", round(luas_terpakai, 2), "m²")

    print("\nTotal beban gabungan:", round(total_berat, 2), "kg")
    print("Batas berat jembatan:", batas_berat, "kg")
    kosong = input("Tekan Enter untuk melanjutkan...")


# input ukuran dan kapasitas jembatan
panjang_jembatan = angka_yang_diinput("Panjang jembatan (m): ", 0)
lebar_jembatan = angka_yang_diinput("Lebar jembatan (m): ", 0)
batas_berat = angka_yang_diinput("Batas berat jembatan (kg): ", 0)

luas_jembatan = panjang_jembatan * lebar_jembatan
kendaraan_di_jembatan = []
nomor_berikutnya = 1


# menu simulasi

# menampilkan menu simulasi
while True:
    print("\n=== Simulasi Jembatan ===")
    print("1. Kendaraan masuk")
    print("2. Kendaraan keluar")
    print("3. Tampilkan kondisi jembatan")
    print("4. Selesai")

    pilihan = input("Pilih menu: ")

    # jika pengguna memilih menu 1
    if pilihan == "1":
        
        # minta input jenis kendaraan dari pengguna dan validasi inputnya
        daftar_jenis = list(jenis_kendaraan.keys())

        print("\nDaftar jenis kendaraan:")
        for nomor in range(len(daftar_jenis)):
            print(str(nomor + 1) + ".", daftar_jenis[nomor]) # nomor + 1 karena nomor urut dimulai dari 1, sedangkan indeks list dimulai dari 0.

        pilihan_jenis = input("Pilih nomor jenis kendaraan: ")

        if not pilihan_jenis.isdigit(): # jika input bukan angka, akan menampilkan pesan kesalahan dan meminta input lagi
            print("Pilihan harus berupa angka.")
            continue 

        nomor_jenis = int(pilihan_jenis) # mengubah input menjadi integer untuk digunakan sebagai indeks list

        if nomor_jenis < 1 or nomor_jenis > len(daftar_jenis):
            print("Nomor jenis kendaraan tidak tersedia.")
            continue
        
        jenis = daftar_jenis[nomor_jenis - 1]
        data = jenis_kendaraan[jenis]

        # tambahan ruang 0,5 m pada panjang dan lebar kendaraan
        panjang_aman = data["panjang"] + 0.5 #0,5 m merupakan tambahan untuk ruang bebas di kendaraan
        lebar_aman = data["lebar"] + 0.5
        luas_aman = panjang_aman * lebar_aman

        beban_kendaraan = data["beratrata"]

        # hitung luas dan berat kendaraan yang sudah ada di jembatan
        luas_sekarang = 0
        total_berat_sekarang = 0

        for kendaraan in kendaraan_di_jembatan:
            luas_sekarang += kendaraan["luas"]
            total_berat_sekarang += kendaraan["beban"]

        # periksa apakah kendaraan terlalu lebar, atau luas maupun berat akan melebihi batas
        lebar_batas = (lebar_aman > lebar_jembatan)
        luas_batas = (luas_sekarang + luas_aman > luas_jembatan)
        berat_batas = (total_berat_sekarang + beban_kendaraan > batas_berat)
        
        # kendaraan ditolak jika terlalu lebar atau kapasitas luas/berat tidak cukup
        if lebar_batas or luas_batas or berat_batas:
            print("\nKendaraan tidak dapat masuk.")

            if lebar_batas:
                print("PERINGATAN: kendaraan terlalu lebar untuk jembatan.")

            if luas_batas:
                print("PERINGATAN: kapasitas luas jembatan tidak cukup.")

            if berat_batas:
                print("PERINGATAN: batas berat jembatan terlampaui.")

        # jika tidak, kendaraan dapat masuk dan data kendaraan akan ditambahkan ke daftar kendaraan di jembatan
        else:
            kendaraan_baru = {
                "nomor": nomor_berikutnya,
                "jenis": jenis,
                "luas": luas_aman,
                "beban": beban_kendaraan}

            kendaraan_di_jembatan.append(kendaraan_baru) # append berfungsi untuk menambahkan item ke daftar kendaraan di jembatan

            print("\nKendaraan #" + str(nomor_berikutnya), "masuk ke jembatan satu arah.")
            nomor_berikutnya += 1

        tampilkan_status()

    # jika pengguna memilih menu 2
    elif pilihan == "2":
        if len(kendaraan_di_jembatan) == 0:
            print("Tidak ada kendaraan di jembatan.")
            continue

        print("\nPilih nomor kendaraan yang keluar:")
        for kendaraan in kendaraan_di_jembatan:
            print(
                "#" + str(kendaraan["nomor"]),
                kendaraan["jenis"],
                "// beban", kendaraan["beban"], "kg"
            )
        # meminta input nomor kendaraan yang ingin dikeluarkan dari jembatan
        nomor_keluar = input("Masukkan nomor kendaraan: ")

        if not nomor_keluar.isdigit():
            print("\nNomor harus berupa angka.")
            continue

        nomor_keluar = int(nomor_keluar)

        for indeks, kendaraan in enumerate(kendaraan_di_jembatan):
            if kendaraan["nomor"] == nomor_keluar:
                # Pada jembatan satu jalur tanpa ruang menyalip, kendaraan yang paling duluan masuk paling duluan
                if indeks != 0:
                    kendaraan_di_depan = kendaraan_di_jembatan[0]
                    print(
                        "Kendaraan #" + str(nomor_keluar),
                        "tidak dapat keluar karena kendaraan #"
                        + str(kendaraan_di_depan["nomor"]),
                        "masih berada di depannya."
                    )
                else:
                    kendaraan_di_jembatan.remove(kendaraan)
                    print("Kendaraan #" + str(nomor_keluar), "sudah keluar.")
                break
        else:
            print("Nomor kendaraan tidak ditemukan.")

    # jika pengguna memilih menu 3
    elif pilihan == "3":
        tampilkan_status()
        
    # jika pengguna memilih menu 4
    elif pilihan == "4":
        print("Simulasi selesai.")
        tampilkan_status()
        break

    # jika pengguna memilih menu yang tidak tersedia
    else:
        print("Pilihan menu tidak tersedia.")
