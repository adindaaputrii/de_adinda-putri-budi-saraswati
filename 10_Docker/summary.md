## Resume Materi Docker

Docker adalah platform perangkat lunak yang digunakan untuk mengembangkan, menguji, dan menjalankan aplikasi di lingkungan yang diisolasi yang disebut sebagai "kontainer". Kontainer adalah unit standar perangkat lunak yang berisi semua yang diperlukan untuk menjalankan aplikasi, termasuk kode, runtime, library, variabel lingkungan, dan dependensi lainnya. Docker memungkinkan pengembang untuk mengemas aplikasi dan semua dependensinya ke dalam kontainer yang portabel dan dapat dijalankan di lingkungan apa pun yang mendukung Docker.

Berikut adalah beberapa konsep dasar terkait dengan Docker:
1. **Kontainer**: kontainer adalah lingkungan yang diisolasi yang berisi semua yang diperlukan untuk menjalankan sebuah aplikasi, termasuk kode, runtime, library, variabel lingkungan, dan dependensi lainnya. Kontainer memungkinkan aplikasi untuk dijalankan dengan konsisten di berbagai lingkungan, dari lingkungan pengembangan hingga produksi.

2. **Dockerfile**: dockerfile adalah file teks yang berisi instruksi-langkah demi langkah-untuk membangun sebuah image Docker. Image Docker adalah templat standar untuk membuat kontainer. Dockerfile mendefinisikan apa yang harus disertakan dalam image, seperti sistem operasi dasar, dependensi, dan aplikasi.

3. **Image**: image Docker adalah template standar yang digunakan untuk membuat kontainer. Image berisi semua yang diperlukan untuk menjalankan sebuah aplikasi, termasuk kode, runtime, library, variabel lingkungan, dan dependensi lainnya. Image bersifat non-perubahan dan dapat digunakan untuk membuat banyak kontainer yang identik.

4. **Docker Engine**: docker Engine adalah komponen inti dari platform Docker yang bertanggung jawab untuk mengelola kontainer, image, dan lingkungan Docker. Docker Engine menyediakan antarmuka berbasis baris perintah untuk mengelola dan berinteraksi dengan kontainer dan image Docker.

<br>

Docker juga memiliki alat untuk mendefinisikan dan menjalankan aplikasi Docker multi-container menggunakan **Docker Compose**. Docker Compose adalah alat yang menggunakan file YAML untuk mendefinisikan aplikasi Docker dan melakukan proses pembuatan dan pengaktifan semua layanan kontainer. Docker Compose mengizinkan pengguna untuk menjalankan perintah terhadap beberapa kontainer secara bersamaan, seperti membangun gambar, mengeksekusi kontainer yang sudah berhenti, dan lain-lain.

Docker juga menyediakan fitur Swarm, yang menyediakan fungsionalitas penggabungan kontainer Docker secara langsung. Swarm mode diterapkan pada Docker 1.12 dan lebih tinggi. Docker Swarm menggunakan alat CLI swarm untuk menjalankan kontainer Swarm, membuat token pemulaan, menampilkan node dalam kumpulan, dan lain-lain. Docker juga memiliki alat CLI node untuk menjalankan berbagai perintah untuk menyediakan node dalam kumpulan, seperti menampilkan node dalam kumpulan, memperbarui node, dan menghapus node dari kumpulan. Docker mengelola kumpulan Swarm menggunakan algoritma konsensus Raft.

Docker juga menyediakan fitur **Volume**, yang memungkinkan data berikutnya untuk berlangsung secara independen, sehingga data tetap tersedia setelah kontainer dihapus atau diperbarui.

**Docker network** merupakan sistem komunikasi yang mengatur bagaimana kontainer Docker dapat berinteraksi dengan satu sama lain, atau dengan sistem operasi atau aplikasi yang bukan Docker. Kontainer Docker memiliki networking enabled by default, dan mereka dapat membuat koneksi keluar. Kontainer tidak memiliki informasi tentang jenis network yang dipasang, atau apakah peer-nya adalah workload Docker atau tidak. Kontainer hanya melihat suatu interface networking dengan alamat IP, gateway, tabel routing, layanan DNS, dan lain-lain. Hal ini hanya berlaku jika container tidak menggunakan driver network none.