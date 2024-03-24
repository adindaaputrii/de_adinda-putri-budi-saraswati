## Resume Materi Pengenalan Data Engineer Part 2

**Data terstruktur**: merupakan data yang terorganisir dan terstruktur dengan format dan skema yang telah ditentukan sebelumnya. Data terstruktur disimpan di dalam database relasional (RDBMS) diproses menggunakan bahasa SQL (Structured Query Language) atau tools pemrosesan data terstruktur. Pengumpulan besar dari penyimpanan data terstruktur disebut *gudang data*. Dalam database relasional, contohnya seperti tabel user dengan kolom-kolom seperti nama, email, nomor telepon.

**Data semi-terstruktur** adalah jenis data yang berisi format data terstruktur dan data tidak terstruktur, yang lebih kompleks daripada data terstruktur, tetapi lebih mudah disimpan daripada data tidak terstruktur. Data semi-terstruktur tidak memiliki model data yang telah ditentukan sebelumnya, tetapi memiliki atribut struktural yang menjadi ciri khas data terstruktur. Contoh data semi-terstruktur adalah email, XML, dan bahasa markup lainnya, paket TCP/IP, file zip, dan integrasi data dari berbagai sumber. Data semi terstruktur sering kali digunakan dalam berbagai aplikasi, termasuk di bidang media sosial, analisis log, dan Internet of Things (IoT), di mana data dapat berasal dari berbagai sumber dengan format yang beragam. Keuntungan utama dari data semi terstruktur adalah fleksibilitasnya dalam menangani variasi struktur data yang berbeda-beda tanpa kehilangan semua manfaat struktur data terstruktur.

**Data tidak terstruktur**: merupakan data yang tidak terorganisir dan tidak terstruktur atau tidak memiliki skema yang telah ditentukan sebelumnya. Pemrosesan data tidak terstruktur biasanya melibatkan teknik-teknik seperti analisis teks, pengenalan pola, atau machine learning. Pengumpulan besar dari penyimpanan data tidak terstruktur disebut *danau data* (data lake). Data tidak terstruktur sering disimpan dalam format file seperti dokumen teks, file gambar, atau file audio/video. Penyimpanan data tidak terstruktur yaitu seperti sistem file, sistem manajemen aset digital (DAM), sistem manajemen konten (CMS), dan sistem kontrol versi.


<br>

**Relational database** adalah jenis database yang berbasis model data relasional, yang mengatur data dalam bentuk tabel dengan hubungan yang terdefinisi. Dalam model data relasional, data disimpan dalam tabel dengan setiap baris mengrepresentasikan satu record dan setiap kolom mengandung suatu jenis data tertentu. Hubungan relasi antara tabel dapat dibuat dengan menggunakan primary key dan foreign key. Sebuah relational database management system (RDBMS) adalah software yang digunakan untuk mengelola tabel relasional. RDBMS memungkinkan pengguna untuk mengakses, mengubah, dan menghapus data dengan mudah. Relational databases memiliki banyak manfaat, seperti pemeliharaan data yang tepat, integritas data, keamanan, dan pengembalian data. Data relasional memiliki beberapa karakteristik khusus, seperti:
- Data terstruktur: Data disimpan dalam tabel dengan hubungan yang terdefinisi, Data dapat diklasifikasikan dalam tabel yang terstruktur.
- Data berhubung: Hubungan antara tabel dapat dibuat dengan menggunakan primary key dan foreign key.
- Data dapat dikonversi: Data dapat dikonversi ke format yang lain, seperti XML atau JSON.

<br>

**NoSQL** merupakan jenis basis data non-relasional yang dirancang untuk mengelola data yang tidak mengikuti model tabel relasional yang digunakan dalam basis data relasional. NoSQL database memungkinkan penyimpanan dan pengambilan data yang lebih fleksibel dan scalable daripada basis data relasional. NoSQL databases tidak memerlukan skema yang terstruktur, sehingga menyediakan skala yang cepat untuk mengelola data besar dan terstruktur. NoSQL systems juga dikenal sebagai "Not only SQL" untuk memperingatkan bahwa mereka mungkin mendukung bahasa query yang mirip dengan SQL atau mungkin tidak.
NoSQL databases dapat dikelompokkan ke dalam beberapa kategori, termasuk:
- **Key-value store**: Ini menggunakan model data associative array (atau map/dictionary) sebagai data model fundamental. Data disimpan dalam bentuk key-value pair, dimana setiap key hanya muncul sekali dalam koleksi. Model key-value dapat diperluas menjadi model data yang terurut dan dapat mengambil data dengan cepat.
- **Wide column store**: Ini menggunakan model data kolom yang lebar sebagai data model fundamental. Data disimpan dalam bentuk kolom yang lebar, yang dapat mengembalikan data dengan cepat.
- **Graph database**: Ini menggunakan model data node dan edge sebagai data model fundamental. Data disimpan dalam bentuk node dan edge, yang dapat mengidentifikasi hubungan antara data dengan mudah.
- **Document database**: Ini menggunakan model data dokumen sebagai data model fundamental. Data disimpan dalam bentuk dokumen yang berbeda, yang memungkinkan mudah untuk mengubah data yang berubah-ubah.

<br><br>

**OLTP (Online Transaction Processing)** adalah sistem pengolahan data yang terutama digunakan untuk **mengelola transaksi** sehari-hari dalam sistem operasi berbasis database, seperti pemrosesan pesanan, reservasi, dan pembayaran. OLTP memiliki tujuan utama untuk mengelola transaksi dalam sistem operasi berbasis database, yang mencakup transaksi dalam bentuk penambahan, perbaruan, dan penghapusan data. OLTP menggunakan model data yang terstruktur, seperti relational database, dan memiliki tinggi kebutuhan konsistensi data dan integritas. OLTP memiliki keunggulan yang mendukung transaksi dengan tinggi kecepatan, tinggi konfigurasi, dan tinggi kemampuan untuk mengelola transaksi yang banyak. Struktur basis data OLTP cenderung sederhana dan terdiri dari banyak tabel yang saling terhubung untuk menyimpan data transaksi.

**OLAP (Online Analytical Processing)** adalah sistem pengolahan data yang terutama digunakan untuk **mengelola analisis data dan laporan**. OLAP menggunakan model data multidimensi, seperti kubus data, dan memiliki tinggi kebutuhan efisiensi dalam pengambilan data dan penganalisis data. OLAP menggunakan model data yang tidak terstruktur, seperti data warehouse, dan memiliki tinggi kebutuhan efisiensi dalam pengambilan data dan penganalisis data. OLAP memiliki keunggulan yang mendukung analisis data dengan tinggi kecepatan, tinggi kemampuan untuk mengelola data yang banyak, dan tinggi kemampuan untuk mengelola analisis data yang kompleks. OLAP digunakan untuk menganalisis data secara agregat untuk mendukung pengambilan keputusan dan analisis bisnis.

    Sebagai contoh, OLTP dapat digunakan untuk mengelola transaksi pembelian dan penjualan di sebuah toko online, sedangkan OLAP dapat digunakan untuk mengelola laporan dan analisis data pembelian dan penjualan di sebuah toko online.

<br><br>

Perbedaan antara database, data lake, data mart, dan data warehouse adalah sebagai berikut:
- **Database**: Database adalah sistem pengelolaan data yang mengumpulkan dan mengelola data yang digunakan dalam proses operasi bisnis. Database dapat berisi data yang berbeda, seperti data transaksi, data pelanggan, dan data produk. Database dapat berbasis relasi, seperti MySQL, atau tidak berbasis relasi, seperti MongoDB. Biasanya digunakan untuk aplikasi operasional sehari-hari dan memungkinkan penggunaan transaksi data secara efisien.

- **Data Lake**: Data lake adalah repositori penyimpanan data mentah dan data tidak terstruktur dalam skala besar yang dapat disimpan dalam bentuk raw. Data lake dapat berisi data dari berbagai sumber, seperti aplikasi, sensor, dan pihak ketiga. Data lake dapat digunakan untuk pengolahan data yang tidak terstruktur dan untuk mengelola data yang banyak. Tidak memiliki skema tetap, memungkinkan analisis yang fleksibel dan eksplorasi data.

- **Data Mart**: Data mart adalah gudang data yang melayani kebutuhan unit bisnis tertentu, seperti departemen keuangan, pemasaran, atau penjualan perusahaan. Data mart dapat dibuat dari data warehouse atau data lake, dan dapat diterapkan untuk pengolahan data yang terstruktur dan untuk mengelola data yang berhubungan dengan unit bisnis tertentu. Biasanya mengandung data yang sudah diolah dan dioptimalkan untuk analisis kebutuhan bisnis tertentu.

- **Data Warehouse**: Data warehouse adalah sistem pengelolaan data yang mengumpulkan dan mengelola data yang digunakan untuk analisis dan kecerdasan bisnis. Data warehouse dapat berisi data yang terstruktur dan yang berhubungan dengan kegiatan bisnis, seperti data transaksi, data pelanggan, dan data produk. Data warehouse dapat digunakan untuk pengolahan data yang terstruktur dan untuk mengelola data yang banyak. Data warehouse mengintegrasikan, membersihkan, dan mengorganisir data menjadi format yang mudah diakses dan dipahami untuk keperluan pelaporan dan analisis.

<br>

    Database dapat digunakan untuk pengelolaan data yang digunakan dalam proses operasi bisnis, sedangkan data lake dapat digunakan untuk pengolahan data yang tidak terstruktur dan untuk mengelola data yang banyak. Data mart dapat digunakan untuk melayani kebutuhan unit bisnis tertentu, sedangkan data warehouse dapat digunakan untuk analisis dan kecerdasan bisnis.