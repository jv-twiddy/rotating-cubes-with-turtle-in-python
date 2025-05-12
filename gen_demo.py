from generalisation import *
import turtle
import math
import random as r

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
t.speed(0)
pos_x = 0
pos_y = 0 
pos_z = 0
fe = 1 
# cube 
cube = {
    "coords3D" : [
  [pos_x-fe,pos_y-fe,pos_z-fe],
  [pos_x+fe,pos_y-fe,pos_z-fe],
  [pos_x+fe,pos_y+fe,pos_z-fe],
  [pos_x-fe,pos_y+fe,pos_z-fe],
  [pos_x-fe,pos_y-fe,pos_z+fe],
  [pos_x+fe,pos_y-fe,pos_z+fe],
  [pos_x+fe,pos_y+fe,pos_z+fe],
  [pos_x-fe,pos_y+fe,pos_z+fe]
  ],
    "connections":[0,1,2,3,0,3,7,6,5,4,0,1,5,6,2,6,7,4]
}

points3D = [
  [pos_x-fe,pos_y-fe,pos_z-fe],
  [pos_x+fe,pos_y-fe,pos_z-fe],
  [pos_x+fe,pos_y+fe,pos_z-fe],
  [pos_x-fe,pos_y+fe,pos_z-fe],
  [pos_x-fe,pos_y-fe,pos_z+fe],
  [pos_x+fe,pos_y-fe,pos_z+fe],
  [pos_x+fe,pos_y+fe,pos_z+fe],
  [pos_x-fe,pos_y+fe,pos_z+fe]
  ]
position = [0,0,0]
rotation = [10, 50, 10]
connections = [0,1,2,3,0,3,7,6,5,4,0,1,5,6,2,6,7,4]
scale = 100

axis6s = [position,rotation,scale]

t.up()
display_frame(t,cube["coords3D"],position, rotation, cube["connections"],scale)

axis6s[2] -= 50 
display_frame_s(t,cube,axis6s)

f = input("end>")