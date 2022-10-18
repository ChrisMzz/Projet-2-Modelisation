from matplotlib.colors import ListedColormap
from projet2_01 import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib as mpl

def bezigon(p, cmp, tn, return_cn_list=False):
    coord = []
    cn_list = []
    for i in range(int(len(cmp)/p)+1):
        temp_c = cmp[p*i-i:p*(i+1)-i]
        cn_list.append(temp_c)
    if return_cn_list:
        return cn_list
    else:
        for cn in cn_list:
            coord.append(bezier(cn, tn))
        return coord



# Bézigons :
# ---------------------------------------------
    
# e dans la première partie
cn = [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3)]
cn += [(2,3), (1,3), (1,3), (1,2), (1,1), (1,1)]
cn += [(2,1), (3,1), (3,1), (3,1.5)]

# mu avec des bézigons p=5 :
# segment initial
cn = [(0.55,0.7),(0.55,0),(0.6,0.9),(0.65,1.8),(0.7,2.7)]
# courbe du milieu
cn += [(0.6,0.9),(0.8,0.8),(1,0.8),(1.1,2.6)]
# repli
cn += [(1,0.8),(1.13,1.5),(1.15,1.75),(1.15,2)]

# mu avec des bézigons p = 8
cn = [(0.55,0.7),(0.55,0),(0.575,0.45),(0.6,0.9),(0.625,1.35),(0.65,1.8),(0.675,2.35),(0.7,2.7)]
# courbe du milieu
cn += [(0.65,1.8),(0.675,1),(0.7,0.8),(0.9,0.8),(0.925,1),(1,1),(1.1,2.6)]
# repli
cn += [(1,1),(1.05,1.25),(1.11,1.25),(1.13,1.5),(1.14,1.675),(1.15,1.75),(1.15,2)]


# xi :
cn = [(6,10.5),(5,11),(4,10.5),(3.5,10.2),(3.5,9.8),(3.5,9),(4,8.5),(5,8),(6,8)]
cn += [(4,8),(3,6),(3,3),(3,1),(7,6),(7,4),(7,3),(6,2.5)]

# zeta : 
cn = [(3.8,10),(3,9.5),(3,8.5),(4.5,9),(4.5,10),(3.5,9),(4,8.5),(5,9),(6,9)]
cn += [(4,8.5),(3,9),(3,3),(3,1),(7,7),(7,4),(7,3),(6,2.5)]


# -------------------------------------------------------------


fig, ax = plt.subplots()

axins1 = inset_axes(ax, width='10%', height='2%', loc='lower right', bbox_to_anchor=(2.03,0.1,-1,2), bbox_transform=ax.transAxes)
axins2 = inset_axes(ax, width='10%', height='2%', loc='lower right', bbox_to_anchor=(2.03,0.05,-1,2), bbox_transform=ax.transAxes)




bezg = bezigon(9, cn, segment(1000))
cn = bezigon(9, cn, segment(1000), True)

cmap_bezg = ListedColormap([[0.5+0.5*i/len(bezg),0,1-0.7*i/len(bezg),1] for i in range(len(bezg))])
cmap_cn = ListedColormap([[0, 1-i/len(cn), 0,1] for i in range(len(cn))])


for i in range(len(cn)):
    ax.plot(extract(cn[i],0), extract(cn[i], 1), "-x", color=(0, 1-i/len(cn), 0))


for i in range(len(bezg)):
    x,y = extract(bezg[i],0), extract(bezg[i],1)
    ax.plot(x,y, color=(0.5+0.5*i/len(bezg),0,1-0.7*i/len(bezg)), label="courbe")
    
cbar1 = fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(5,10),cmap=cmap_bezg), cax=axins1, orientation='horizontal')
cbar2 = fig.colorbar(mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(5,10),cmap=cmap_cn), cax=axins2, orientation='horizontal')
cbar1.ax.set_xticklabels([])
cbar2.ax.set_xticklabels([])

ax.set_xlim((2,8))
ax.set_ylim((0,12))
fig.set_figheight(8)
fig.set_figwidth(5)

# --------------------------------------------------
"""
# no :
nocn = [(5.5,2.5),(7,4),(7,6),(2,6),(2,3),(5,0),(5,4.8)]

bez = bezier(nocn,segment(1000))
x,y = extract(bez,0), extract(bez,1)
fig.set_figheight(6)
fig.set_figwidth(5)
ax.plot(x,y,color=(0.6,0,1))
ax.plot(extract(nocn,0),extract(nocn,1),color=(1,0,0))
"""
# -------------------------------------------------

#fig.savefig("images-11/zeta.png", dpi=300, format="png")