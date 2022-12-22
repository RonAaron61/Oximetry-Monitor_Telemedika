# Oximetry-Monitor_Telemedika

Oximetry dan BPM Monitoring berbasis IoT

_Note: project ini untuk saat ini belum dalam keadaan sepenuhnya selesai dan siap pakai, karena masih terdapat banyak kekurangan dalam hal GUI dan progam alat_

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
*Jika ingin menggunakan sensor MAX30100 rangakain tidak jauh berbeda, hanya perlu memerhatikan sambungan pin saja
![image](https://user-images.githubusercontent.com/105662575/209171813-1a55ab80-e4c6-45f5-b320-b20f54b2ebac.png)


## Beberapa jurnal yang membantu dalam pembuatan:

https://ejournal.unsrat.ac.id/v3/index.php/elekdankom/article/view/558/446

https://journal.ugm.ac.id/v3/jntt/article/download/4804/1720/


## Beberapa website yang membantu dalam pembuatan:

https://randomnerdtutorials.com/esp32-firebase-realtime-database/

https://github.com/ozgur/python-firebase

https://github.com/TomSchimansky/CustomTkinter/wiki/AppearanceMode
