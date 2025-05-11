import turtle
import math
import random as r
# here we will try and make a callable function that can run the 

def rotation(a,b,angli):    # rotates the point around one axis 
  
  
  hypo=math.sqrt(a**2+b**2) # turns 2d co-ordinate into polar co-ord 
  if a==0 and b==0:
    pheta=angli
  elif a==0 and b>0: 
    pheta=math.pi/2 + angli     # idk what maths i am doing here tbf. 
  elif a==0 and b<0:
    pheta=math.pi*1.5 +angli    # probably trying to account for the old if a = 0 problem 
  elif a<0:
    pheta=math.atan(b/a)+angli+math.pi # because we are using a to divide b here, math problems 
  else:
    pheta=math.atan(b/a)+angli      # adds the angle to rotate by 
  
  
  x=hypo*math.cos(pheta)       # turns the polar co-ordinate 
  
  y=hypo*math.sin(pheta)

  return(x,y)

def translate(point,angler): # makes a 2d coord after rotating it 3 times

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

def rotate3D(point, angler):
    
  midway=rotation(point[0],point[2],angler[0])         # as a wise man once said just do it 3 times
  point[0]=midway[0]                                   # just for each axes/plane 
  point[2]=midway[1]
  
  midway=rotation(point[1],point[2],angler[1])
  point[1]=midway[0]
  point[2]=midway[1]
  
  midway=rotation(point[0],point[1],angler[2])
  point[0]=midway[0]
  point[1]=midway[1]
  
  return point
  
def display_frame(t,coords3D, position, rotation, connections,scale=1):
    # scale all the coords first 
    points2D = []
    # we need to rotate rotate 
    for x in range(len(coords3D)): 
        a = coords3D[x]
        # scale it
        scaled = [a[0]*scale,a[1]*scale,a[2]*scale]
        #rotate it 
        rotated = rotate3D(scaled,rotation)
        # reposition it  
        c = rotated
        d = [c[0]+position[0],c[1]+position[1],c[2]+position[2]]
        coords3D[x] = d
        points2D.append([d[0],d[1]])
    
    # then we draw it 
    start = True
    for x in connections:
        t.goto(points2D[x])
        if start:
            t.down()
            start = False
    
    t.up()
    
    