# Projet 2 de Modélisation

Voici une collection de tous les fichiers qu'on utilise pour étudider les courbes de Bézier et leurs liens avec la typographie moderne. 
Nous avons inclus en particulier nos recherches sur la création et personnalisation d'une police pour mettre nos recherches en application réelle.

## Les courbes de Bézier

Ce projet a pour but d'étudier le côté mathématique des [courbes de Bézier](https://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier) pour essayer d'en utiliser, 
et ainsi dessiner des figures, notamment des lettres, dans un cadre externe au projet.

### Le rapport
Un rapport LaTeX collaboratif a été écrit sur Overleaf pour détailler les observations et simulations faites, ainsi que les résultats théoriques obtenus.
Le rapport contient une majorité des graphiques exportés, sur lequel il s'appuie pour justifier des conjectures et/ou manipulations.


### Le code
Les fichiers utilisés pour mettre en application notre étude sont tous regroupés dans la section dédiée au code Code Questions. 

Les fichiers liés aux questions du sujet étudié sont libellés en fonction des numéros des questions traitées.

---

Les fonctions `bezier()` et `castljau()` renvoient des tableaux contenant les abscisses et ordonnées des points de la courbe de Bézier à chaque temps t d'un vecteur de discrétisation donné (qu'on formatte avec la fonction `segment()`), et on les représente sur des graphiques à l'aide du module `matplotlib` et d'une fonction `extract()` que l'on a écrite qui sépare les abscisses et ordonnées en deux listes distinctes :

```py
import matplotlib.pyplot as plt

def segment(n):
    return [i/n for i in range(n+1)]

# Au cas où on décide de passer une liste de points de contrôle en paramètres
def segmentc(cn):
    return segment(len(cn))

def bezier(cn, tn):
    n = len(cn)-1
    tempg = []
    for t in tn:
        gamma = Point()
        for k in range(n+1):
            ck = Point(cn[k]) # ck est un nombre de R x R (un Point)
            gamma += B(n,k,t)*ck
        tempg.append(tuple(gamma))
    return np.array(tempg)

def casteljau(cn, tn):
    tempd = []
    for t in tn:
        tempd.append(delta(cn, len(cn)-1, t))
    return np.array(tempd)

def extract(iter, pos):
    return [iter[i][pos] for i in range(len(iter))]
```

Le formattage des graphiques de `matplotlib` est très flexible, on peut profiter notamment de l'option de colorier les courbes en RGB pour pouvoir personnaliser les couleurs et tracer des dégradés : 

```py
def move(N):
    ...
    for k in range(N):
        c8[0] += 0.2/N
        c8[1] -= 1/N
        cn = cn1 + [(c8[0], c8[1])] + cn2
        x = extract(bezier(cn,segment(1000)), 0)
        y = extract(bezier(cn,segment(1000)), 1)    
        ax.plot(x,y, color=(0.5+0.3*k/N,0.3+0.6*k/N,1))
```

![](https://github.com/ChrisMzz/Projet-2-Modelisation/tree/main/Code%20Questions/images-02/c8_modifié.png)


Lors de la créations des Bézigons, on profite à nouveau de la flexibilité et du niveau de détail offert par `matplotlib` : 
```py
from matplotlib.colors import ListedColormap

cmap_bezg = ListedColormap([[0.5+0.5*i/len(bezg),0,1-0.7*i/len(bezg),1] for i in range(len(bezg))])
cmap_cn = ListedColormap([[0, 1-i/len(cn), 0,1] for i in range(len(cn))])
...
cbar1 = fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(5,10),cmap=cmap_bezg), cax=axins1, orientation='horizontal')
cbar2 = fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(5,10),cmap=cmap_cn), cax=axins2, orientation='horizontal')
cbar1.ax.set_xticklabels([])
cbar2.ax.set_xticklabels([])
```

---


## Le lien avec la typographie

On mettra cette étude théorique et à base de simulations en application en créant un caractère à la manière d'une police traditionnelle, justifiant avec des exemples réels.
Des constructions interactives par méthode de De Casteljau de ces lettres sont accessibles sur les pages suivantes :
 - [Construction du caractère の](https://www.geogebra.org/m/zmjjbupm)
 - [Construction du caractère ζ](https://www.geogebra.org/m/sqdbawpu)
 - [Construction du caractère ξ](https://www.geogebra.org/m/xpeuyn6q)
 

![](https://github.com/ChrisMzz/Projet-2-Modelisation/blob/main/Code%20Questions/images-11/xi.gif)

Nous avions commencé à créer un outil d'animation de la méthode de De Casteljau sur n'importe quel polygone de contrôle en décompressant les fichiers GeoGebra `.ggb`, en les regroupant individuellement dans des dossiers dont les noms commençaient par `ggb_` et en exécutant le script suivant :

```bat
@echo on
setlocal EnableExtensions EnableDelayedExpansion
for /D /r %%G in ("ggb_*") do (
    cd %%G
    for %%i in ("!%%G") do ren %%~ni.ggb %%~ni.zip
    cd ..
)
```

mais les fichiers qui contiennent les informations nécessaires sont encodés en `.xml` et il nous faudrait plus de temps pour écrire un fichier python qui puisse exporter des données sous formattage `xml`.

---


