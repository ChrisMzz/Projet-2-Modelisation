#%%
import numpy as np
from  math import*
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter




class Point:
    def __init__(self,iter=(0,0)):
        self.x = iter[0]
        self.y = iter[1]

    def __iadd__(self, other):
        return Point((self.x + other.x, self.y + other.y))
        
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
        
    def __radd__(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __mul__(self, other):
        return Point((self.x*other, self.y*other))

    def __rmul__(self, other):
        return Point((self.x*other, self.y*other))
        
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __iter__(self):
        for pos in (self.x,self.y):
            yield pos





def B(n, k, t):
    return (factorial(n))/(factorial(k)*factorial(n-k))*(t**k)*(1-t)**(n-k)

# print(B(4,3,0.7))
# donne la même chose que binomial(4,3)*(0.7)^3*(1-0.7)^(4-3) sur wolframalpha.com



def segment(n):
    return [i/n for i in range(n+1)]

# Au cas où on décide de passer une liste de points de contrôle en paramètres
def segmentc(cn):
    return segment(len(cn))


def extract(iter, pos):
    """
    Args:
        iter (list): liste de tuples
        pos (int): 0 ou 1
    Renvoie une liste des abscisses (pos=0) ou ordonnées (pos=1) des tuples de iter.
    """
    return [iter[i][pos] for i in range(len(iter))]






def bezier(cn, tn):
    """bezier(cn, tn) -> np.array contenant des 2-tuples (abscisse, ordonnée) des points de la courbe à un temps t (segmenté selon tn).

    Args:
        cn (list): liste de taille n de tuples c correspondant aux points de contrôle.
        tn (list): liste de taille n de nombres correspondant à la segmentation de [0,1].
            Utiliser la fonction segment(cn) ou segment(n) pour optimiser.

    Returns:
        numpy.ndarray: tableau des points de la courbe de Bézier
    """
    n = len(cn)-1
    tempg = []
    for t in tn:
        gamma = Point()
        for k in range(n+1):
            ck = Point(cn[k]) # ck est un nombre de R x R (un Point)
            gamma += B(n,k,t)*ck
        tempg.append(tuple(gamma))
    return np.array(tempg)







#Exemple juste pour tester la fonctionnalité
#cn = [(i,j) for i in range(11) for j in range(11)]


# Pour e : 
cn = [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3)]
cn += [(2,3), (1,3), (1,3), (1,2), (1,1), (1,1)]
cn += [(2,1), (3,1), (3,1), (3,1.5)]

# Pour U :
#cn = [(1,8),(1,0),(1.1,-0.5),(3.9,-0.5),(4,0),(4,8)]

# Pour faire autre chose : 
#cn =
#cn = [(np.random.randint(0,10),np.random.randint(0,10)) for i in range(11) for j in range(11)]


x, y = extract(bezier(cn,segment(1000)), 0), extract(bezier(cn,segment(1000)), 1)

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
fig.set_figheight(4)
fig.set_figwidth(5)

#ax.plot(extract(cn,0), extract(cn,1), "b-x")
#ax.plot(x,y, color=(0.8,0,1))
#fig.savefig("images-01/autre.png", dpi=300, format="png")









# %%
