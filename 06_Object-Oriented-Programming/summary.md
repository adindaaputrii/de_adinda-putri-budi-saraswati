## Resume Materi Object Oriented Programming

Object Oriented Programming (OOP) merupakan paradigma pemrograman di mana program dibangun menggunakan objek, yang merupakan instance dari kelas. Objek tersebut memiliki:
- Atribut: karakteristik atau properti yang dimiliki objek, misalnya nama, id, atau data lainnya
- Metode: fungsi atau perilaku yang dapat dilakukan oleh kelas tersebut, misalnya menyala, berjalan, atau yang lainnya 

Program dalam OOP dibangun dengan mendefinisikan kelas yang merupakan blueprint atau template untuk objek. Kelas menentukan struktur dan perilaku objek yang akan dibuat. Objek individual yang dibuat dari kelas disebut instance.

Berikut ini merupakan **konsep dasar dalam OOP**:
1. **Enkapsulasi**: data (atribut) dan logika (metode) yang terkait dengan objek dikelola secara internal, melindungi data dari akses langsung yang tidak diinginkan (hanya mengekspos fungsionalitas yang diperlukan)
2. **Polimorfisme**: kemampuan objek dari kelas yang berbeda yang dapat merespons fungsi dengan nama yang sama
3. **Pewarisan (Inheritance)**: kelas dapat mewarisi atribut dan metode dari kelas lain, memungkinkan penggunaan ulang kode dan pembuatan struktur hierarki kelas
4. **Abstraksi (Data Abstraction)**: objek menyembunyikan detail internal dan hanya mengekspos informasi dan perilaku yang relevan kepada pengguna lain

Dalam OOP, terdapat **tipe akses** yang mengatur tingkat aksesibilitas atributnya. Tiga tipe akses utama dalam OOP, yaitu:
1. **Public** (nama): atribut dapat diakses dari mana saja, baik dari dalam maupun luar kelas, umumnya digunakan untuk atribut yang perlu diakses dan dimodifikasi oleh objek lain 
2. **Private** (__nama): atribut hanya dapat diakses dari dalam kelas tempat mereka didefinisikan. Tipe ini memberikan enkapsulasi data, melindungi data dari akses dan modifikasi yang tidak diinginkan dari luar kelas dan digunakan untuk atribut yang hanya perlu diakses oleh metode di dalam kelas untuk menjaga integritas data
3. **Protected** (_nama): atribut hanya dapat diakses dari dalam kelas tempat mereka didefinisikan dan juga dari kelas turunan (interitance) dari kelas tersebut. Tipe ini memungkinkan penggunaan ulang dan perluasan perilaku namun tetap menjaga kontrol akses tertentu dan digunakan untuk atribut yang perlu dibagikan dan mungkin dimodifikasi oleh kelas turunan, namun tidak ingin diakses langsung dari luar hierarki kelas

Pemilihan tipe akses penting untuk:
- **Mencegah akses data yang tidak diinginkan**: melindungi data sensitif dan menjaga integritas internal objek
- **Mempromosikan modularitas**: membatasi ketergantungan kode, membuat program lebih mudah diubah dan dipelihara
- **Mendorong enkapsulasi**: menyembunyikan detail internal objek dan hanya mengekspos informasi yang relevan melalui metode publik