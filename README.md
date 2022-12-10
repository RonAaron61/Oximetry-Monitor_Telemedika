# Oximetry-Monitor_Telemedika

For English [documentation](README-en.md)

Oximetry dan BPM Monitoring berbasis IoT

## Deskripsi
Melakukan pembacaan oximetry dan BPM secara _realtime_ menggunakan alat pembaca dan data dikirimkan ke database untuk kemudian dibaca oleh client/user

**Alat pembaca/sensor** terdiri dari Wemos D1 R1 mini sebagai mikrokontroler, MAX03100 sebagai sensor, modul cas baterai, dan baterai Li-Ion. Alat kemudian menggunakan case dengan di 3D print bahan .....

**Database** menggunakan google Firebase

**GUI** yang digunakan berbasis python dengan library customtkinter (tkinter)

## GUI

Library yang dibutuhkan:

- customtkinter
- firebase (https://github.com/ozgur/python-firebase)

## Alat

## Beberapa jurnal/ website yang membantu dalam pembuatan:

https://randomnerdtutorials.com/esp32-firebase-realtime-database/

https://github.com/ozgur/python-firebase
