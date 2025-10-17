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
fe = 1 
# cube 
cube = {
    "coords3D" : [
  [-fe,-fe,-fe],
  [+fe,-fe,-fe],
  [+fe,+fe,-fe],
  [-fe,+fe,-fe],
  [-fe,-fe,+fe],
  [+fe,-fe,+fe],
  [+fe,+fe,+fe],
  [-fe,+fe,+fe]
  ],
    "connections":[0,1,2,3,0,3,7,6,5,4,0,1,5,6,2,6,7,4]
}

tetrahedron = {
  "coords3D":[
    [0,0,0.8819195201], # tip is that far from the base 
    [0,2/3,0],
    [1/2,-1/3,0],
    [-1/2,-1/3,0]
  ],
  "connections":[0,1,2,0,3,1,3,2]
}

points3D = [
  [-fe,-fe,-fe],
  [+fe,-fe,-fe],
  [+fe,+fe,-fe],
  [-fe,+fe,-fe],
  [-fe,-fe,+fe],
  [+fe,-fe,+fe],
  [+fe,+fe,+fe],
  [-fe,+fe,+fe]
  ]
position = [0,0,0]
rotation = [30, 50, 10]
connections = [0,1,2,3,0,3,7,6,5,4,0,1,5,6,2,6,7,4]
scale = 100

axis6s = [position,rotation,scale]

t.up()
# draw here:



# display_frame(t,cube["coords3D"],position, rotation, cube["connections"],scale)

# axis6s[2] -= 50 
display_frame_s(t,tetrahedron,axis6s)

f = input("end>")