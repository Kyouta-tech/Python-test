
#Imports
import shutil as s
import math as m
from tkinter import *;
from PIL import ImageTk,Image
import os
import tkinter as tk
from tkinter import messagebox as mb



#Title
root = Tk()
root.title('Ohms Law Calculator')
root.iconbitmap('c:/Pythonfiles/ohms.ico')



#Frames
FrameHome = LabelFrame(root, text = "Welcome To Ohms Law Calculator", padx = 5, pady = 5, width = 1920, height = 1080)

FrameHome2 = LabelFrame(root, text = "What Do You Want To Compute?", padx = 5, pady = 5, width = 1920, height = 1080)

FrameVoltage = LabelFrame(root, text = "Solving for Voltage", padx = 5, pady = 5, width = 1920, height = 1080)
FramePowerandOhmsV = LabelFrame(root, text = "Solving for Voltage ", padx = 5, pady = 5, width = 1920, height = 1080)
FramePowerandCurrentV = LabelFrame(root, text = "Solving for Voltage.", padx = 5, pady = 5, width = 1920, height = 1080)
FrameCurrentandOhmsV = LabelFrame(root, text = "Solving for Voltage", padx = 5, pady = 5, width = 1920, height = 1080)

FrameCurrent = LabelFrame(root, text = "Solving for Current", padx = 5, pady = 5, width = 1920, height = 1080)
FramePowerandOhmsC = LabelFrame(root, text = "Solving for Current", padx = 5, pady = 5, width = 1920, height = 1080)
FramePowerandVoltageC = LabelFrame(root, text = "Solving for Current", padx = 5, pady = 5, width = 1920, height = 1080)
FrameVoltageandOhmsC = LabelFrame(root, text = "Solving for Current", padx = 5, pady = 5, width = 1920, height = 1080)

FramePower = LabelFrame(root, text = "Solving for Power", padx = 5, pady = 5, width = 1920, height = 1080)
FrameVoltageandCurrentP = LabelFrame(root, text = "Solving for Power", padx = 5, pady = 5, width = 1920, height = 1080)
FrameCurrentandOhmsP = LabelFrame(root, text = "Solving for Power", padx = 5, pady = 5, width = 1920, height = 1080)
FrameVoltageandOhmsP = LabelFrame(root, text = "Solving for Power", padx = 5, pady = 5, width = 1920, height = 1080)

FrameOhms = LabelFrame(root, text = "Solving for Ohms", padx = 5, pady = 5, width = 1920, height = 1080)
FrameVoltageandCurrentR = LabelFrame(root, text = "Solving for Ohms", padx = 5, pady = 5, width = 1920, height = 1080)
FrameVoltageandPowerR = LabelFrame(root, text = "Solving for Ohms", padx = 5, pady = 5, width = 1920, height = 1080)
FramePowerandCurrentR = LabelFrame(root, text = "Solving for Ohms", padx = 5, pady = 5, width = 1920, height = 1080)



#bg
#cz1 = ImageTk.PhotoImage(Image.open("c:/Pythonfiles/Apply/Main.png"))
#cv1= Canvas(FrameHome,width = 500, height = 500)
#cv1.place(x = 0, y = 0)
#cv1.create_image(0,0,image=cz1)




#FramePacks
FrameHome.pack(padx = 10,pady = 10)








#Defines
#CALC DEFINE
	#CALC 1
def re(number):
    current = a.get()
    a.delete(0, END)
    a.insert(0,str(current) + str(number))
def ro():
    a.delete(0,END)
def rex(number):
    current = en.get()
    en.delete(0, END)
    en.insert(0,str(current) + str(number))
def rox():
    en.delete(0,END)
def dd():
	current = en.get()
	en.insert(END,("."))
def ddx():
	current = a.get()
	a.insert(END,".")
def Enter1x():
	try:
		pax = float(en.get())
		pax1 = float(a.get())
		lol = pax * pax1
		lol1 = m.sqrt(lol)
		lol2 = str(lol1)
		lol3 = "{:.2f}".format(lol1)
		mox = Button(FramePowerandOhmsV,text = lol3+" Volts",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")



	#CALC 2
def re1(number):
    current1 = a1.get()
    a1.delete(0, END)
    a1.insert(0,str(current1) + str(number))
def ro1():
    a1.delete(0,END)
def rex1(number):
    current1 = en1.get()
    en1.delete(0, END)
    en1.insert(0,str(current1) + str(number))
def rox1():
    en1.delete(0,END)
def dd1():
	current1 = en1.get()
	en1.insert(END,("."))
def ddx1():
	current1 = a1.get()
	a1.insert(END,".")
def Enter2x():
	try:
		pax1 = float(en1.get())
		pax11 = float(a1.get())
		
		lol11 = pax11 / pax1
		lol21 = str(lol11)
		lol31 = "{:.2f}".format(lol11)
		mox1 = Button(FramePowerandCurrentV,text = lol31+" Volts",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox1.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")



	#CALC 3
def re11(number):
    current11 = a11.get()
    a11.delete(0, END)
    a11.insert(0,str(current11) + str(number))
def ro11():
    a11.delete(0,END)
def rex11(number):
    current11 = en11.get()
    en11.delete(0, END)
    en11.insert(0,str(current11) + str(number))
def rox11():
    en11.delete(0,END)
def dd11():
	current11 = en11.get()
	en11.insert(END,("."))
def ddx11():
	current11 = a11.get()
	a11.insert(END,".")
def Enter3x():
	try:
		pax111 = float(a11.get())
		pax11 = float(en11.get())
		
		lol111 = pax111 * pax11
		lol211 = str(lol111)
		lol311 = "{:.2f}".format(lol111)
		mox11 = Button(FrameCurrentandOhmsV,text = lol311+" Volts",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox11.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")


#CURR1
def re111(number):
    current111 = a111.get()
    a111.delete(0, END)
    a111.insert(0,str(current111) + str(number))
def ro111():
    a111.delete(0,END)
def rex111(number):
    current111 = en111.get()
    en111.delete(0, END)
    en111.insert(0,str(current111) + str(number))
def rox111():
    en111.delete(0,END)
def dd111():
	current111 = en111.get()
	en111.insert(END,("."))
def ddx111():
	current111 = a111.get()
	a111.insert(END,".")
def Enter4x():
	try:
		pax1111 = float(a111.get())
		pax111 = float(en111.get())
		lol222 = pax1111 / pax111
		lol1111 = m.sqrt(lol222)
		lol2111 = str(lol1111)
		lol3111 = "{:.2f}".format(lol1111)
		mox111 = Button(FramePowerandOhmsC,text = lol3111+" Amperes",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")

#CURR2
def re1111(number):
    current1111 = a1111.get()
    a1111.delete(0, END)
    a1111.insert(0,str(current1111) + str(number))
def ro1111():
    a1111.delete(0,END)
def rex1111(number):
    current1111 = en1111.get()
    en1111.delete(0, END)
    en1111.insert(0,str(current1111) + str(number))
def rox1111():
    en1111.delete(0,END)
def dd1111():
	current1111 = en1111.get()
	en1111.insert(END,("."))
def ddx1111():
	current1111 = a1111.get()
	a1111.insert(END,".")
def Enter5x():
	try:
		pax11111 = float(a1111.get())
		pax1111 = float(en1111.get())
		lol11111 = pax11111 / pax1111
		lol21111 = str(lol11111)
		lol31111 = "{:.2f}".format(lol11111)
		mox1111 = Button(FramePowerandVoltageC,text = lol31111+" Amperes",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox1111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")

#CURR3
def rx1(number):
    gax = awx.get()
    awx.delete(0, END)
    awx.insert(0,str(gax) + str(number))
def rx2():
    awx.delete(0,END)
def rxx1(number):
    gax = ens.get()
    ens.delete(0, END)
    ens.insert(0,str(gax) + str(number))
def rxx2():
    ens.delete(0,END)
def rxx3():
	gax = ens.get()
	ens.insert(END,("."))
def rx3():
	gax = awx.get()
	awx.insert(END,".")
def Enter6x():
	try:
		pisu1 = float(awx.get())
		pisu2 = float(ens.get())
		abs1 = pisu1 / pisu2
		abs2 = str(abs1)
		abs3 = "{:.2f}".format(abs1)
		mox11111 = Button(FrameVoltageandOhmsC,text = abs3+" Amperes",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox11111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")


#power1
def rx11(number):
    gax1 = awx1.get()
    awx1.delete(0, END)
    awx1.insert(0,str(gax1) + str(number))
def rx21():
    awx1.delete(0,END)
def rxx11(number):
    gax1 = ens1.get()
    ens1.delete(0, END)
    ens1.insert(0,str(gax1) + str(number))
def rxx21():
    ens1.delete(0,END)
def rxx31():
	gax1 = ens1.get()
	ens1.insert(END,("."))
def rx31():
	gax1 = awx1.get()
	awx1.insert(END,".")
def Enter7x():
	try:
		pisu11 = float(awx1.get())
		pisu21 = float(ens1.get())
		abs11 = pisu11 * pisu21
		abs21 = str(abs11)
		abs31 = "{:.2f}".format(abs11)
		mox111111 = Button(FrameVoltageandCurrentP,text = abs31+" Watts",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox111111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")


#Power2
def rx111(number):
    gax11 = awx11.get()
    awx11.delete(0, END)
    awx11.insert(0,str(gax11) + str(number))
def rx211():
    awx11.delete(0,END)
def rxx111(number):
    gax11 = ens11.get()
    ens11.delete(0, END)
    ens11.insert(0,str(gax11) + str(number))
def rxx211():
    ens11.delete(0,END)
def rxx311():
	gax11 = ens11.get()
	ens11.insert(END,("."))
def rx311():
	gax11 = awx11.get()
	awx11.insert(END,".")
def Enter8x():
	try:
		pisu111 = float(awx11.get())
		pisu211 = float(ens11.get())
		abm = pisu111 * pisu111
		abs111 = abm * pisu211
		abs211 = str(abs111)
		abs311 = "{:.2f}".format(abs111)
		mox1111111 = Button(FrameCurrentandOhmsP,text = abs311+" Watts",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox1111111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")

#power3
def rx1111(number):
    gax111 = awx111.get()
    awx111.delete(0, END)
    awx111.insert(0,str(gax111) + str(number))
def rx2111():
    awx111.delete(0,END)
def rxx1111(number):
    gax111 = ens111.get()
    ens111.delete(0, END)
    ens111.insert(0,str(gax111) + str(number))
def rxx2111():
    ens111.delete(0,END)
def rxx3111():
	gax111 = ens111.get()
	ens111.insert(END,("."))
def rx3111():
	gax111 = awx111.get()
	awx111.insert(END,".")
def Enter9x():
	try:
		pisu1111 = float(awx111.get())
		pisu2111 = float(ens111.get())
		abm1 = pisu1111 * pisu1111
		abs1111 = abm1 / pisu2111
		abs2111 = str(abs1111)
		abs3111 = "{:.2f}".format(abs1111)
		mox11111111 = Button(FrameVoltageandOhmsP,text = abs3111+" Watts",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox11111111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")


#Ohms
def rx11111(number):
    gax1111 = awx1111.get()
    awx1111.delete(0, END)
    awx1111.insert(0,str(gax1111) + str(number))
def rx21111():
    awx1111.delete(0,END)
def rxx11111(number):
    gax1111 = ens1111.get()
    ens1111.delete(0, END)
    ens1111.insert(0,str(gax1111) + str(number))
def rxx21111():
    ens1111.delete(0,END)
def rxx31111():
	gax1111 = ens1111.get()
	ens1111.insert(END,("."))
def rx31111():
	gax1111 = awx1111.get()
	awx1111.insert(END,".")
def Enter10x():
	try:
		pisu11111 = float(awx1111.get())
		pisu21111 = float(ens1111.get())
		
		abs11111 = pisu11111 / pisu21111
		abs21111 = str(abs11111)
		abs31111 = "{:.2f}".format(abs11111)
		mox111111111 = Button(FrameVoltageandCurrentR,text = abs31111+" Ohms",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox111111111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")

#Ohms2
def rx111111(number):
    gax11111 = awx11111.get()
    awx11111.delete(0, END)
    awx11111.insert(0,str(gax11111) + str(number))
def rx211111():
    awx11111.delete(0,END)
def rxx111111(number):
    gax11111 = ens11111.get()
    ens11111.delete(0, END)
    ens11111.insert(0,str(gax11111) + str(number))
def rxx211111():
    ens11111.delete(0,END)
def rxx311111():
	gax11111 = ens11111.get()
	ens11111.insert(END,("."))
def rx311111():
	gax11111 = awx11111.get()
	awx11111.insert(END,".")
def Enter11x():
	try:
		pisu111111 = float(awx11111.get())
		pisu211111 = float(ens11111.get())
		alls = pisu111111 * pisu111111
		abs111111 = alls / pisu211111
		abs211111 = str(abs111111)
		abs311111 = "{:.2f}".format(abs111111)
		mox1111111111 = Button(FrameVoltageandPowerR,text = abs311111+" Ohms",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox1111111111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")


#Ohms 3
def rx1111111(number):
    gax111111 = awx111111.get()
    awx111111.delete(0, END)
    awx111111.insert(0,str(gax111111) + str(number))
def rx2111111():
    awx111111.delete(0,END)
def rxx1111111(number):
    gax111111 = ens111111.get()
    ens111111.delete(0, END)
    ens111111.insert(0,str(gax111111) + str(number))
def rxx2111111():
    ens111111.delete(0,END)
def rxx3111111():
	gax111111 = ens111111.get()
	ens111111.insert(END,("."))
def rx3111111():
	gax111111 = awx111111.get()
	awx111111.insert(END,".")
def Enter12x():
	try:
		pisu1111111 = float(awx111111.get())
		pisu2111111 = float(ens111111.get())
		alls1 = pisu2111111 * pisu2111111
		abs1111111 = pisu1111111 / alls1
		abs2111111 = str(abs1111111)
		abs3111111 = "{:.2f}".format(abs1111111)
		mox11111111111 = Button(FramePowerandCurrentR,text = abs3111111+" Ohms",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
		mox11111111111.place(x = 525 , y = 200)
	except (SyntaxError, NameError, ZeroDivisionError,ValueError):
		mb.showerror("Name Error","We cannot calculate variables")



#Return

#to main window
def rr1():
	FrameHome2.pack_forget()
	FrameHome.pack(padx = 10,pady = 10)




#to Home2
def rr2():
	FrameVoltage.pack_forget()
	FrameHome2.pack(padx = 10,pady = 10)

def rr3():
	FrameCurrent.pack_forget()
	FrameHome2.pack(padx = 10,pady = 10)

def rr4():
	FramePower.pack_forget()
	FrameHome2.pack(padx = 10,pady = 10)

def rr5():
	FrameOhms.pack_forget()
	FrameHome2.pack(padx = 10,pady = 10)




#Volt Window
def rr6():
	FramePowerandOhmsV.pack_forget()
	FrameVoltage.pack(padx = 10,pady = 10)

def rr7():
	FramePowerandCurrentV.pack_forget()
	FrameVoltage.pack(padx = 10,pady = 10)

def rr8():
	FrameCurrentandOhmsV.pack_forget()
	FrameVoltage.pack(padx = 10,pady = 10)




#Current Window
def rr9():
	FramePowerandOhmsC.pack_forget()
	FrameCurrent.pack(padx = 10,pady = 10)

def rr10():
	FramePowerandVoltageC.pack_forget()
	FrameCurrent.pack(padx = 10,pady = 10)

def rr11():
	FrameVoltageandOhmsC.pack_forget()
	FrameCurrent.pack(padx = 10,pady = 10)



#Power Window
def rr12():
	FrameVoltageandCurrentP.pack_forget()
	FramePower.pack(padx = 10,pady = 10)

def rr13():
	FrameCurrentandOhmsP.pack_forget()
	FramePower.pack(padx = 10,pady = 10)

def rr14():
	FrameVoltageandOhmsP.pack_forget()
	FramePower.pack(padx = 10,pady = 10)




#Ohms Window
def rr15():
	FrameVoltageandCurrentR.pack_forget()
	FrameOhms.pack(padx = 10,pady = 10)

def rr16():
	FrameVoltageandPowerR.pack_forget()
	FrameOhms.pack(padx = 10,pady = 10)

def rr17():
	FramePowerandCurrentR.pack_forget()
	FrameOhms.pack(padx = 10,pady = 10)






#FRAMEDEFINE
def Home1():
	FrameHome.pack_forget()
	FrameHome2.pack(padx = 10,pady = 10)
def Home2():
	FrameHome2.pack_forget()
	FrameVoltage.pack(padx = 10,pady = 10)
def Home3():
	FrameHome2.pack_forget()
	FrameCurrent.pack(padx = 10,pady = 10)
def Home4():
	FrameHome2.pack_forget()
	FrameOhms.pack(padx = 10,pady = 10)
def Home5():
	FrameHome2.pack_forget()
	FramePower.pack(padx = 10,pady = 10)





#volume
def Vol1():
	FrameVoltage.pack_forget()
	FramePowerandOhmsV.pack(padx = 10,pady = 10)
def Vol2():
	FrameVoltage.pack_forget()
	FramePowerandCurrentV.pack(padx = 10,pady = 10)
def Vol3():
	FrameVoltage.pack_forget()
	FrameCurrentandOhmsV.pack(padx = 10,pady = 10)


#current
def cre1():
	FrameCurrent.pack_forget()
	FramePowerandOhmsC.pack(padx = 10,pady = 10)
def cre2():
	FrameCurrent.pack_forget()
	FramePowerandVoltageC.pack(padx = 10,pady = 10)
def cre3():
	FrameCurrent.pack_forget()
	FrameVoltageandOhmsC.pack(padx = 10,pady = 10)



#Power
def pwe1():
	FramePower.pack_forget()
	FrameVoltageandCurrentP.pack(padx = 10,pady = 10)
def pwe2():
	FramePower.pack_forget()
	FrameCurrentandOhmsP.pack(padx = 10,pady = 10)
def pwe3():
	FramePower.pack_forget()
	FrameVoltageandOhmsP.pack(padx = 10,pady = 10)



#Ohms
def owe1():
	FrameOhms.pack_forget()
	FrameVoltageandCurrentR.pack(padx = 10,pady = 10)
def owe2():
	FrameOhms.pack_forget()
	FrameVoltageandPowerR.pack(padx = 10,pady = 10)
def owe3():
	FrameOhms.pack_forget()
	FramePowerandCurrentR.pack(padx = 10,pady = 10)


		





#Buttons
#Return Button
#To home
Return1 = Button(FrameHome2,text = "<<<", command = rr1)
Return1.place(x = 0, y = 0)


#to HOme 2
Return2 = Button(FrameVoltage,text = "<<<", command = rr2)
Return2.place(x = 0, y = 0)

Return3 = Button(FrameCurrent,text = "<<<", command = rr3)
Return3.place(x = 0, y = 0)

Return4 = Button(FramePower,text = "<<<", command = rr4)
Return4.place(x = 0, y = 0)

Return5 = Button(FrameOhms,text = "<<<", command = rr5)
Return5.place(x = 0, y = 0)


#to volt
Return6 = Button(FramePowerandOhmsV,text = "<<<", command = rr6)
Return6.place(x = 1300, y = 0)

Return7 = Button(FramePowerandCurrentV,text = "<<<", command = rr7)
Return7.place(x = 1300, y = 0)

Return8 = Button(FrameCurrentandOhmsV,text = "<<<", command = rr8)
Return8.place(x = 1300, y = 0)

#To current
Return9 = Button(FramePowerandOhmsC,text = "<<<", command = rr9)
Return9.place(x = 1300, y = 0)

Return10 = Button(FramePowerandVoltageC,text = "<<<", command = rr10)
Return10.place(x = 1300, y = 0)

Return11 = Button(FrameVoltageandOhmsC,text = "<<<", command = rr11)
Return11.place(x = 1300, y = 0)


#to Power
Return12 = Button(FrameVoltageandCurrentP,text = "<<<", command = rr12)
Return12.place(x = 1300, y = 0)

Return13 = Button(FrameCurrentandOhmsP,text = "<<<", command = rr13)
Return13.place(x = 1300, y = 0)

Return14 = Button(FrameVoltageandOhmsP,text = "<<<", command = rr14)
Return14.place(x = 1300, y = 0)


#to Ohms
Return15 = Button(FrameVoltageandCurrentR,text = "<<<", command = rr15)
Return15.place(x = 1300, y = 0)

Return16 = Button(FrameVoltageandPowerR,text = "<<<", command = rr16)
Return16.place(x = 1300, y = 0)

Return17 = Button(FramePowerandCurrentR,text = "<<<", command = rr17)
Return17.place(x = 1300, y = 0)



	#FrameHome
Home = Button(FrameHome,text = "Click to Enter",command = Home1,width = 20, height = 7)
Home.place(x = 500, y = 350)

Home1 = Button(FrameHome,text = "Click to Exit", command = root.quit,width = 20, height = 7)
Home1.place(x = 650, y = 350)





	#FrameHome2
Frame2x = Button(FrameHome2,text = "Voltage", command = Home2, width = 60, height = 18)
Frame3x = Button(FrameHome2,text = "Current", command = Home3, width = 60, height = 18)
Frame4x = Button(FrameHome2,text = "Ohms", command = Home4, width = 60, height = 18)
Frame5x = Button(FrameHome2,text = "Power", command = Home5, width = 60, height = 18)

Frame2x.place(x = 200, y = 20)
Frame3x.place(x = 750, y = 20)
Frame4x.place(x = 200, y = 350)
Frame5x.place(x = 750, y = 350)



	#FrameVoltage
Volt1 = Button(FrameVoltage,text = "Power and Ohms",command = Vol1, width = 60, height = 18)
Volt2 = Button(FrameVoltage,text = "Power and Current",command = Vol2, width = 60, height = 18)
Volt3 = Button(FrameVoltage,text = "Current and Ohms",command = Vol3, width = 60, height = 18)

Volt1.place(x = 150, y = 20)
Volt2.place(x = 750, y = 20)
Volt3.place(x = 450,y = 350)



		#FramePowerandOhmsV

#Part 1

a = Entry(FramePowerandOhmsV,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
a.place(x = 0, y = 30)
a.insert(0,"Enter Your Power")

b = Button(FramePowerandOhmsV, text="1" , padx = 40,  pady = 20,  command = lambda:   re(1))
c = Button(FramePowerandOhmsV, text="2",  padx = 40,  pady = 20,  command = lambda:   re(2))
d = Button(FramePowerandOhmsV, text="3",  padx = 40,  pady = 20,  command = lambda:   re(3))
e = Button(FramePowerandOhmsV, text="4",  padx = 40,  pady = 20,  command = lambda:   re(4))
f = Button(FramePowerandOhmsV, text="5",  padx = 40,  pady = 20,  command = lambda:   re(5))
g = Button(FramePowerandOhmsV, text="6",  padx = 40,  pady = 20,  command = lambda:   re(6))
h = Button(FramePowerandOhmsV, text="7",  padx = 40,  pady = 20,  command = lambda:   re(7))
i = Button(FramePowerandOhmsV, text="8",  padx = 40,  pady = 20,  command = lambda:   re(8))
j = Button(FramePowerandOhmsV, text="9",  padx = 40,  pady = 20,  command = lambda:   re(9))
k = Button(FramePowerandOhmsV, text="0",  padx = 40,  pady = 20,  command = lambda:   re(0))
u= Button(FramePowerandOhmsV, text="Clear",  padx = 29,  pady = 20,  command =ro)
dot4 = Button(FramePowerandOhmsV, text=".",  padx = 41.4,  pady = 20,  command =ddx)

b.place(x = 0  ,y = 80 )
c.place(x = 95 ,y = 80 )
d.place(x = 190 ,y = 80 )
e.place(x = 0 ,y = 145 )
f.place(x = 95 ,y = 145 )
g.place(x = 190 ,y = 145 )
h.place(x = 0 ,y = 210 )
i.place(x = 95 ,y = 210 )
j.place(x = 190 ,y = 210 )
k.place(x = 0,y = 275 )
dot4.place(x = 95,y = 275)
u.place(x = 190,y = 275 )









#Part 2
en = Entry(FramePowerandOhmsV,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
en.place(x =750, y =30)
en.insert(0,"Enter your Ohms")

ba = Button(FramePowerandOhmsV, text="1" , padx = 40,  pady = 20,  command = lambda:   rex(1))
ca = Button(FramePowerandOhmsV, text="2",  padx = 40,  pady = 20,  command = lambda:   rex(2))
da = Button(FramePowerandOhmsV, text="3",  padx = 40,  pady = 20,  command = lambda:   rex(3))
ea = Button(FramePowerandOhmsV, text="4",  padx = 40,  pady = 20,  command = lambda:   rex(4))
fa = Button(FramePowerandOhmsV, text="5",  padx = 40,  pady = 20,  command = lambda:   rex(5))
ga = Button(FramePowerandOhmsV, text="6",  padx = 40,  pady = 20,  command = lambda:   rex(6))
ha = Button(FramePowerandOhmsV, text="7",  padx = 40,  pady = 20,  command = lambda:   rex(7))
ia = Button(FramePowerandOhmsV, text="8",  padx = 40,  pady = 20,  command = lambda:   rex(8))
ja = Button(FramePowerandOhmsV, text="9",  padx = 40,  pady = 20,  command = lambda:   rex(9))
ka = Button(FramePowerandOhmsV, text="0",  padx = 40,  pady = 20,  command = lambda:   rex(0))
ua = Button(FramePowerandOhmsV, text="Clear",  padx = 29,  pady = 20,  command =rox)
dot6 = Button(FramePowerandOhmsV, text=".",  padx = 41.4,  pady = 20,  command = dd)

ba.place(x = 750  ,y = 80 )
ca.place(x = 845 ,y = 80 )
da.place(x = 940 ,y = 80 )
ea.place(x =750 ,y = 145 )
fa.place(x = 845 ,y = 145 )
ga.place(x = 940 ,y = 145 )
ha.place(x = 750 ,y = 210 )
ia.place(x = 845 ,y = 210 )
ja.place(x = 940 ,y = 210 )
ka.place(x = 750,y = 275 )
dot6.place(x = 845,y = 275)
ua.place(x = 940,y = 275 )

text1 = Button(FramePowerandOhmsV,text = "This is Your Power",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text1.place(x = 0, y = 0)
text2 = Button(FramePowerandOhmsV,text = "This is Your Ohms",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text2.place(x = 750, y = 0)
Enter1 = Button(FramePowerandOhmsV,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter1x)
Enter1.place(x = 440, y = 150)
answersh = Button(FramePowerandOhmsV,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
answersh.place(x = 440 , y = 200)












		#FramePowerandCurrentV
		#Part 1
a1 = Entry(FramePowerandCurrentV,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
a1.place(x = 0, y = 30)
a1.insert(0,"Enter Your Power")

b1 = Button(FramePowerandCurrentV, text="1" , padx = 40,  pady = 20,  command = lambda:   re1(1))
c1 = Button(FramePowerandCurrentV, text="2",  padx = 40,  pady = 20,  command = lambda:   re1(2))
d1 = Button(FramePowerandCurrentV, text="3",  padx = 40,  pady = 20,  command = lambda:   re1(3))
e1 = Button(FramePowerandCurrentV, text="4",  padx = 40,  pady = 20,  command = lambda:   re1(4))
f1 = Button(FramePowerandCurrentV, text="5",  padx = 40,  pady = 20,  command = lambda:   re1(5))
g1 = Button(FramePowerandCurrentV, text="6",  padx = 40,  pady = 20,  command = lambda:   re1(6))
h1 = Button(FramePowerandCurrentV, text="7",  padx = 40,  pady = 20,  command = lambda:   re1(7))
i1 = Button(FramePowerandCurrentV, text="8",  padx = 40,  pady = 20,  command = lambda:   re1(8))
j1 = Button(FramePowerandCurrentV, text="9",  padx = 40,  pady = 20,  command = lambda:   re1(9))
k1 = Button(FramePowerandCurrentV, text="0",  padx = 40,  pady = 20,  command = lambda:   re1(0))
u1 = Button(FramePowerandCurrentV, text="Clear",  padx = 29,  pady = 20,  command =ro1)
dot41 = Button(FramePowerandCurrentV, text=".",  padx = 41.4,  pady = 20,  command =ddx1)

b1.place(x = 0  ,y = 80 )
c1.place(x = 95 ,y = 80 )
d1.place(x = 190 ,y = 80 )
e1.place(x = 0 ,y = 145 )
f1.place(x = 95 ,y = 145 )
g1.place(x = 190 ,y = 145 )
h1.place(x = 0 ,y = 210 )
i1.place(x = 95 ,y = 210 )
j1.place(x = 190 ,y = 210 )
k1.place(x = 0,y = 275 )
dot41.place(x = 95,y = 275)
u1.place(x = 190,y = 275 )









#Part 2
en1 = Entry(FramePowerandCurrentV,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
en1.place(x =750, y =30)
en1.insert(0,"Enter your Current")

ba1 = Button(FramePowerandCurrentV, text="1" , padx = 40,  pady = 20,  command = lambda:   rex1(1))
ca1 = Button(FramePowerandCurrentV, text="2",  padx = 40,  pady = 20,  command = lambda:   rex1(2))
da1 = Button(FramePowerandCurrentV, text="3",  padx = 40,  pady = 20,  command = lambda:   rex1(3))
ea1 = Button(FramePowerandCurrentV, text="4",  padx = 40,  pady = 20,  command = lambda:   rex1(4))
fa1 = Button(FramePowerandCurrentV, text="5",  padx = 40,  pady = 20,  command = lambda:   rex1(5))
ga1 = Button(FramePowerandCurrentV, text="6",  padx = 40,  pady = 20,  command = lambda:   rex1(6))
ha1 = Button(FramePowerandCurrentV, text="7",  padx = 40,  pady = 20,  command = lambda:   rex1(7))
ia1 = Button(FramePowerandCurrentV, text="8",  padx = 40,  pady = 20,  command = lambda:   rex1(8))
ja1 = Button(FramePowerandCurrentV, text="9",  padx = 40,  pady = 20,  command = lambda:   rex1(9))
ka1 = Button(FramePowerandCurrentV, text="0",  padx = 40,  pady = 20,  command = lambda:   rex1(0))
ua1 = Button(FramePowerandCurrentV, text="Clear",  padx = 29,  pady = 20,  command =rox1)
dot61 = Button(FramePowerandCurrentV, text=".",  padx = 41.4,  pady = 20,  command = dd1)

ba1.place(x = 750  ,y = 80 )
ca1.place(x = 845 ,y = 80 )
da1.place(x = 940 ,y = 80 )
ea1.place(x =750 ,y = 145 )
fa1.place(x = 845 ,y = 145 )
ga1.place(x = 940 ,y = 145 )
ha1.place(x = 750 ,y = 210 )
ia1.place(x = 845 ,y = 210 )
ja1.place(x = 940 ,y = 210 )
ka1.place(x = 750,y = 275 )
dot61.place(x = 845,y = 275)
ua1.place(x = 940,y = 275 )

text11 = Button(FramePowerandCurrentV,text = "This is Your Power",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text11.place(x = 0, y = 0)
text21 = Button(FramePowerandCurrentV,text = "This is Your Current",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text21.place(x = 750, y = 0)
Enter11 = Button(FramePowerandCurrentV,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter2x)
Enter11.place(x = 440, y = 150)
answersh1 = Button(FramePowerandCurrentV,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
answersh1.place(x = 440 , y = 200)


		

		#FrameCurrentandOhmsV
		#Part 1
a11 = Entry(FrameCurrentandOhmsV,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
a11.place(x = 0, y = 30)
a11.insert(0,"Enter Your Current")

b11 = Button(FrameCurrentandOhmsV, text="1" , padx = 40,  pady = 20,  command = lambda:   re11(1))
c11 = Button(FrameCurrentandOhmsV, text="2",  padx = 40,  pady = 20,  command = lambda:   re11(2))
d11 = Button(FrameCurrentandOhmsV, text="3",  padx = 40,  pady = 20,  command = lambda:   re11(3))
e11 = Button(FrameCurrentandOhmsV, text="4",  padx = 40,  pady = 20,  command = lambda:   re11(4))
f11 = Button(FrameCurrentandOhmsV, text="5",  padx = 40,  pady = 20,  command = lambda:   re11(5))
g11 = Button(FrameCurrentandOhmsV, text="6",  padx = 40,  pady = 20,  command = lambda:   re11(6))
h11 = Button(FrameCurrentandOhmsV, text="7",  padx = 40,  pady = 20,  command = lambda:   re11(7))
i11 = Button(FrameCurrentandOhmsV, text="8",  padx = 40,  pady = 20,  command = lambda:   re11(8))
j11 = Button(FrameCurrentandOhmsV, text="9",  padx = 40,  pady = 20,  command = lambda:   re11(9))
k11 = Button(FrameCurrentandOhmsV, text="0",  padx = 40,  pady = 20,  command = lambda:   re11(0))
u11 = Button(FrameCurrentandOhmsV, text="Clear",  padx = 29,  pady = 20,  command =ro11)
dot411 = Button(FrameCurrentandOhmsV, text=".",  padx = 41.4,  pady = 20,  command =ddx11)

b11.place(x = 0  ,y = 80 )
c11.place(x = 95 ,y = 80 )
d11.place(x = 190 ,y = 80 )
e11.place(x = 0 ,y = 145 )
f11.place(x = 95 ,y = 145 )
g11.place(x = 190 ,y = 145 )
h11.place(x = 0 ,y = 210 )
i11.place(x = 95 ,y = 210 )
j11.place(x = 190 ,y = 210 )
k11.place(x = 0,y = 275 )
dot411.place(x = 95,y = 275)
u11.place(x = 190,y = 275 )



#Part 2
en11 = Entry(FrameCurrentandOhmsV,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
en11.place(x =750, y =30)
en11.insert(0,"Enter your Current")



ba11 = Button(FrameCurrentandOhmsV, text="1" , padx = 40,  pady = 20,  command = lambda:   rex11(1))
ca11 = Button(FrameCurrentandOhmsV, text="2",  padx = 40,  pady = 20,  command = lambda:   rex11(2))
da11 = Button(FrameCurrentandOhmsV, text="3",  padx = 40,  pady = 20,  command = lambda:   rex11(3))
ea11 = Button(FrameCurrentandOhmsV, text="4",  padx = 40,  pady = 20,  command = lambda:   rex11(4))
fa11 = Button(FrameCurrentandOhmsV, text="5",  padx = 40,  pady = 20,  command = lambda:   rex11(5))
ga11 = Button(FrameCurrentandOhmsV, text="6",  padx = 40,  pady = 20,  command = lambda:   rex11(6))
ha11 = Button(FrameCurrentandOhmsV, text="7",  padx = 40,  pady = 20,  command = lambda:   rex11(7))
ia11 = Button(FrameCurrentandOhmsV, text="8",  padx = 40,  pady = 20,  command = lambda:   rex11(8))
ja11 = Button(FrameCurrentandOhmsV, text="9",  padx = 40,  pady = 20,  command = lambda:   rex11(9))
ka11 = Button(FrameCurrentandOhmsV, text="0",  padx = 40,  pady = 20,  command = lambda:   rex11(0))
ua11 = Button(FrameCurrentandOhmsV, text="Clear",  padx = 29,  pady = 20,  command =rox11)
dot611 = Button(FrameCurrentandOhmsV, text=".",  padx = 41.4,  pady = 20,  command = dd11)




ba11.place(x = 750  ,y = 80 )
ca11.place(x = 845 ,y = 80 )
da11.place(x = 940 ,y = 80 )
ea11.place(x =750 ,y = 145 )
fa11.place(x = 845 ,y = 145 )
ga11.place(x = 940 ,y = 145 )
ha11.place(x = 750 ,y = 210 )
ia11.place(x = 845 ,y = 210 )
ja11.place(x = 940 ,y = 210 )
ka11.place(x = 750,y = 275 )
dot611.place(x = 845,y = 275)
ua11.place(x = 940,y = 275 )

text111 = Button(FrameCurrentandOhmsV,text = "This is Your Current",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text111.place(x = 0, y = 0)
text211 = Button(FrameCurrentandOhmsV,text = "This is Your Ohms",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text211.place(x = 750, y = 0)
Enter111 = Button(FrameCurrentandOhmsV,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter3x)
Enter111.place(x = 440, y = 150)
answersh11 = Button(FrameCurrentandOhmsV,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
answersh11.place(x = 440 , y = 200)












	#FrameCurrent
curr1 = Button(FrameCurrent,text = "Power and Ohms",command = cre1, width = 60, height = 18)
curr2 = Button(FrameCurrent,text = "Power and Current",command = cre2, width = 60, height = 18)
curr3 = Button(FrameCurrent,text = "Current and Ohms",command = cre3, width = 60, height = 18)

curr1.place(x = 150, y = 20)
curr2.place(x = 750, y = 20)
curr3.place(x = 450,y = 350)








		#FramePowerandOhmsC
		#Part 1
a111 = Entry(FramePowerandOhmsC,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
a111.place(x = 0, y = 30)
a111.insert(0,"Enter Your Power")

b111 = Button(FramePowerandOhmsC, text="1" , padx = 40,  pady = 20,  command = lambda:   re111(1))
c111 = Button(FramePowerandOhmsC, text="2",  padx = 40,  pady = 20,  command = lambda:   re111(2))
d111 = Button(FramePowerandOhmsC, text="3",  padx = 40,  pady = 20,  command = lambda:   re111(3))
e111 = Button(FramePowerandOhmsC, text="4",  padx = 40,  pady = 20,  command = lambda:   re111(4))
f111 = Button(FramePowerandOhmsC, text="5",  padx = 40,  pady = 20,  command = lambda:   re111(5))
g111 = Button(FramePowerandOhmsC, text="6",  padx = 40,  pady = 20,  command = lambda:   re111(6))
h111 = Button(FramePowerandOhmsC, text="7",  padx = 40,  pady = 20,  command = lambda:   re111(7))
i111 = Button(FramePowerandOhmsC, text="8",  padx = 40,  pady = 20,  command = lambda:   re111(8))
j111 = Button(FramePowerandOhmsC, text="9",  padx = 40,  pady = 20,  command = lambda:   re111(9))
k111 = Button(FramePowerandOhmsC, text="0",  padx = 40,  pady = 20,  command = lambda:   re111(0))
u111 = Button(FramePowerandOhmsC, text="Clear",  padx = 29,  pady = 20,  command =ro111)
dot4111 = Button(FramePowerandOhmsC, text=".",  padx = 41.4,  pady = 20,  command =ddx111)

b111.place(x = 0  ,y = 80 )
c111.place(x = 95 ,y = 80 )
d111.place(x = 190 ,y = 80 )
e111.place(x = 0 ,y = 145 )
f111.place(x = 95 ,y = 145 )
g111.place(x = 190 ,y = 145 )
h111.place(x = 0 ,y = 210 )
i111.place(x = 95 ,y = 210 )
j111.place(x = 190 ,y = 210 )
k111.place(x = 0,y = 275 )
dot4111.place(x = 95,y = 275)
u111.place(x = 190,y = 275 )


#Part 2
en111 = Entry(FramePowerandOhmsC,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
en111.place(x =750, y =30)
en111.insert(0,"Enter your Ohms")

ba111 = Button(FramePowerandOhmsC, text="1" , padx = 40,  pady = 20,  command = lambda:   rex111(1))
ca111 = Button(FramePowerandOhmsC, text="2",  padx = 40,  pady = 20,  command = lambda:   rex111(2))
da111 = Button(FramePowerandOhmsC, text="3",  padx = 40,  pady = 20,  command = lambda:   rex111(3))
ea111 = Button(FramePowerandOhmsC, text="4",  padx = 40,  pady = 20,  command = lambda:   rex111(4))
fa111 = Button(FramePowerandOhmsC, text="5",  padx = 40,  pady = 20,  command = lambda:   rex111(5))
ga111 = Button(FramePowerandOhmsC, text="6",  padx = 40,  pady = 20,  command = lambda:   rex111(6))
ha111 = Button(FramePowerandOhmsC, text="7",  padx = 40,  pady = 20,  command = lambda:   rex111(7))
ia111 = Button(FramePowerandOhmsC, text="8",  padx = 40,  pady = 20,  command = lambda:   rex111(8))
ja111 = Button(FramePowerandOhmsC, text="9",  padx = 40,  pady = 20,  command = lambda:   rex111(9))
ka111 = Button(FramePowerandOhmsC, text="0",  padx = 40,  pady = 20,  command = lambda:   rex111(0))
ua111 = Button(FramePowerandOhmsC, text="Clear",  padx = 29,  pady = 20,  command =rox111)
dot6111 = Button(FramePowerandOhmsC, text=".",  padx = 41.4,  pady = 20,  command = dd111)

ba111.place(x = 750  ,y = 80 )
ca111.place(x = 845 ,y = 80 )
da111.place(x = 940 ,y = 80 )
ea111.place(x =750 ,y = 145 )
fa111.place(x = 845 ,y = 145 )
ga111.place(x = 940 ,y = 145 )
ha111.place(x = 750 ,y = 210 )
ia111.place(x = 845 ,y = 210 )
ja111.place(x = 940 ,y = 210 )
ka111.place(x = 750,y = 275 )
dot6111.place(x = 845,y = 275)
ua111.place(x = 940,y = 275 )

text1111 = Button(FramePowerandOhmsC,text = "This is Your Power",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text1111.place(x = 0, y = 0)
text2111 = Button(FramePowerandOhmsC,text = "This is Your Ohms",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text2111.place(x = 750, y = 0)
Enter1111 = Button(FramePowerandOhmsC,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter4x)
Enter1111.place(x = 440, y = 150)
answersh111 = Button(FramePowerandOhmsC,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
answersh111.place(x = 440 , y = 200)











		#FramePowerandVoltageC
				#Part 1
a1111 = Entry(FramePowerandVoltageC,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
a1111.place(x = 0, y = 30)
a1111.insert(0,"Enter Your Power")

b1111 = Button(FramePowerandVoltageC, text="1" , padx = 40,  pady = 20,  command = lambda:   re1111(1))
c1111 = Button(FramePowerandVoltageC, text="2",  padx = 40,  pady = 20,  command = lambda:   re1111(2))
d1111 = Button(FramePowerandVoltageC, text="3",  padx = 40,  pady = 20,  command = lambda:   re1111(3))
e1111 = Button(FramePowerandVoltageC, text="4",  padx = 40,  pady = 20,  command = lambda:   re1111(4))
f1111 = Button(FramePowerandVoltageC, text="5",  padx = 40,  pady = 20,  command = lambda:   re1111(5))
g1111 = Button(FramePowerandVoltageC, text="6",  padx = 40,  pady = 20,  command = lambda:   re1111(6))
h1111 = Button(FramePowerandVoltageC, text="7",  padx = 40,  pady = 20,  command = lambda:   re1111(7))
i1111 = Button(FramePowerandVoltageC, text="8",  padx = 40,  pady = 20,  command = lambda:   re1111(8))
j1111 = Button(FramePowerandVoltageC, text="9",  padx = 40,  pady = 20,  command = lambda:   re1111(9))
k1111 = Button(FramePowerandVoltageC, text="0",  padx = 40,  pady = 20,  command = lambda:   re1111(0))
u1111 = Button(FramePowerandVoltageC, text="Clear",  padx = 29,  pady = 20,  command =ro1111)
dot41111 = Button(FramePowerandVoltageC, text=".",  padx = 41.4,  pady = 20,  command =ddx1111)

b1111.place(x = 0  ,y = 80 )
c1111.place(x = 95 ,y = 80 )
d1111.place(x = 190 ,y = 80 )
e1111.place(x = 0 ,y = 145 )
f1111.place(x = 95 ,y = 145 )
g1111.place(x = 190 ,y = 145 )
h1111.place(x = 0 ,y = 210 )
i1111.place(x = 95 ,y = 210 )
j1111.place(x = 190 ,y = 210 )
k1111.place(x = 0,y = 275 )
dot41111.place(x = 95,y = 275)
u1111.place(x = 190,y = 275 )


#Part 2
en1111 = Entry(FramePowerandVoltageC,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
en1111.place(x =750, y =30)
en1111.insert(0,"Enter your Voltage")

ba1111 = Button(FramePowerandVoltageC, text="1" , padx = 40,  pady = 20,  command = lambda:   rex1111(1))
ca1111 = Button(FramePowerandVoltageC, text="2",  padx = 40,  pady = 20,  command = lambda:   rex1111(2))
da1111 = Button(FramePowerandVoltageC, text="3",  padx = 40,  pady = 20,  command = lambda:   rex1111(3))
ea1111 = Button(FramePowerandVoltageC, text="4",  padx = 40,  pady = 20,  command = lambda:   rex1111(4))
fa1111 = Button(FramePowerandVoltageC, text="5",  padx = 40,  pady = 20,  command = lambda:   rex1111(5))
ga1111 = Button(FramePowerandVoltageC, text="6",  padx = 40,  pady = 20,  command = lambda:   rex1111(6))
ha1111 = Button(FramePowerandVoltageC, text="7",  padx = 40,  pady = 20,  command = lambda:   rex1111(7))
ia1111 = Button(FramePowerandVoltageC, text="8",  padx = 40,  pady = 20,  command = lambda:   rex1111(8))
ja1111 = Button(FramePowerandVoltageC, text="9",  padx = 40,  pady = 20,  command = lambda:   rex1111(9))
ka1111 = Button(FramePowerandVoltageC, text="0",  padx = 40,  pady = 20,  command = lambda:   rex1111(0))
ua1111 = Button(FramePowerandVoltageC, text="Clear",  padx = 29,  pady = 20,  command =rox1111)
dot61111 = Button(FramePowerandVoltageC, text=".",  padx = 41.4,  pady = 20,  command = dd1111)

ba1111.place(x = 750  ,y = 80 )
ca1111.place(x = 845 ,y = 80 )
da1111.place(x = 940 ,y = 80 )
ea1111.place(x =750 ,y = 145 )
fa1111.place(x = 845 ,y = 145 )
ga1111.place(x = 940 ,y = 145 )
ha1111.place(x = 750 ,y = 210 )
ia1111.place(x = 845 ,y = 210 )
ja1111.place(x = 940 ,y = 210 )
ka1111.place(x = 750,y = 275 )
dot61111.place(x = 845,y = 275)
ua1111.place(x = 940,y = 275 )

text1111 = Button(FramePowerandVoltageC,text = "This is Your Power",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text1111.place(x = 0, y = 0)
text2111 = Button(FramePowerandVoltageC,text = "This is Your Voltage",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
text2111.place(x = 750, y = 0)
Enter1111 = Button(FramePowerandVoltageC,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter5x)
Enter1111.place(x = 440, y = 150)
answersh111 = Button(FramePowerandVoltageC,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
answersh111.place(x = 440 , y = 200)










		#FrameVoltageandOhmsC
				#Part 1
awx = Entry(FrameVoltageandOhmsC,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
awx.place(x = 0, y = 30)
awx.insert(0,"Enter Your Voltage")

bz1 = Button(FrameVoltageandOhmsC, text="1" , padx = 40,  pady = 20,  command = lambda:   rx1(1))
bz2 = Button(FrameVoltageandOhmsC, text="2",  padx = 40,  pady = 20,  command = lambda:   rx1(2))
bz3 = Button(FrameVoltageandOhmsC, text="3",  padx = 40,  pady = 20,  command = lambda:   rx1(3))
bz4 = Button(FrameVoltageandOhmsC, text="4",  padx = 40,  pady = 20,  command = lambda:   rx1(4))
bz5 = Button(FrameVoltageandOhmsC, text="5",  padx = 40,  pady = 20,  command = lambda:   rx1(5))
bz6 = Button(FrameVoltageandOhmsC, text="6",  padx = 40,  pady = 20,  command = lambda:   rx1(6))
bz7 = Button(FrameVoltageandOhmsC, text="7",  padx = 40,  pady = 20,  command = lambda:   rx1(7))
bz8 = Button(FrameVoltageandOhmsC, text="8",  padx = 40,  pady = 20,  command = lambda:   rx1(8))
bz9 = Button(FrameVoltageandOhmsC, text="9",  padx = 40,  pady = 20,  command = lambda:   rx1(9))
bz10 = Button(FrameVoltageandOhmsC, text="0",  padx = 40,  pady = 20,  command = lambda:   rx1(0))
bz11 = Button(FrameVoltageandOhmsC, text="Clear",  padx = 29,  pady = 20,  command =rx2)
bz12 = Button(FrameVoltageandOhmsC, text=".",  padx = 41.4,  pady = 20,  command =rx3)

bz1.place(x = 0  ,y = 80 )
bz2.place(x = 95 ,y = 80 )
bz3.place(x = 190 ,y = 80 )
bz4.place(x = 0 ,y = 145 )
bz5.place(x = 95 ,y = 145 )
bz6.place(x = 190 ,y = 145 )
bz7.place(x = 0 ,y = 210 )
bz8.place(x = 95 ,y = 210 )
bz9.place(x = 190 ,y = 210 )
bz10.place(x = 0,y = 275 )
bz12.place(x = 95,y = 275)
bz11.place(x = 190,y = 275 )


#Part 2
ens = Entry(FrameVoltageandOhmsC,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
ens.place(x =750, y =30)
ens.insert(0,"Enter your Ohms")

az1 = Button(FrameVoltageandOhmsC, text="1" , padx = 40,  pady = 20,  command = lambda:   rxx1(1))
az2 = Button(FrameVoltageandOhmsC, text="2",  padx = 40,  pady = 20,  command = lambda:   rxx1(2))
az3 = Button(FrameVoltageandOhmsC, text="3",  padx = 40,  pady = 20,  command = lambda:   rxx1(3))
az4 = Button(FrameVoltageandOhmsC, text="4",  padx = 40,  pady = 20,  command = lambda:   rxx1(4))
az5 = Button(FrameVoltageandOhmsC, text="5",  padx = 40,  pady = 20,  command = lambda:   rxx1(5))
az6 = Button(FrameVoltageandOhmsC, text="6",  padx = 40,  pady = 20,  command = lambda:   rxx1(6))
az7 = Button(FrameVoltageandOhmsC, text="7",  padx = 40,  pady = 20,  command = lambda:   rxx1(7))
az8 = Button(FrameVoltageandOhmsC, text="8",  padx = 40,  pady = 20,  command = lambda:   rxx1(8))
az9 = Button(FrameVoltageandOhmsC, text="9",  padx = 40,  pady = 20,  command = lambda:   rxx1(9))
az10 = Button(FrameVoltageandOhmsC, text="0",  padx = 40,  pady = 20,  command = lambda:   rxx1(0))
az11 = Button(FrameVoltageandOhmsC, text="Clear",  padx = 29,  pady = 20,  command =rxx2)
az12 = Button(FrameVoltageandOhmsC, text=".",  padx = 41.4,  pady = 20,  command = rxx3)

az1.place(x = 750  ,y = 80 )
az2.place(x = 845 ,y = 80 )
az3.place(x = 940 ,y = 80 )
az4.place(x =750 ,y = 145 )
az5.place(x = 845 ,y = 145 )
az6.place(x = 940 ,y = 145 )
az7.place(x = 750 ,y = 210 )
az8.place(x = 845 ,y = 210 )
az9.place(x = 940 ,y = 210 )
az10.place(x = 750,y = 275 )
az12.place(x = 845,y = 275)
az11.place(x = 940,y = 275 )

az = Button(FrameVoltageandOhmsC,text = "This is Your Voltage",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
az.place(x = 0, y = 0)
bz = Button(FrameVoltageandOhmsC,text = "This is Your Ohms",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
bz.place(x = 750, y = 0)
cz = Button(FrameVoltageandOhmsC,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter6x)
cz.place(x = 440, y = 150)
dz = Button(FrameVoltageandOhmsC,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
dz.place(x = 440 , y = 200)




	#FramePower
Pow1 = Button(FramePower,text = "Voltage and Current",command = pwe1, width = 60, height = 18)
Pow2 = Button(FramePower,text = "Current and Ohms",command = pwe2, width = 60, height = 18)
Pow3 = Button(FramePower,text = "Voltage and Ohms",command = pwe3, width = 60, height = 18)

Pow1.place(x = 150, y = 20)
Pow2.place(x = 750, y = 20)
Pow3.place(x = 450,y = 350)











		#FrameVoltageandCurrentP
				#Part 1
awx1 = Entry(FrameVoltageandCurrentP,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
awx1.place(x = 0, y = 30)
awx1.insert(0,"Enter Your Voltage")

bzz1 = Button(FrameVoltageandCurrentP, text="1" , padx = 40,  pady = 20,  command = lambda:   rx11(1))
bzz2 = Button(FrameVoltageandCurrentP, text="2",  padx = 40,  pady = 20,  command = lambda:   rx11(2))
bzz3 = Button(FrameVoltageandCurrentP, text="3",  padx = 40,  pady = 20,  command = lambda:   rx11(3))
bzz4 = Button(FrameVoltageandCurrentP, text="4",  padx = 40,  pady = 20,  command = lambda:   rx11(4))
bzz5 = Button(FrameVoltageandCurrentP, text="5",  padx = 40,  pady = 20,  command = lambda:   rx11(5))
bzz6 = Button(FrameVoltageandCurrentP, text="6",  padx = 40,  pady = 20,  command = lambda:   rx11(6))
bzz7 = Button(FrameVoltageandCurrentP, text="7",  padx = 40,  pady = 20,  command = lambda:   rx11(7))
bzz8 = Button(FrameVoltageandCurrentP, text="8",  padx = 40,  pady = 20,  command = lambda:   rx11(8))
bzz9 = Button(FrameVoltageandCurrentP, text="9",  padx = 40,  pady = 20,  command = lambda:   rx11(9))
bzz10 = Button(FrameVoltageandCurrentP, text="0",  padx = 40,  pady = 20,  command = lambda:   rx11(0))
bzz11 = Button(FrameVoltageandCurrentP, text="Clear",  padx = 29,  pady = 20,  command =rx21)
bzz12 = Button(FrameVoltageandCurrentP, text=".",  padx = 41.4,  pady = 20,  command =rx31)

bzz1.place(x = 0  ,y = 80 )
bzz2.place(x = 95 ,y = 80 )
bzz3.place(x = 190 ,y = 80 )
bzz4.place(x = 0 ,y = 145 )
bzz5.place(x = 95 ,y = 145 )
bzz6.place(x = 190 ,y = 145 )
bzz7.place(x = 0 ,y = 210 )
bzz8.place(x = 95 ,y = 210 )
bzz9.place(x = 190 ,y = 210 )
bzz10.place(x = 0,y = 275 )
bzz12.place(x = 95,y = 275)
bzz11.place(x = 190,y = 275 )


#Part 2
ens1 = Entry(FrameVoltageandCurrentP,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
ens1.place(x =750, y =30)
ens1.insert(0,"Enter your Current")

azz1 = Button(FrameVoltageandCurrentP, text="1" , padx = 40,  pady = 20,  command = lambda:   rxx11(1))
azz2 = Button(FrameVoltageandCurrentP, text="2",  padx = 40,  pady = 20,  command = lambda:   rxx11(2))
azz3 = Button(FrameVoltageandCurrentP, text="3",  padx = 40,  pady = 20,  command = lambda:   rxx11(3))
azz4 = Button(FrameVoltageandCurrentP, text="4",  padx = 40,  pady = 20,  command = lambda:   rxx11(4))
azz5 = Button(FrameVoltageandCurrentP, text="5",  padx = 40,  pady = 20,  command = lambda:   rxx11(5))
azz6 = Button(FrameVoltageandCurrentP, text="6",  padx = 40,  pady = 20,  command = lambda:   rxx11(6))
azz7 = Button(FrameVoltageandCurrentP, text="7",  padx = 40,  pady = 20,  command = lambda:   rxx11(7))
azz8 = Button(FrameVoltageandCurrentP, text="8",  padx = 40,  pady = 20,  command = lambda:   rxx11(8))
azz9 = Button(FrameVoltageandCurrentP, text="9",  padx = 40,  pady = 20,  command = lambda:   rxx11(9))
azz10 = Button(FrameVoltageandCurrentP, text="0",  padx = 40,  pady = 20,  command = lambda:   rxx11(0))
azz11 = Button(FrameVoltageandCurrentP, text="Clear",  padx = 29,  pady = 20,  command =rxx21)
azz12 = Button(FrameVoltageandCurrentP, text=".",  padx = 41.4,  pady = 20,  command = rxx31)

azz1.place(x = 750  ,y = 80 )
azz2.place(x = 845 ,y = 80 )
azz3.place(x = 940 ,y = 80 )
azz4.place(x =750 ,y = 145 )
azz5.place(x = 845 ,y = 145 )
azz6.place(x = 940 ,y = 145 )
azz7.place(x = 750 ,y = 210 )
azz8.place(x = 845 ,y = 210 )
azz9.place(x = 940 ,y = 210 )
azz10.place(x = 750,y = 275 )
azz12.place(x = 845,y = 275)
azz11.place(x = 940,y = 275 )

azz = Button(FrameVoltageandCurrentP,text = "This is Your Voltage",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
azz.place(x = 0, y = 0)
bzz = Button(FrameVoltageandCurrentP,text = "This is Your Current",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
bzz.place(x = 750, y = 0)
czz = Button(FrameVoltageandCurrentP,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter7x)
czz.place(x = 440, y = 150)
dzz = Button(FrameVoltageandCurrentP,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
dzz.place(x = 440 , y = 200)







		#FrameCurrentandOhmsP
				#Part 1
awx11 = Entry(FrameCurrentandOhmsP,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
awx11.place(x = 0, y = 30)
awx11.insert(0,"Enter Your Current")

bzzz1 = Button(FrameCurrentandOhmsP, text="1" , padx = 40,  pady = 20,  command = lambda:   rx111(1))
bzzz2 = Button(FrameCurrentandOhmsP, text="2",  padx = 40,  pady = 20,  command = lambda:   rx111(2))
bzzz3 = Button(FrameCurrentandOhmsP, text="3",  padx = 40,  pady = 20,  command = lambda:   rx111(3))
bzzz4 = Button(FrameCurrentandOhmsP, text="4",  padx = 40,  pady = 20,  command = lambda:   rx111(4))
bzzz5 = Button(FrameCurrentandOhmsP, text="5",  padx = 40,  pady = 20,  command = lambda:   rx111(5))
bzzz6 = Button(FrameCurrentandOhmsP, text="6",  padx = 40,  pady = 20,  command = lambda:   rx111(6))
bzzz7 = Button(FrameCurrentandOhmsP, text="7",  padx = 40,  pady = 20,  command = lambda:   rx111(7))
bzzz8 = Button(FrameCurrentandOhmsP, text="8",  padx = 40,  pady = 20,  command = lambda:   rx111(8))
bzzz9 = Button(FrameCurrentandOhmsP, text="9",  padx = 40,  pady = 20,  command = lambda:   rx111(9))
bzzz10 = Button(FrameCurrentandOhmsP, text="0",  padx = 40,  pady = 20,  command = lambda:   rx111(0))
bzzz11 = Button(FrameCurrentandOhmsP, text="Clear",  padx = 29,  pady = 20,  command =rx211)
bzzz12 = Button(FrameCurrentandOhmsP, text=".",  padx = 41.4,  pady = 20,  command =rx311)

bzzz1.place(x = 0  ,y = 80 )
bzzz2.place(x = 95 ,y = 80 )
bzzz3.place(x = 190 ,y = 80 )
bzzz4.place(x = 0 ,y = 145 )
bzzz5.place(x = 95 ,y = 145 )
bzzz6.place(x = 190 ,y = 145 )
bzzz7.place(x = 0 ,y = 210 )
bzzz8.place(x = 95 ,y = 210 )
bzzz9.place(x = 190 ,y = 210 )
bzzz10.place(x = 0,y = 275 )
bzzz12.place(x = 95,y = 275)
bzzz11.place(x = 190,y = 275 )


#Part 2
ens11 = Entry(FrameCurrentandOhmsP,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
ens11.place(x =750, y =30)
ens11.insert(0,"Enter your Ohms")

azzz1 = Button(FrameCurrentandOhmsP, text="1" , padx = 40,  pady = 20,  command = lambda:   rxx111(1))
azzz2 = Button(FrameCurrentandOhmsP, text="2",  padx = 40,  pady = 20,  command = lambda:   rxx111(2))
azzz3 = Button(FrameCurrentandOhmsP, text="3",  padx = 40,  pady = 20,  command = lambda:   rxx111(3))
azzz4 = Button(FrameCurrentandOhmsP, text="4",  padx = 40,  pady = 20,  command = lambda:   rxx111(4))
azzz5 = Button(FrameCurrentandOhmsP, text="5",  padx = 40,  pady = 20,  command = lambda:   rxx111(5))
azzz6 = Button(FrameCurrentandOhmsP, text="6",  padx = 40,  pady = 20,  command = lambda:   rxx111(6))
azzz7 = Button(FrameCurrentandOhmsP, text="7",  padx = 40,  pady = 20,  command = lambda:   rxx111(7))
azzz8 = Button(FrameCurrentandOhmsP, text="8",  padx = 40,  pady = 20,  command = lambda:   rxx111(8))
azzz9 = Button(FrameCurrentandOhmsP, text="9",  padx = 40,  pady = 20,  command = lambda:   rxx111(9))
azzz10 = Button(FrameCurrentandOhmsP, text="0",  padx = 40,  pady = 20,  command = lambda:   rxx111(0))
azzz11 = Button(FrameCurrentandOhmsP, text="Clear",  padx = 29,  pady = 20,  command =rxx211)
azzz12 = Button(FrameCurrentandOhmsP, text=".",  padx = 41.4,  pady = 20,  command = rxx311)

azzz1.place(x = 750  ,y = 80 )
azzz2.place(x = 845 ,y = 80 )
azzz3.place(x = 940 ,y = 80 )
azzz4.place(x =750 ,y = 145 )
azzz5.place(x = 845 ,y = 145 )
azzz6.place(x = 940 ,y = 145 )
azzz7.place(x = 750 ,y = 210 )
azzz8.place(x = 845 ,y = 210 )
azzz9.place(x = 940 ,y = 210 )
azzz10.place(x = 750,y = 275 )
azzz12.place(x = 845,y = 275)
azzz11.place(x = 940,y = 275 )

azzz = Button(FrameCurrentandOhmsP,text = "This is Your Current",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
azzz.place(x = 0, y = 0)
bzzz = Button(FrameCurrentandOhmsP,text = "This is Your Ohms",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
bzzz.place(x = 750, y = 0)
czzz = Button(FrameCurrentandOhmsP,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter8x)
czzz.place(x = 440, y = 150)
dzzz = Button(FrameCurrentandOhmsP,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
dzzz.place(x = 440 , y = 200)






		#FrameVoltageandOhmsP
				#Part 1
awx111 = Entry(FrameVoltageandOhmsP,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
awx111.place(x = 0, y = 30)
awx111.insert(0,"Enter Your Voltage")

bzzzz1 = Button(FrameVoltageandOhmsP, text="1" , padx = 40,  pady = 20,  command = lambda:   rx1111(1))
bzzzz2 = Button(FrameVoltageandOhmsP, text="2",  padx = 40,  pady = 20,  command = lambda:   rx1111(2))
bzzzz3 = Button(FrameVoltageandOhmsP, text="3",  padx = 40,  pady = 20,  command = lambda:   rx1111(3))
bzzzz4 = Button(FrameVoltageandOhmsP, text="4",  padx = 40,  pady = 20,  command = lambda:   rx1111(4))
bzzzz5 = Button(FrameVoltageandOhmsP, text="5",  padx = 40,  pady = 20,  command = lambda:   rx1111(5))
bzzzz6 = Button(FrameVoltageandOhmsP, text="6",  padx = 40,  pady = 20,  command = lambda:   rx1111(6))
bzzzz7 = Button(FrameVoltageandOhmsP, text="7",  padx = 40,  pady = 20,  command = lambda:   rx1111(7))
bzzzz8 = Button(FrameVoltageandOhmsP, text="8",  padx = 40,  pady = 20,  command = lambda:   rx1111(8))
bzzzz9 = Button(FrameVoltageandOhmsP, text="9",  padx = 40,  pady = 20,  command = lambda:   rx1111(9))
bzzzz10 = Button(FrameVoltageandOhmsP, text="0",  padx = 40,  pady = 20,  command = lambda:   rx1111(0))
bzzzz11 = Button(FrameVoltageandOhmsP, text="Clear",  padx = 29,  pady = 20,  command =rx2111)
bzzzz12 = Button(FrameVoltageandOhmsP, text=".",  padx = 41.4,  pady = 20,  command =rx3111)

bzzzz1.place(x = 0  ,y = 80 )
bzzzz2.place(x = 95 ,y = 80 )
bzzzz3.place(x = 190 ,y = 80 )
bzzzz4.place(x = 0 ,y = 145 )
bzzzz5.place(x = 95 ,y = 145 )
bzzzz6.place(x = 190 ,y = 145 )
bzzzz7.place(x = 0 ,y = 210 )
bzzzz8.place(x = 95 ,y = 210 )
bzzzz9.place(x = 190 ,y = 210 )
bzzzz10.place(x = 0,y = 275 )
bzzzz12.place(x = 95,y = 275)
bzzzz11.place(x = 190,y = 275 )


#Part 2
ens111 = Entry(FrameVoltageandOhmsP,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
ens111.place(x =750, y =30)
ens111.insert(0,"Enter your Ohms")

azzzz1 = Button(FrameVoltageandOhmsP, text="1" , padx = 40,  pady = 20,  command = lambda:   rxx1111(1))
azzzz2 = Button(FrameVoltageandOhmsP, text="2",  padx = 40,  pady = 20,  command = lambda:   rxx1111(2))
azzzz3 = Button(FrameVoltageandOhmsP, text="3",  padx = 40,  pady = 20,  command = lambda:   rxx1111(3))
azzzz4 = Button(FrameVoltageandOhmsP, text="4",  padx = 40,  pady = 20,  command = lambda:   rxx1111(4))
azzzz5 = Button(FrameVoltageandOhmsP, text="5",  padx = 40,  pady = 20,  command = lambda:   rxx1111(5))
azzzz6 = Button(FrameVoltageandOhmsP, text="6",  padx = 40,  pady = 20,  command = lambda:   rxx1111(6))
azzzz7 = Button(FrameVoltageandOhmsP, text="7",  padx = 40,  pady = 20,  command = lambda:   rxx1111(7))
azzzz8 = Button(FrameVoltageandOhmsP, text="8",  padx = 40,  pady = 20,  command = lambda:   rxx1111(8))
azzzz9 = Button(FrameVoltageandOhmsP, text="9",  padx = 40,  pady = 20,  command = lambda:   rxx1111(9))
azzzz10 = Button(FrameVoltageandOhmsP, text="0",  padx = 40,  pady = 20,  command = lambda:   rxx1111(0))
azzzz11 = Button(FrameVoltageandOhmsP, text="Clear",  padx = 29,  pady = 20,  command =rxx2111)
azzzz12 = Button(FrameVoltageandOhmsP, text=".",  padx = 41.4,  pady = 20,  command = rxx3111)

azzzz1.place(x = 750  ,y = 80 )
azzzz2.place(x = 845 ,y = 80 )
azzzz3.place(x = 940 ,y = 80 )
azzzz4.place(x =750 ,y = 145 )
azzzz5.place(x = 845 ,y = 145 )
azzzz6.place(x = 940 ,y = 145 )
azzzz7.place(x = 750 ,y = 210 )
azzzz8.place(x = 845 ,y = 210 )
azzzz9.place(x = 940 ,y = 210 )
azzzz10.place(x = 750,y = 275 )
azzzz12.place(x = 845,y = 275)
azzzz11.place(x = 940,y = 275 )

azzzz = Button(FrameVoltageandOhmsP,text = "This is Your Voltage",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
azzzz.place(x = 0, y = 0)
bzzzz = Button(FrameVoltageandOhmsP,text = "This is Your Ohms",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
bzzzz.place(x = 750, y = 0)
czzzz = Button(FrameVoltageandOhmsP,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter9x)
czzzz.place(x = 440, y = 150)
dzzzz = Button(FrameVoltageandOhmsP,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
dzzzz.place(x = 440 , y = 200)





	#FrameOhms
ohms1 = Button(FrameOhms,text = "Voltage and Current",command = owe1, width = 60, height = 18)
ohms2 = Button(FrameOhms,text = "Voltage and Power",command = owe2, width = 60, height = 18)
ohms3 = Button(FrameOhms,text = "Power and Current",command = owe3, width = 60, height = 18)

ohms1.place(x = 150, y = 20)
ohms2.place(x = 750, y = 20)
ohms3.place(x = 450,y = 350)



		#FrameVoltageandCurrentR
				#Part 1
awx1111 = Entry(FrameVoltageandCurrentR,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
awx1111.place(x = 0, y = 30)
awx1111.insert(0,"Enter Your Voltage")

bzzzzz1 = Button(FrameVoltageandCurrentR, text="1" , padx = 40,  pady = 20,  command = lambda:   rx11111(1))
bzzzzz2 = Button(FrameVoltageandCurrentR, text="2",  padx = 40,  pady = 20,  command = lambda:   rx11111(2))
bzzzzz3 = Button(FrameVoltageandCurrentR, text="3",  padx = 40,  pady = 20,  command = lambda:   rx11111(3))
bzzzzz4 = Button(FrameVoltageandCurrentR, text="4",  padx = 40,  pady = 20,  command = lambda:   rx11111(4))
bzzzzz5 = Button(FrameVoltageandCurrentR, text="5",  padx = 40,  pady = 20,  command = lambda:   rx11111(5))
bzzzzz6 = Button(FrameVoltageandCurrentR, text="6",  padx = 40,  pady = 20,  command = lambda:   rx11111(6))
bzzzzz7 = Button(FrameVoltageandCurrentR, text="7",  padx = 40,  pady = 20,  command = lambda:   rx11111(7))
bzzzzz8 = Button(FrameVoltageandCurrentR, text="8",  padx = 40,  pady = 20,  command = lambda:   rx11111(8))
bzzzzz9 = Button(FrameVoltageandCurrentR, text="9",  padx = 40,  pady = 20,  command = lambda:   rx11111(9))
bzzzzz10 = Button(FrameVoltageandCurrentR, text="0",  padx = 40,  pady = 20,  command = lambda:   rx11111(0))
bzzzzz11 = Button(FrameVoltageandCurrentR, text="Clear",  padx = 29,  pady = 20,  command =rx21111)
bzzzzz12 = Button(FrameVoltageandCurrentR, text=".",  padx = 41.4,  pady = 20,  command =rx31111)

bzzzzz1.place(x = 0  ,y = 80 )
bzzzzz2.place(x = 95 ,y = 80 )
bzzzzz3.place(x = 190 ,y = 80 )
bzzzzz4.place(x = 0 ,y = 145 )
bzzzzz5.place(x = 95 ,y = 145 )
bzzzzz6.place(x = 190 ,y = 145 )
bzzzzz7.place(x = 0 ,y = 210 )
bzzzzz8.place(x = 95 ,y = 210 )
bzzzzz9.place(x = 190 ,y = 210 )
bzzzzz10.place(x = 0,y = 275 )
bzzzzz12.place(x = 95,y = 275)
bzzzzz11.place(x = 190,y = 275 )


#Part 2
ens1111 = Entry(FrameVoltageandCurrentR,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
ens1111.place(x =750, y =30)
ens1111.insert(0,"Enter your Current")

azzzzz1 = Button(FrameVoltageandCurrentR, text="1" , padx = 40,  pady = 20,  command = lambda:   rxx11111(1))
azzzzz2 = Button(FrameVoltageandCurrentR, text="2",  padx = 40,  pady = 20,  command = lambda:   rxx11111(2))
azzzzz3 = Button(FrameVoltageandCurrentR, text="3",  padx = 40,  pady = 20,  command = lambda:   rxx11111(3))
azzzzz4 = Button(FrameVoltageandCurrentR, text="4",  padx = 40,  pady = 20,  command = lambda:   rxx11111(4))
azzzzz5 = Button(FrameVoltageandCurrentR, text="5",  padx = 40,  pady = 20,  command = lambda:   rxx11111(5))
azzzzz6 = Button(FrameVoltageandCurrentR, text="6",  padx = 40,  pady = 20,  command = lambda:   rxx11111(6))
azzzzz7 = Button(FrameVoltageandCurrentR, text="7",  padx = 40,  pady = 20,  command = lambda:   rxx11111(7))
azzzzz8 = Button(FrameVoltageandCurrentR, text="8",  padx = 40,  pady = 20,  command = lambda:   rxx11111(8))
azzzzz9 = Button(FrameVoltageandCurrentR, text="9",  padx = 40,  pady = 20,  command = lambda:   rxx11111(9))
azzzzz10 = Button(FrameVoltageandCurrentR, text="0",  padx = 40,  pady = 20,  command = lambda:   rxx11111(0))
azzzzz11 = Button(FrameVoltageandCurrentR, text="Clear",  padx = 29,  pady = 20,  command =rxx21111)
azzzzz12 = Button(FrameVoltageandCurrentR, text=".",  padx = 41.4,  pady = 20,  command = rxx31111)

azzzzz1.place(x = 750  ,y = 80 )
azzzzz2.place(x = 845 ,y = 80 )
azzzzz3.place(x = 940 ,y = 80 )
azzzzz4.place(x =750 ,y = 145 )
azzzzz5.place(x = 845 ,y = 145 )
azzzzz6.place(x = 940 ,y = 145 )
azzzzz7.place(x = 750 ,y = 210 )
azzzzz8.place(x = 845 ,y = 210 )
azzzzz9.place(x = 940 ,y = 210 )
azzzzz10.place(x = 750,y = 275 )
azzzzz12.place(x = 845,y = 275)
azzzzz11.place(x = 940,y = 275 )

azzzzz = Button(FrameVoltageandCurrentR,text = "This is Your Voltage",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
azzzzz.place(x = 0, y = 0)
bzzzzz = Button(FrameVoltageandCurrentR,text = "This is Your Current",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
bzzzzz.place(x = 750, y = 0)
czzzzz = Button(FrameVoltageandCurrentR,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter10x)
czzzzz.place(x = 440, y = 150)
dzzzzz = Button(FrameVoltageandCurrentR,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
dzzzzz.place(x = 440 , y = 200)








		#FrameVoltageandPowerR
				#Part 1
awx11111 = Entry(FrameVoltageandPowerR,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
awx11111.place(x = 0, y = 30)
awx11111.insert(0,"Enter Your Voltage")

bzzzzzz1 = Button(FrameVoltageandPowerR, text="1" , padx = 40,  pady = 20,  command = lambda:   rx111111(1))
bzzzzzz2 = Button(FrameVoltageandPowerR, text="2",  padx = 40,  pady = 20,  command = lambda:   rx111111(2))
bzzzzzz3 = Button(FrameVoltageandPowerR, text="3",  padx = 40,  pady = 20,  command = lambda:   rx111111(3))
bzzzzzz4 = Button(FrameVoltageandPowerR, text="4",  padx = 40,  pady = 20,  command = lambda:   rx111111(4))
bzzzzzz5 = Button(FrameVoltageandPowerR, text="5",  padx = 40,  pady = 20,  command = lambda:   rx111111(5))
bzzzzzz6 = Button(FrameVoltageandPowerR, text="6",  padx = 40,  pady = 20,  command = lambda:   rx111111(6))
bzzzzzz7 = Button(FrameVoltageandPowerR, text="7",  padx = 40,  pady = 20,  command = lambda:   rx111111(7))
bzzzzzz8 = Button(FrameVoltageandPowerR, text="8",  padx = 40,  pady = 20,  command = lambda:   rx111111(8))
bzzzzzz9 = Button(FrameVoltageandPowerR, text="9",  padx = 40,  pady = 20,  command = lambda:   rx111111(9))
bzzzzzz10 = Button(FrameVoltageandPowerR, text="0",  padx = 40,  pady = 20,  command = lambda:   rx111111(0))
bzzzzzz11 = Button(FrameVoltageandPowerR, text="Clear",  padx = 29,  pady = 20,  command =rx211111)
bzzzzzz12 = Button(FrameVoltageandPowerR, text=".",  padx = 41.4,  pady = 20,  command =rx311111)

bzzzzzz1.place(x = 0  ,y = 80 )
bzzzzzz2.place(x = 95 ,y = 80 )
bzzzzzz3.place(x = 190 ,y = 80 )
bzzzzzz4.place(x = 0 ,y = 145 )
bzzzzzz5.place(x = 95 ,y = 145 )
bzzzzzz6.place(x = 190 ,y = 145 )
bzzzzzz7.place(x = 0 ,y = 210 )
bzzzzzz8.place(x = 95 ,y = 210 )
bzzzzzz9.place(x = 190 ,y = 210 )
bzzzzzz10.place(x = 0,y = 275 )
bzzzzzz12.place(x = 95,y = 275)
bzzzzzz11.place(x = 190,y = 275 )


#Part 2
ens11111 = Entry(FrameVoltageandPowerR,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
ens11111.place(x =750, y =30)
ens11111.insert(0,"Enter your Power")

azzzzzz1 = Button(FrameVoltageandPowerR, text="1" , padx = 40,  pady = 20,  command = lambda:   rxx111111(1))
azzzzzz2 = Button(FrameVoltageandPowerR, text="2",  padx = 40,  pady = 20,  command = lambda:   rxx111111(2))
azzzzzz3 = Button(FrameVoltageandPowerR, text="3",  padx = 40,  pady = 20,  command = lambda:   rxx111111(3))
azzzzzz4 = Button(FrameVoltageandPowerR, text="4",  padx = 40,  pady = 20,  command = lambda:   rxx111111(4))
azzzzzz5 = Button(FrameVoltageandPowerR, text="5",  padx = 40,  pady = 20,  command = lambda:   rxx111111(5))
azzzzzz6 = Button(FrameVoltageandPowerR, text="6",  padx = 40,  pady = 20,  command = lambda:   rxx111111(6))
azzzzzz7 = Button(FrameVoltageandPowerR, text="7",  padx = 40,  pady = 20,  command = lambda:   rxx111111(7))
azzzzzz8 = Button(FrameVoltageandPowerR, text="8",  padx = 40,  pady = 20,  command = lambda:   rxx111111(8))
azzzzzz9 = Button(FrameVoltageandPowerR, text="9",  padx = 40,  pady = 20,  command = lambda:   rxx111111(9))
azzzzzz10 = Button(FrameVoltageandPowerR, text="0",  padx = 40,  pady = 20,  command = lambda:   rxx111111(0))
azzzzzz11 = Button(FrameVoltageandPowerR, text="Clear",  padx = 29,  pady = 20,  command =rxx211111)
azzzzzz12 = Button(FrameVoltageandPowerR, text=".",  padx = 41.4,  pady = 20,  command = rxx311111)

azzzzzz1.place(x = 750  ,y = 80 )
azzzzzz2.place(x = 845 ,y = 80 )
azzzzzz3.place(x = 940 ,y = 80 )
azzzzzz4.place(x =750 ,y = 145 )
azzzzzz5.place(x = 845 ,y = 145 )
azzzzzz6.place(x = 940 ,y = 145 )
azzzzzz7.place(x = 750 ,y = 210 )
azzzzzz8.place(x = 845 ,y = 210 )
azzzzzz9.place(x = 940 ,y = 210 )
azzzzzz10.place(x = 750,y = 275 )
azzzzzz12.place(x = 845,y = 275)
azzzzzz11.place(x = 940,y = 275 )

azzzzzz = Button(FrameVoltageandPowerR,text = "This is Your Voltage",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
azzzzzz.place(x = 0, y = 0)
bzzzzzz = Button(FrameVoltageandPowerR,text = "This is Your Power",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
bzzzzzz.place(x = 750, y = 0)
czzzzzz = Button(FrameVoltageandPowerR,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter11x)
czzzzzz.place(x = 440, y = 150)
dzzzzzz = Button(FrameVoltageandPowerR,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
dzzzzzz.place(x = 440 , y = 200)






		#FramePowerandCurrentR
				#Part 1
awx111111 = Entry(FramePowerandCurrentR,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
awx111111.place(x = 0, y = 30)
awx111111.insert(0,"Enter Your Power")

bzzzzzzz1 = Button(FramePowerandCurrentR, text="1" , padx = 40,  pady = 20,  command = lambda:   rx1111111(1))
bzzzzzzz2 = Button(FramePowerandCurrentR, text="2",  padx = 40,  pady = 20,  command = lambda:   rx1111111(2))
bzzzzzzz3 = Button(FramePowerandCurrentR, text="3",  padx = 40,  pady = 20,  command = lambda:   rx1111111(3))
bzzzzzzz4 = Button(FramePowerandCurrentR, text="4",  padx = 40,  pady = 20,  command = lambda:   rx1111111(4))
bzzzzzzz5 = Button(FramePowerandCurrentR, text="5",  padx = 40,  pady = 20,  command = lambda:   rx1111111(5))
bzzzzzzz6 = Button(FramePowerandCurrentR, text="6",  padx = 40,  pady = 20,  command = lambda:   rx1111111(6))
bzzzzzzz7 = Button(FramePowerandCurrentR, text="7",  padx = 40,  pady = 20,  command = lambda:   rx1111111(7))
bzzzzzzz8 = Button(FramePowerandCurrentR, text="8",  padx = 40,  pady = 20,  command = lambda:   rx1111111(8))
bzzzzzzz9 = Button(FramePowerandCurrentR, text="9",  padx = 40,  pady = 20,  command = lambda:   rx1111111(9))
bzzzzzzz10 = Button(FramePowerandCurrentR, text="0",  padx = 40,  pady = 20,  command = lambda:   rx1111111(0))
bzzzzzzz11 = Button(FramePowerandCurrentR, text="Clear",  padx = 29,  pady = 20,  command =rx2111111)
bzzzzzzz12 = Button(FramePowerandCurrentR, text=".",  padx = 41.4,  pady = 20,  command =rx3111111)

bzzzzzzz1.place(x = 0  ,y = 80 )
bzzzzzzz2.place(x = 95 ,y = 80 )
bzzzzzzz3.place(x = 190 ,y = 80 )
bzzzzzzz4.place(x = 0 ,y = 145 )
bzzzzzzz5.place(x = 95 ,y = 145 )
bzzzzzzz6.place(x = 190 ,y = 145 )
bzzzzzzz7.place(x = 0 ,y = 210 )
bzzzzzzz8.place(x = 95 ,y = 210 )
bzzzzzzz9.place(x = 190 ,y = 210 )
bzzzzzzz10.place(x = 0,y = 275 )
bzzzzzzz12.place(x = 95,y = 275)
bzzzzzzz11.place(x = 190,y = 275 )


#Part 2
ens111111 = Entry(FramePowerandCurrentR,width=45, borderwidth = 10, state = NORMAL, relief = SUNKEN)
ens111111.place(x =750, y =30)
ens111111.insert(0,"Enter your Current")

azzzzzzz1 = Button(FramePowerandCurrentR, text="1" , padx = 40,  pady = 20,  command = lambda:   rxx1111111(1))
azzzzzzz2 = Button(FramePowerandCurrentR, text="2",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(2))
azzzzzzz3 = Button(FramePowerandCurrentR, text="3",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(3))
azzzzzzz4 = Button(FramePowerandCurrentR, text="4",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(4))
azzzzzzz5 = Button(FramePowerandCurrentR, text="5",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(5))
azzzzzzz6 = Button(FramePowerandCurrentR, text="6",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(6))
azzzzzzz7 = Button(FramePowerandCurrentR, text="7",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(7))
azzzzzzz8 = Button(FramePowerandCurrentR, text="8",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(8))
azzzzzzz9 = Button(FramePowerandCurrentR, text="9",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(9))
azzzzzzz10 = Button(FramePowerandCurrentR, text="0",  padx = 40,  pady = 20,  command = lambda:   rxx1111111(0))
azzzzzzz11 = Button(FramePowerandCurrentR, text="Clear",  padx = 29,  pady = 20,  command =rxx2111111)
azzzzzzz12 = Button(FramePowerandCurrentR, text=".",  padx = 41.4,  pady = 20,  command = rxx3111111)

azzzzzzz1.place(x = 750  ,y = 80 )
azzzzzzz2.place(x = 845 ,y = 80 )
azzzzzzz3.place(x = 940 ,y = 80 )
azzzzzzz4.place(x =750 ,y = 145 )
azzzzzzz5.place(x = 845 ,y = 145 )
azzzzzzz6.place(x = 940 ,y = 145 )
azzzzzzz7.place(x = 750 ,y = 210 )
azzzzzzz8.place(x = 845 ,y = 210 )
azzzzzzz9.place(x = 940 ,y = 210 )
azzzzzzz10.place(x = 750,y = 275 )
azzzzzzz12.place(x = 845,y = 275)
azzzzzzz11.place(x = 940,y = 275 )

azzzzzzz = Button(FramePowerandCurrentR,text = "This is Your Power",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
azzzzzzz.place(x = 0, y = 0)
bzzzzzzz = Button(FramePowerandCurrentR,text = "This is Your Current",state = DISABLED,bg = "red",font = ('Times_New_Roman',11,'bold'),width = 31,foreground = "Blue",)
bzzzzzzz.place(x = 750, y = 0)
czzzzzzz = Button(FramePowerandCurrentR,text = "Click To Solve",bg = "red", relief = SUNKEN,font = ('Algerian',15,'bold'),command = Enter12x)
czzzzzzz.place(x = 440, y = 150)
dzzzzzzz = Button(FramePowerandCurrentR,text = "Answer",bg = "red",relief = SUNKEN , font = ("Arial",15,"bold"),state = DISABLED)
dzzzzzzz.place(x = 440 , y = 200)










root.mainloop()