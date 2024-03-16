## Resume Materi Relational Database

**Database** adalah sistem untuk menyimpan, mengorganisir, dan mengelola data elektronik. Data yang disimpan dapat berupa teks, angka, gambar, atau yang lainnya. Database dapat digunakan untuk berbagai tujuan, seperti pengelolaan data karyawan, pengelolaan data pelanggan, pengelolaan data transaksi, dan lain-lain. 

**Database Relationship** merupakan hubungan yang dibuat antar tabel-tabel yang berbeda di dalam sebuah database. Hubungan ini mencerminkan bagaimana data dalam satu tabel terkait atau terhubung dengan data dalam tabel lainnya. Hubungan basis data membantu mengorganisir dan mengelola data dengan cara yang logis, serta memfasilitasi penggunaan dan analisis data yang lebih efisien.
Berikut ini merupakan tiga jenis utama dari relasi database:
1. **One-to-One** (1:1): dalam relasi ini, sebuah record/baris tunggal pada satu tabel dikaitkan dengan satu record pada tabel lain. Contohnya berupa hubungan antara tabel pengguna dan tabel profil yang di mana setiap pengguna hanya dapat memiliki satu profil, dan satu profil hanya dimiliki oleh satu pengguna.

2. **One-to-Many** (1:N): dalam relasi ini, sebuah record tunggal pada satu tabel dikaitkan dengan banyak record pada tabel lain. Contohnya berupa hubungan antara tabel customer dan tabel order yang di mana setiap pelanggan dapat memiliki banyak pesanan.

3. **Many-to-Many** (N:M): dalam relasi ini, banyak record pada satu tabel dapat dikaitkan dengan banyak record pada tabel lain. Contohnya adalah pada tabel pengguna dan tabel kursus yang di mana seorang pengguna dapat mengikuti banyak kursus, dan sebuah kursus dapat memiliki banyak pengguna yang terdaftar. Untuk merepresentasikan relasi ini, seringkali digunakan tabel terpisah yang disebut tabel junction (penghubung). Tabel junction ini menyimpan foreign key untuk pengguna dan kursus, sehingga terjalin koneksi many-to-many.

**Entity Relationship Diagram** (ERD) merupakan representasi visual dari struktur data dalam suatu sistem informasi yang menggunakan notasi untuk menggambarkan entitas (tabel), atribut (kolom), dan hubungan antara entitas. Berikut ini komponen utama yang terdapat dalam ERD:
1. Entitas: merupakan objek yang direpresentasikan dalam basis data.Dalam ERD, entitas direpresentasikan oleh persegi panjang. Contoh entitas adalah "Customer", "Product", "Order", atau "Employee".

2. Atribut: merupakan sifat atau karakteristik dari suatu entitas yang membantu dalam menggambarkan dan mengidentifikasi entitas tersebut. Dalam ERD, atribut direpresentasikan oleh oval dan terhubung ke entitas yang sesuai dengan garis. Contoh atribut untuk entitas "Customer" adalah "Nama", "Alamat", atau "Nomor Telepon".

3. Hubungan (Relationship): merupakan keterkaitan antara entitas dalam basis data. Ini menunjukkan bagaimana entitas terkait satu sama lain. Hubungan dapat berupa one-to-one, one-to-many, atau many-to-many, dan direpresentasikan oleh garis yang menghubungkan antara dua entitas yang terlibat. Contohnya seperti satu "Customer" memiliki banyak "Order" (one-to-many), atau "Product" terdaftar dalam "Order" (many-to-many).

4. Primary Key: merupakan atribut atau kombinasi atribut yang dapat digunakan untuk secara unik mengidentifikasi setiap baris dalam tabel. Biasanya, kunci utama direpresentasikan oleh garis bercabang yang digarisbawahi pada atribut yang menjadi primary key.

5. Foreign Key: merupakan atribut yang menyimpan nilai dari kunci utama di tabel lain. Ini digunakan untuk membangun hubungan antara dua tabel. foreign key direpresentasikan dalam ERD dengan menggunakan tanda panah yang menghubungkan atribut kunci asing ke atribut kunci utama di tabel lain.

**Relational Database Management System** (RDBMS) adalah jenis sistem manajemen database yang didasarkan pada model data relasional. RDBMS mengorganisir data ke dalam tabel yang terdiri dari baris dan kolom, di mana setiap baris mewakili entitas tunggal dan setiap kolom mewakili atribut atau sifat dari entitas tersebut.

DDL dan DML adalah dua bahasa yang digunakan untuk mengatur struktur dan memanipulasi data di dalam database. Berikut adalah penjelasan untuk DDL dan DML:

1. DDL (Data Definition Language - Bahasa Definisi Data):
DDL digunakan untuk menentukan keseluruhan struktur database, termasuk membuat, mengubah, dan menghapus objek database seperti tabel, kolom, batasan (constraint), indeks, dan pengguna.
Pernyataan DDL adalah instruksi/perintah yang secara permanen mengubah skema database. Berikut ini beberapa perintah DDL:
- CREATE: Membuat objek baru dalam basis data. <br> 
Contoh query untuk membuat tabel baru: *create table nama_tabel*

- ALTER: Mengubah struktur tabel yang ada, seperti menambahkan kolom atau menghapus indeks. <br>
Contoh query untuk menambahkan kolom pada suatu tabel: *alter table nama_tabel add nama_kolom tipe_data*

- DROP TABLE: Menghapus tabel dari basis data. <br>
Contoh query untuk menghapus tabel: *drop table nama_tabel*

2. DML (Data Manipulation Language - Bahasa Manipulasi Data):
DML digunakan untuk memanipulasi data yang tersimpan di dalam tabel database. DML digunakan untuk memasukkan, memperbarui, menghapus, dan mengambil data dalam tabel.
Pernyataan DML adalah instruksi/perintah yang berinteraksi dengan struktur database yang ada untuk mengelola data. Berikut ini beberapa perintah DML:
- INSERT: Memasukkan record baru ke dalam tabel. <br>
Contoh query untuk memasukkan data ke dalam tabel: *insert into user (nama, email, password) values ('John Doe', 'john.doe@example.com', 'secret123')*

- UPDATE: Memodifikasi/memperbarui data yang ada di dalam tabel. <br>
Contoh query untuk update data: *update user set password = 'new_password' where email = 'john.doe@example.com'*

- DELETE: Menghapus record dari tabel. <br>
Contoh query untuk hapus data: *delete from user where user_id = 10*

- SELECT: Mengambil data dari tabel. <br>
Contoh query mengambil seluruh data dari suatu tabel: *select * from mahasiswa*

