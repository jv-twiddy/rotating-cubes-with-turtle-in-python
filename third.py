
import turtle
import math
import random as r
# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
t.speed(0)

def rotation(a,b,angli):    # rotates the point around one axis 
  
  
  hypo=math.sqrt(a**2+b**2) # turns 2d co-ordinate into polar co-ord
  if a==0 and b==0:
    pheta=angli
  elif a==0 and b>0: 
    pheta=math.pi/2 + angli 
  elif a==0 and b<0:
    pheta=math.pi*1.5 +angli
  elif a<0:
    pheta=math.atan(b/a)+angli+math.pi
  else:
    pheta=math.atan(b/a)+angli      # adds the angle to rotate by 
  
  
  x=hypo*math.cos(pheta)       # turns the polar co-ordinate 
  
  y=hypo*math.sin(pheta)

  return(x,y)

def translate(point,angler):

  midway=rotation(point[0],point[2],angler[0])         # as a wise man once said just do it 3 times
  point[0]=midway[0]                                   # just for each axes/plane 
  point[2]=midway[1]
  
  midway=rotation(point[1],point[2],angler[1])
  point[1]=midway[0]
  point[2]=midway[1]
  
  midway=rotation(point[0],point[1],angler[2])
  point[0]=midway[0]
  point[1]=midway[1]
  
  point_x=point[0]
  point_y=point[1]

  return (point_x,point_y)

x_it=0
y_it=0
z_it=0

a_it=45
b_it=45
c_it=0
g=0 
m=0
fe=0


def cube():
  
  global x_it
  global y_it
  global z_it
  
  global a_it
  global b_it
  global c_it 
  global g 
  global fe
  global m
  
  pos_x=x_it 
  pos_y=y_it
  pos_z=z_it
  
  angle_a=a_it
  angle_ar=math.radians(angle_a)
  
  angle_b=b_it
  angle_br=math.radians(angle_b)
  
  angle_c=c_it
  angle_cr=math.radians(angle_c)
  
  
  angle=[angle_a,angle_b,angle_c]
  angler=[angle_ar,angle_br,angle_cr]
  
  A=[pos_x-fe,pos_y-fe,pos_z-fe]
  B=[pos_x+fe,pos_y-fe,pos_z-fe]
  C=[pos_x+fe,pos_y+fe,pos_z-fe]
  D=[pos_x-fe,pos_y+fe,pos_z-fe]
  E=[pos_x-fe,pos_y-fe,pos_z+fe]
  F=[pos_x+fe,pos_y-fe,pos_z+fe]
  G=[pos_x+fe,pos_y+fe,pos_z+fe]
  H=[pos_x-fe,pos_y+fe,pos_z+fe]
   
  A2=translate(A,angler)
  B2=translate(B,angler)
  C2=translate(C,angler)
  D2=translate(D,angler)
  E2=translate(E,angler)
  F2=translate(F,angler)
  G2=translate(G,angler)
  H2=translate(H,angler)
  
  print(A2,B2,C2,D2,E2,F2,G2,H2)
  t.up()
  t.goto(A2[0],A2[1])
  t.down()
  t.goto(B2[0],B2[1])
  t.goto(C2[0],C2[1])
  t.goto(D2[0],D2[1])
  t.goto(A2[0],A2[1])
  t.goto(D2[0],D2[1])
  t.goto(H2[0],H2[1])
  t.goto(G2[0],G2[1])
  t.goto(F2[0],F2[1])
  t.goto(E2[0],E2[1])
  t.goto(A2[0],A2[1])
  t.goto(B2[0],B2[1])
  t.goto(F2[0],F2[1])
  t.goto(G2[0],G2[1])
  t.goto(C2[0],C2[1])
  t.goto(G2[0],G2[1])
  t.goto(H2[0],H2[1])
  t.goto(E2[0],E2[1])
  
  m=100*math.atan(g)
  x_it+=5
  y_it+=0
  z_it+=0

  a_it+=0
  b_it+=0
  c_it+=10

  g+=0.06
  fe=30*math.atan(g)
while True:
  cube()
  