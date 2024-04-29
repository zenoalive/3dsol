
from vpython import *
import numpy as np

Sun = sphere(radius=8, color=vector(0.8,0.2,0), pos= vector(0,0,0), texture = textures.stucco)
l0= label(pos=vector(0, 0, 0),
                            text='Sun', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=0.1,
                            font='sans' )
# rate of change in x position
delta=0.02

# Planets Attributes

# mercury
mxPos=0.0
mReal= 20.0
Mercury= sphere(radius=1, color=vector(0.5,0.5,0.5), pos= vector(0,0,mReal), make_trail= True, trail_type='points', texture = textures.rock)
l1= label(pos=vector(0, 0, 0),
                            text='Mercury', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=0.1,
                            font='sans')
p1=[Mercury,mxPos,mReal,mReal, delta,l1]

# venus
mvPos =0.0
mvreal= 30.0
Venus= sphere(radius=2, color=vector(0.6,0.2,0.3), pos= vector(0,0,mvreal),  make_trail= True, trail_type='points', texture = textures.wood)
l2= label(pos=vector(0, 0, 0),
                            text='Venus', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=0.1,
                            font='sans')
p2=[Venus,mvPos,mvreal,mvreal, delta, l2]

# earth
eloc =0.0
realeloc= 40.0
Earth= sphere(radius=2, color=vector(0.1,0.3,.7), pos= vector(0,0,realeloc), make_trail= True, trail_type='points', texture= textures.earth       )
l3= label(pos=vector(0, 0, 0),
                            text='Earth', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=4,
                            font='sans')
p3=[Earth,eloc,realeloc,realeloc, delta, l3]

# mars
maPos=0.0
realma=50.0
Mars= sphere(radius=1.5, color=vector(0.7,0.2,.1), pos= vector(0,0, realma), make_trail= True, trail_type='points', texture = textures.rock)
l4= label(pos=vector(0, 0, 0),
                            text='Mars', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=4,
                            font='sans')
p4=[Mars,maPos,realma,realma, delta, l4]

# jupiter
jaPos=0.0
realJup=70.0
Jupiter= sphere(radius=4, color=vector(0.7,0.5,0.2), pos= vector(0, 0, realJup), make_trail= True, trail_type='points', texture = textures.granite)
l5= label(pos=vector(0, 0, 0),
                            text='Jupiter', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=4,
                            font='sans')
p5=[Jupiter,jaPos,realJup,realJup, delta, l5]

# saturn
saPos=0.0
realSat=90.0
Saturn= sphere(radius=3.5, color=vector(0.5,0.5,0.9), pos= vector(0, 0, realSat), make_trail= True, trail_type='points', texture = textures.rough)
l6= label(pos=vector(0, 0, 0),
                            text='Saturn', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=4,
                            font='sans')
p6=[Saturn,saPos,realSat,realSat, delta, l6]

# saturn's ring
rex=cylinder(radius= 4, color= vector(0.8,0.1,0.1), length=.2, pos=vector(0, 0, realSat), rotate=vector(np.pi/2,np.pi/2,0), axis=vector(0,1,0.3), texture = textures.flower)

# uranus
urPos=0.0
realUr=110.0
Uranus= sphere(radius=2.9, color=vector(0.2,0.7,0.8), pos= vector(0, 0, realUr), make_trail= True, trail_type='points', texture = textures.gravel)
l7= label(pos=vector(0, 0, 0),
                            text='Uranus', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=4,
                            font='sans')
p7=[Uranus,urPos,realUr,realUr, delta, l7]

#neptune
nepPos=0.0
realNep=130.0
Neptune= sphere(radius=2.8, color=vector(0.3,0.3,0.9), pos= vector(0, 0, realNep), make_trail= True, trail_type='points', texture = textures.metal)
l8= label(pos=vector(0, 0, 0),
                            text='Neptune', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=4,
                            font='sans')
p8=[Neptune,nepPos,realNep,realNep, delta, l8]

# pluto
plPos=0.0
realPl=150.0
Pluto= sphere(radius=1, color=vector(0.9,0.9,0.8), pos= vector(0, 0, realPl), make_trail= True, trail_radius=0.2, trail_type='points', texture = textures.stones)
l9= label(pos=vector(0, 0, 0),
                            text='Pluto', xoffset=20,
                            yoffset=50, space=30,
                            height=16, border=4,
                            font='sans')
p9=[Pluto,plPos,realPl,realPl, delta, l9]
planets=[]
planets.append(p1)
planets.append(p2)
planets.append(p3)
planets.append(p4)
planets.append(p5)
planets.append(p6)
planets.append(p7)
planets.append(p8)
planets.append(p9)
rotation_rate = 0.005

while True:
    rate(100)
    for planet in planets:
            planet[0].rotate(angle=rotation_rate, axis=vector(0.25, 1, 0))
            planet[1]=planet[1]+planet[4]
            planet[2]=  np.sqrt(np.square(planet[3])-np.square(planet[1]))
                
            if planet[4]==(-.02):
                planet[2]=-planet[2]
            if(np.square(planet[1])+np.square(planet[2])==np.square(planet[3])):
                planet[0].pos = vector(planet[1], 0, planet[2])
                planet[5].pos= vector(planet[1],0,planet[2])
            
            if(planet[1]>=planet[3] or planet[1]<= -planet[3]):
                planet[4]=-planet[4]
            if(planet[0]==Saturn):
                rex.pos=vector(planet[1],0,planet[2])
                

