## Resume Materi Data Warehouse and Data Lake Part 1

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



