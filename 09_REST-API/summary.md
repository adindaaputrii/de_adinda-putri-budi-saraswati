## Resume Materi REST API

**Application Programming Interface** (API): merupakan sekumpulan aturan dan protokol yang memungkinkan berbagai perangkat lunak berinteraksi satu sama lain. Dalam konteks pengembangan perangkat lunak, API biasanya digunakan untuk memungkinkan aplikasi berkomunikasi dengan perangkat lunak atau layanan lainnya. 

**REST API**: merupakan gaya arsitektur API yang berbasis pada konsep-konsep REST (Representational State Transfer). REST API menggunakan protokol HTTP dan prinsip-prinsip dasar REST, yang mencakup penggunaan metode HTTP (GET, POST, PUT, DELETE) untuk mengakses dan memanipulasi sumber daya (resource) melalui URI (Uniform Resource Identifier). Representasi data dalam REST API biasanya dalam format JSON atau XML.

**JSON** (JavaScript Object Notation) adalah format data ringan yang digunakan untuk pertukaran data antar aplikasi. JSON mudah dibaca dan ditulis oleh manusia, serta mudah diproses dan dihasilkan oleh komputer. Format JSON terinspirasi dari sintaks objek JavaScript dan umumnya digunakan dalam pertukaran data di web. Data dalam JSON disusun dalam pasangan nama-nilai yang diatur dalam format pasangan key-value, dan dapat mewakili objek, array, string, angka, boolean, dan null. 

**Hypertext Transfer Protocol** (HTTP): mendefinisikan beberapa metode yang digunakan untuk mengatur interaksi antara klien (misalnya browser web) dan server. Berikut ini beberapa HTTP methods yang umum digunakan:
1. **GET**: metode ini digunakan untuk mendapatkan/mengambil data dari server. Metode ini hanya mengambil data dan tidak mempengaruhi sumber daya di server.
2. **POST**: metode ini digunakan untuk mengirimkan/membuat data baru ke server. Metode ini biasanya digunakan untuk mengirimkan data formulir atau mengirimkan data dalam format JSON.
3. **PUT**: metode ini digunakan untuk memperbarui/mengganti sumber daya secara keseluruhan pada lokasi yang ditentukan.
4. **PATCH**: metode ini mirip dengan *PUT*, tetapi metode ini digunakan untuk memperbarui/memodifikasi bagian-bagian tertentu dari sumber daya, **bukan seluruhnya**. Hal ini memungkinkan untuk memperbarui sumber daya dengan detail yang lebih kecil daripada *PUT*.
5. **DELETE**: metode ini digunakan untuk menghapus sumber daya yang ditentukan dari server.
6. **HEAD**: metode ini serupa dengan *GET*, tetapi pada metode ini, server hanya mengembalikan header respons **tanpa** response body. Hal ini berfungsi untuk mendapatkan informasi tentang sumber daya tanpa mengunduh seluruh kontennya.
7. **OPTIONS**: metode ini digunakan untuk mendapatkan informasi tentang metode yang didukung oleh server untuk sumber daya tertentu. Hal ini berguna untuk menentukan metode apa yang dapat digunakan untuk berinteraksi dengan sumber daya tersebut.

**HTTP Response Code** merupakan serangkaian kode numerik yang digunakan oleh server web untuk memberikan informasi tentang hasil dari request HTTP yang dikirim oleh klien. Berikut ini beberapa HTTP response code yang umum digunakan:
1. **1xx (Informational)**: kode respon dalam rentang 1xx memberikan informasi hanya sebagai tanggapan atas permintaan klien dan tidak memengaruhi pemrosesan permintaan itu sendiri.
- **100 (Continue)**: server telah menerima request header, dan klien harus melanjutkan dengan mengirimkan request body
- **101 (Switching Protocols)**: server memahami request, tetapi meminta klien beralih ke protokol yang berbeda.

<br>

2. **2xx (Success)**: kode respon dalam rentang 2xx menunjukkan bahwa request telah berhasil diterima, dipahami, dan diterima oleh server.
- **200 (OK)**: request berhasil.
- **201 (Created)**: request telah berhasil dan sumber daya baru telah dibuat.
- **204 (No Content)**: request berhasil diproses tetapi tidak ada konten yang akan dikembalikan.

<br>

3. **3xx (Redirection)**: kode respon dalam rentang 3xx menunjukkan bahwa klien harus melakukan tindakan tambahan untuk menyelesaikan request.
- **301 (Moved Permanently)**: sumber daya yang diminta telah dipindahkan secara permanen ke lokasi baru.
- **302 (Found)**: sumber daya yang diminta telah ditemukan di lokasi sementara yang berbeda.
- **304 (Not Modified)**: sumber daya tidak dimodifikasi sejak versi terakhir yang diakses.

<br>

4. **4xx (Client Error)**: kode respon dalam rentang 4xx menunjukkan bahwa ada kesalahan pada sisi klien yang menyebabkan request tidak dapat diproses oleh server.
- **400 (Bad Request)**: request tidak dapat diproses karena sintaks yang tidak valid.
- **401 (Unauthorized)**: klien tidak diotorisasi untuk mengakses sumber daya.
- **404 (Not Found)**: sumber daya yang diminta tidak ditemukan di server.

<br>

5. **5xx (Server Error)**: kode respon dalam rentang 5xx menunjukkan bahwa server mengalami kesalahan internal yang mencegahnya memenuhi request klien.
- **500 (Internal Server Error)**: terjadi kesalahan yang tidak terduga di server.
- **503 (Service Unavailable)**: server tidak tersedia untuk menangani request karena overload atau pemeliharaan.