## Prioritas 1
### Input:
aku adalah seorang data engineer yang berfokus pada sql queries. buatkan aku query ddl dan dml untuk membangun database perpustakaan

### Output:
Tentu! Untuk membangun database perpustakaan, kita akan membuat beberapa tabel yang mencakup informasi tentang buku, pengarang, kategori, dan peminjaman. Berikut adalah contoh query DDL (Data Definition Language) untuk membuat skema database perpustakaan, menggunakan SQL (menggunakan sintaks yang umum digunakan dalam MySQL, PostgreSQL, atau SQL Server):

##### DDL (Data Definition Language)
- Tabel books untuk menyimpan informasi buku:
```sql
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    category_id INT NOT NULL,
    publish_date DATE,
    ISBN VARCHAR(20),
    -- tambahkan kolom lain sesuai kebutuhan
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
```

<br>

- Tabel authors untuk menyimpan informasi pengarang:
```sql
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL,
    country VARCHAR(100)
    -- tambahkan kolom lain sesuai kebutuhan
);
```

<br>

- Tabel categories untuk menyimpan informasi kategori buku:
```sql
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
    -- tambahkan kolom lain sesuai kebutuhan
);
```

<br>

- Tabel members untuk menyimpan informasi anggota perpustakaan (opsional, tergantung pada kebutuhan):
```sql
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    member_name VARCHAR(100) NOT NULL,
    join_date DATE,
    -- tambahkan kolom lain sesuai kebutuhan
);
```

<br>

- Tabel loans untuk menyimpan informasi peminjaman buku:
```sql
CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE,
    -- tambahkan kolom lain sesuai kebutuhan
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
```
<br>

##### DML (Data Manipulation Language)
Setelah tabel-tabel telah dibuat, kita dapat mengisi tabel-tabel tersebut dengan data menggunakan perintah DML, seperti INSERT INTO.

- Contoh pengisian data ke tabel authors:
```sql
INSERT INTO authors (author_name, country)
VALUES ('J.K. Rowling', 'UK'),
       ('Haruki Murakami', 'Japan'),
       ('Agatha Christie', 'UK'),
       -- tambahkan pengarang lainnya
       ;
```

<br>

- Contoh pengisian data ke tabel categories:
```sql
INSERT INTO categories (category_name)
VALUES ('Fiction'),
       ('Mystery'),
       ('Science Fiction'),
       -- tambahkan kategori lainnya
       ;
```

<br>

- Contoh pengisian data ke tabel books:
```sql
INSERT INTO books (title, author_id, category_id, publish_date, ISBN)
VALUES ('Harry Potter and the Philosopher''s Stone', 1, 1, '1997-06-26', '0747532699'),
       ('Norwegian Wood', 2, 1, '1987-08-04', '4061863026'),
       ('Murder on the Orient Express', 3, 2, '1934-01-01', '0007282633'),
       -- tambahkan buku lainnya
       ;
```
Ini adalah beberapa contoh query DDL dan DML yang dapat digunakan untuk membangun dan mengelola database perpustakaan. Pastikan untuk menyesuaikan dengan kebutuhan spesifik dan menambahkan kolom atau tabel lain sesuai kebutuhan aplikasi perpustakaan yang lebih kompleks.


<br><br>

### Penjelasan Hasil
AI melalui beberapa proses untuk dapat memproses input yang dimasukkan dan menghasilkan output yang sesuai, berikut ini proses yang dilakukan AI:
- Proses Tokenisasi: pada proses ini, model memecah input teks menjadi unit-unit yang lebih kecil, yang disebut dengan token (dapat berupa simbol lain atau tanda baca)
- Kemudian model melakukan pemahaman konteks dari input yang diberikan 
- Dengan pemahaman konteks yang memadai, model akan menghasilkan teks secara prediktif dan model akan melakukan penyempurnaan pada output agar output yang dihasilkan relevan dengan input yang diberikan

<br>

Pemanfaatan AI dalam Data Engineering dapat membantu dalam optimasi tugas dan meningkatkan efisiensi, berikut ini beberapa potensi aplikasi hasil dalam data engineering:
- Automatisasi pembuatan skema database: AI dapat membantu menyusun kueri DDL untuk mendefinisikan struktur database, tabel, dan hubungan antar tabel berdasarkan deskripsi yang disediakan. Hal ini meminimalkan kesalahan manusia dan mempercepat proses desain database.
- Pengisian data awal: AI dapat membantu menghasilkan kueri DML untuk mengisi tabel dengan data awal. Hal ini berguna saat membuat database dummy untuk tujuan pengujian atau memigrasi data dari sistem lama ke sistem baru.
- Optimasi query: AI dapat membantu dalam mengoptimalkan kueri SQL. Contohnya, AI dapat merekomendasikan indeks yang sesuai atau penulisan ulang kueri untuk efisiensi yang lebih baik.
