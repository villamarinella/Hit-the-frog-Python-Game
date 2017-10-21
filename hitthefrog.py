from Tkinter import *
from PIL import ImageTk, Image
import os
import sys
import subprocess
import time
import random
import thread

sound=True  ## for Linux, for Windows you have to change th code in applaus()

wait3=1 ## sec game speed

path1 = "frog1.jpg"
path2 = "water.jpg"
path3 = "frog0.jpg"
ziel=1
zaehler=0
treffer=0
nummer=1
xrow=1
xcol=1
xwert=1
yrow=1
ycol=1
wait1=1000
wait2=2000
los=True
root = Tk()
e = Entry(root)

img1= ImageTk.PhotoImage(Image.open(path1))
img2 = ImageTk.PhotoImage(Image.open(path2))
img3 = ImageTk.PhotoImage(Image.open(path3))
pos=['00','01','02','03','04','11','12','13','14','21','22','23','24','31','32','33','34']

def zufall():
  global yrow,ycol,ziel
  for x in range(1):
      ziel = random.randint(1,16)
      xwert=pos[ziel]
      yrow=int(xwert[0])
      ycol=int(xwert[1])

def applaus():
    if sound:
        output = subprocess.Popen("aplay ap.wav",shell=True)
    
    
def write_slogan(x):
    global zaehler,treffer
    zaehler=zaehler+1
    xl = len(x)
    if xl == 4:
        nummer=x[:2]
        xrow=x[2]
        xcol=x[3]
    else:
        nummer=x[0]
        xrow=x[1]
        xcol=x[2]
    if nummer == str(ziel):
        treffer =treffer+1
        trefferbutton()
        applaus()
        e.after(wait1, lambda: zeigalles())
        zufall()
        e.after(wait2, lambda: zielbutton())
    else:
        e.after(wait1, lambda: zeigalles())
        zufall()
        e.after(wait2, lambda: zielbutton())

def zeigalles():
    MyButton1 = Button(root, image=img2, width=150, command=lambda: write_slogan('101'))
    MyButton1.grid(row=0, column=1)
    MyButton2 = Button(root, image=img2, width=150, command=lambda: write_slogan('202'))
    MyButton2.grid(row=0, column=2)
    MyButton3 = Button(root, image=img2, width=150, command=lambda: write_slogan('303'))
    MyButton3.grid(row=0, column=3)
    MyButton4 = Button(root, image=img2, width=150, command=lambda: write_slogan('404'))
    MyButton4.grid(row=0, column=4)
    
    MyButton5 = Button(root, image=img2, width=150, command=lambda: write_slogan('511'))
    MyButton5.grid(row=1, column=1)
    MyButton6 = Button(root, image=img2, width=150, command=lambda: write_slogan('612'))
    MyButton6.grid(row=1, column=2)
    MyButton7 = Button(root, image=img2, width=150, command=lambda: write_slogan('713'))
    MyButton7.grid(row=1, column=3)
    MyButton8 = Button(root, image=img2, width=150, command=lambda: write_slogan('814'))
    MyButton8.grid(row=1, column=4)
    
    MyButton9 = Button(root, image=img2, width=150, command=lambda: write_slogan('921'))
    MyButton9.grid(row=2, column=1)
    MyButton10 = Button(root, image=img2, width=150, command=lambda: write_slogan('1022'))
    MyButton10.grid(row=2, column=2)
    MyButton11 = Button(root, image=img2, width=150, command=lambda: write_slogan('1123'))
    MyButton11.grid(row=2, column=3)
    MyButton12= Button(root, image=img2, width=150, command=lambda: write_slogan('1224'))
    MyButton12.grid(row=2, column=4)
    
  
    MyButton13 = Button(root, image=img2, width=150, command=lambda: write_slogan('1331'))
    MyButton13.grid(row=3, column=1)
    MyButton14 = Button(root, image=img2, width=150, command=lambda: write_slogan('1432'))
    MyButton14.grid(row=3, column=2)
    MyButton15 = Button(root, image=img2, width=150, command=lambda: write_slogan('1533'))
    MyButton15.grid(row=3, column=3)
    MyButton16 = Button(root, image=img2, width=150, command=lambda: write_slogan('1634'))
    MyButton16.grid(row=3, column=4)
    
def zielbutton():
    
    MyButtonziel = Button(root, image=img1, width=150, command=  lambda: write_slogan(str(ziel)+str(yrow)+str(ycol)))
    MyButtonziel.grid(row=yrow, column=ycol)
    
def trefferbutton():
    
    MyButtontreffer = Button(root, image=img3, width=150, command=lambda: write_slogan(str(ziel)+str(yrow)+str(ycol)))
    MyButtontreffer.grid(row=yrow, column=ycol)
   
def leerbutton():
   
    MyButtonwater = Button(root, image=img2, width=150, command=lambda: write_slogan(str(ziel)+str(yrow)+str(ycol)))
    MyButtonwater.grid(row=yrow, column=ycol)
   
def endless():
    aq=1
    while True:
        aq+=1
        #print aq
        Label(text="Zaehler: "+str(zaehler),font="Helvetica"+'16').grid(row=4,column=1)
        Label(text="Treffer: "+str(treffer),font="Helvetica"+'16',).grid(row=4,column=2)
        leerbutton()
        zufall()
        time.sleep(wait3)
        zielbutton()
        time.sleep(wait3)
 

def go():
    thread.start_new_thread(endless,()) 

zeigalles()
zufall()
zielbutton()

go()
root.geometry("620x700")
root.configure(background='white')
root.mainloop()
