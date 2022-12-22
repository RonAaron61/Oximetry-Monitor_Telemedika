# Oximetry-Monitor_Telemedika

Oximetry dan BPM Monitoring berbasis IoT

_*Note: project ini untuk saat ini belum dalam keadaan sepenuhnya selesai dan siap pakai, karena masih terdapat banyak kekurangan dalam hal GUI dan progam alat_

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

rangakaian kemudian dipasangkan pada _case_ 3D print (saat ini belum dibuat) namun akan menyerupai seperti oximeter pada umunya dengan penempatan baterai dan modul pada sisi atas, dan _microcontroller_ dan sensor pada sisi bagian bawah
![oxxxxx](https://user-images.githubusercontent.com/105662575/209172616-8d1e4adc-9878-4e8e-a86f-10e55a85c4d4.png | width=100)


## Beberapa jurnal yang membantu dalam pembuatan:

https://ejournal.unsrat.ac.id/v3/index.php/elekdankom/article/view/558/446

https://journal.ugm.ac.id/v3/jntt/article/download/4804/1720/

https://repository.uinjkt.ac.id/dspace/bitstream/123456789/48663/1/CANDRA%20RIZKI%20NUGROHO-FST.pdf

http://jfu.fmipa.unand.ac.id/index.php/jfu/article/view/726


## Beberapa website yang membantu dalam pembuatan:

https://randomnerdtutorials.com/esp32-firebase-realtime-database/

https://github.com/ozgur/python-firebase

https://github.com/TomSchimansky/CustomTkinter/wiki/AppearanceMode
