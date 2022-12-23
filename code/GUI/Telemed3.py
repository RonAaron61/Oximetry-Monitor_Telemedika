import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from firebase import firebase
import webbrowser
import time as tm

app_db = firebase.FirebaseApplication('Masukan Link Firebase anda', None)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Inisiasi beberapa variable
        self.ke = 0
        self.wifidata = ["none","none"]
        self.MainData = []
        self.tabelData = []
        self.tabelupdate = {1: False, 2: False, 3: False} #Buat var tabel berapa aja yang keisi dan mau di iupdate
        self.tabelupdatedata = {1: False, 2: False, 3: False}

        #Log - App opened
        self.isilog("App Opened")

        # configure window
        self.iconbitmap('logo.ico')
        self.title("Monitoring V0.1")
        self.width = self.winfo_screenwidth() 
        self.height = self.winfo_screenheight() 
        #self.geometry("%dx%d"%(self.width, self.height))
        self.geometry(f"{1100}x{580}")

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, height=self.winfo_screenheight(), corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Oximetry and BPM\nMonitoring", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.delete_side = customtkinter.CTkButton(self.sidebar_frame, text="Delete")
        self.delete_side.grid(row=1, column=0, padx=20, pady=10)

        self.new_side = customtkinter.CTkButton(self.sidebar_frame, text="New", command=self.newKamar)
        self.new_side.grid(row=2, column=0, padx=20, pady=10)

        self.send_side = customtkinter.CTkButton(self.sidebar_frame, text="Send")
        self.send_side.grid(row=3, column=0, padx=20, pady=10)

        self.setting = customtkinter.CTkButton(self.sidebar_frame, text="Setting", command=self.pengaturan)
        self.setting.grid(row=5, column=0, padx=20, pady=10)

        self.log = customtkinter.CTkTabview(self.sidebar_frame, width = 100, height=320)
        self.log.grid(row=4, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.log.add("Warning")
        self.log.add("Log")

        #Main Frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, rowspan=4 ,padx=(10, 10), pady=(10, 10),sticky="nsew")
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.kamar()
        self.Tab_Data()
        self.updatedata()

        #Clossing Window Attemp event popup
        self.protocol("WM_DELETE_WINDOW", self.onClosing)


    def Tab_Data(self):
        self.kamar_label1 = customtkinter.CTkLabel(self.tabC[0], text="-", anchor="center")
        self.kamar_label1.grid(row=0, column=2, columnspan=2 ,padx=20, pady=(10, 0))
        self.nama_label1 = customtkinter.CTkLabel(self.tabC[0], text="-", anchor="center")
        self.nama_label1.grid(row=1, column=2, columnspan=2 ,padx=20, pady=(10, 0))
        self.oxi2_label1 = customtkinter.CTkLabel(self.tabC[0], text="-", font=("Arial",35), anchor="center")
        self.oxi2_label1.grid(row=3, column=0, columnspan=2 ,padx=20, pady=(10, 0))
        self.bpm2_label1 = customtkinter.CTkLabel(self.tabC[0], text=f"-", font=("Arial",35), anchor="center")
        self.bpm2_label1.grid(row=3, column=2, columnspan=2, padx=20, pady=(10, 0))
        self.status2_label1 = customtkinter.CTkLabel(self.tabC[0], text=f"-", font=("Arial",35), anchor="center")
        self.status2_label1.grid(row=3, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.kamar_label2 = customtkinter.CTkLabel(self.tabC[1], text="-", anchor="center")
        self.kamar_label2.grid(row=0, column=2, columnspan=2 ,padx=20, pady=(10, 0))
        self.nama_label2 = customtkinter.CTkLabel(self.tabC[1], text="-", anchor="center")
        self.nama_label2.grid(row=1, column=2, columnspan=2 ,padx=20, pady=(10, 0))  
        self.oxi2_label2 = customtkinter.CTkLabel(self.tabC[1], text="-", font=("Arial",35), anchor="center")
        self.oxi2_label2.grid(row=3, column=0, columnspan=2 ,padx=20, pady=(10, 0))
        self.bpm2_label2 = customtkinter.CTkLabel(self.tabC[1], text=f"-", font=("Arial",35), anchor="center")
        self.bpm2_label2.grid(row=3, column=2, columnspan=2, padx=20, pady=(10, 0))
        self.status2_label2 = customtkinter.CTkLabel(self.tabC[1], text=f"-", font=("Arial",35), anchor="center")
        self.status2_label2.grid(row=3, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.kamar_label3 = customtkinter.CTkLabel(self.tabC[2], text="-", anchor="center")
        self.kamar_label3.grid(row=0, column=2, columnspan=2 ,padx=20, pady=(10, 0))
        self.nama_label3 = customtkinter.CTkLabel(self.tabC[2], text="-", anchor="center")
        self.nama_label3.grid(row=1, column=2, columnspan=2 ,padx=20, pady=(10, 0))
        self.oxi2_label3 = customtkinter.CTkLabel(self.tabC[2], text="-", font=("Arial",35), anchor="center")
        self.oxi2_label3.grid(row=3, column=0, columnspan=2 ,padx=20, pady=(10, 0))
        self.bpm2_label3 = customtkinter.CTkLabel(self.tabC[2], text=f"-", font=("Arial",35), anchor="center")
        self.bpm2_label3.grid(row=3, column=2, columnspan=2, padx=20, pady=(10, 0))
        self.status2_label3 = customtkinter.CTkLabel(self.tabC[2], text=f"-", font=("Arial",35), anchor="center")
        self.status2_label3.grid(row=3, column=4, columnspan=2, padx=20, pady=(10, 0))

        #==== Belum lengkap kodenya, kode 1-3 yang sudah lengkap ====
        self.oxi2_label4 = customtkinter.CTkLabel(self.tabC[3], text="-", font=("Arial",35), anchor="center")
        self.oxi2_label4.grid(row=3, column=0, columnspan=2 ,padx=20, pady=(10, 0))
        self.bpm2_label4 = customtkinter.CTkLabel(self.tabC[3], text=f"-", font=("Arial",35), anchor="center")
        self.bpm2_label4.grid(row=3, column=2, columnspan=2, padx=20, pady=(10, 0))
        self.status2_label4 = customtkinter.CTkLabel(self.tabC[3], text=f"-", font=("Arial",35), anchor="center")
        self.status2_label4.grid(row=3, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.oxi2_label5 = customtkinter.CTkLabel(self.tabC[4], text="-", font=("Arial",35), anchor="center")
        self.oxi2_label5.grid(row=3, column=0, columnspan=2 ,padx=20, pady=(10, 0))
        self.bpm2_label5 = customtkinter.CTkLabel(self.tabC[4], text=f"-", font=("Arial",35), anchor="center")
        self.bpm2_label5.grid(row=3, column=2, columnspan=2, padx=20, pady=(10, 0))
        self.status2_label5 = customtkinter.CTkLabel(self.tabC[4], text=f"-", font=("Arial",35), anchor="center")
        self.status2_label5.grid(row=3, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.oxi2_label6 = customtkinter.CTkLabel(self.tabC[5], text="-", font=("Arial",35), anchor="center")
        self.oxi2_label6.grid(row=3, column=0, columnspan=2 ,padx=20, pady=(10, 0))
        self.bpm2_label6 = customtkinter.CTkLabel(self.tabC[5], text=f"-", font=("Arial",35), anchor="center")
        self.bpm2_label6.grid(row=3, column=2, columnspan=2, padx=20, pady=(10, 0))
        self.status2_label6 = customtkinter.CTkLabel(self.tabC[5], text=f"-", font=("Arial",35), anchor="center")
        self.status2_label6.grid(row=3, column=4, columnspan=2, padx=20, pady=(10, 0))

    def updatedata(self):
        if self.tabelupdate[1] == True:
            Id = self.tabelupdatedata[1]
            self.kamar_label1.configure(text = f"{Id[1]}")
            self.nama_label1.configure(text = f"{Id[2]}")
            oxibpm = self.get_data(Id[0])
            self.bpm2_label1.configure(text = f"{oxibpm['BPM']}")
            self.oxi2_label1.configure(text = f"{oxibpm['SpO2']}")
            self.status2_label1.configure(text = f"{oxibpm['Status']}")

        if self.tabelupdate[2] == True:
            Id = self.tabelupdatedata[2]
            oxibpm = self.get_data(Id[0])
            self.bpm2_label2.configure(text = f"{oxibpm['BPM']}")
            self.oxi2_label2.configure(text = f"{oxibpm['SpO2']}")
            self.status2_label2.configure(text = f"{oxibpm['Status']}")

        if self.tabelupdate[3] == True:
            Id = self.tabelupdatedata[3]
            oxibpm = self.get_data(Id[0])
            self.bpm2_label3.configure(text = f"{oxibpm['BPM']}")
            self.oxi2_label3.configure(text = f"{oxibpm['SpO2']}")
            self.status2_label3.configure(text = f"{oxibpm['Status']}")

        self.after(2000, self.updatedata)

    def newKamar(self):
        kamarB = customtkinter.CTkToplevel(self)
        kamarB.title("Input Kamar Baru")
        kamarB.geometry(f"{580}x{220}")
        kamarB.grid_columnconfigure(3, weight=1)

        #Agar tidak bisa di maximize
        kamarB.resizable(0,0)

        kamar_label= customtkinter.CTkLabel(kamarB, text= "No Kamar:", anchor="w")
        kamar_label.grid(row=0, column=0, padx=20, pady=(10, 0))       
        self.kamar = customtkinter.CTkEntry(kamarB, placeholder_text="No Kamar")
        self.kamar.grid(row=0, column=1, columnspan=3, padx=(0, 20), pady=(10, 0), sticky="nsew")

        nama_label= customtkinter.CTkLabel(kamarB, text= "Nama:", anchor="w")
        nama_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.nama = customtkinter.CTkEntry(kamarB, placeholder_text="Nama Pasien")
        self.nama.grid(row=1, column=1, columnspan=3, padx=(0, 20), pady=(10, 0), sticky="nsew")

        id_label= customtkinter.CTkLabel(kamarB, text= "Kode:", anchor="w")
        id_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.id = customtkinter.CTkEntry(kamarB,placeholder_text="Id dari alat yang digunakan")
        self.id.grid(row=2, column=1, columnspan=3, padx=(0, 20), pady=(10, 0), sticky="nsew")

        tab_label= customtkinter.CTkLabel(kamarB, text= "Tab:", anchor="w")
        tab_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        """self.tab = customtkinter.CTkEntry(kamarB,placeholder_text="Tab")
        self.tab.grid(row=3, column=1, columnspan=3, padx=(0, 20), pady=(10, 0), sticky="nsew")"""
        tab_option = customtkinter.CTkOptionMenu(kamarB, values=["tab 1", "tab 2", "tab 3", "tab 4", "tab 5"], command=self.optionmenu_callback)
        tab_option.grid(row=3, column=1, padx=(0, 20), pady=(10, 0), sticky="nsew")

        submit = customtkinter.CTkButton(kamarB, text="Submit", command=self.buatKamar)
        submit.grid(row=4, column=0, columnspan=4, padx=20, pady=20)
    
    def buatKamar(self):
        Kamar = self.kamar.get()
        Nama = self.nama.get()
        Id = self.id.get()
        Tab = self.tab_value
        self.MainData.append([self.ke,Tab,Id,Kamar,Nama])

        #Log - App opened
        self.isilog(f"New Kamar Added {self.MainData}")

        self.tabelupdate[Tab] = True
        self.tabelupdatedata[Tab] = [Id,Kamar,Nama]
        print(self.tabelupdatedata)

# // ============================ LIST KAMAR ========================== //
    def kamar(self):
        self.main_tab_frame = customtkinter.CTkTabview(self, width = int(self.width*0.83))
        self.main_tab_frame.grid(row = 0, column=1, padx=(10,10), pady=(0,0), sticky="nsew")
        self.main_tab_frame.add("1")
        self.main_tab_frame.add("2")

        self.tabview1 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26), height = int(self.height*0.1))
        self.tabview1.grid(row=0, column=0, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview1.add("1")
        self.tabview1.add("Detail")
        kamar_label1 = customtkinter.CTkLabel(self.tabview1.tab("1"), text="Kamar :", anchor="w")
        kamar_label1.grid(row=0, column=0, padx=10, pady=(10, 0))
        nama_label = customtkinter.CTkLabel(self.tabview1.tab("1"), text="Nama :", anchor="w")
        nama_label.grid(row=1, column=0, padx=10, pady=(10, 0))
        oxi_label = customtkinter.CTkLabel(self.tabview1.tab("1"), text="SpO2", anchor="w")
        oxi_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 0))
        bpm_label = customtkinter.CTkLabel(self.tabview1.tab("1"), text="BPM", anchor="w")
        bpm_label.grid(row=2, column=2, columnspan=2, padx=20, pady=(10, 0))
        status_label = customtkinter.CTkLabel(self.tabview1.tab("1"), text="Status", anchor="w")
        status_label.grid(row=2, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.tabview2 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview2.grid(row=0, column=1, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview2.add("2")
        self.tabview2.add("Detail")
        kamar_label = customtkinter.CTkLabel(self.tabview2.tab("2"), text="Kamar :", anchor="w")
        kamar_label.grid(row=0, column=0, padx=10, pady=(10, 0))
        nama_label = customtkinter.CTkLabel(self.tabview2.tab("2"), text="Nama :", anchor="w")
        nama_label.grid(row=1, column=0, padx=10, pady=(10, 0))
        oxi_label = customtkinter.CTkLabel(self.tabview2.tab("2"), text="SpO2", anchor="w")
        oxi_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 0))
        bpm_label = customtkinter.CTkLabel(self.tabview2.tab("2"), text="BPM", anchor="w")
        bpm_label.grid(row=2, column=2, columnspan=2, padx=20, pady=(10, 0))
        status_label = customtkinter.CTkLabel(self.tabview2.tab("2"), text="Status", anchor="w")
        status_label.grid(row=2, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.tabview3 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview3.grid(row=0, column=2, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview3.add("3")
        self.tabview3.add("Detail")
        kamar_label = customtkinter.CTkLabel(self.tabview3.tab("3"), text="Kamar :", anchor="w")
        kamar_label.grid(row=0, column=0, padx=10, pady=(10, 0))
        nama_label = customtkinter.CTkLabel(self.tabview3.tab("3"), text="Nama :", anchor="w")
        nama_label.grid(row=1, column=0, padx=10, pady=(10, 0))
        oxi_label = customtkinter.CTkLabel(self.tabview3.tab("3"), text="SpO2", anchor="w")
        oxi_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 0))
        bpm_label = customtkinter.CTkLabel(self.tabview3.tab("3"), text="BPM", anchor="w")
        bpm_label.grid(row=2, column=2, columnspan=2, padx=20, pady=(10, 0))
        status_label = customtkinter.CTkLabel(self.tabview3.tab("3"), text="Status", anchor="w")
        status_label.grid(row=2, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.tabview4 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview4.grid(row=1, column=0, padx=(10,10), pady=(0,0), sticky="nsew")
        self.tabview4.add("4")
        self.tabview4.add("Detail")
        kamar_label = customtkinter.CTkLabel(self.tabview4.tab("4"), text="Kamar :", anchor="w")
        kamar_label.grid(row=0, column=0, padx=10, pady=(10, 0))
        nama_label = customtkinter.CTkLabel(self.tabview4.tab("4"), text="Nama :", anchor="w")
        nama_label.grid(row=1, column=0, padx=10, pady=(10, 0))
        oxi_label = customtkinter.CTkLabel(self.tabview4.tab("4"), text="SpO2", anchor="w")
        oxi_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 0))
        bpm_label = customtkinter.CTkLabel(self.tabview4.tab("4"), text="BPM", anchor="w")
        bpm_label.grid(row=2, column=2, columnspan=2, padx=20, pady=(10, 0))
        status_label = customtkinter.CTkLabel(self.tabview4.tab("4"), text="Status", anchor="w")
        status_label.grid(row=2, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.tabview5 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview5.grid(row=1, column=1, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview5.add("5")
        self.tabview5.add("Detail")
        kamar_label = customtkinter.CTkLabel(self.tabview5.tab("5"), text="Kamar :", anchor="w")
        kamar_label.grid(row=0, column=0, padx=10, pady=(10, 0))
        nama_label = customtkinter.CTkLabel(self.tabview5.tab("5"), text="Nama :", anchor="w")
        nama_label.grid(row=1, column=0, padx=10, pady=(10, 0))
        oxi_label = customtkinter.CTkLabel(self.tabview5.tab("5"), text="SpO2", anchor="w")
        oxi_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 0))
        bpm_label = customtkinter.CTkLabel(self.tabview5.tab("5"), text="BPM", anchor="w")
        bpm_label.grid(row=2, column=2, columnspan=2, padx=20, pady=(10, 0))
        status_label = customtkinter.CTkLabel(self.tabview5.tab("5"), text="Status", anchor="w")
        status_label.grid(row=2, column=4, columnspan=2, padx=20, pady=(10, 0))

        self.tabview6 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview6.grid(row=1, column=2, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview6.add("6")
        self.tabview6.add("Detail")
        kamar_label = customtkinter.CTkLabel(self.tabview6.tab("6"), text="Kamar :", anchor="w")
        kamar_label.grid(row=0, column=0, padx=10, pady=(10, 0))
        nama_label = customtkinter.CTkLabel(self.tabview6.tab("6"), text="Nama :", anchor="w")
        nama_label.grid(row=1, column=0, padx=10, pady=(10, 0))
        oxi_label = customtkinter.CTkLabel(self.tabview6.tab("6"), text="SpO2", anchor="w")
        oxi_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 0))
        bpm_label = customtkinter.CTkLabel(self.tabview6.tab("6"), text="BPM", anchor="w")
        bpm_label.grid(row=2, column=2, columnspan=2, padx=20, pady=(10, 0))
        status_label = customtkinter.CTkLabel(self.tabview6.tab("6"), text="Status", anchor="w")
        status_label.grid(row=2, column=4, columnspan=2, padx=20, pady=(10, 0)) 

        self.tabview7 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview7.grid(row=2, column=0, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview7.add("7")
        self.tabview7.add("Detail")    
        #// ================= belum diisi ================== //

        self.tabview8 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview8.grid(row=2, column=1, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview8.add("8")
        self.tabview8.add("Detail")\

        self.tabview9 = customtkinter.CTkTabview(self.main_tab_frame.tab("1"), width = int(self.width*0.26))
        self.tabview9.grid(row=2, column=2, padx=(10,5), pady=(0,0), sticky="nsew")
        self.tabview9.add("9")
        self.tabview9.add("Detail")


        self.tabC = [self.tabview1.tab("1"), self.tabview2.tab("2"),self.tabview3.tab("3"),self.tabview4.tab("4"),self.tabview5.tab("5"), self.tabview6.tab("6")]

    def pengaturan(self):
        setting = customtkinter.CTkToplevel(self)
        setting.title("Pengaturan")
        setting.geometry(f"{580}x{320}")
        setting.grid_columnconfigure(3, weight=1)

        #Agar tidak bisa di maximize
        setting.resizable(0,0)

        tabview = customtkinter.CTkTabview(setting, width = 540, height=280)
        tabview.grid(row=0, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        tabview.add("General")
        tabview.add("WiFi")
        tabview.add("Help")
        tabview.add("About")
        tabview.tab("General").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        tabview.tab("WiFi").grid_columnconfigure(1, weight=1)
        tabview.tab("Help").grid_columnconfigure(0, weight=1)
        tabview.tab("About").grid_columnconfigure(0, weight=1)

        #General Setting
        appearance_mode_label = customtkinter.CTkLabel(tabview.tab("General"), text="Appearance Mode:", anchor="center")
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(tabview.tab("General"), values=["Dark", "Light", "System"],command=self.change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        scaling_label = customtkinter.CTkLabel(tabview.tab("General"), text="UI Scaling:", anchor="w")
        scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        scaling_optionemenu = customtkinter.CTkOptionMenu(tabview.tab("General"), values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #WiFi Setting
        ssid_label= customtkinter.CTkLabel(tabview.tab("WiFi"), text= "SSID:", anchor="w")
        ssid_label.grid(row=0, column=0, padx=20, pady=(10, 0))       
        self.ssid = customtkinter.CTkEntry(tabview.tab("WiFi"), placeholder_text="SSID")
        self.ssid.grid(row=0, column=1, columnspan=3, padx=(0, 20), pady=(10, 0), sticky="nsew")

        curent_Ssid = customtkinter.CTkLabel(tabview.tab("WiFi"), text=f"SSID saat ini : {self.wifidata[0]}")
        curent_Ssid.grid(row=1, column=0, columnspan=2, padx=0, pady=(5, 0)) 

        pass_label= customtkinter.CTkLabel(tabview.tab("WiFi"), text= "Password:", anchor="w")
        pass_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.Pass = customtkinter.CTkEntry(tabview.tab("WiFi"), placeholder_text="WiFi Password")
        self.Pass.grid(row=2, column=1, columnspan=3, padx=(0, 20), pady=(10, 0), sticky="nsew")

        curent_Pass = customtkinter.CTkLabel(tabview.tab("WiFi"), text=f"Password saat ini : {self.wifidata[1]}")
        curent_Pass.grid(row=3, column=0, columnspan=2, padx=0, pady=(5, 0))

        save = customtkinter.CTkButton(tabview.tab("WiFi"), text="Save Change", command=self.savewifi)
        save.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        #Help
        info = customtkinter.CTkLabel(tabview.tab("Help"), text="Informasi mengenai fungsi aplikasi dapat dilihat pada", anchor="w")
        info.grid(row=0, column=0, padx=20, pady=(20,10))
        info1 = customtkinter.CTkButton(tabview.tab("Help"), text="Document", command=self.about)
        info1.grid(row=1, column=0, columnspan=1, padx=20, pady=20)

        #About
        about = customtkinter.CTkLabel(tabview.tab("About"), text=
        "Applikasi ini dibuat untuk memenuhi tugas akhir mata kuliah Telemedika\nS-1 Teknik Biomedis, Fakultas Sains dan Teknologi, Universitas Airlangga"
        , anchor="w")
        about.grid(row=0, column=0, padx=20, pady=(50,10))
        about1 = customtkinter.CTkLabel(tabview.tab("About"), text="RonAaron\n\nTerima Kasih", anchor="w")
        about1.grid(row=1, column=0, padx=20, pady=(0,10))
        

    def savewifi(self):
        Ssid = self.ssid.get()
        Pass = self.Pass.get()
        self.wifidata[0] = Ssid
        self.wifidata[1] = Pass

        #Log - WiFi
        self.isilog(f"WiFi changed '{self.wifidata[0]}' '{self.wifidata[1]}'")

    def about(self):
        url = "https://github.com/RonAaron61/Oximetry-Monitor_Telemedika"
        webbrowser.get().open(url,new=2)

    def isilog(self, log_):
        date = tm.localtime()[0:6]
        log = log_
        logprint = "{tahun}/{bulan}/{hari} - {jam}:{menit}:{detik}".format(tahun = date[0], bulan=date[1], hari=date[2], jam=date[3], menit=date[4],detik=date[5])
        print(f"{logprint} --> {log}")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def optionmenu_callback(self, new_scaling: str):
        self.tab_value = int(new_scaling.replace("tab", ""))

    def onClosing(self):
        if messagebox.askokcancel("Quit", "Yakin ingin keluar aplikasi?"):
            #Log - App opened
            self.isilog("App Clossed")
            self.destroy()

    def get_data(self, alat_):
        alat = alat_
        result_db = app_db.get(f'/Alat/{alat}/', None)
        return result_db

if __name__ == "__main__":
    app = app()  
    app.after_idle(app.updatedata)  
    app.mainloop()
