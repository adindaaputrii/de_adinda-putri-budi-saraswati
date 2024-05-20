## Rangkuman Materi Data Quality dan Data Governance

**Data Quality** adalah konsep yang menggambarkan keunggulan data dalam konteks kegunaan bisnis atau analisis. Kualitas data mencerminkan seberapa baik data tersebut memenuhi persyaratan yang ditetapkan, seperti akurasi, kebenaran, dan relevansi dalam mendukung tujuan bisnis atau analisis yang ingin dicapai.
Data berkualitas tinggi adalah landasan bagi pengambilan keputusan yang cerdas dan analisis yang efektif.

Data yang buruk, tidak akurat, atau tidak lengkap dapat menyebabkan hasil yang salah, kesimpulan yang keliru, dan keputusan bisnis yang merugikan. Oleh karena itu, penting untuk memastikan data Anda memiliki kualitas yang baik sebelum digunakan untuk analisis atau pengambilan keputusan.

Dimensi Kualitas Data adalah karakteristik atau atribut yang digunakan untuk mengukur kualitas suatu data. Setiap dimensi memiliki peran penting dalam menentukan seberapa baik atau buruk kualitas data tersebut. Berikut adalah penjelasan singkat mengenai masing-masing dimensi kualitas data:

- **Accuracy** (Akurasi): akurasi mengacu pada sejauh mana data Anda benar dan mencerminkan realitas. Ini berarti nilai data harus sesuai dengan entitas dunia nyata yang mereka wakili. Misalnya, alamat email harus valid dan nomor telepon harus berfungsi. Data yang akurat bebas dari kesalahan atau bias yang signifikan.

- **Completeness** (Kelengkapan): menunjukkan sejauh mana data sudah lengkap, yaitu apakah semua informasi yang seharusnya ada sudah tersedia. Data yang lengkap tidak memiliki nilai yang hilang atau tidak lengkap. Data yang tidak lengkap dapat membatasi kemampuan Anda untuk melakukan analisis yang akurat.

- **Reliability** (Keandalan): konsistensi mengacu pada apakah data yang dimiliki terformat dan didefinisikan secara konsisten di seluruh kumpulan data. Ini berarti data serupa harus memiliki format dan definisi yang sama, terlepas dari sumbernya. Inconsistency dapat menyebabkan kebingungan dan kesalahan dalam analisis.

- **Relevance** (Relevansi): relevansi mengacu pada apakah data sesuai dan relevan untuk tujuan yang diinginkan. Data yang tidak relevan tidak akan memberikan wawasan yang berharga untuk analisis. Penting untuk memastikan data yang digunakan terkait dengan pertanyaan yang dicoba jawab.

- **Timeliness** (Keterkinian): keterkinian mengacu pada seberapa terbaru data yang dimiliki. Data yang usang mungkin tidak mencerminkan keadaan saat ini dan mungkin tidak berguna untuk pengambilan keputusan. Semakin baru data Anda, semakin baik untuk sebagian besar analisis.

- **Uniqueness** (Keunikan): keunikan mengacu pada apakah setiap record data dalam kumpulan data Anda unik dan tidak diduplikasi. Data yang unik memastikan bahwa setiap entitas hanya direpresentasikan satu kali dalam dataset. Duplikasi data dapat menyebabkan hasil yang meningkat secara artifisial dan analisis yang tidak akurat.

<br><br>

Berikut ini beberapa cara untuk meningkatkan kualitas data:
1. **Data Cleaning**
- Mengidentifikasi dan memperbaiki kesalahan: Ini bisa berupa nilai yang hilang, outlier, format yang tidak konsisten, dan duplikasi data.
- Alat yang bisa digunakan: OpenRefine, Trifacta Wrangler, DataCleaner (alat web)
- Tips:
    - Definisikan aturan pembersihan data yang jelas.
    - Otomatiskan tugas pembersihan data yang berulang.
    - Verifikasi keakuratan data setelah pembersihan.

2. **Data Governance**
- Menetapkan kerangka kerja untuk pengelolaan data yang efektif.
- Memastikan data akurat, konsisten, dan aman.
- Komponen penting:
    - Kebijakan dan prosedur data.
    - Standar data.
    - Roles dan tanggung jawab terkait data.
- Tips:
    - Dapatkan dukungan manajemen untuk inisiatif tata kelola data.
    - Komunikasikan kebijakan dan prosedur data kepada semua pemangku kepentingan.
    - Tetapkan proses penegakan untuk memastikan kepatuhan.

3. **Data Profiling**
- Menganalisis data Anda untuk memahami karakteristiknya.
- Mengidentifikasi masalah potensial seperti inkonsistensi, duplikasi, dan format yang tidak valid.
- Alat yang bisa digunakan: Profiler bawaan pada alat analisa data (mis. Tableau Prep), Pandas Profiling (library Python)
- Tips:
    - Profil data secara teratur untuk mengidentifikasi masalah kualitas data yang baru muncul.
    - Gunakan hasil profiling data untuk memandu upaya pembersihan data. 

4. **Data Matching**
- Mencocokkan record data yang berbeda yang merujuk pada entitas yang sama.
- Digunakan untuk menghilangkan duplikasi dan meningkatkan konsistensi data.
- Algoritma umum:
    - Deterministic matching (berdasarkan atribut yang sama persis)
    - Probabilistic matching (berdasarkan kemiripan atribut)
- Tips:
    - Pilih algoritma pencocokan yang tepat berdasarkan karakteristik data yang dimiliki.
    - Verifikasi kecocokan data secara manual untuk memastikan akurasi.

5. **Data Quality Reporting**
- Melacak dan melaporkan metrik kualitas data.
- Membantu dalam mengukur kemajuan dan mengidentifikasi area untuk perbaikan.
- Metrik umum:
    - Persentase nilai yang hilang.
    - Tingkat akurasi.
    - Tingkat duplikasi.
- Tips:
    - Tetapkan target untuk metrik kualitas data.
    - Laporkan metrik kualitas data secara teratur kepada pemangku kepentingan.
    - Gunakan pelaporan untuk mendorong peningkatan kualitas data secara berkelanjutan.


<br><br>


**Data Governance** adalah kerangka kerja yang mengatur dan mengelola aspek-aspek pengumpulan, pengelolaan, penggunaan, dan keamanan data dalam sebuah organisasi. Tujuan utama dari data governance adalah untuk memastikan bahwa data yang digunakan dalam organisasi adalah akurat, lengkap, konsisten, dan dapat dipercaya, serta sesuai dengan kebijakan dan standar yang ditetapkan.

Tujuan utama data governance adalah untuk memastikan bahwa data:
- Akurat dan dapat diandalkan: Meminimalkan kesalahan dan inkonsistensi dalam data.
- Aman dan terlindungi: Mencegah akses yang tidak sah dan kebocoran data.
- Tersedia dan dapat diakses: Memastikan data tersedia bagi mereka yang membutuhkannya untuk melakukan pekerjaan mereka.
- Digunakan secara efektif: Mendorong penggunaan data yang etis dan bertanggung jawab.

Pilar-pilar Data Governance adalah bagian-bagian utama atau elemen-elemen yang membentuk kerangka kerja data governance. Berikut adalah penjelasan singkat mengenai masing-masing pilar data governance:

1. **Data Management (Manajemen Data)**
- Berfokus pada bagaimana data didefinisikan, disimpan, dipelihara, dan diakses.
- Ini mencakup kegiatan seperti:
    - Mengembangkan dan menerapkan standar data.
    - Mendesain dan mengimplementasikan infrastruktur data.
    - Menetapkan proses untuk pencadangan dan pemulihan data.

2. **Data Quality (Kualitas Data)**
- Berfokus pada memastikan data akurat, lengkap, konsisten, keandalan data, dan tepat waktu.
- Ini mencakup kegiatan seperti:
    - Menetapkan standar kualitas data.
    - Menerapkan proses pembersihan dan validasi data.
    - Memantau kualitas data secara berkelanjutan.

3. **Data Stewardship (Pengelolaan Data)**
- Menetapkan kepemilikan dan tanggung jawab atas data.
- Pemilik data (data steward) bertanggung jawab untuk memastikan data dikelola dan digunakan sesuai dengan kebijakan dan standar organisasi.
- Melakukan pengelolaan aktif terhadap data, termasuk pemantauan, perbaikan, dan pelaporan kualitas data.

4. **Data Protection & Compliance (Perlindungan Data & Kepatuhan)**
- Berfokus pada melindungi data dari akses yang tidak sah, penggunaan yang tidak tepat, dan kebocoran.
- Menjaga kepatuhan terhadap peraturan dan kebijakan privasi data yang berlaku, seperti GDPR atau CCPA.
- Ini mencakup kegiatan seperti:
    - Menerapkan kontrol keamanan data.
    - Mematuhi peraturan privasi data yang relevan.
    - Mengelola risiko keamanan data..
