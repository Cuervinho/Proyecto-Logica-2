import tkinter as tk

minas = tk.Tk()
minas.title("Busca Minas")
minas.geometry("360x360")
minas.config(bg = "grey")

#clase árbol binario
class Tree:
    def __init__(self, l, izq, der):
        self.label = l
        self.left = izq
        self.right = der

#valor interpretación
def VI(f, I):
    if f.right == None:
        return I[f.label]
    elif f.label == "-":
        return 1 - VI(f.right, I)
    elif f.label == "Y":
        return VI(f.right, I) * VI(f.left, I)
    elif f.label == "O":
        return max(VI(f.left, I), VI(f.right, I))
    elif f.label == ">":
        return max(1 - VI(f.left, I), VI(f.right, I))
    elif f.label == "=":
        return 1 - (VI(f.left, I) - VI(f.right, I))**2
    else:
        return "Hay algun error en el planteamiento"
    
#convertir de polaca inversa a árbol
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

#imprimir árbol a string
def Inorder(A):
    if A.right == None:
        return A.label
    elif A.label == "-":
        return "-" + Inorder(A.right)
    elif A.label in ["Y", "O", ">"]:
        return "(" + Inorder(A.left) + A.label + Inorder(A.right) + ")"
    
    
#tabla de verdad de todas las proposiciones
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


#forma normal conjuntiva
def enFNC(A):
#    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 900)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    atomos = letrasProposicionalesA + letrasProposicionalesB
    L = []
    pila = []
    i = -1
    s = A[0]
    
    while len(A) > 0:
        if s in atomos and len(pila) > 0 and pila[-1] == "-":
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            L.append(atomo + "=" + "-" + s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ")":
            w = pila[-1]
            O = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila) - 4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo + "=" + "(" + v + O + w + ")")
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    
    B = ""
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    
    for X in L:
        Y = enFNC(X)
        B += "Y" + Y
    
    B = atomo + B
    return B
                


def Clausula(C):
    L = []
    while len(C) > 0:
        s = C[0]
        if s == "O":
            C = C[1:]
        elif s == "-":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L

def formaClausal(A):
    L = []
    i = 0
    while len(A) > 0:
        if i >= len(A):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == "Y":
                L.append(Clausula(A[:i]))
                A = A[i + 1:]
                i = 0
            else:
                i += 1
    return L
    

def unitPropagate(S,I):
    unitaria = False
    C = []
    while len(S)!=0:
        for x in S:
            if len(x)==1:
                l = x
                unitaria = True
                break
            elif len(x)==2 and x[0]=='-':
                l = x
                unitaria = True
                break
        if unitaria == True:
            C = S[:]
            count = 0
            for m in S:
                C[count]=m
                for c in range(len(m)):
                    if len(l) == 1:
                        if (m[c] == '-' and m[c+1] == l):
                            yolo = len(m)
                            C[count] = C[count].replace('-'+C[count][c+1],'')
                            #C[count] = C[count].replace(C[count][c],'')
                            if len(C[count])<yolo:
                                break
                        elif m[c] == l:
                            C.remove(C[count])
                            count-=1

                    elif len(l) == 2:
                        if m[c] == l[1]:
                            yolo = len(m)
                            C[count]= C[count].replace(C[count][c],'')
                            if len(C[count])<yolo:
                                break
                        elif m[c] == '-' and m[c+1] == l[1]:
                            C.remove(C[count])
                            count-=1
                            break
                        
                            

                count+=1
            S = C[:]
            if len(l) == 1:
                I[l[0]]=1
            elif len(l)==2:
                I[x[1]]=0
            unitaria=False
        else:
            break
    return S,I



def DPLL(S,I):
    S,I = unitPropagate(S,I)
    clau_vacia = ""
    if clau_vacia in S:
        return "Insatisfacible" ,{}
    elif len(S)==0:
        return "Satisfacible" ,I
    S2 = S[:]
    count = 0
    for m in S:
        S2[count] = m
        for c in range(len(m)):
            if m[c] not in I.keys():
                if m[c] != '-':
                    l = m[c]
                    break
        break
    for m in S:
        for c in range(len(m)):
            if len(l) == 1:
                if (m[c] == '-' and m[c+1] == l):
                    yolo = len(m)
                    S2[count] = S2[count].replace('-'+S2[count][c+1],'')
                    if len(S2[count])<yolo:
                        break
                elif m[c] == l:
                    S2.remove(S2[count])
                    count-=1
        count+=1
    S = S2[:]
    if len(l) == 1:
        I[l]=1
    elif len(l)==2:
        I[l]=0
    
    #if DPLL(S2,I)== ("Satisfacible",I):
        #return "Satisfacible",I
    S,I = unitPropagate(S,I)
    if len(S)==0:
        return "Satisfacible" ,I
    else:
        S3 = S2[:]
        count = 0
        for m in S:
            S3[count] = m
            for c in range(len(m)):
                if m[c] not in I.keys():
                    if m[c] != '-':
                        l = m[c]
                        break
            break
        for m in S:
            S3[count] = m
            for c in range(len(m)):
                if len(l)==1:
                    if m[c] == l:
                        
                        yolo = len(m)
                        S3[count] = S3[count].replace(S3[count][c],'')
                        if len(S3[count])<yolo:
                            break
                    elif (m[c] == '-' and m[c+1] == l):
                        S3.remove(S3[count])
                        count-=1
                        break
                   
            count+=1
        S = S3[:]
        if len(l)==1:
            I[l]=0
        elif len(l)==2:

            I[l]=1
        return DPLL(S3,I)
    
def grafico(I):
    if I["a"] == 1 and I["b"] == 1:
        C1 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["a"] == 1 and I["d"] == 1:
        C1 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["b"] == 1 and I["c"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["b"] == 1 and I["e"] == 1:
        C1 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, bg = "red",width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["c"] == 1 and I["f"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["d"] == 1 and I["e"] == 1:
        C1 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["f"] == 1 and I["e"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

    if I["h"] == 1 and I["e"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
        
    if I["f"] == 1 and I["i"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["g"] == 1 and I["d"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
    
    if I["g"] == 1 and I["h"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 240)
        
    if I["i"] == 1 and I["h"] == 1:
        C1 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 0)
        C2 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 120, y = 0)
        C3 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 240, y = 0)
        C4 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 120)
        C5 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 120, y = 120)
        C6 = tk.Button(minas, bg = "red", width = 15, height = 7, relief ="groove").place(x = 240, y = 120)
        C7 = tk.Button(minas, width = 15, height = 7, relief ="groove").place(x = 0, y = 240)
        C8 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 120, y = 240)
        C9 = tk.Button(minas, text = "1", width = 15, height = 7, relief ="groove").place(x = 240, y = 240)

LetrasProposicionales = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "A", "B", "C", "D", "E", "F", "G", "H", "I"]

R1 = "i-h-g-f-e-d-c-baYYYYYYYY"
R2 = "i-h-g-f-e-c-b-daYYYYYYYY"
R3 = "i-h-g-f-d-c-a-ebYYYYYYYY"
R4 = "i-h-g-f-e-d-a-cbYYYYYYYY"
R5 = "i-h-g-e-d-b-a-fcYYYYYYYY"
R6 = "i-h-g-f-c-b-a-edYYYYYYYY"
R7 = "i-h-f-e-c-b-a-gdYYYYYYYY"
R8 = "i-h-g-d-c-b-a-feYYYYYYYY"
R9 = "i-g-f-d-c-b-a-heYYYYYYYY"
R10 = "h-g-e-d-c-b-a-ifYYYYYYYY"
R11 = "i-f-e-d-c-b-a-hgYYYYYYYY"
R12 = "g-f-e-d-c-b-a-ihYYYYYYYY"

RP1 = R1+R2+R3+R4+R5+R6+R7+R8+R9+R10+R11+R12+"OOOOOOOOOOO"

R13 = "EDObaY>"
R14 = "EBOdaY>"
R15 = "FDOCOAOebY>"
R16 = "FEOcbY>"
R17 = "EBOfcY>"
R18 = "HEOgdY>"
R19 = "HGOBOAOedY>"
R20 = "HEOifY>"
R21 = "FEOihY>"
R22 = "IHOCOBOfeY>"
R23 = "IGOFODOheY>"
R24 = "EDOhgY>"

RP2 = R13+R14+R15+R16+R17+R18+R19+R20+R21+R22+R23+R24+"YYYYYYYYYYY"

REGLA_FINAL = RP1+RP2+"Y"

formula_global = string2tree(REGLA_FINAL, LetrasProposicionales)

form = Inorder(formula_global)

tseitin = Tseitin(form, LetrasProposicionales)

causal = formaClausal(tseitin)


par = causal[:]

count= 0
for x in par:
    par[count] = ''
    for y in x:
        par[count]  = par[count] + y
    count+=1


dpll = DPLL(par, {})
print(dpll)


grafico(dpll[1])

"""
#interpretaciones_form = interpretaciones(LetrasProposicionales)
#interpretaciones_form_aux = []
#
#for i in interpretaciones_form:
#    aux = VI(formula_global, i)
#    if (aux == 1):
#        interpretaciones_form_aux.append(i)


#print(Inorder(formula_global))

#print(interpretaciones_form_aux)

"""
minas.mainloop()