import tkinter as tk
class Tree:
    def __init__(self, l, izq, der):
        self.label = l
        self.left = izq
        self.right = der

def VI(f, I):
    if f.right == None:
        return I[f.label]
    elif f.label == "-":
        return 1 - VI(f.right, I)
    elif f.label == "&":
        return VI(f.right, I) * VI(f.left, I)
    elif f.label == "v":
        return max(VI(f.left, I), VI(f.right, I))
    elif f.label == "->":
        return max(1 - VI(f.left, I), VI(f.right, I))
    elif f.label == "<->":
        return 1 - (VI(f.left, I) - VI(f.right, I))**2
    else:
        return "Hay algun error en el planteamiento"
    
def string2tree(A, LetrasProposicionales):
    conectivos = ["O", "Y", ">"]
    pila = []
    for c in A:
        if c in LetrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == "-":
            formulaaux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaaux)
        elif c in conectivos:
            formulaaux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaaux)
    return pila[-1]

def Inorder(A):
    if A.right == None:
        return A.label
    elif A.label == "-":
        return "-" + Inorder(A.right)
    elif A.label in ["Y", "O", ">"]:
        return "(" + Inorder(A.left) + A.label + Inorder(A.right) + ")"

def interpretaciones(LetrasProposicionales):
    interps = []
    aux = {}
    for a in LetrasProposicionales:
        aux[a] = 1
    interps.append(aux)
    for a in LetrasProposicionales:
        interps_aux = [i for i in interps]
        for i in interps_aux:
            aux1 = {}
            for b in LetrasProposicionales:
                if a == b:
                    aux1[b] = 1 - i[b]
                else:
                    aux1[b] = i[b]
            interps.append(aux1)
    return interps
    
LetrasProposicionales = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

C1 = "d-b-YeYe-b-YdYOe-d-YbYOa->"
C2 = "e-d-Yc-Ya-YfYf-d-Yc-Ya-YeYOf-e-Yc-Ya-YdYOf-e-Yd-Ya-YcYOf-e-Yd-Yc-YaYOb->"
C3 = "e-b-YfYf-b-YeYOf-e-YbYOc->"
C4 = "ha-Ye-Yb-Ya-Yh-aYe-Yb-Ya-YOh-g-YeYb-Ya-YOh-g-Ye-YbYa-YOh-g-Ye-Yb-YaYOd->"
C51 = "ih-Yg-Yf-Yd-Yc-Yb-Ya-Yi-hYg-Yf-Yd-Yc-Yb-Ya-YOi-h-YgYf-"
C52 = "Yd-Yc-Yb-Ya-YOi-h-Yg-YfYd-Yc-Yb-Ya-YOi-h-Yg-Yf-YdYc-Yb-"
C53 = "Ya-YOi-h-Yg-Yf-Yd-YcYb-Ya-YOi-h-Yg-Yf-Yd-Yc-YbYa-YO"
C54 = "i-h-Yg-Yf-Yd-Yc-Yb-YaYOe->"
C5T = C51+C52+C53+C54
C6 = "ih-Ye-Yc-Yb-Yi-hYe-Yc-Yb-YOi-h-YeYc-Yb-YOi-h-Ye-YcYb-YOi-h-Ye-Yc-YbYOf->"
C7 = "he-Yd-Yh-eYd-YOh-e-YdYOg->"
C8 = "ig-Yf-Ye-Yd-Yi-gYf-Ye-Yd-YOi-g-YfYe-Yd-YOi-g-Yf-YeYd-YOi-g-Yf-Ye-YdYOh->"
C9 = "hf-Ye-Yh-fYe-YOh-f-YeYOi->"

R1 = "ed-Ye-dYOb-a-Y->"
R2 = "eb-Ye-bYOd-a-Y->"
R3 = "f-eYfe-YOc-b-Y->"
R4 = "db-Ybd-YOf-c-Y->"
R5 = "eh-Yhe-YOg-d-Y->"
R6 = "h-g-Yb-YaYh-g-YbYa-YOh-gYb-Ya-YOhg-Yb-Ya-YOe-d-Y->"
R7 = "eh-Yhe-YOi-f-Y->"
R8 = "f-eYfe-YOi-h-Y->"
R9 = "d-eYde-YOh-g-Y->"
R10 = "ih-Yc-Yb-Yi-hYc-Yb-YOi-Yh-YcYb-YOi-h-Yc-YbYOf-e-Y->"
R11 = "ig-Yf-Yd-Yi-gYf-Yd-YOi-Yg-YfYd-YOi-g-Yf-YdYOh-e-Y->"
R12 = "e-d-Yc-YaYe-d-YcYa-YOe-dYc-Ya-YOe-d-Yc-Ya-YOe-b-Y->"

SumCi = C1+C2+C3+C4+C5T+C6+C7+C8+C9+"YYYYYYYY"

SumRi = R1+R2+R3+R4+R5+R6+R7+R8+R9+R10+R11+R12+"YYYYYYYYYYY"

formula_global = string2tree(SumCi, LetrasProposicionales)
form = string2tree(SumRi,LetrasProposicionales)

interpretaciones_form = interpretaciones(LetrasProposicionales)
interpretaciones_form_aux = []

print(Inorder(string2tree(R1, LetrasProposicionales)))

#for i in interpretaciones_form:
#    if (VI(form, i) == 1):
#        interpretaciones_form_aux.append(i)
#for i in interpretaciones_form:
#    print("entre")
#    if (VI(formula_global, i) == 1):
#        interpretaciones_form_aux.append(i)
#
#print(interpretaciones_form_aux)
        


#------ creación ventana -----------------
#minas = tk.Tk()
#minas.title("Busca Minas")
#minas.geometry("360x360")
#minas.config(bg = "grey")
#
#def show_number():
#    C1 = tk.Button(text = "1")
#
##------ creación botones -----------------
#C1 = tk.Button(minas, command = show_number, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
#C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
#C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
#C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
#C5 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
#C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
#C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
#C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
#C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
#
#minas.mainloop()