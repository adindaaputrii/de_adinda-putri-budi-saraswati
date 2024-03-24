## Jawaban Soal Prioritas 1

1. Perbedaan antara data terstruktur dan tidak terstruktur:
- **Data terstruktur**: merupakan data yang terorganisir dan terstruktur dengan format dan skema yang telah ditentukan sebelumnya. 
<p>

Data terstruktur disimpan di dalam database relasional (RDBMS) diproses menggunakan bahasa SQL (Structured Query Language) atau tools pemrosesan data terstruktur. Pengumpulan besar dari penyimpanan data terstruktur disebut *gudang data*. Dalam database relasional, contohnya seperti tabel user dengan kolom-kolom seperti nama, email, nomor telepon.

</p> 

- Contoh data terstruktur biasanya disimpan dalam format berikut ini:

a. JSON: {"nama": "John Doe", "usia": 25, "alamat": "Jalan Belakang 123"}

b. XML: <person> <name>John Doe</name> <age>25</age> <address>Jalan Belakang 123</address> </person>

c. CSV: 'nama,usia,alamat John Doe,25,Jalan Belakang 123'

<br>

- **Data tidak terstruktur**: merupakan data yang tidak terorganisir dan tidak terstruktur atau tidak memiliki skema yang telah ditentukan sebelumnya. 
<p>

Pemrosesan data tidak terstruktur biasanya melibatkan teknik-teknik seperti analisis teks, pengenalan pola, atau machine learning. Pengumpulan besar dari penyimpanan data tidak terstruktur disebut *danau data* (data lake). Data tidak terstruktur sering disimpan dalam format file seperti dokumen teks, file gambar, atau file audio/video. Penyimpanan data tidak terstruktur yaitu seperti sistem file, sistem manajemen aset digital (DAM), sistem manajemen konten (CMS), dan sistem kontrol versi.

</p>  

- Contoh data tidak terstruktur biasanya disimpan dalam format berikut ini:

a. Teks: 'John Doe, 25, Jalan Belakang 123'

b. Gambar: [gamnbar mobil merah]

c. Audio: [bunyi burung berkicau]

<br>

2. **Basis data relasional** (relational database) adalah jenis basis data yang menggunakan model data relasional untuk mengorganisasi dan mengelompokkan data dalam tabel. Setiap tabel merepresentasikan jenis entitas tertentu dan tabel-tabel tersebut terhubung melalui *foreign key*. Dalam model data relasional, data disimpan dalam tabel yang terhubung oleh hubungan relasi, yang mengatur ketergantungan dan keterkaitan antara data. Contoh penggunaan basis data relasional dalam dunia nyata adalah basis data user dan peminjaman buku di sebuah perpustakaan. Cara kerja basis data relasional yaitu menggunakan kueri bahasa SQL untuk mengambil, menyimpan, memperbarui, dan menghapus data dalam databasenya.

<br>

3. **Normalisasi** adalah proses untuk mengubah data yang tidak sesuai dengan model data relasional ke dalam format yang sesuai. Normalisasi membantu mengurangi redundansi data, menghilangkan anomali, dan memastikan data berada di posisi yang tepat. Hal ini dilakukan dengan membagi tabel menjadi tabel yang lebih kecil dan lebih terorganisir, serta memastikan bahwa setiap tabel memiliki struktur yang sesuai dan konsisten. Normalisasi penting dalam konteks basis data relasional karena ia memungkinkan pengelolaan data yang lebih mudah, menghindari kompleksitas, menghilangkan duplikat, memastikan integritas data, dan meminimalisir redundansi data.

<br><br>


## Jawaban Soal Prioritas 2

Perusahaan e-commerce umumnya memiliki data yang beragam, terstruktur, dan tidak terstruktur. Sehingga dengan kombinasi penggunaan basis data relasional dan NoSQL dapat menjaga pengelolaan data secara efektif. Basis data relasional cocok digunakan untuk mengelola data terstruktur seperti informasi pelanggan, produk, transaksi pelanggan, sedangkan NoSQL lebih cocok digunakan untuk mengelola data tidak terstruktur seperti log interaksi pengguna di e-commerce karena NoSQL menawarkan skalabilitas yang lebih baik untuk data dengan volume besar dan fleksibel terhadap perubahan skema. Untuk integrasi antara data terstruktur dan tidak terstruktur dapat dilakukan dengan menggunakan teknik ETL (Extract, Transform, Load) yang di mana data dari kedua sumber akan di extract kemudian ditransformasi untuk dijadikan format yang selaras, lalu dimuat ke gudang data untuk analisis data yang lebih lanjut.

<br><br>


## Jawaban Soal Ekplorasi

Untuk merancang dan mengimplementasikan data lake yang mengelola data terstruktur, semi-terstruktur, dan tidak terstruktur pada suatu perusahaan, perlu dilakukan analisis kebutuhan data perusahaan terlebih dahulu, seperti identifikasi sumber data dan jenis data, serta merancang arsitektur dan kebijakan data lake. Untuk penyimpanan data yang besar, dapat menggunakan platform data lake seperti Amazon S3, Google Cloud Storage, atau Apache Hadoop. Untuk mengintegrasikan data lake dengan sistem data lainnya di perusahaan, dapat menggunakan data mart atau layanan pekerjaan analitik seperti Azure Data Lake Analytics atau AWS Lake Formation dengan memastikan kesesuaian skema data dan format data antara data lake dengan sistem data lainnya di perusahaan untuk menghindari terjadinya konflik.


<br><br>

*referensi:*
- AWS: Apa perbedaan Antara Data terstruktur dan tidan terstruktur
- AWS: Data Lakes and Analytics
- Materi Alterra Academy