print("Tarif Pengiriman Paket Berdasarkan Berat dan Jarak")

def jumlah_tarif_berat(berat):
    if berat <= 20:
        return 10000
    elif 21 <= berat <= 30:
        return 15000
    elif 31 <= berat <= 60:
        return 20000
    else:
        return 45000

def jumlah_tarif_jarak(jarak):
    if jarak <= 5:
        return 2000
    elif 6 <= jarak <= 15:
        return 5000
    elif 16 <= jarak <= 30:
        return 10000
    else:
        return 15000

def perhitungan_tarif():
    berat = float(input("Masukkan berat paket: "))
    jarak = float(input("Masukkan jarak tempuh: "))

    tarif_berat = jumlah_tarif_berat(berat)
    tarif_jarak = jumlah_tarif_jarak(jarak)

    total_tarif = tarif_berat + tarif_jarak
    print("Tarif pengiriman paket:", total_tarif)

perhitungan_tarif()

