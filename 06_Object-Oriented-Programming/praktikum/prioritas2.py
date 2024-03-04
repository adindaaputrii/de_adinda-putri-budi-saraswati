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

# polymorphism
def polymorphism(KelasLatihan):
    print("Kelas Tersedia:")
    for kelas in KelasLatihan:
        kelas.tampilkanInfo()
        print("")

# metode khusus
def metode_khusus(KelasLatihan):
    for kelas in KelasLatihan:
        if isinstance(kelas, Yoga):
            kelas.atur_posisi_yoga("Tadasana")
        elif isinstance(kelas, AngkatBeban):
            kelas.atur_berat_badan(88)
        print("")

# polymorphism lanjutan
def infoSpesifik(kelas):
    if isinstance(kelas, Yoga):
        kelas.atur_posisi_yoga("Balasana")
        kelas.tampilkanInfo()
    elif isinstance(kelas, AngkatBeban):
        kelas.atur_berat_badan(70)
        kelas.tampilkanInfo()
    print("")

latihan_yoga = Yoga("Zizi", "Fitness", 6, "Yoga", "Senin-Kamis", "Sulit")
latihan_angkat_beban = AngkatBeban("Zaky", "Fitness", 3, "AngkatBeban", "Senin-Mingu", "90 kg")

polymorphism([latihan_yoga, latihan_angkat_beban])
metode_khusus([latihan_yoga, latihan_angkat_beban])
infoSpesifik(latihan_yoga)
infoSpesifik(latihan_angkat_beban)
