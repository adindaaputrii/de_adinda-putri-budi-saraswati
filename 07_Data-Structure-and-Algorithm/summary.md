## Resume Materi Data Structure and Algorithm

Struktur data (data structure) merupakan cara mengatur dan menyimpan data secara terstruktur pada sistem komputer atau database agar dapat diakses dan digunakan secara efisien. Struktur data menentukan hubungan antara data dan operasi yang dapat dilakukan pada data tersebut. Struktur data mempunyai tipe yang berbeda, seperti array, stack, queue, tree, dan graph, yang setiap satunya memiliki layout dan cara mengelola data yang berbeda. Struktur data digunakan untuk menyimpan, mengambil, dan menyusun data, memudahkan pencarian data, dan mengurangi penggunaan memori.

Python memiliki beberapa jenis struktur data yang dapat digunakan untuk menyimpan, mengelola, dan mengakses data. Berikut adalah beberapa jenis struktur data yang tersedia di Python:
1. **List**: jenis struktur data yang digunakan untuk menyimpan data dengan urutan tertentu. Setiap elemen dalam list memiliki indeks yang dimulai dari 0, dan elemen dapat diakses menggunakan indeks positif atau negatif. List dapat berisi data dari berbagai jenis, seperti angka, teks, dan objek lainnya.

2. **Tuple**: jenis struktur data yang mirip dengan list, tetapi ia **tidak dapat diubah** setelah dibuat. Tuple digunakan untuk menyimpan data yang tidak akan berubah dan tidak diperlukan perubahan. Tuple dapat berisi data dari berbagai jenis, seperti angka, teks, dan objek lainnya.

3. **Dictionary**: jenis struktur data yang digunakan untuk menyimpan data dalam pembagian-pembagian tertentu. Setiap pembagian dalam dictionary disebut **key**, dan setiap pembagian memiliki nilai yang disebut **value**. Dictionary dapat digunakan untuk menyimpan data yang dapat diakses menggunakan key.

4. **Set**: jenis struktur data yang digunakan untuk menyimpan data yang **tidak memiliki urutan**. Set hanya dapat memiliki data yang unik, dan setiap elemen hanya dapat terdapat satu kali. Set dapat digunakan untuk menyimpan data yang dapat diakses secara random.

5. **Stack**: jenis struktur data yang digunakan untuk menyimpan data dalam urutan yang berlawanan. Setiap elemen yang ditambahkan ke stack akan menjadi elemen terakhir, dan elemen terakhir akan terakhir yang diambil (*Last In First Out*). Stack dapat digunakan untuk menyimpan data yang akan diproses secara berurutan.

6. **Queue**: jenis struktur data yang digunakan untuk menyimpan data dalam urutan yang berurutan. Setiap elemen yang ditambahkan ke queue akan menjadi elemen pertama yang diambil (*First In First Out*). Queue dapat digunakan untuk menyimpan data yang akan diproses secara berurutan.

7. **Array**: jenis struktur data yang digunakan untuk menyimpan data dalam jumlah yang besar. Array dapat berisi data dari berbagai jenis, seperti angka, teks, dan objek lainnya. Array dapat digunakan untuk menyimpan data yang dapat diakses menggunakan indeks.


*Searching* adalah proses mencari informasi atau data yang diinginkan dari sebuah database, file, atau sistem informasi. Dalam pemrograman, searching adalah proses mencari elemen tertentu dalam sebuah list, array, atau database. Ada beberapa jenis searching yang dapat digunakan, seperti linear search, binary search, dan searching menggunakan indeks. Berikut ini penjelasan singkat mengenai linear search:<br>
- **Linear search** adalah algoritma pencarian yang digunakan untuk mencari sebuah elemen dalam sebuah list atau array. Algoritma ini mencari elemen dengan cara membandingkan setiap elemen dengan elemen yang dicari, mulai dari elemen pertama hingga elemen terakhir. Jika elemen yang dicari ditemukan, algoritma akan mengembalikan indeks elemen tersebut. Jika tidak, algoritma akan mengembalikan nilai -1.
<br><br>

*Sorting* adalah proses mengurutkan elemen dalam sebuah list atau array dalam urutan tertentu. Ini dapat dilakukan menggunakan berbagai algoritma pengurutan, seperti bubblesort, insertion sort, selection sort, merge sort, atau quicksort. Berikut ini penjelasan singkat terkait beberapa metode sorting:<br>

- **Selection sort** adalah algoritma pengurutan yang mengurutkan elemen dalam sebuah list atau array. Algoritma ini bekerja dengan cara mencari elemen terkecil atau terbesar dalam bagian unsorted (belum terurut) dari list dan mengganti elemen tersebut dengan elemen terlebih dahulu dalam bagian sorted (terurut). Proses ini dilakukan berulang kali hingga list terurut. Kompleksitas waktu untuk algoritma selection sort adalah O(n^2), dimana n adalah jumlah elemen dalam list. Algoritma ini tidak memerlukan ruang tambahan, sehingga ia adalah algoritma in-place. <br>

- **Counting sort** adalah algoritma pengurutan yang mengurutkan elemen dalam sebuah list atau array berdasarkan nilai-nilai yang berada dalam range tertentu. Algoritma ini bekerja dengan cara menghitung jumlah elemen yang memiliki nilai tertentu dan menggunakan hasil dari operasi tersebut untuk mengurutkan elemen dalam list. Algoritma counting sort dapat diterapkan pada data yang memiliki range kecil dan jumlah elemen yang besar. Kompleksitas waktu untuk algoritma counting sort adalah O(n+k), dimana n adalah jumlah elemen dalam list dan k adalah range yang digunakan. Algoritma ini tidak memerlukan penyimpanan tambahan, sehingga ia adalah algoritma in-place.<br>

- **Merge sort** adalah algoritma pengurutan yang menggunakan metode divide and conquer. Algoritma ini membagi array atau list yang akan diurutkan menjadi sub-array yang lebih kecil, mengurutkan setiap sub-array, dan kemudian menggabungkan sub-arrays tersebut menjadi array yang terurut. Merge sort adalah algoritma stabil, yang artinya ia mengurutkan elemen yang sama dalam urutan yang sama sebagaimana diinputkan.
Algoritma merge sort adalah algoritma in-place, yang artinya ia tidak membutuhkan ruang tambahan untuk mengurutkan elemen. Namun, ia memerlukan ruang tambahan sebagai buffer untuk menggabungkan sub-arrays terurut.
Algoritma merge sort memiliki kompleksitas waktu yang terjamin O(n log n), dimana n adalah jumlah elemen dalam array atau list. Algoritma ini sangat efektif untuk mengurutkan data yang besar.
Algoritma merge sort dapat disesuaikan untuk mengurutkan data dengan distribusi berbeda, seperti data yang tidak terurut, data yang hampir terurut, atau data yang tidak terurut. Algoritma ini juga dapat diparalelkan untuk menggunakan lebih dari satu prosesor atau thread.