# Créé par Eleve, le 17/11/2023 en Python 3.7
from tkinter import messagebox
from customtkinter import *
from math import *
import cmath
from Fonctionnement.calculs import calculer_racines, textbox
from Data.data import data_factoriser, data_light, data_delta, data_options, data_menu
from Fonctionnement.Menu import Menu1, Menu2


app = CTk()

app.title("Calculer les racines d'un polynôme du second degré")

set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

with open("Data/dataLongueur.txt", "r") as file:
    dataLongueur = file.readline().strip()
with open("Data/dataLargeur.txt", "r") as file:
    dataLargeur = file.readline().strip()
with open("Data/dataFactoriser.txt", "r") as file:
    first_line = file.readline().strip()
with open("data/dataLight.txt", "r") as file:
    second_line = file.readline().strip()
with open("data/dataDelta.txt", "r") as file:
    third_line = file.readline().strip()
with open("data/dataOptions.txt", "r") as file:
    fourth_line = file.readline().strip()
with open("data/dataHistorique.txt", "r") as file:
    line_historique = file.readline().strip()





dataLarg=float(dataLargeur)
resultatt = 0.672 * dataLarg - 5.8975

# Arrondi à l'unité près
resultat_arrondi = round(resultatt)


dataLo=float(dataLongueur)
resultattt = 0.672 * dataLo - 5.8975

# Arrondi à l'unité près
resultat_arrondii = round(resultattt)






delta_neg = False


def delta_neg() :
    global delta_neg
    if delta_neg == True :
        delta_neg = False
    else :
        delta_neg = True


    data_delta()




factorisation = False
def factoriser() :
    global factorisation
    if factorisation == True :
        factorisation = False
    else :
        factorisation = True
    data_factoriser()

##tar=False
options=False
def options1() :
    global options
    if options == True :
        afficher()
        options = False
    else :
        masquer()
        options = True

    data_options()






def on_enter_key(event):
    calculI()




def format_coefficient(coefficient, variable):
    if coefficient < 0:
        return f"{int(coefficient)}{variable}"
    else:
        return f"+{int(coefficient)}{variable}"


def calculI() :
    def enregistrer_historique(a, b, c):
        with open("data/historique.txt", "w") as fichier:
            fichier.write("")
    def enregistrer_historique1(a, b, c):
     if line_historique=="1":
        with open("data/historique.txt", "a") as fichier:
            fichier.write(nouvelle_ligne + contenu_actuel)


    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Exécuter le calcul des racines (remplacez cette ligne par votre propre logique)
        calculer_racines(a, b, c, app, factorisation, delta_neg)
        nouvelle_ligne = f"{int(a)}x² {format_coefficient(b, 'x')} {format_coefficient(c, 'x')}\n"
        with open("data/historique.txt", "r") as fichier:
          contenu_actuel = fichier.read()


        # Simulons un calcul en attendant 2 secondes
        app.after(200, lambda: enregistrer_historique(a, b, c))
        app.after(300, lambda: enregistrer_historique1(a, b, c))




    except ValueError:
        messagebox.showerror("Erreur", "Veuillez saisir des valeurs numériques valides pour a, b et c")


label1 = CTkLabel(master=app, text="x² +", font=("Roboto", 20))
label1.place(relx=0.45, rely=0.15, anchor="center")
label2 = CTkLabel(master=app, text="x +", font=("Roboto", 20))
label2.place(relx=0.55, rely=0.15, anchor="center")
entry_a = CTkEntry(master=app, placeholder_text="a", width=50,)
entry_a.place(relx=0.4, rely=0.15, anchor="center")
entry_b = CTkEntry(master=app, placeholder_text="b", width=50,)
entry_b.place(relx=0.5, rely=0.15, anchor="center")
entry_c = CTkEntry(master=app, placeholder_text="c", width=50,)
entry_c.place(relx=0.6, rely=0.15, anchor="center")















cadre = CTkFrame(app) # Un cadre pour les labels
cadre.place(relx=0.9, rely=0.25, anchor="center")

def afficher():# On utilise la variable globale

        cadre.place(relx=0.9, rely=0.25, anchor="center")
        switch_delta_neg.pack(ipady=10, ipadx=5, anchor="w") # On remet le switch en bas du cadre
        switch_factoriser.pack(ipady=10, ipadx=5, anchor="w")


def masquer() :
        cadre.place_forget()
        switch_delta_neg.pack_forget() # On enlève le switch du cadre
        switch_factoriser.pack_forget()


switch_delta_neg = CTkSwitch(master=cadre, text="Δ<0", switch_height=20, switch_width=40, corner_radius=36, command=delta_neg)
switch_delta_neg.pack(ipady=10, ipadx=5, anchor="w") # On le met en bas du cadre
switch_factoriser = CTkSwitch(master=cadre, text="Factoriser", switch_height=20, switch_width=40, corner_radius=36, command=factoriser)
switch_factoriser.pack(ipady=10, ipadx=5, anchor="w")



if first_line=="1":
    switch_factoriser.select()
    factorisation = True
elif first_line=="0" :
    switch_factoriser.deselect()

if third_line=="1":
    switch_delta_neg.select()
    delta_neg = True
elif third_line=="0" :
    switch_delta_neg.deselect()

if second_line=="1":

    set_appearance_mode("light")

elif second_line=="0" :

    set_appearance_mode("dark")

if fourth_line=="1":
    print("")
elif fourth_line=="0" :

    app.after(1, lambda : masquer())
    options=True




bouton = CTkButton(app, text="Options", command=options1)
bouton.place(relx=0.9, rely=0.05, anchor="center")








df=True
def HISTT():
    global df, hj, label33
    if df==True:
         with open("data/historique.txt", "r") as fichier:
            contenu = fichier.read()
         hj = CTkScrollableFrame(app, width= 150, height=10) # Un cadre pour les labels
         hj.place(relx=0.1, rely=0.4, anchor="center")
         label33 = CTkLabel(master=hj, text=contenu)
         label33.pack()
         df=False
    else :
        try :
            hj.place_forget()
            label33.place_forget()
            label33.pack_forget()
            df=True
        except:pass
def HISTTE():
    reponsee = messagebox.askyesno("Validation", "Êtes-vous sûr de vouloir supprimer l'historique ?")
    if reponsee:
        with open("data/historique.txt", "w") as fichier:
            fichier.write("")



boutonnnn = CTkButton(app, text="Historique", command=HISTT)
boutonnnnR = CTkButton(app, text="X", command=HISTTE, width =10, height=10, fg_color="darkred",corner_radius=36, hover_color="red")
if line_historique=="1":
        boutonnnn.place(relx=0.1, rely=0.2, anchor="center")
        boutonnnnR.place(relx=0.17, rely=0.2, anchor="center")


























btn = CTkButton(master=app, text="Calculer les racines", corner_radius=32, command=calculI)
btn.place(relx=0.5, rely=0.25, anchor="center")
frame1 = CTkFrame(master=app, corner_radius=10, fg_color= ("#3a7ebf", "#1f538d"))
CTkLabel(master=frame1, text="Calcul des racines d'un polynôme du second degré", font=("Roboto", 13), text_color="#FFFFFF", justify="center").pack(expand=True, pady=(7, 7), padx=(50, 50))
frame1.place(relx=0.5, rely=0.05, anchor="center")
kok=True
shift_quit=False
def on_shift_press(event):
    if event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        global shift_quit
        shift_quit=True

def on_shift_release(event):
    if event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        global shift_quit
        shift_quit=True


app.bind('<Shift_L>', on_shift_press)
app.bind('<Shift_R>', on_shift_press)
app.bind('<KeyRelease-Shift_L>', on_shift_release)
app.bind('<KeyRelease-Shift_R>', on_shift_release)


def on_resize():
    if shift_quit==True :
        largeur = f"{app.winfo_width()}"
        longueur = f"{app.winfo_height()}"
        with open("data/dataLargeur.txt", "w") as file:
            file.write(largeur)
        with open("data/dataLongueur.txt", "w") as file:
            file.write(longueur)
    app.destroy()

if resultat_arrondi>app.winfo_screenwidth():
           app.after(0, lambda : app.wm_state('zoomed'))


else :
    app.geometry(f"{resultat_arrondi}x{resultat_arrondii}")
app.minsize(900, 400)











bouton_racines = CTkButton(app, text="Calculer racines")
bouton_racines.place(relx=0.5, rely=0.5, anchor="center")



global main
main=True
def main1():
    global bouton_racines, frame2, main, textbox, bouton_parametre

    if main==True :
        main=False
        textbox(app)
        cadre.place_forget()
        switch_delta_neg.pack_forget() # On enlève le switch du cadre
        switch_factoriser.pack_forget()

        bouton.place_forget()
        btn.place_forget()
        frame1.place_forget()
        label1.place_forget()
        label2.place_forget()
        entry_a.place_forget()
        entry_b.place_forget()
        entry_c.place_forget()
        bouton_menu.place_forget()
        bouton_racines.place(relx=0.5, rely=0.5, anchor="center")
        boutonnnnR.place_forget()
        boutonnnn.place_forget()
        try : hj.place_forget()
        except :pass


        app.title("Menu")

        ##bouton_parametre.place(relx=0.9, rely=0.05, anchor="center")
        with open("data/dataHistorique.txt", "r") as file:
          line_historique = file.readline().strip()

        Menu1(app, main, bouton_racines, kok, line_historique)

####################
    elif main==False:

        main=True
        app.title("Calculer les racines d'un polynôme du second degré")
        cadre.place(relx=0.9, rely=0.25, anchor="center")
        switch_delta_neg.pack(ipady=10, ipadx=5, anchor="w") # On remet le switch en bas du cadre
        switch_factoriser.pack(ipady=10, ipadx=5, anchor="w")

        bouton.place(relx=0.9, rely=0.05, anchor="center")
        btn.place(relx=0.5, rely=0.25, anchor="center")
        frame1.place(relx=0.5, rely=0.05, anchor="center")
        label1.place(relx=0.45, rely=0.15, anchor="center")
        label2.place(relx=0.55, rely=0.15, anchor="center")
        entry_a.place(relx=0.4, rely=0.15, anchor="center")
        entry_b.place(relx=0.5, rely=0.15, anchor="center")
        entry_c.place(relx=0.6, rely=0.15, anchor="center")
        bouton_menu.place(relx=0.1, rely=0.05, anchor="center")
        bouton_racines.place_forget()
        with open("data/dataHistorique.txt", "r") as file:
          line_historique = file.readline().strip()
        if line_historique=="1":
            boutonnnn.place(relx=0.1, rely=0.2, anchor="center")
            boutonnnnR.place(relx=0.17, rely=0.2, anchor="center")


        try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                c = float(entry_c.get())
                calculer_racines(a, b, c, app, factorisation, delta_neg)
        except ValueError:
                print("")

        ##bouton_parametre.place_forget()
        Menu2(app, main)
    global ook
    try :
        if ook==1 :
            data_menu()
    except : pass
    ook=1



bouton_racines.configure(command=main1)


bouton_menu = CTkButton(app, text="Menu", command=main1)
bouton_menu.place(relx=0.1, rely=0.05, anchor="center")



def key_pressed(event):
    if event.keysym == 'm' and event.state == 4:  # Vérifie si la touche pressée est 'm' et que la touche Ctrl est également enfoncée
     if main==True :

        main1()



with open("data/dataMenu.txt", "r") as file:
    DMenu = file.readline().strip()

DMenu=int(DMenu)


if DMenu == 1:

    main1()


elif DMenu == 0 :


    main=False
    main1()

app.iconbitmap("Images/Logo1.ico")

app.bind('<Key>', key_pressed)
app.bind("<Return>", lambda event=None: calculI())
app.protocol("WM_DELETE_WINDOW", on_resize)
app.mainloop()
