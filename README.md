# linked_list-kevin.A.A.A

Nama: Kevin Aditya Agusto Awang

Nim : 2209116101

prodi: Sistem Informasi B 2022

penjelasan program:
Program ini merupakan implementasi dari linked list yang menampilkan daftar HP Samsung dengan sistem paging.

Class Node merepresentasikan sebuah simpul pada linked list. Setiap simpul memiliki dua atribut yaitu data yang merupakan nilai dari simpul tersebut dan next yang merupakan referensi ke simpul berikutnya.

Class LinkedList merepresentasikan linked list yang memiliki atribut head yang merepresentasikan simpul pertama pada linked list. Metode add digunakan untuk menambahkan sebuah simpul pada linked list. Metode display digunakan untuk menampilkan isi linked list dengan membaginya menjadi beberapa halaman dengan ukuran tertentu. Metode count digunakan untuk menghitung jumlah simpul pada linked list.

Pada fungsi main, dibuat sebuah objek hp_list yang merupakan instance dari class LinkedList. Kemudian data dari daftar HP Samsung ditambahkan ke dalam linked list menggunakan metode add. Selanjutnya, dilakukan pengaturan ukuran halaman dan halaman saat ini. Total halaman dihitung dengan membagi jumlah data pada linked list dengan ukuran halaman dan dibulatkan ke atas menggunakan fungsi //.

Program akan terus menampilkan isi linked list pada halaman saat ini dan menampilkan menu untuk melihat halaman selanjutnya, halaman sebelumnya, atau keluar dari program. Pilihan menu tersebut akan diinputkan oleh pengguna dan akan dievaluasi menggunakan kondisional if-elif-else untuk melakukan perpindahan halaman atau keluar dari program.

Penjelasan fungsi-fungsi yang ada di dalam program:
Node: Class ini merepresentasikan simpul atau node dalam linked list. Setiap simpul memiliki sebuah atribut data untuk menyimpan data dan atribut next yang merujuk ke simpul berikutnya dalam linked list.

LinkedList: Class ini merepresentasikan linked list secara keseluruhan. Setiap linked list memiliki sebuah atribut head yang merepresentasikan simpul pertama dalam linked list.

add: Fungsi ini menerima sebuah data dan menambahkan simpul baru ke akhir linked list.

display: Fungsi ini digunakan untuk menampilkan data pada linked list dengan membaginya ke dalam beberapa halaman. Fungsi ini menerima dua parameter, yaitu nomor halaman dan ukuran halaman. Fungsi ini kemudian menghitung indeks data pada halaman tersebut dan menampilkan data dari linked list pada indeks tersebut.

count: Fungsi ini menghitung jumlah simpul dalam linked list dan mengembalikan hasilnya.

main: Fungsi ini merupakan fungsi utama program yang menjalankan semua operasi pada linked list. Pertama, fungsi ini membuat sebuah linked list dan menambahkan beberapa data ke dalamnya. Kemudian, fungsi ini menampilkan halaman pertama dari linked list dengan memanggil fungsi display. Setelah itu, fungsi ini menampilkan menu untuk navigasi halaman dan mengambil pilihan pengguna untuk berpindah ke halaman selanjutnya, halaman sebelumnya, atau keluar dari program. Fungsi ini terus menampilkan halaman dan menu hingga pengguna memilih untuk keluar dari program.

Fungsionalitas utama dari program ini:
Fungsionalitas program adalah menampilkan daftar smartphone tersebut secara terbagi ke dalam beberapa halaman, dengan jumlah smartphone per halaman dapat diatur. Pengguna dapat menavigasi halaman dengan memilih menu "Halaman selanjutnya" atau "Halaman sebelumnya". Program akan terus berjalan hingga pengguna memilih opsi "Keluar".

elemen penting yang digunakan dalam program:
Linked list: Program ini menggunakan struktur data linked list untuk menyimpan dan mengatur data dari daftar HP Samsung yang akan ditampilkan.

Class: Program ini menggunakan konsep class untuk membuat sebuah objek yang merepresentasikan setiap node dalam linked list. Class Node merepresentasikan setiap node, sedangkan class LinkedList merepresentasikan keseluruhan linked list.

Method: Program ini menggunakan method yang didefinisikan dalam class LinkedList, seperti add(), display(), dan count(), untuk menambahkan data ke dalam linked list, menampilkan data dari linked list, dan menghitung jumlah data dalam linked list.

Perulangan while: Program ini menggunakan perulangan while untuk menampilkan data dari linked list secara halaman per halaman. Perulangan while ini akan terus berjalan sampai pengguna memilih opsi "Keluar" pada menu.

Variabel: Program ini menggunakan beberapa variabel seperti page_size untuk menentukan jumlah data yang akan ditampilkan dalam setiap halaman, current_page untuk menyimpan halaman yang sedang ditampilkan, dan total_pages untuk menyimpan total halaman yang tersedia. Variabel-variabel ini sangat penting dalam menjalankan program dan menampilkan data dengan benar.

output dari program:
<img width="216" alt="kevin otp" src="https://user-images.githubusercontent.com/126884174/225960403-747847d8-09d2-4b11-aa6b-b060772570d9.png">
<img width="253" alt="otp2" src="https://user-images.githubusercontent.com/126884174/225960502-65844248-9a90-4c39-ad6f-9033425bf0ad.png">
<img width="218" alt="otp3" src="https://user-images.githubusercontent.com/126884174/225960546-41d53d94-cc35-4936-b0a3-2663ccde9c8f.png">
<img width="155" alt="otp4" src="https://user-images.githubusercontent.com/126884174/225960618-1dacacfb-b5cb-4d41-bbf0-97c2176888e8.png">
