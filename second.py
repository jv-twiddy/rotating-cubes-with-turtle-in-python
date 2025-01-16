
import turtle
import math

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

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



def cube():

  pos_x=int(input('x'))
  pos_y=int(input('y'))
  pos_z=int(input('z'))
  
  angle_a=int(input('angle_a:'))
  angle_ar=math.radians(angle_a)
  
  angle_b=int(input('angle_b:'))
  angle_br=math.radians(angle_b)
  
  angle_c=int(input('angle_c:'))
  angle_cr=math.radians(angle_c)
  
  
  angle=[angle_a,angle_b,angle_c]
  angler=[angle_ar,angle_br,angle_cr]
  
  A=[pos_x-20.0,pos_y-20.0,pos_z-20.0]
  B=[pos_x+20.0,pos_y-20.0,pos_z-20.0]
  C=[pos_x+20.0,pos_y+20.0,pos_z-20.0]
  D=[pos_x-20.0,pos_y+20.0,pos_z-20.0]
  E=[pos_x-20.0,pos_y-20.0,pos_z+20.0]
  F=[pos_x+20.0,pos_y-20.0,pos_z+20.0]
  G=[pos_x+20.0,pos_y+20.0,pos_z+20.0]
  H=[pos_x-20.0,pos_y+20.0,pos_z+20.0]
   
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


while True:
  cube()
  
x=input()