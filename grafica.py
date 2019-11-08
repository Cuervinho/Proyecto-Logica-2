import tkinter as tk

minas = tk.Tk()
minas.title("Busca Minas")
minas.geometry("360x360")
minas.config(bg = "grey")

#elegir first como primera casilla elegida y second como segunda
#las letras a, b, ... , i corresponden a 1, 2, ... , 9 respectivamente
#considerar que las posibles combinaciones son:
#a-b, a-d, b-c, b-e, c-f, d-e, d-g, e-f, e-h, f-i, g-h, h-i
#además de sus respectivas elecciones inversas

first = "a"
second = "b"

#-------- a y otro ------------
if first == "a" and second == "b":
    C1 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "a" and second == "d":
    C1 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

#-------- b y otro ------------

if first == "b" and second == "a":
    C1 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

if first == "b" and second == "c":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

if first == "b" and second == "e":
    C1 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red",width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
#-------- c y otro ------------

if first == "c" and second == "b":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

if first == "c" and second == "f":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

#-------- d y otro ------------

if first == "d" and second == "a":
    C1 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "d" and second == "e":
    C1 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "d" and second == "g":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

#-------- e y otro ------------

if first == "e" and second == "b":
    C1 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "e" and second == "d":
    C1 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

if first == "e" and second == "f":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

if first == "e" and second == "h":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

#-------- f y otro ------------

if first == "f" and second == "c":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "f" and second == "e":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "f" and second == "i":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

#-------- g y otro ------------

if first == "g" and second == "d":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "g" and second == "h":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
#-------- h y otro ------------

if first == "h" and second == "g":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
if first == "h" and second == "e":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

if first == "h" and second == "i":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

#-------- i e otro ------------

if first == "i" and second == "h":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

if first == "i" and second == "f":
    C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
    C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
    C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
    C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
    C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
    C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
    C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
    C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
    C9 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

minas.mainloop()