from projet2_01 import *


def center_of_gravity(cn):
    temp = Point()
    for c in cn:
        temp += Point(c)
    return Point((temp.x/len(cn), temp.y/len(cn)))


def rotation(cn, rot_angle):
    new_coord_list = []
    for coord in cn:
        x,y = coord
        r = sqrt(x**2 + y**2)
        angle = atan(y/x)
        new_coord = (r*cos(angle + rot_angle), r*sin(angle + rot_angle))
        new_coord_list.append(new_coord)
    return new_coord_list

def translation(cn,vec):
    new_coord_list = []
    for coord in cn:
        new_coord_list.append(tuple(Point(coord) + Point(vec)))
    return new_coord_list
    
def dilatation(cn,factor):
    new_coord_list = []
    for coord in cn:
        new_coord_list.append(tuple(factor*Point(coord)))
    return new_coord_list

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

#U
cn = [(1,8),(1,0),(1.1,-0.5),(3.9,-0.5),(4,0),(4,8)]

#e
cn = [(1,2), (2,2), (2,2), (3,2), (3,3), (3,3)]
cn += [(2,3), (1,3), (1,3), (1,2), (1,1), (1,1)]
cn += [(2,1), (3,1), (3,1), (3,1.5)]

print(center_of_gravity(cn))


#bez = bezier(cn, segment(1000))
x,y = extract(bez, 0), extract(bez, 1)
ax.plot(extract(cn, 0), extract(cn, 1), "c-x")
ax.plot(x, y, color=(0.8,0,1))


# Translation de e :
#cn = translation(cn,(0,-1))


# Rotation de U :
#cn = rotation(cn, -pi/2)
# Pour conserver la position : 
#centre = center_of_gravity(cn)
#cn = translation(cn, -centre)
#cn = rotation(cn, -pi/2)
#cn = translation(cn, centre)


# Dilatation de e :
#cn = dilatation(cn, 3)
# Pour conserver la position : 
#centre = center_of_gravity(cn)
#cn = translation(cn, -centre)
#cn = dilatation(cn, 3)
#cn = translation(cn, centre)



bez = bezier(cn, segment(1000))
x,y = extract(bez, 0), extract(bez, 1)



fig.set_figheight(6)
fig.set_figwidth(5)


ax.plot(extract(cn, 0), extract(cn, 1), "r-x")
ax.plot(x, y, color=(0.2,0.7,1))
#fig.savefig("images-09/e_dilaté.png", dpi=300, format="png")