# Oximetry-Monitor_Telemedika

Oximetry dan BPM Monitoring berbasis IoT

## Deskripsi
Melakukan pembacaan oximetry dan BPM secara _realtime_ menggunakan alat pembaca dan data dikirimkan ke database untuk kemudian dibaca oleh client/user

**Alat pembaca/sensor** terdiri dari Wemos D1 mini sebagai mikrokontroler, MAX03102 sebagai sensor, modul cas baterai, dan baterai Li-Ion. **Database** menggunakan google Firebase, **GUI** yang digunakan berbasis python dengan library customtkinter (tkinter)

## GUI

Library yang dibutuhkan:
- customtkinter (https://github.com/TomSchimansky/CustomTkinter/wiki/AppearanceMode)
- firebase (https://github.com/ozgur/python-firebase)

## Alat

Skema rangakaian:
![image](https://user-images.githubusercontent.com/105662575/209170958-75564051-75c8-47ca-8226-235822ba2568.png)


## Beberapa jurnal yang membantu dalam pembuatan:

https://ejournal.unsrat.ac.id/v3/index.php/elekdankom/article/view/558/446

https://journal.ugm.ac.id/v3/jntt/article/download/4804/1720/)


## Beberapa website yang membantu dalam pembuatan:

https://randomnerdtutorials.com/esp32-firebase-realtime-database/

https://github.com/ozgur/python-firebase

https://github.com/TomSchimansky/CustomTkinter/wiki/AppearanceMode
