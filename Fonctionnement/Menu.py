from customtkinter import *
from Data.data import data_hist
def Menu1(app, main, bouton_racines, line_historique, kok) :
     global frame2, bouton_parametre, second_line, switch_light, light1, koko, pop
     from Data.data import data_light
     with open("Data/dataLight.txt", "r") as file:
        second_line = file.readline().strip()
     light1=False
     def light() :
                global light1
                if light1 == True :
                    light1= False
                    set_appearance_mode("dark")
                else :
                    light1 = True
                    set_appearance_mode("light")
                data_light()
     def his():
         data_hist()
     def param() :
        Menu1(app, main, bouton_racines, kok, line_historique)
        app.after(1, lambda : switch_light.pack_forget())
        app.after(1, lambda : cadre.place_forget())
     def paramètre1():
            global bouton_retour, cadre, switch_light, koko
            cadre = CTkScrollableFrame(app, width= 500, height=600) # Un cadre pour les labels
            cadre.place(relx=0.5, rely=0.5, anchor="center")
            frame2.place_forget()
            bouton_parametre.place_forget()
            bouton_racines.place_forget()
            bouton_retour = CTkButton(app, text="Menu", fg_color="transparent", hover_color="#D3D3D3", border_width=2, text_color=("gray10", "#DCE4EE"), command=param)
            bouton_retour.place(relx=0.9, rely=0.05, anchor="center")
            switch_light = CTkSwitch(master=cadre, text="Arrière-plan", switch_height=20, switch_width=40, corner_radius=36, command=light)
            switch_light.pack(ipady=10, ipadx=5, anchor="w")
            if second_line=="1":
             switch_light.select()
            elif second_line=="0" :
                 switch_light.deselect()
            switch_historique = CTkSwitch(master=cadre, text="Historique", switch_height=20, switch_width=40, corner_radius=36, command=his)
            switch_historique.pack(ipady=10, ipadx=5, anchor="w")
            with open("Data/dataHistorique.txt", "r") as file:
                 line_historique = file.readline().strip()
            if line_historique=="1":
             app.after(1, lambda : switch_historique.select())
            else :
                app.after(1, lambda : switch_historique.deselect())
            frame2.place_forget()
     if main==False:
        app.title("Menu")
        frame2 = CTkFrame(master=app, corner_radius=10, fg_color= "#77B5FE")
        CTkLabel(master=frame2, text="Menu", font=("Roboto", 20), text_color="#FFFFFF", justify="center").pack(expand=True, pady=(7, 7), padx=(75, 75))
        frame2.place(relx=0.5, rely=0.05, anchor="center")
        bouton_parametre = CTkButton(app, text="Paramètres", fg_color="transparent", hover_color="#D3D3D3", border_width=2, text_color=("gray10", "#DCE4EE"), command=paramètre1)
        bouton_parametre.place(relx=0.9, rely=0.05, anchor="center")
        bouton_racines.place(relx=0.5, rely=0.5, anchor="center")
     try :
            bouton_retour.place_forget()
     except :
            print("")
     if second_line=="1":
            light1 = True
            set_appearance_mode("light")
     elif second_line=="0" :
            set_appearance_mode("dark")
     koko=True
     pop=False
     def ctrl_p_pressed(event):
            global koko
            if pop==False:
                if koko==True :
                    paramètre1()
                    koko=False
                else :
                  param()
                  koko=True
     app.bind('<Control-p>', ctrl_p_pressed)
def Menu2(app, main) :
        global pop
        pop=True
        try :
            frame2.place_forget()
            bouton_parametre.place_forget()
            frame3.place_forget()
            bouton_paramètre1.place_forget()
        except :
            print()
