#%%
from projet2_01 import*
import numpy as np



# Matrice originale : trace une lettre alpha
C = np.array([[1,0,0,1],[1,-2,3,0]])

# La matrice intermédiaire ; sans ajout du point de contrôle de compensation
#C = np.array([[1,0,0,0.8,1],[1,-2,3,-0.3,0.3]])

# La matrice que j'ai trouvée en ajoutant et modifiant les points de contrôle
C = np.array([[1,0,0,0.8,0.8,1],[1,-2,3,1.5,-0.3,0.3]])




# Extrait les ci de la matrice C donnée
cn = [tuple(C[:,i]) for i in range(len(C[1]))]




x,y = extract(bezier(cn,segment(1000)),0), extract(bezier(cn,segment(1000)),1)

fig, ax = plt.subplots()


fig.set_figheight(10)
fig.set_figwidth(5)
ax.plot(extract(cn,0), extract(cn,1), "b-x")
ax.plot(x,y, color=(0.8,0,1))


fig.savefig("images-08/alpha_arrondi_02.png",dpi=300, format="png")




# %%
