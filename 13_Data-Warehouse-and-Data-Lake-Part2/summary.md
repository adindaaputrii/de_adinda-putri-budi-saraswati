## Resume Materi Data Warehouse and Data Lake Part 2

**Data Warehouse** adalah sistem pengelolaan data yang mengumpulkan dan mengelola data dari berbagai sumber yang berbeda yang digunakan untuk analisis bisnis dan pengambilan keputusan. Data warehouse dapat berisi data yang terstruktur dan yang berhubungan dengan kegiatan bisnis, seperti data transaksi, data pelanggan, dan data produk. Data warehouse dapat digunakan untuk pengolahan data yang terstruktur dan untuk mengelola data yang banyak. Tujuan utama dari Data Warehouse adalah untuk mengintegrasikan data dari berbagai sumber, mengelompokkannya ke dalam format yang konsisten, dan menyediakan akses yang mudah bagi pengguna untuk menganalisis data tersebut.

Berikut adalah beberapa karakteristik utama dari Data Warehouse:
1. **Sumber Data yang Beragam**: Data Warehouse menerima data dari berbagai sumber yang berbeda, termasuk sistem operasional, database eksternal, file, dan sumber data lainnya.
2. **Integrasi Data**: Data Warehouse mengintegrasikan data dari berbagai sumber menjadi satu tempat penyimpanan tunggal. Hal ini memungkinkan pengguna untuk melihat data secara holistik dan mendapatkan pemahaman yang lebih baik tentang operasi bisnis.
3. **Penyimpanan Data Historis**: Data Warehouse menyimpan data historis dalam jangka waktu yang panjang. Ini memungkinkan pengguna untuk melacak dan menganalisis tren sepanjang waktu.
4. **Optimasi untuk Analisis**: Data Warehouse dirancang khusus untuk mendukung analisis data. Ini termasuk struktur data yang dioptimalkan, indeks yang dibuat dengan bijak, dan kueri yang dioptimalkan untuk kinerja yang cepat.
5. **Akses Mudah**: Data Warehouse menyediakan akses yang mudah bagi pengguna untuk melakukan analisis data. Ini dapat dilakukan melalui antarmuka pengguna berbasis GUI (Graphical User Interface) atau melalui kueri SQL.
6. **Kesatuan Data**: Data Warehouse menyediakan satu sumber kebenaran (single source of truth) untuk data bisnis. Ini membantu memastikan konsistensi dan akurasi data di seluruh organisasi.

**Data Lake** adalah sebuah konsep penyimpanan data yang memungkinkan organisasi untuk menyimpan data dalam format mentah dan tidak terstruktur, serta memungkinkan pengolahan dan analisis data yang lebih fleksibel. Data Lake dapat menyimpan berbagai jenis data, termasuk data terstruktur, semi-terstruktur, dan tidak terstruktur, tanpa perlu memperhatikan skema data terlebih dahulu.

Berikut adalah beberapa karakteristik utama dari Data Lake:
1. **Penyimpanan Data Mentah**: Data Lake menyimpan data dalam format mentah dan tidak terstruktur, tanpa perlu mengubah atau menyusunnya ke dalam format yang terstruktur sebelumnya. Ini memungkinkan penyimpanan data dalam bentuk aslinya dan memungkinkan akses lebih fleksibel.
2. **Skala yang Besar**: Data Lake dirancang untuk menangani volume data yang sangat besar. Ini memungkinkan organisasi untuk menyimpan data dari berbagai sumber dan dalam berbagai format tanpa khawatir tentang batasan kapasitas.
3. **Fleksibilitas Analisis**: Data Lake menyediakan fleksibilitas yang tinggi dalam analisis data. Pengguna dapat menjalankan berbagai jenis analisis, mulai dari analisis tradisional hingga analisis prediktif dan machine learning, tanpa perlu mentransformasi atau mengubah struktur data terlebih dahulu.
4. **Data Tidak Terstruktur**: Data Lake tidak memerlukan skema data yang ketat atau struktur data yang terdefinisi sebelumnya. Ini memungkinkan organisasi untuk menyimpan data dalam format tidak terstruktur seperti file teks, file JSON, file CSV, dan lain-lain.


Berikut adalah beberapa perbedaan utama antara data lake dan data warehouse:

**1. Struktur data**:
- Data lake: Mentah, tidak terstruktur, dan beragam format.
- Data warehouse: Terstruktur, terorganisir, dan formatnya konsisten.

**2. Tujuan**:
- Data lake: Menyimpan semua data dalam format aslinya untuk arsip dan eksplorasi data di masa depan.
- Data warehouse: Mendukung analisis data dan pelaporan bisnis.

**3. Skalabilitas**:
- Data lake: Sangat skalabel dan dapat menampung data dalam jumlah besar.
- Data warehouse: Skalabilitasnya lebih terbatas dibandingkan data lake.

**4. Akses**:
- Data lake: Akses data lebih kompleks dan membutuhkan keterampilan teknis.
- Data warehouse: Akses data lebih mudah dan dapat digunakan oleh berbagai pengguna bisnis.

**5. Keamanan**:
- Data lake: Keamanan data perlu diimplementasikan secara manual.
- Data warehouse: Keamanan data biasanya terintegrasi dengan sistem.

**6. Biaya**:

- Data lake: Biaya awal lebih rendah karena tidak memerlukan struktur data yang kompleks.
- Data warehouse: Biaya awal lebih tinggi karena memerlukan infrastruktur dan perangkat lunak khusus.

<br>

**Data Lakehouse** adalah konsep yang menggabungkan keunggulan dari Data Lake dan Data Warehouse ke dalam satu platform tunggal. Ini adalah evolusi dari kedua konsep tersebut yang bertujuan untuk menyediakan lingkungan penyimpanan data yang lebih holistik dan terintegrasi.

Berikut adalah beberapa ciri utama dari Data Lakehouse:
1. **Penyimpanan Skema-on-Read**: Seperti pada Data Lake, Data Lakehouse menggunakan penyimpanan skema-on-read, yang memungkinkan data disimpan dalam format yang mentah atau mentah (raw) tanpa perlu diperlakukan dengan skema tertentu pada saat disimpan. Data dapat diolah dan disusun sesuai dengan kebutuhan saat diperlukan.

2. **Struktur Data dan Skema**: Data Lakehouse mempertahankan fitur-fitur struktur data dan skema seperti pada Data Warehouse. Ini memungkinkan definisi skema pada saat query atau analisis, yang memungkinkan konsistensi dan struktur yang lebih teratur dalam penyimpanan dan pengolahan data.

3. **Performa dan Konsistensi**: Data Lakehouse bertujuan untuk menyediakan performa dan konsistensi yang lebih baik daripada Data Lake tradisional. Dengan menggunakan teknologi dan optimasi yang serupa dengan Data Warehouse, Data Lakehouse dapat memberikan performa yang lebih baik dalam mengakses dan menganalisis data, sambil mempertahankan fleksibilitas skema-on-read.

4. **Kemampuan Analitik**: Data Lakehouse menyediakan kemampuan analitik yang kuat, termasuk pengolahan data real-time, analisis yang mendalam, dan visualisasi data. Ini memungkinkan organisasi untuk mendapatkan wawasan yang lebih baik dari data mereka, mempercepat pengambilan keputusan, dan mendukung inovasi.

5. **Integrasi dan Interoperabilitas**: Data Lakehouse memungkinkan integrasi yang lebih baik dengan alat dan platform analitik yang ada, serta interoperabilitas yang lebih tinggi dengan infrastruktur data yang sudah ada. Ini memudahkan organisasi untuk menggabungkan data dari berbagai sumber dan menjalankan analisis lintas-data yang komprehensif.

<br>

**Citus** adalah sebuah ekstensi untuk basis data PostgreSQL yang dirancang untuk mengelola data dalam skala yang sangat besar. Tujuan utamanya adalah untuk memperluas PostgreSQL agar dapat digunakan dalam lingkungan yang membutuhkan kinerja tinggi dan skalabilitas horizontal. Berikut adalah beberapa poin utama terkait Citus:

1. **Skalabilitas Horizontal**: Citus memungkinkan PostgreSQL untuk membagi tabel besar menjadi bagian-bagian yang lebih kecil, yang disebut shard, dan mendistribusikannya di beberapa node atau server. Ini memungkinkan untuk menangani kumpulan data yang sangat besar dengan mendistribusikan beban kerja secara merata di antara node-node yang tersedia.

2. **Paralelisasi dan Kinerja Tinggi**: Dengan membagi data menjadi shard-shard yang dapat diakses secara independen, Citus memungkinkan kueri untuk dieksekusi secara paralel di beberapa node. Ini meningkatkan kinerja secara signifikan, terutama untuk kueri-kueri yang memerlukan pemrosesan data yang intensif.

3. **Fitur-Fitur PostgreSQL yang Ditingkatkan**: Citus mempertahankan kompatibilitas penuh dengan PostgreSQL dan memperluasnya dengan fitur-fitur tambahan yang dioptimalkan untuk lingkungan data yang besar. Ini termasuk fitur-fitur seperti partisi yang didistribusikan, indeks yang didistribusikan, dan join yang didistribusikan.

4. **Fleksibilitas dan Kemampuan Analitik**: Citus memungkinkan untuk mengelola berbagai jenis data, termasuk data transaksional dan analitik. Ini membuatnya cocok untuk berbagai jenis aplikasi, mulai dari aplikasi e-commerce hingga analisis data tingkat perusahaan.

5. **Integrasi dengan Ekosistem PostgreSQL**: Citus terintegrasi dengan ekosistem alat-alat dan library-library yang tersedia untuk PostgreSQL, seperti pgAdmin, psql, dan JDBC. Ini mempermudah pengembangan dan administrasi aplikasi yang menggunakan Citus.

Ada beberapa situasi di mana penggunaan Citus mungkin tidak ideal. Beberapa contoh di antaranya termasuk:

- **Ukuran Data yang Kecil**: Jika ukuran data Anda relatif kecil dan dapat diakomodasi oleh satu instance PostgreSQL standar, maka penggunaan Citus mungkin terlalu kompleks dan berlebihan. Citus dirancang terutama untuk menangani skala data yang sangat besar dan kompleksitasnya akan memberikan overhead tambahan jika digunakan untuk kasus penggunaan yang lebih sederhana.

- **Sifat Transaksional yang Rumit**: Jika aplikasi Anda memiliki kebutuhan transaksional yang sangat kompleks, terutama yang melibatkan banyak operasi transaksi yang sering terjadi pada data yang sama, penggunaan Citus mungkin tidak cocok. Meskipun Citus mendukung transaksi dalam pengaturan distribusi, kompleksitasnya dapat membuat pengelolaan transaksi menjadi lebih rumit.

- **Keterbatasan Penyimpanan pada Node**: Citus mendistribusikan data ke beberapa node, dan kapasitas penyimpanan pada setiap node menjadi faktor yang penting. Jika kapasitas penyimpanan pada setiap node terlalu kecil untuk menangani data yang diperlukan, atau jika distribusi data yang tidak merata menyebabkan ketidakseimbangan penggunaan ruang penyimpanan, maka penggunaan Citus mungkin tidak tepat.

- **Kasus Penggunaan yang Sederhana**: Jika Anda memiliki aplikasi atau kasus penggunaan yang sederhana dengan kebutuhan pengolahan data yang relatif kecil dan tidak ada kebutuhan akan skalabilitas horizontal, maka menggunakan Citus mungkin menjadi overkill. Dalam kasus-kasus seperti itu, penggunaan PostgreSQL standar dapat cukup memadai.

- **Biaya dan Kompleksitas Operasional**: Penggunaan Citus juga bisa membawa biaya tambahan, baik dalam hal biaya infrastruktur (untuk menambah node tambahan) maupun biaya operasional (untuk mengelola dan memelihara kluster Citus). Jika biaya dan kompleksitas operasional menjadi masalah, terutama untuk skala yang tidak membutuhkan Citus, maka penggunaan Citus mungkin tidak diinginkan.

<br>

**Tabel columnar** (atau kadang disebut juga dengan columnar storage atau penyimpanan kolom) adalah cara penyimpanan data di mana data dalam tabel disimpan dalam kolom-kolom secara terpisah, bukan dalam baris-baris seperti pada penyimpanan baris tradisional. Dalam penyimpanan kolom, nilai-nilai dalam setiap kolom dikelompokkan bersama dalam struktur data yang disebut kolomar, yang memungkinkan untuk mengakses nilai-nilai tersebut dengan lebih efisien.

**Replikasi** mengacu pada proses menyalin data dari satu node Citus ke node lain dalam kluster. Tujuan utama dari replikasi adalah untuk meningkatkan ketersediaan data dan ketahanan sistem secara keseluruhan. Berikut adalah beberapa poin penting terkait replikasi di Citus:

- **Ketersediaan Tinggi**: Dengan memiliki salinan data di beberapa node, Citus dapat terus melayani kueri bahkan jika satu node mengalami kegagalan. Dengan replikasi yang tepat, Citus dapat memberikan tingkat ketersediaan yang tinggi bagi aplikasi Anda.

- **Pengaturan Replikasi**: Citus mendukung beberapa mode replikasi yang dapat dikonfigurasi sesuai kebutuhan. Salah satu mode replikasi yang umum adalah replikasi multi-master, di mana setiap node berfungsi sebagai master dan replika, sehingga data dapat ditulis dan dibaca dari setiap node. Citus juga mendukung replikasi satu arah, di mana data hanya dapat ditulis ke node master dan disalin ke node replika.

- **Pengoptimalan Kueri**: Replikasi dapat membantu dalam mendistribusikan beban kueri di antara node-node dalam kluster. Dengan replikasi yang tepat, Citus dapat mengoptimalkan lokasi eksekusi kueri untuk meminimalkan latensi dan memaksimalkan kinerja.

- **Replica-Failover**: Citus menyediakan mekanisme otomatis untuk failover jika node master mengalami kegagalan. Dengan replikasi yang sudah disiapkan, Citus dapat secara otomatis mempromosikan salah satu node replika menjadi master baru dan melanjutkan operasi dengan minimal gangguan.

- **Konsistensi Data**: Replikasi di Citus dirancang untuk memastikan konsistensi data di seluruh kluster. Setiap kali data ditulis ke master, itu juga disalin ke node-node replika dengan cara yang memastikan integritas data.

Dengan demikian, replikasi merupakan fitur penting dalam arsitektur Citus yang memungkinkan untuk meningkatkan ketersediaan, kinerja, dan ketahanan sistem secara keseluruhan. Itu juga memungkinkan Citus untuk menangani aplikasi dengan volume data yang besar dengan lebih efisien dan dapat diandalkan.

<br>

**Sharding** mengacu pada proses membagi data menjadi bagian-bagian yang lebih kecil yang disebut shard dan mendistribusikannya di antara beberapa node atau server dalam kluster Citus. Tujuannya adalah untuk meningkatkan kinerja dan skalabilitas sistem dengan mendistribusikan beban kerja secara merata di antara node-node yang tersedia.

Berikut adalah beberapa poin penting terkait sharding dalam Citus:

- **Pemecahan Data**: Dalam sharding, data dipecah menjadi bagian-bagian yang lebih kecil yang disebut shard. Setiap shard berisi subset data yang dapat dikelola secara independen oleh node-node dalam kluster.

- **Distribusi Data**: Setelah data dipecah menjadi shard-shard, Citus mendistribusikan shard-shard tersebut di antara beberapa node dalam kluster. Distribusi data biasanya dilakukan berdasarkan kunci partisi tertentu, seperti kunci hash atau rentang nilai.

- **Skalabilitas Horizontal**: Sharding memungkinkan untuk menangani volume data yang besar dengan memperluas kapasitas penyimpanan dan daya komputasi sistem secara horizontal. Dengan menambahkan node baru ke kluster, Citus dapat secara otomatis mendistribusikan shard-shard tambahan ke node-node tersebut, sehingga meningkatkan kapasitas keseluruhan kluster.

- **Optimasi Kueri**: Dengan sharding, Citus dapat membagi kueri menjadi subkueri yang dapat dieksekusi secara paralel di beberapa node. Ini memungkinkan Citus untuk mengoptimalkan kinerja kueri dengan mendistribusikan beban kerja secara merata di antara node-node dalam kluster.

- **Konsistensi Data**: Meskipun data dibagi menjadi shard-shard yang dikelola secara terpisah, Citus memastikan konsistensi data di seluruh kluster. Operasi tulis dan baca yang konsisten diterapkan di semua node, sehingga memastikan integritas data.

Dengan demikian, sharding merupakan fitur kunci dalam Citus yang memungkinkan untuk meningkatkan kinerja, skalabilitas, dan ketersediaan sistem dengan mendistribusikan data di antara beberapa node dalam kluster. Ini adalah pendekatan yang umum digunakan dalam arsitektur data yang besar dan kompleks untuk mengatasi tantangan dalam mengelola volume data yang besar.

<br>

**Schema** dalam data warehouse merujuk pada struktur organisasi dari data yang disimpan di dalamnya. Schema dalam data warehouse mendefinisikan bagaimana data disusun, diorganisasi, dan dihubungkan satu sama lain. Schema ini terdiri dari objek seperti tabel dan indeks yang menggambarkan hubungan logis data dalam data warehouse. Ada empat jenis schema yang sering digunakan dalam data warehouse: *Star Schema, Snowflake Schema, Galaxy Schema dan One Big Table (OBT)*.
1. **Star Schema**: Star schema adalah jenis skema di mana terdapat satu tabel fakta yang berhubungan dengan beberapa tabel dimensi. Tabel fakta berisi data numerik atau kuantitatif yang diukur atau dihitung, sedangkan tabel dimensi berisi atribut-atribut yang menggambarkan dimensi atau sudut pandang dari data tersebut. Dalam skema ini, tabel fakta berada di tengah, sementara tabel dimensi tersebar di sekelilingnya, membentuk struktur seperti bintang. Star schema sering digunakan karena kesederhanaannya dan kemudahan dalam melakukan analisis data. Ini merupakan schema terbaik untuk perusahaan yang ingin maksimal kegunaan simpel dan bisa mengikuti tinggi disk space.

2. **Snowflake Schema**: Snowflake schema adalah variasi dari star schema di mana tabel dimensi dibagi menjadi beberapa tabel yang lebih kecil, membentuk struktur yang menyerupai kristal salju. Hal ini dilakukan untuk mengurangi redundansi dan memperbaiki normalisasi pada skema serta mengurangi biaya overhead, sehingga memungkinkan pengelolaan data yang lebih efisien. Namun, snowflake schema dapat menyulitkan kueri dan pemrosesan data karena harus bergantung pada gabungan dan operasi lainnya untuk menggabungkan data dari tabel dimensi yang terkait.

3. **Galaxy Schema**: Galaxy Schema adalah sebuah schema data warehouse yang menggunakan beberapa tabel fakta yang terhubung dengan tabel dimensi yang diteruskan melalui relasi foreign key. Galaxy Schema mengurangi redundansi dan ideal untuk sistem database yang kompleks.

4. **One Big Table**: One big table, atau flat schema, adalah sebuah model data yang menggunakan satu tabel yang besar untuk menyimpan semua data, tanpa memperlukan tabel dimensi terpisah. Dalam skema ini, semua atribut atau dimensi direpresentasikan sebagai kolom dalam satu tabel. Meskipun sederhana dalam strukturnya dan dapat mempercepat proses query, namun pendekatan ini dapat menjadi sulit untuk dikelola dan dianalisis karena cenderung menghasilkan banyak redundansi data dan sulit untuk melacak hubungan antara data.

<br>

**Colocation** adalah sebuah konfigurasi yang mengatur bagaimana data dikelompokkan dan tersimpan serta mempertahankan data yang terkait atau saling terkait pada node yang sama dalam klaster Citus. Dengan kata lain, colocation mengacu pada pengelompokan atau penempatan bersama data yang memiliki hubungan yang erat, seperti data yang sering digabungkan atau di-join dalam kueri yang sama.

Colocation juga memungkinkan pengguna untuk mengelompokkan data berdasarkan dimensi yang berbeda, seperti waktu, lokasi, dan produk, yang dapat mempermudah analisis data. Colocation di Citus dapat diterapkan pada berbagai tipe data warehouse, termasuk Star Schema, Snowflake Schema, dan Galaxy Schema. Di dalam tabel fakta, data dikelompokkan berdasarkan dimensi yang berbeda, seperti waktu, lokasi, dan produk, yang dapat mempermudah analisis data. Tabel dimensi dapat dibuat untuk setiap dimensi yang digunakan, seperti waktu, lokasi, dan produk, yang dapat mengelompokkan data berdasarkan kriteria yang berbeda.

Colocation sangat penting dalam sistem basis data terdistribusi seperti Citus karena dapat mempengaruhi kinerja kueri. Ketika data yang terkait disimpan bersama-sama pada satu node, Citus dapat melakukan operasi gabungan atau join secara lokal di node tersebut, mengurangi latensi dan overhead jaringan yang terkait dengan mentransfer data di antara node-node dalam klaster.

<br>

**BigQuery** adalah sebuah layanan analisis data yang disediakan oleh Google Cloud Platform (GCP). Ini adalah layanan data warehouse berbasis cloud yang sangat dipercepat dan didesain untuk menganalisis set data yang sangat besar dengan cepat. BigQuery adalah platform as a service (PaaS) yang menyediakan kemampuan untuk query data menggunakan SQL. Sistem ini dapat mengelola data dari berbagai sumber, termasuk data yang berasal dari Google Cloud Storage, Google Cloud Pub/Sub, dan lain-lain. BigQuery memungkinkan pengguna untuk menyimpan, mengeksekusi, dan menganalisis data dalam skala besar tanpa perlu mengelola infrastruktur yang rumit. 

Beberapa fitur utama dari BigQuery meliputi:
1. **Skalabilitas**: BigQuery dirancang untuk menangani kuantitas data yang besar dengan cepat dan efisien. Ini dapat menangani terabyte hingga petabyte data tanpa perlu merancang atau memperluas infrastruktur secara manual.

2. **Pengelolaan data**: Pengguna dapat membuat dan menghapus objek seperti tabel, tabel dimensi, dan fungsi user-defined.

3. **Kecepatan**: BigQuery menggunakan teknologi khusus untuk memproses kueri dengan cepat, termasuk teknik seperti distribusi data secara otomatis dan eksekusi kueri paralel di infrastruktur Google.

4. **Fleksibilitas**: Pengguna dapat mengakses dan menganalisis data menggunakan SQL standar, yang membuatnya mudah diakses oleh para analis data dan pengembang yang sudah terbiasa dengan SQL.

5. **Integrasi dan Import data**: BigQuery terintegrasi dengan berbagai layanan Google Cloud lainnya, seperti Google Cloud Storage, Google Data Studio, dan Google Cloud Dataflow, sehingga memudahkan untuk mengimpor data sehingga pengguna dapat mengimport data dari format-format seperti CSV, Parquet, Avro, dan JSON, memvisualisasikan hasil analisis, dan mengelola aliran data. Selain itu, BigQuery dapat digunakan dari aplikasi Google Apps Script, atau dari bahasa pemrograman lain yang dapat bekerja dengan REST API atau client libraries.

6. **Keamanan**: BigQuery menyediakan fitur keamanan yang kuat, termasuk kontrol akses granular, enkripsi data selama istirahat dan saat penyimpanan, dan audit log untuk melacak aktivitas pengguna.

<br>

**Google Cloud Storage** adalah layanan pengelolaan data yang dikelola oleh Google Cloud Platform (GCP). 
GCS memungkinkan pengguna untuk menyimpan berbagai jenis data, termasuk gambar, video, file teks, arsip, dan banyak lagi, dalam bentuk objek (atau disebut juga "blob"), dengan kemampuan untuk mengambil data secara terus menerus. Google Cloud Storage memungkinkan pengguna untuk menyimpan data dengan biaya per GiB bulanan yang berubah-ubah, dan menyediakan tarif untuk pengiriman data dan layanan jaringan spesifik. Layanan ini dapat digunakan untuk menyimpan data yang tidak terstruktur, seperti file, video, dan gambar, dengan kemampuan untuk mengambil data secara terus menerus. Google Cloud Storage memiliki fitur seperti Object Lifecycle Management (OLM) dan Autoclass, yang mengizinkan pengguna untuk mengoptimalkan biaya dengan pemindahan objek ke storage classes yang lebih murah berdasarkan waktu terakhir akses. Layanan ini juga mendukung dua tipe bucket: single-region bucket dan dual-region bucket, yang menyediakan Recovery Time Objective (RTO) nol dan Recovery Point Objective (RPO) yang berbeda. Google Cloud Storage dapat digunakan untuk menyimpan data training, model, dan checkpoints untuk proyek machine learning, serta dapat digunakan dengan Cloud Storage FUSE untuk memudahkan penggunaan aplikasi yang memerlukan sistem file semantik.