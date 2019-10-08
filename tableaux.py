from random import choice

##############################################################################
# Definicion de objeto tree y funciones
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def StringtoTree(A, letrasProposicionales):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            formulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
            formulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
    return pila[-1]

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def imprime_hoja(H):
	cadena = "["
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "]"

def imprime_tableau(tableau):
	primero = True
	for H in tableau:
		if primero == True:
			cadena = '[' + imprime_hoja(H)
			primero = False
		else:
		    cadena += ", " + imprime_hoja(H)
	return cadena + "]"
         


        
        

def literal(H):
    for f in H:
        if f.right == None:
            return True
        elif f.label =='-':
            if f.right.right==None:
                return True
            else:
                return False
        else:
            return False
        
    
    


letrasProposicionales = ['p', 'q','a','z','y','v','t','x','u','s','r']
P = StringtoTree('p', letrasProposicionales)
Q = StringtoTree('q', letrasProposicionales)
S= StringtoTree('p--',letrasProposicionales)
T= StringtoTree('q-',letrasProposicionales)
A = StringtoTree('qp>-', letrasProposicionales)
B = StringtoTree('aYzyOOvt-Ox-u>Osr>qpOOOO-', letrasProposicionales)
t = [[Q, A], [B, P]]

x = [P,Q]
y = [P,Q,S]
Z = [P,Q,S,T]





print(imprime_tableau(B))
#print(imprime_hoja(prue))
#print(literal(prue))
#print(tiene_par(x))