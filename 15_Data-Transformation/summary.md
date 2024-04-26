## Rangkuman Materi Data Transformation

**Transformasi data** adalah proses mengubah data dari format asli ke format lain  dengan tujuan untuk memperbaiki karakteristik data dan  memudahkan analisis.  Proses ini dilakukan untuk  meningkatkan kualitas data sehingga dapat digunakan secara efektif dalam proses pengambilan keputusan,  pelatihan model machine learning, atau visualisasi data.


Berikut beberapa alasan dan tujuan dilakukannya transformasi data:
1. **Memperbaiki kualitas data**: Transformasi data dapat membantu mengatasi masalah-masalah seperti *missing value*, *outlier* (nilai ekstrim), inkonsistensi format data, dan ketidaksesuaian skala data.
2. **Mempersiapkan data untuk analisis**: Transformasi data dapat membuat data lebih mudah dianalisis dengan teknik statistik atau *machine learning* tertentu. Misalnya, transformasi data diperlukan untuk memastikan data numerik berada pada skala yang sama.
3. **Meningkatkan akurasi model**: Data yang bersih dan tertransformasi dengan baik akan menghasilkan model yang lebih akurat dan dapat diandalkan.
4. **Mempermudah visualisasi data**: Transformasi data dapat membantu menampilkan data secara visual dengan lebih jelas dan mudah dipahami. Misalnya, transformasi data dapat digunakan untuk menormalkan data sehingga distribusi data terlihat lebih jelas pada grafik.

<br>

Beberapa teknik transformasi data yang umum digunakan:
1. **Normalisasi**: merupakan proses mengubah nilai-nilai dalam dataset sehingga mereka memiliki skala yang seragam. Tujuan normalisasi adalah untuk memastikan bahwa semua fitur atau variabel memiliki rentang nilai yang sama atau setidaknya rentang nilai yang seragam. Teknik ini digunakan untuk menskalakan data numerik ke dalam rentang tertentu, biasanya antara 0 dan 1 atau -1 dan 1.

<br> 

**A. Alasan Melakukan Normalisasi**
- **Menghindari bias**: Tanpa normalisasi, fitur dengan skala yang lebih besar akan memiliki pengaruh lebih besar pada model, terlepas dari hubungan sebenarnya antar fitur. Normalisasi membantu menyeimbangkan pengaruh masing-masing fitur.
- **Meningkatkan performa algoritma**: Banyak algoritma machine learning bekerja lebih baik dengan data yang memiliki skala yang sama. Normalisasi dapat membantu algoritma tersebut konvergen lebih cepat dan mencapai akurasi yang lebih baik.
- **Mempermudah interpretasi**: Ketika fitur memiliki skala yang sama, koefisien model yang dihasilkan lebih mudah untuk diinterpretasikan.

<br>

**B. Metode Normalisasi**
- **Min-Max Normalization**: 
    - Proses ini dilakukan dengan mengurangkan nilai minimum dari setiap nilai dalam dataset dan membaginya dengan selisih antara nilai maksimum dan minimum.
    - Menskalakan data ke rentang antara 0 dan 1 (atau -1 dan 1).
    - Min-Max Normalization baik digunakan ketika Anda ingin membatasi data ke rentang tertentu (misalnya antara 0 dan 1).

<br>

    Rumus: normalized_value = (x - min_value) / (max_value - min_value) 
    
di mana:
- x adalah nilai data asli
- min_value adalah nilai minimum dari semua data
- max_value adalah nilai maksimum dari semua data.

<br>

- **Z-score normalization (Standardization)**:
    - Menskalakan data dengan mean (rata-rata) dan standar deviasi dari data tersebut.
    - Z-score normalization baik digunakan ketika distribusi data diasumsikan normal (berbentuk bell curve).
    - Nilai hasil normalisasi akan memiliki mean 0 dan standar deviasi 1.

<br>

    Rumus: normalized_value = (x - mean) / standard_deviation

<br><br>

2. **Standarisasi**: Teknik ini menskalakan data numerik untuk memiliki rata-rata (mean) 0 dan standar deviasi 1. Ini berarti setelah standarisasi, data akan terpusat di sekitar 0 dan memiliki standar deviasi 1.

Meskipun normalisasi dan standarisasi bertujuan untuk menskalakan data ke rentang yang sama, keduanya berbeda dalam rentang target:
- Normalisasi: Biasanya menskalakan data ke rentang antara 0 dan 1 (atau -1 dan 1), tergantung pada metode yang dipilih.
- Standarisasi: Secara khusus menskalakan data ke mean 0 dan standar deviasi 1.

<br>

    Rumus Standarisasi: nilai_terstandarisasi = (x - mean) / standar_deviation

di mana:
- nilai_terstandarisasi adalah nilai terstandarisasi
- x adalah nilai data asli
- mean adalah mean dari semua nilai data
- standar_deviasi adalah standar deviasi dari semua nilai data

<br><br>

3. **Encoding data kategorikal**: Teknik ini digunakan untuk mengubah data kategorikal menjadi data numerik yang dapat digunakan dalam model machine learning. Data kategorikal adalah data yang berisi kategori atau label, seperti warna (merah, hijau, biru), jenis kelamin (pria, wanita), atau tipe properti (apartemen, townhouse, rumah).

**A. Metode Encoding yang Umum Digunakan**
- **One-Hot Encoding**: Teknik ini membuat kolom baru untuk setiap kategori. Setiap kolom baru berisi 0 atau 1, di mana 1 menunjukkan keberadaan kategori tersebut dan 0 menunjukkan ketiadaan. Misalnya, untuk fitur "warna" dengan kategori "merah", "hijau", dan "biru", akan dibuat tiga kolom baru: "warna_merah", "warna_hijau", dan "warna_biru". Kolom yang sesuai dengan kategori yang ada di data akan diberi nilai 1, dan kolom lainnya akan diberi nilai 0.

    Metode ini lebih umum dan bekerja dengan baik untuk semua jenis data kategorikal, terlepas dari urutan atau peringkat. Namun, one-hot encoding dapat meningkatkan dimensionalitas data (jumlah fitur), yang dapat memengaruhi kinerja model pada dataset kecil.

<br>

- **Label Encoding**: Teknik ini menetapkan angka unik untuk setiap kategori. Misalnya, warna "merah" mungkin diberi angka 1, "hijau" angka 2, dan "biru" angka 3.

    Cocok untuk data kategorikal dengan urutan atau peringkat alami (misalnya, tingkat kepuasan pelanggan: tidak puas, puas, sangat puas). Namun, perlu diingat bahwa label encoding dapat memengaruhi model jika urutan numerik ditafsirkan sebagai hubungan kuantitatif (misalnya, "merah" dianggap "lebih besar" daripada "hijau"). 
    
<br>

- **Ordinal Encoding**: Teknik khusus untuk mengkonversi data kategorikal ke dalam representasi numerik. Berbeda dengan label encoding yang sekedar menetapkan angka unik untuk setiap kategori, ordinal encoding memperhatikan urutan atau peringkat inheren yang dimiliki kategori-kategori tersebut.

    Misalkan terdapat fitur "tingkat kepuasan pelanggan" dengan kategori "tidak puas", "puas", dan "sangat puas". Dalam ordinal encoding, kategori ini dapat dikonversi ke angka sebagai berikut:
    - Tidak puas = 1
   - Puas = 2
    - Sangat puas = 3

Encoding diperlukan karena kebanyakan algoritma pembelajaran mesin dan statistik hanya dapat menerima input berupa bilangan numerik. Dengan menggunakan encoding, kita dapat mengubah data kategorikal menjadi format yang dapat digunakan untuk melatih model atau melakukan analisis data.

<br><br>

4. **Agregasi data**: Teknik ini digunakan untuk meringkas data berdasarkan kelompok atau kategori tertentu. Hasilnya adalah kumpulan data yang lebih kecil yang menangkap tren dan pola keseluruhan dari data asli. Proses ini sering digunakan untuk mengurangi dimensionalitas data, sehingga lebih mudah dianalisis dan divisualisasikan. Misalnya, menghitung rata-rata harga kendaraan berdasarkan transmisinya.

**A. Teknik Agregasi Data Secara Umum**
- **Jumlah** (Sum): Menghitung total nilai semua titik data dalam suatu kelompok atau kategori.
- **Rata-Rata** (Average): Menghitung nilai rata-rata semua titik data dalam suatu kelompok atau kategori.
- **Hitung** (Count): Menentukan jumlah titik data dalam suatu kelompok atau kategori.
- **Minimum**: Mengidentifikasi nilai terkecil dalam suatu kelompok atau kategori.
- **Maksimum**: Mengidentifikasi nilai terbesar dalam suatu kelompok atau kategori.
- **Jangkauan** (Range): Menghitung perbedaan antara nilai maksimum dan minimum dalam suatu kelompok atau kategori.

<br><br>

5. **Feature engineering**: Teknik ini melibatkan pembuatan atau mengekstrak fitur-fitur baru dari data mentah atau fitur-fitur yang sudah ada. Tujuan utama dari feature engineering adalah untuk meningkatkan kualitas data dan meningkatkan kinerja model machine learning atau analisis data.

**A. Beberapa Teknik Feature Engineering**
- **Pemilihan Fitur**: Mengidentifikasi dan memilih fitur yang paling relevan dan informatif dari dataset asli. Ini dapat melibatkan penghapusan fitur yang redundan atau tidak relevan yang tidak berkontribusi pada kekuatan prediktif model.
- **Transformasi Fitur**: Memodifikasi atau mentransformasi fitur yang ada agar lebih sesuai untuk algoritma machine learning. Ini mungkin termasuk penskalaan fitur, pengkodean data kategorikal, atau pembuatan fitur baru melalui operasi matematis atau pengetahuan domain.
- **Pembuatan Fitur**: Menghasilkan fitur baru dari data yang ada atau pengetahuan domain. Ini dapat melibatkan penggabungan fitur, menghitung statistik, atau mengekstrak pola spesifik dari data.

*Contoh feature engineering:*

Pertimbangkan dataset yang berisi informasi tentang pelanggan dan perilaku pembelian mereka. Anda mungkin membuat fitur baru seperti:
- Customer Lifetime Value: Mewakili total pendapatan yang dihasilkan oleh pelanggan selama hubungan mereka dengan perusahaan.
- Frekuensi Pembelian Rata-rata: Menghitung rata-rata jumlah pembelian yang dilakukan pelanggan per bulan atau kuartal.
- Keafinan Produk: Mengukur preferensi pelanggan untuk kategori produk atau merek tertentu.

Dengan menggabungkan fitur-fitur baru ini, model machine learning dapat lebih baik memprediksi churn pelanggan, kemungkinan pembelian, atau rekomendasi produk.

<br><br>

### Tantangan dalam Data Transformasi
**1. Mengatasi Missing Values**
**Missing values**, atau nilai yang hilang, adalah salah satu masalah umum yang dihadapi dalam transformasi data. Nilai-nilai ini dapat hilang karena berbagai alasan, seperti kesalahan input data, pengumpulan data yang tidak lengkap, atau sifat data itu sendiri. Keberadaan missing values dapat berdampak negatif pada analisis dan pemodelan data, sehingga penting untuk mengatasinya dengan tepat.

**Berikut beberapa strategi umum untuk mengatasi missing values dalam transformasi data:**
1. **Penghapusan Baris/Kolom**:
- Penghapusan Baris: Hapus seluruh baris data yang mengandung missing values. Strategi ini paling sederhana, namun berpotensi kehilangan informasi penting jika hanya ada beberapa nilai yang hilang.
- Penghapusan Kolom: Hapus seluruh kolom data yang mengandung banyak missing values. Strategi ini dapat membantu mengurangi dimensionalitas data, namun berpotensi kehilangan informasi penting dari kolom tersebut.

<br>

2. **Imputasi Nilai**:
- **Mean Imputation**: Mengganti missing values dengan nilai rata-rata dari kolom yang bersangkutan. Strategi ini sederhana dan cepat, namun tidak mempertimbangkan variasi data dan dapat menghasilkan bias jika nilai yang hilang tidak terdistribusi secara normal.
- **Median Imputation**: Mengganti missing values dengan nilai median dari kolom yang bersangkutan. Strategi ini lebih kuat terhadap outlier dibandingkan mean imputation, namun tidak mempertimbangkan distribusi data secara keseluruhan.
- **Mode Imputation**: Mengganti missing values dengan nilai yang paling sering muncul dalam kolom yang bersangkutan. Strategi ini cocok untuk data kategorikal, namun tidak efektif jika tidak ada nilai yang dominan.
- **Hot-Deck Imputation**: Mengganti missing values dengan nilai yang diambil dari baris lain dalam dataset yang memiliki karakteristik serupa. Strategi ini lebih kompleks, namun dapat menghasilkan imputasi yang lebih akurat.
- **Nearest Neighbor Imputation**: Mengganti missing values dengan nilai rata-rata dari data terdekat dalam ruang fitur. Strategi ini lebih kompleks, namun dapat mempertimbangkan hubungan antar variabel.

3. **Teknik Khusus Domain**: Kadang-kadang, dalam domain tertentu, terdapat metode khusus untuk mengatasi missing values. Misalnya, dalam data deret waktu, nilai yang hilang dapat diisi dengan nilai sebelumnya atau setelahnya.

4. **Pencocokan**: Menggunakan teknik pencocokan data untuk menemukan nilai yang hilang yang cocok dengan pola data yang ada.

5. **Menggunakan Variabel Tambahan**: Menggunakan variabel tambahan untuk menandai apakah nilai asli suatu variabel itu hilang atau tidak.

6. **Interpolasi**: Menggunakan teknik interpolasi untuk mengisi nilai yang hilang berdasarkan nilai yang ada sebelumnya dan sesudahnya dalam deret waktu atau data spasial.

<br><br>

**2. Mengatasi Outlier**
**Outlier**, atau pencilan, adalah nilai yang jauh berbeda dari mayoritas data lainnya. Keberadaan outlier dapat memengaruhi analisis dan pemodelan data secara signifikan, sehingga penting untuk mengidentifikasi dan mengatasi outlier dengan tepat selama transformasi data.

Z-score method dan IQR (Interquartile Range) adalah dua metode umum yang digunakan untuk mengidentifikasi dan menangani outlier dalam transformasi data.

1. **Z-Score Method**:
- Z-score mengukur seberapa jauh sebuah titik data berada dari rata-rata dalam satuan standar deviasi.
- Nilai Z-score yang biasanya digunakan sebagai batas untuk outlier adalah ±3 yang berarti data yang nilainya lebih besar dari 3 (atau kurang dari -3) standar deviasi dari rata-rata dianggap sebagai outlier..
- Cocok untuk: Data numerik yang mengikuti distribusi normal.

**Kelebihan**:
- Sederhana dan mudah dihitung.
- Memberikan interpretasi yang mudah (nilai z-score yang tinggi menunjukkan outlier yang ekstrim).

**Kekurangan**:
- Kurang efektif untuk data yang tidak mengikuti distribusi normal.
- Sensitif terhadap outlier ekstrim, yang dapat memengaruhi ambang batas z-score.

<br>

2. **IQR** (Interquartile Range):
- IQR adalah perbedaan antara kuartil atas (Q3) dan kuartil bawah (Q1) dari sebuah dataset.
- Rumus: IQR = Q3 - Q1
- Batas bawah dan atas untuk outlier ditentukan dengan menggunakan kriteria **𝑄1−1.5×𝐼𝑄𝑅** dan **𝑄3+1.5×𝐼𝑄𝑅**. Data di luar kisaran ini dianggap sebagai outlier.
- Cocok untuk: Berbagai jenis data, termasuk data numerik dan kategorikal.

**Kelebihan**:
- Lebih robust terhadap outlier ekstrim dibandingkan z-score method.
- Tidak bergantung pada distribusi data.

**Kekurangan**:
- Interpretasi batas IQR kurang intuitif dibandingkan nilai z-score.
- Sensitif terhadap distribusi data yang miring.

<br><br>

3. **Memastikan Integritas Data dan Menghindari Kehilangan Data**
Menjaga integritas data dan menghindari kehilangan data adalah upaya untuk memastikan bahwa data tetap akurat, lengkap, dan relevan selama proses transformasi. Ini melibatkan langkah-langkah untuk mencegah, mengidentifikasi, dan menangani data yang hilang dengan tepat. 

**Tujuan**:
- Integritas data memastikan bahwa data tetap akurat, konsisten, dan tidak berubah selama penyimpanan atau transfer.
- Menghindari kehilangan data sangat penting untuk menjaga kelengkapan kumpulan data dan memastikan analisis yang andal.

**Metode yang Umum Digunakan**:
- **Pencadangan Reguler**: Membuat salinan kumpulan data secara berkala.
- **Pemeriksaan Validasi**: Menerapkan aturan untuk memastikan data yang dimasukkan ke dalam sistem mematuhi kriteria yang telah ditentukan.
- **Checksum**: Menggunakan algoritma untuk memverifikasi integritas data selama transfer.