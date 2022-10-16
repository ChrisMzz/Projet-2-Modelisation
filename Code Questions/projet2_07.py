#%%
from functools import lru_cache
import time
from projet2_01 import*
from  math import*
import matplotlib.pyplot as plt


# Pour e : 
cn = [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3)]
cn += [(2,3), (1,3), (1,3), (1,2), (1,1), (1,1)]
cn += [(2,1), (3,1), (3,1), (3,1.5)]








# Méthode de De Casteljau

@lru_cache
def c(cn, i, m, t):
    """c_i^m(t) : Calcule le point entre cn[i] et cn[i+1] en fonction de t

    Args:
        cn (tuple): tuple des tuples correspondant aux points de contrôle
        cn doit être un tuple pour faire fonctionner lru_cache
        i (int)
        m (int)
        t (float)

    Returns:
        tuple: point entre c[i] et c[i+1] en fonction de t
    """
    if m == 1:
        return (1-t)*Point(cn[i]) + t*Point(cn[i+1])
    else:
        return (1-t)*c(cn, i, m-1, t) + t*c(cn, i+1, m-1, t)
    
def delta(cn, n, t):
    return tuple(c(tuple(cn), 0, n, t))

def casteljau(cn, tn):
    """casteljau(cn,tn) -> np.array contenant des 2-tuples correspondants aux points pour un temps t de la courbe de Bézier

    Args:
        cn (list): liste de tuples correspondant aux points de contrôle
        tn (list): liste correspondant à une discrétisation du segment [0,1]
            Utiliser la fonction segment(cn) ou segment(n) pour optimiser.

    Returns:
        numpy.ndarray: tableau des points de la courbe de Bézier
    """
    tempd = []
    for t in tn:
        tempd.append(delta(cn, len(cn)-1, t))
    return np.array(tempd)












# On réutilisera les mêmes fonctions pour discrétiser un segment de [0,1] et tracer les courbes
tn = segment(1000)


# Méthode de Casteljau

start_time = time.time() # Pour comparer avec et sans lru_cache

castel = casteljau(cn, tn) # Pour ne pas faire tourner la fonction deux fois
x,y = extract(castel,0), extract(castel,1)

print(f"--- {(time.time() - start_time)} secondes ---")


# Méthode avec polynôme de Bernstein
#bez = bezier(cn,tn)
#x, y = extract(bez, 0), extract(bez, 1)



fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
fig.set_figheight(4)
fig.set_figwidth(5)

ax.plot(x,y, color=(0.8,0,1))

fig.savefig("images-07/casteljau.png", dpi=300, format="png")



    

    






# %%
