Identifikasi endpoint dan fungsinya pada dokumentasi API https://app.swaggerhub.com/apis-docs/sepulsa/RentABook-API/1.0.0

1. *Authentication* (GET /token)
- Fungsi: untuk meminta token akses. <br><br>

2. *Client & User Resource*
<br>

**GET /client** & **GET /user**
- Fungsi: mendapatkan daftar semua client/user yang terdaftar di sistem.

**GET /client/{id}** & **GET /user/{id}**
- Fungsi: mendapatkan informasi tentang client/user tertentu berdasarkan ID.

**POST /client** & **POST /user**
- Fungsi: menambahkan client/user baru ke dalam sistem.

**PUT /client/{id}** & **PUT /user/{id}**
- Fungsi: memperbarui informasi client/user tertentu berdasarkan ID.

**DELETE /client/{id}** & **DELETE /client/{id}**
- Fungsi: menghapus client/user tertentu dari sistem berdasarkan ID.

<br><br>

3. *Book Resource*
<br>

**GET /book**
- Fungsi: mendapatkan daftar semua buku yang terdaftar di sistem.

**GET /book/{id}**
- Fungsi: mendapatkan informasi tentang buku tertentu berdasarkan ID.

**POST /book**
- Fungsi: menambahkan buku baru ke dalam sistem.

**PUT /book/{id}**
- Fungsi: memperbarui informasi buku tertentu berdasarkan ID.

**DELETE /book/{id}**
- Fungsi: menghapus buku tertentu dari sistem berdasarkan ID.

<br><br>

4. *Rent Transaction Resource*
<br>

**GET /rent**
- Fungsi: mendapatkan semua daftar transaksi sewa yang terdaftar di sistem.

**GET /rent/{id}**
- Fungsi: mendapatkan informasi tentang transaksi sewa tertentu berdasarkan ID.

**POST /rent**
- Fungsi: menambahkan transaksi sewa baru ke dalam sistem.