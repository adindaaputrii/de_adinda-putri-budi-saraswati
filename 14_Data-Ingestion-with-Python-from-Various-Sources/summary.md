## Ranguman Materi Data Ingestion with Python from Various Sources

**Data Ingestion** adalah proses pengumpulan, pemindahan, dan pemuatan data dari berbagai sumber ke dalam sistem penyimpanan atau analisis data terpusat. Proses ini melibatkan pemindahan, pemrosesan, dan pembebanan data dari berbagai sumber ke dalam sistem penyimpanan data yang sentral dan terstruktur. **Tujuan** utama dari data ingestion adalah untuk mengambil data dari sumbernya, mengubah formatnya (jika diperlukan), memastikan data tersedia dan siap digunakan untuk analisis lebih lanjut, dan memuatnya ke dalam sistem penyimpanan data yang tepat. Proses ini dapat melibatkan berbagai jenis data, termasuk data terstruktur dan tidak terstruktur, serta data streaming atau batch.

<br>

Berikut adalah beberapa poin penting tentang data ingestion:
1. **Sumber Data**: Data dapat berasal dari berbagai sumber, seperti database relasional, aplikasi bisnis, media sosial, sensor, perangkat IoT, dan lainnya.
2. **Transformasi Data**: Data yang diambil mungkin perlu diubah dan dibersihkan sebelum dimuat ke sistem target. Proses ini dapat mencakup pemformatan ulang data, menangani nilai yang hilang, dan memastikan konsistensi data.
3. **Sistem Target**: Data yang telah melalui proses ingestion biasanya disimpan dalam data warehouse, data lake, atau sistem analitik lainnya.

<br>

Data ingestion memiliki beberapa tipe tergantung pada karakteristik data dan proses pemindahannya. **Berikut beberapa tipe umum data ingestion:**

1. *Batch Data Ingestion*:
- Ini adalah tipe ingestion data tradisional dimana data dipindahkan secara berkala (misalnya, harian, mingguan, bulanan) dalam kumpulan besar yang sudah lengkap.
- Cocok untuk data yang tidak memerlukan pemrosesan real-time dan volumenya besar.

Contoh: memindahkan data penjualan dari sistem point-of-sale ke data warehouse setiap malam.

2. *Real-time Data Ingestion*:
- Data dipindahkan dan diproses secara terus menerus (real-time) saat data tersebut dibuat.
- Digunakan untuk data yang membutuhkan analitik real-time dan pengambilan keputusan instan.

Contoh: data streaming dari sensor di pabrik untuk memantau performa mesin secara langsung.

3. *Hybrid Data Ingestion*:
Hybrid data ingestion adalah proses penggabungan pendekatan batch dan real-time data ingestion untuk menangani berbagai jenis data secara efisien.

Konsep dasarnya adalah:
- Data yang tidak memerlukan pemrosesan real-time dan volumenya besar, bisa ditangani dengan pendekatan batch yang lebih efisien.
- Sebaliknya, data yang membutuhkan analitik real-time dan pengambilan keputusan instan, ditangani dengan pendekatan real-time.

<br>

Beberapa cara untuk menerapkan hybrid data Igestion:
- *Micro-batching*: Memindahkan data dalam kumpulan kecil secara berkala (misalnya, setiap menit, jam) untuk mendekati real-time namun tetap efisien.
- *Lambda Architecture*: Membagi aliran data menjadi jalur batch dan real-time, yang diproses secara terpisah. Jalur batch digunakan untuk data historis dan analitik mendalam, sedangkan jalur real-time digunakan untuk pemrosesan data yang membutuhkan respons cepat.
- *Change Data Capture* (CDC): Hanya menangkap perubahan yang terjadi pada data sumber secara real-time dan memindahkannya, bukan keseluruhan data. Ini mengurangi beban dibanding memindahkan seluruh data secara berkala.

<br>

Keuntungan Hybrid Data Ingestion:
- Fleksibilitas: Menangani berbagai jenis data dengan pendekatan yang sesuai.
- Efisiensi: Mengoptimalkan sumber daya komputasi dengan memproses data batch secara efisien dan data real-time secara cepat.
- Skalabilitas: Dapat menangani volume data yang besar dan beragam.
- Menyediakan data terkini dan historis: Memungkinkan analisis data terkini dari aliran real-time dan data historis dari pemrosesan batch.

<br>

Teknologi yang digunakan dalam data ingestion:
- ETL tools (Extract, Transform, Load): Alat ETL mengekstrak data dari berbagai sumber, mengubahnya sesuai kebutuhan, dan memuatnya ke dalam sistem target.
- Data integration platforms: Platform integrasi data menyediakan alat dan layanan untuk menghubungkan berbagai sumber data dan memfasilitasi pertukaran data.
- Streaming data platforms: Platform streaming data digunakan untuk memproses data real-time yang berasal dari sumber seperti sensor dan perangkat IoT.

<br>

**Sumber Data untuk Ingestion dengan Python**
1. **Database**:
- Database relasional: MySQL, PostgreSQL, Oracle, SQL Server
- NoSQL databases: MongoDB, Cassandra, CouchDB
- Data warehouse: Teradata, Amazon Redshift, Google BigQuery

<br>

2. **Sistem File**:
- File CSV: Data terstruktur dalam format CSV (Comma Separated Values)
- File JSON: Data terstruktur dalam format JSON (JavaScript Object Notation)
- File log: Data teks yang berisi informasi tentang aktivitas sistem

<br>

3. **API**:
- API RESTful: Menyediakan akses ke data melalui HTTP requests
- API streaming: Menyediakan data real-time melalui protokol streaming seperti WebSocket
- API web scraping: Mengambil data dari situs web

<br>

4. **Platform Cloud**:
- Amazon S3: Layanan penyimpanan objek cloud
- Google Cloud Storage: Layanan penyimpanan objek cloud
- Microsoft Azure Blob Storage: Layanan penyimpanan objek cloud

<br>

5. **Sensor dan Perangkat IoT**:
- Sensor suhu: Mengumpulkan data temperatur
- Sensor tekanan: Mengumpulkan data tekanan
- Sensor akselerasi: Mengumpulkan data pergerakan

<br> <br>

Ada beberapa **library Python yang dapat digunakan untuk ingestion data**, berikut beberapa contohnya:
- *Pandas*: Library populer untuk analisis data yang menyediakan fungsi untuk membaca data dari berbagai sumber seperti CSV, JSON, database, dan API.
- *SQLAlchemy*: Library Object Relational Mapper (ORM) untuk interaksi dengan database relasional.
- *psycopg2*: Library untuk koneksi dan interaksi dengan database PostgreSQL.
- *requests*: Library untuk membuat HTTP requests ke API.
- *Beautiful Soup*: Library untuk parsing HTML dan scraping data dari situs web.
- *Kafka*: Platform streaming data untuk memproses data real-time.

<br><br>

**Data storage**, atau penyimpanan data, adalah proses menyimpan data yang telah di-ingest ke dalam suatu sistem penyimpanan data. Data storage merupakan langkah penting dalam pengelolaan data karena untuk:

1. Menyimpan data secara aman dan terorganisir: Data storage memastikan data Anda tersimpan dengan aman dan terhindar dari kerusakan atau kehilangan.
2. Memudahkan akses data: Data storage memudahkan Anda untuk mengakses data saat dibutuhkan untuk analisis, pelaporan, atau keperluan lainnya.
3. Memungkinkan skalabilitas: Data storage memungkinkan Anda untuk menyimpan data dalam jumlah besar dan skalabel seiring dengan pertumbuhan kebutuhan Anda.

<br>

Berikut ini beberapa **jenis data storage** yang umum digunakan, antara lain:
- **Storage lokal**: Menyimpan data pada perangkat fisik seperti hard disk drive (HDD) atau solid-state drive (SSD).
- **Storage cloud**: Menyimpan data di server cloud yang dapat diakses melalui internet.
- **Storage terdistribusi**: Menyimpan data di beberapa lokasi fisik yang berbeda untuk meningkatkan redundansi dan performa.

<br>

Ada berbagai **teknologi yang digunakan untuk data storage**, berikut beberapa contohnya:
- **Sistem file**: Menyediakan struktur untuk mengatur dan mengelola data di dalam penyimpanan.
- **Database**: Menyimpan data terstruktur dalam tabel dan kolom.
- **Data warehouse**: Menyimpan data historis dan teragregasi untuk analisis dan pelaporan.
- **Data lake**: Menyimpan data dalam format aslinya tanpa struktur tertentu untuk analisis dan eksplorasi data.

<br>

*Pemilihan solusi data storage yang tepat tergantung pada beberapa faktor, seperti*:
1. **Jenis dan volume data**: Jenis dan volume data yang ingin disimpan akan menentukan jenis penyimpanan yang Anda perlukan.
2. **Kebutuhan akses data**: Seberapa sering dan oleh siapa data perlu diakses akan menentukan jenis penyimpanan yang diperlukan.
3. **Anggaran**: Biaya solusi data storage bervariasi tergantung pada jenis dan fiturnya.
4. **Keamanan**: Pastikan solusi data storage yang dipilih memiliki fitur keamanan yang memadai untuk melindungi data.