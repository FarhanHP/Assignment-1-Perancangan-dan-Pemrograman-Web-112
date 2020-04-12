# Olshop

Olshop adalah aplikasi desktop yang diperuntukan agar pemilik toko bisa men-digitalisasi toko mereka. Terdapat beberapa aktor pada aplikasi ini yaitu, Owner selaku pemilik toko, Employee selaku karyawan toko, Customer sebagai pelanggan toko, dan Guest yang merupakan tamu yang belum membuat akun.

## Fitur Aplikasi:

### Owner : 
* mengangkat atau memecat Employee
* CRUD produk yang ada di toko 
* Edit data pribadi
* Melihat history aktifitas yang dilakukan Customer, Employee, dan Owner itu sendiri. History aktifitas tersebut meliputi history pengangkatan dan pemecatan karyawan, history penghapusan Product, history penginputan Product, history pengeditan produk, dan history transaksi yang dilakukan customer
* Melihat informasi detil semua user baik itu Employee maupun Customer

### Employee: 
* CRUD produk yang ada di toko 
* Edit data pribadi
* Melihat history aktifitas yang dilakukan diri sendiri, seperti history input, delete, dan edit Product

### Customer: 
* Membeli produk 
* Edit data pribadi
* Melihat history transaksi yang dilakukan diri sendiri

### Guest: 
* login 
* register

## Hal yang Diperlukan:

### Python 3:
* Karena aplikasi ini dibuat dengan bahasa Python3 maka komputer anda harus sudah menginstall python3

### MongoDB:
* MongoDB dapat didownload pada tautan berikut : https://www.mongodb.com/download-center/community?tck=docs_server

### Python Library:
* pymongo : 
  > pip install pymongo
* pillow : 
  > pip install pillow

## Cara Menjalankan App:
* Aktifkan MongoDB
* Export database pada folder dumb dengan cara:
  > mongorestore -d olshop (lokasi folder dump)/dump
* Jalankan file app/main.py
  
 ## Video Tentang Aplikasi ini:
 Coming Soon
