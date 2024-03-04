class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan

    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def get_usia(self):
        return self.__usia
    
    def set_usia(self, usia):
        self.__usia = usia

    def get_id_pelanggan(self):
        return self.__id_pelanggan
    
    def set_id_pelanggan(self, id_pelanggan):
        self.__id_pelanggan = id_pelanggan
        
    def tampilkanInfo(self):
        print("Nama:", self.__nama)
        print("Usia:", self.__usia)
        print("ID Pelanggan:", self.__id_pelanggan)

class Pelatih:
    def __init__(self, nama, spesialisasi, tahun_pengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahun_pengalaman = tahun_pengalaman

    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama

    def get_spesialisasi(self):
        return self.__spesialisasi
    
    def set_spesialisasi(self, spesialisasi):
        self.__spesialisasi = spesialisasi

    def get_tahun_pengalaman(self):
        return self.__tahun_pengalaman
    
    def set_tahun_pengalaman(self, tahun_pengalaman):
        self.__tahun_pengalaman = tahun_pengalaman

    def tampilkanInfo(self):
        print("Nama:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahun_pengalaman)

class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        super().__init__(nama, spesialisasi, tahun_pengalaman)
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal
        self.__terpesan = 0

    def get_jenis_latihan(self):
        return self.__jenis_latihan

    def set_jenis_latihan(self, jenis_latihan):
        self.__jenis_latihan = jenis_latihan
    
    def get_jadwal(self):
        return self.__jadwal

    def set_jadwal(self, jadwal):
        self.__jadwal = jadwal

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Jenis Latihan:", self.__jenis_latihan)
        print("Jadwal:", self.__jadwal)
        print("")

    def pesanKelas(self):
        if self.__terpesan < 10:
            self.__terpesan += 1
            print("Kelas " + self.__jenis_latihan + " berhasil dipesan oleh " + daftar_pelanggan[self.__terpesan-1].get_nama() + " . Kuota kelas tersisa: " + str(10 - self.__terpesan))
        else:
            print("Kelas " + self.__jenis_latihan + "sudah penuh")

    def batalkanKelas(self):
        if self.__terpesan > 0:
            self.__terpesan -= 1
            print("Pemesanan kelas " + self.__jenis_latihan + " telah dibatalkan oleh " + daftar_pelanggan[self.__terpesan].get_nama() + " . Kuota kelas tersisa: " + str(10 + self.__terpesan))
        else:
            print("Pesanan kelas " + self.__jenis_latihan + "tidak ada")

class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, tingkat_kesulitan):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan
    
    def atur_posisi_yoga(self, posisi):
        print("Atur posisi yoga:", posisi)

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Tingkat kesulitan:", self.__tingkat_kesulitan)

class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, berat_maksimum):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum

    def atur_berat_badan(self, berat_badan):
        print("Berat badan:", berat_badan)

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Berat maksimum:", self.__berat_maksimum)


daftar_pelanggan = [
Pelanggan("Joni", 46, "C123"),
Pelanggan("David", 26, "A123"),
Pelanggan("Nanda", 26, "B123"),
Pelanggan("Joya", 25, "D123")
]

coach = [
    Yoga("Rini", "Fitness", 8, "Kelas Yoga", "Senin dan Rabu", "Sulit"),
    Yoga("Zuni", "Fitness", 3, "Kelas Yoga", "Senin-Sabtu", "Mudah"),
    AngkatBeban("Dino", "Bodybuilding", 3, "Kelas Angkat Beban", "Senin, Rabu, Kamis", 80),
    AngkatBeban("Gilang", "Bodybuilding", 10, "Kelas Angkat Beban", "Senin-Kamis", 95)
]

# pemesanan
for kelas in coach:
    kelas.pesanKelas()

print("")

# pembatalan
for kelas in coach:
    kelas.batalkanKelas()
