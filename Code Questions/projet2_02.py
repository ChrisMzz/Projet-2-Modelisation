#%%
from projet2_01 import*
from  math import*
import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation



# Pour e : 
cn = [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3)]
cn += [(2,3), (1,3), (1,3), (1,2), (1,1), (1,1)]
cn += [(2,1), (3,1), (3,1), (3,1.5)]
    

def get_cn(): # Pour retourner le cn original sans modifier la valeur du cn actuel
    return [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3), (2,3), (1,3), (1,3), (1,2), (1,1), (1,1), (1.8,2), (3,1), (3,1), (3,1.5)]

def reset(): # Pour reset le cn original
    global cn1
    global c8
    global cn2
    cn1 = [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3)]
    cn1 += [(2,3), (1,3), (1,3), (1,2), (1,1), (1,1)]
    c8 = [1.8,2]
    cn2 = [(3,1), (3,1), (3,1.5)]

plt.clf()
fig, ax = plt.subplots()
N = 40



def move(N):
    global cn1
    global c8
    global cn2
    reset()
    for k in range(N):
        c8[0] += 0.2/N
        c8[1] -= 1/N
        cn = cn1 + [(c8[0], c8[1])] + cn2
        x = extract(bezier(cn,segment(1000)), 0)
        y = extract(bezier(cn,segment(1000)), 1)
        ax.plot(extract(cn,0), extract(cn,1), "-x", color=(0.8 + 0.2*k/N, 0.8 - 0.2*k/N, 0.8 - 0.4*k/N))
    reset()
    cn = cn1 + [(c8[0], c8[1])] + cn2
    x = extract(bezier(cn,segment(1000)), 0)
    y = extract(bezier(cn,segment(1000)), 1)
    ax.plot(x,y, color="blue")
    ax.plot(extract(cn,0), extract(cn,1), color="blue")
    for k in range(N):
        c8[0] += 0.2/N
        c8[1] -= 1/N
        cn = cn1 + [(c8[0], c8[1])] + cn2
        x = extract(bezier(cn,segment(1000)), 0)
        y = extract(bezier(cn,segment(1000)), 1)    
        ax.plot(x,y, color=(0.5+0.3*k/N,0.3+0.6*k/N,1))
    ax.plot(extract(bezier(get_cn(),segment(1000)), 0),extract(bezier(get_cn(),segment(1000)), 1), color="blue")
    x = extract(bezier(cn,segment(1000)), 0)
    y = extract(bezier(cn,segment(1000)), 1)
    ax.plot(x,y, color="red")
    ax.plot(extract(cn,0), extract(cn,1), color="red")
    #fig.savefig("images-02/c8_modifié.png", dpi=300, format="png")

def swap(i):
    plt.clf()
    fig, ax = plt.subplots()
    cn = [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3)]
    cn += [(2,3), (1,3), (1,3), (1,2), (1,1), (1,1)]
    cn += [(2,1), (3,1), (3,1), (3,1.5)]
    x = extract(bezier(cn,segment(1000)), 0)
    y = extract(bezier(cn,segment(1000)), 1) 
    ax.plot(x,y, color=(0.8,0.8,0.8))
    temp = cn[i]
    cn[i] = cn[i+1]
    cn[i+1] = temp
    cs = [cn[i], cn[i+1]]
    x = extract(bezier(cn,segment(1000)), 0)
    y = extract(bezier(cn,segment(1000)), 1)    
    ax.plot(x,y, color=(0.4,0.2,1))
    ax.plot(extract(cn,0), extract(cn,1), "-x", color="b")
    ax.plot(extract(cs,0), extract(cs,1), "-x", color="r")
    #fig.savefig(f"images-02/swap/c{i}c{i+1}_échangés.png", dpi=300, format="png")


#move(30)

for i in range(len(cn)-1):
    swap(i)




