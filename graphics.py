#!/usr/bin/python

# Multiplication table on points of circle
# Nature's patterns
# crysanthus@gmail.com
# 16/7/2019

from graphics import *  # depends Tkinter / tkinter
import math
import time

winsz = 700  # size of the window
sx, sy, cx, cy = winsz, winsz, winsz/2, winsz/2
r = int((winsz/2)-10)  # radius of circle
npts = 360  # points on circle
maxtbl = 100  # multiplication tables from 0 ... ?
pt = []  # to hold Points table on circle

win = GraphWin('Multiplication Table Points On Circle', sx, sy)

# radius
Text(Point(15, 20), "Enter Radius -").draw(win)
ier = Entry(Point(110, 20), 5)
ier.setText(r)
ier.draw(win)

# nos points on circle
Text(Point(225, 20), "Nos Points -").draw(win)
iep = Entry(Point(300, 20), 5)
iep.setText(npts)
iep.draw(win)

# table
Text(Point(400, 20), "Table -").draw(win)
iet = Entry(Point(475, 20), 5)
iet.setText(maxtbl)
iet.draw(win)

Text(Point(168, 50), "Fill params, Click mouse on window to start ...").draw(win)

win.getMouse()

# read all 3 inputs
r = int(ier.getText())
npts = int(iep.getText())
maxtbl = int(iet.getText())+1

win.close()  # close input window

# generate points on circle
for x in range(0, npts):
 pt.append(Point((math.cos(2*math.pi/npts*x)*r)+cx, (math.sin(2*math.pi/npts*x)*r)+cy))
 
# table
for tbl in range(0, maxtbl):
 
 win = GraphWin('Multiplication Table Points On Circle x' + str(tbl), sx, sy, autoflush=False)
 
 # draw lines from point to point
 for i in range(0, npts):
  loc = tbl*i if (tbl*i) < npts else (tbl*i)-npts*int((tbl*i/npts))
  ln = Line(pt[i], pt[loc])
  
  color = "red" if i % 3 == 0 else 'blue' if i % 2 == 0 else 'green'
  ln.setOutline(color)
  ln.draw(win)
  
  akey = win.checkKey()
  if akey == "Escape":
   break
 
 update()
 time.sleep(1)
 win.close()
 
 if akey == "Escape":
  break
# EOF
