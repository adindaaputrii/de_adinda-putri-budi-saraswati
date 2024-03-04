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

daftar_pelanggan = [
Pelanggan("Joni", 46, "C123"),
Pelanggan("David", 26, "A123"),
Pelanggan("Nanda", 26, "B123"),
Pelanggan("Joya", 25, "D123")
]

daftar_pelatih = [
Pelatih("Vicky", "Fitness", 4),
Pelatih("Gilang", "Bodybuilding", 5),
Pelatih("Dini", "Pilates", 4),
Pelatih("Rini", "Poundfit", 3)
]

daftar_kelas_latihan = [
KelasLatihan("Rini", "Poundfit", 3, "Kebugaran", "Rabu dan Kamis"),
KelasLatihan("Vicky", "Fitness", 4, "Kebugaran", "Senin - Jumat"),
KelasLatihan("Dini", "Pilates", 4, "Kebugaran", "Selasa - Kamis"),
KelasLatihan("Gilang", "Bodybuilding", 5, "Kebugaran", "Sabtu dan Minggu")
]

print("Informasi Pelanggan:")
for pelanggan in daftar_pelanggan:
    pelanggan.tampilkanInfo()
    print("")

print("\nInformasi Pelatih:")
for pelatih in daftar_pelatih:
    pelatih.tampilkanInfo()
    print("")

print("\nInformasi Kelas Latihan:")
for kelas_latihan in daftar_kelas_latihan:
    kelas_latihan.tampilkanInfo()
    print("")