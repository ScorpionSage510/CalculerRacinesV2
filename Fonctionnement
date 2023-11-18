from tkinter import messagebox
from customtkinter import *
from math import *
import cmath
def format_coefficient(coefficient, variable):
    if coefficient < 0:
        return f"{int(coefficient)}{variable}"
    else:
        return f"+{int(coefficient)}{variable}"
def calculer_racines(a, b, c, app, factorisation, delta_neg):
    global textbox
    try:
        D = b**2 - 4 * a * c
        if D > 0:
            x1 = ((-b - sqrt(D)) / (2 * a))
            x2 = ((-b + sqrt(D)) / (2 * a))
            if factorisation == False :
                     Résultat = f"f(x)={int(a)}x² {format_coefficient(b, 'x')} {format_coefficient(c, 'x')}\nΔ={D}>0\nIl y a deux racines :\nx1=({-b} + √{D}) / {2 * a}={x1}\nx2=({-b} - √{D}) / {2 * a}={x2}"
            else :
                        Résultat = f"f(x)={int(a)}x² {format_coefficient(b, 'x')} {format_coefficient(c, 'x')}\nΔ={D}>0\nIl y a deux racines :\nx1=({-b} + √{D}) / {2 * a}={x1}\nx2=({-b} - √{D}) / {2 * a}={x2}\n\nf(x)={a}(x-({-b} + √{D}) / {2 * a}))(x-({-b} - √{D}) / {2 * a})"
        elif D == 0:
            x0 = -b / (2 * a)
            if factorisation == False :
                        Résultat = f"f(x)={int(a)}x² {format_coefficient(b, 'x')} {format_coefficient(c, 'x')}\nΔ={D}\nIl y a une racine :\nx0=({-b} + √{D}) / {2 * a})={x0}"
            else :
                        Résultat = f"f(x)={int(a)}x² {format_coefficient(b, 'x')} {format_coefficient(c, 'x')}\nΔ={D}\nIl y a une racine :\nx0=({-b} + √{D}) / {2 * a})={x0}\n\nf(x)={a}(x-({-b} + √{D}) / {2 * a}))²"
        else:
                    if delta_neg==True :
                        x1 = ((-b - cmath.sqrt(D)) / (2 * a))
                        x2 = ((-b + cmath.sqrt(D)) / (2 * a))
                        if factorisation == False :
                                    Résultat = f"f(x)={int(a)}x² {format_coefficient(b, 'x')} {format_coefficient(c, 'x')}\nΔ={D}>0\nIl y a deux racines imaginaires :\nx1=({-b} + j√{-D}) / {2 * a})={x1}\nx2=({-b} - j√{-D}) / {2 * a}={x2}"
                        else :
                                    Résultat = f"f(x)={int(a)}x² {format_coefficient(b, 'x')} {format_coefficient(c, 'x')}\nΔ={D}>0\nIl y a deux racines imaginaires :\nx1=({-b} + j√{-D}) / {2 * a})={x1}\nx2=({-b} - j√{-D}) / {2 * a}={x2}\n\nf(x)={a}(x-({-b} + j√{-D}) / {2 * a}))(x-({-b} - j√{-D}) / {2 * a}))"
                    else :
                                Résultat = f"f(x)={int(a)}x² {format_coefficient(b, 'x')} {int(c)}\nΔ={D}<0\nIl n'y a pas de racine réelle"
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez saisir des valeurs numériques valides pour a, b et c")
    textbox = CTkTextbox(master=app, border_color="#7d9ed4", border_width=2, width=550, height=220, font=("Roboto", 16))
    textbox.insert("0.0", Résultat)
    textbox.grid(row = 0, column= 0)
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    def tracer() :
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-10, 10, 1000)
        y = a * x ** 2 + b * x + c
        plt.plot(x, y)
        plt.axhline(0, color='red')
        plt.axvline(0, color='red')
        plt.xlim(-20, 20)
        plt.ylim(-50, 50)
        plt.show()
    global bouton_tracer
    bouton_tracer = CTkButton(app, text="Tracer f(x)", fg_color="transparent", hover_color="#D3D3D3", border_width=2, text_color=("gray10", "#DCE4EE"), command=tracer)
    bouton_tracer.place(relx=0.5, rely=0.8, anchor="center")
def textbox(app):
    try :
        app.after(1, lambda : textbox.place_forget())
        app.after(1, lambda : bouton_tracer.place_forget())
    except :
        pass
