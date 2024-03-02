print("Menentukan Prioritas Proyek")

def skor_budget(budget):
    if budget <= 50:
        return 4
    elif 51 <= budget <= 80:
        return 3
    elif 81 <= budget <= 100:
        return 2
    else:
        return 1

def skor_waktu_pengerjaan(waktu):
    if waktu <= 20:
        return 10
    elif 21 <= waktu <= 30:
        return 5
    elif 31 <= waktu <= 50:
        return 2
    else:
        return 1

def skor_kesulitan(tingkat_kesulitan):
    if tingkat_kesulitan <= 3:
        return 10
    elif 4 <= tingkat_kesulitan <= 6:
        return 5
    elif 8 <= tingkat_kesulitan <= 10:
        return 1
    else:
        return 0

def total_skor(hasil):
    if 17 <= hasil <= 24:
        return "High"
    elif 10 <= hasil <= 16:
        return "Medium"
    elif 3 <= hasil <= 9:
        return "Low"
    else:
        return "Impossible"

def prioritas():
    budget = float(input("Masukkan budget: "))
    waktu = int(input("Masukkan waktu pengerjaan: "))
    tingkat_kesulitan = int(input("Masukkan tingkat kesulitan: "))

    jumlah_skor_budget = skor_budget(budget)
    jumlah_skor_pengerjaan = skor_waktu_pengerjaan(waktu)
    jumlah_skor_kesulitan = skor_kesulitan(tingkat_kesulitan)

    total_hasil = jumlah_skor_budget + jumlah_skor_kesulitan + jumlah_skor_pengerjaan

    prioritas_proyek = total_skor(total_hasil)
    print("Prioritas proyek:", prioritas_proyek)

prioritas()