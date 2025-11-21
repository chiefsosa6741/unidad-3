#proyecto submodulo 
import tkinter as tk
from tkinter import ttk,Toplevel,font


ventana= tk.Tk()
ventana.title("contador")
ventana.geometry("300x260")
ventana.resizable(0,0)
d=0
c=0
b=0
l=0
def buton1():
    vent.deiconify()

def reg():
    global d
    print (d)

    if d<1:
   
     c= str(entnombre.get())
     b= int(entaportacion.get())
     etinom1.config(text=c)
     etiapo1.config(text=b)
     print (c)
     print (b)
     print (d)
     d=+1

    elif d<2:
   
     c= str(entnombre.get())
     b= int(entaportacion.get())
     etinom2.config(text=c)
     etiapo2.config(text=b)
     print (c)
     print (b)
     print (d)
     d=d+1


    elif d<3:
   
     c= str(entnombre.get())
     b= int(entaportacion.get())
     etinom3.config(text=c)
     etiapo3.config(text=b)
     print (c)
     print (b)
     d=d+1



    elif d<4:
   
     c= str(entnombre.get())
     b= int(entaportacion.get())
     etinom4.config(text=c)
     etiapo4.config(text=b)
     print (c)
     print (b)
     d=d+1
   

    elif d<5:
   
     c= str(entnombre.get())
     b= int(entaportacion.get())
     etinom5.config(text=c)
     etiapo5.config(text=b)
     print (c)
     print (b)
     d=d+1


    elif d<6:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom6.config(text=c)
      etiapo6.config(text=b)
      print (c)
      print (b)
      d=d+1


    elif d<7:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom7.config(text=c)
      etiapo7.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<8:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom8.config(text=c)
      etiapo8.config(text=b)
      print (c)
      print (b)
      d=d+1


    elif d<9:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom9.config(text=c)
      etiapo9.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<10:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom10.config(text=c)
      etiapo10.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<11:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom11.config(text=c)
      etiapo11.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<12:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom12.config(text=c)
      etiapo12.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<13:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom13.config(text=c)
      etiapo13.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<14:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom14.config(text=c)
      etiapo14.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<15:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom15.config(text=c)
      etiapo15.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<16:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom16.config(text=c)
      etiapo16.config(text=b)
      print (c)
      print (b)
      d=d+1
    elif d<17:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom17.config(text=c)
      etiapo17.config(text=b)
      print (c)
      print (b)
      d=d+1
    elif d<18:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom18.config(text=c)
      etiapo18.config(text=b)
      print (c)
      print (b)
      d=d+1

    elif d<19:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom19.config(text=c)
      etiapo19.config(text=b)
      print (c)
      print (b)
      d=d+1


    elif d<20:
   
      c= str(entnombre.get())
      b= int(entaportacion.get())
      etinom20.config(text=c)
      etiapo20.config(text=b)
      print (c)
      print (b)
      d=d+1


etimax=tk.Label(ventana,text="maximo 20")
etinombre=tk.Label(ventana,text="Nombre: ")
etiaportacion=tk.Label(ventana,text="aportacion: ")
entnombre=tk.Entry(ventana,fg="black")
entaportacion=tk.Entry(ventana)
btn_reg=tk.Button(ventana,text="registrar",command=reg)
btn_ver=tk.Button(ventana,text="ver",command=buton1)
etinombre.grid(row=6,column=0,columnspan=30,rowspan=30,pady=1,sticky="NW")
entnombre.grid(row=8,column=6,sticky="w")
etiaportacion.grid(row=6,column=15,sticky="NW")
entaportacion.grid(row=8,column=15,sticky="E")
btn_ver.grid(row=18,column=6,sticky="S")
btn_reg.grid(row=18,column=15,sticky="S")

vent=Toplevel()
vent.title("aportaciones")
vent.withdraw()
etinomtit2=tk.Label(vent,text="Nombres: ")
etiapotit2=tk.Label(vent,text="aportaciones :")
vent.geometry("480x800")
etinom1=tk.Label(vent,text="sin datos ")
etinom2=tk.Label(vent,text="sin datos ")
etinom3=tk.Label(vent,text="sin datos ")
etinom4=tk.Label(vent,text="sin datos ")
etinom5=tk.Label(vent,text="sin datos ")
etinom6=tk.Label(vent,text="sin datos ")
etinom7=tk.Label(vent,text="sin datos ")
etinom8=tk.Label(vent,text="sin datos ")
etinom9=tk.Label(vent,text="sin datos ")
etinom10=tk.Label(vent,text="sin datos ")
etinom11=tk.Label(vent,text="sin datos ")
etinom12=tk.Label(vent,text="sin datos ")
etinom13=tk.Label(vent,text="sin datos ")
etinom14=tk.Label(vent,text="sin datos ")
etinom15=tk.Label(vent,text="sin datos ")
etinom16=tk.Label(vent,text="sin datos ")
etinom17=tk.Label(vent,text="sin datos ")
etinom18=tk.Label(vent,text="sin datos ")
etinom19=tk.Label(vent,text="sin datos ")
etinom20=tk.Label(vent,text="sin datos ")


etiapo1=tk.Label(vent,text="sin datos ")
etiapo2=tk.Label(vent,text="sin datos ")
etiapo3=tk.Label(vent,text="sin datos ")
etiapo4=tk.Label(vent,text="sin datos ")
etiapo5=tk.Label(vent,text="sin datos ")
etiapo6=tk.Label(vent,text="sin datos ")
etiapo7=tk.Label(vent,text="sin datos ")
etiapo8=tk.Label(vent,text="sin datos ")
etiapo9=tk.Label(vent,text="sin datos ")
etiapo10=tk.Label(vent,text="sin datos ")
etiapo11=tk.Label(vent,text="sin datos ")
etiapo12=tk.Label(vent,text="sin datos ")
etiapo13=tk.Label(vent,text="sin datos ")
etiapo14=tk.Label(vent,text="sin datos ")
etiapo15=tk.Label(vent,text="sin datos ")
etiapo16=tk.Label(vent,text="sin datos ")
etiapo17=tk.Label(vent,text="sin datos ")
etiapo18=tk.Label(vent,text="sin datos ")
etiapo19=tk.Label(vent,text="sin datos ")
etiapo20=tk.Label(vent,text="sin datos ")


etinomtit2.grid(column=0,row=1,pady=20,sticky="w")


etinom1.grid(column=0,row=2)
etinom2.grid(column=0,row=3) 
etinom3.grid(column=0,row=4)
etinom4.grid(column=0,row=5)
etinom5.grid(column=0,row=6)
etinom6.grid(column=0,row=7)
etinom7.grid(column=0,row=8)
etinom8.grid(column=0,row=9)
etinom9.grid(column=0,row=10)
etinom10.grid(column=0,row=11)
etinom11.grid(column=0,row=12)
etinom12.grid(column=0,row=13)
etinom13.grid(column=0,row=14)
etinom14.grid(column=0,row=15)
etinom15.grid(column=0,row=16)
etinom16.grid(column=0,row=17)
etinom17.grid(column=0,row=18)
etinom18.grid(column=0,row=19)
etinom19.grid(column=0,row=20)
etinom20.grid(column=0,row=21)


etiapotit2.grid(column=3,row=1,sticky="E")


etiapo1.grid(column=200,row=2)
etiapo2.grid(column=200,row=3)
etiapo3.grid(column=200,row=4)
etiapo4.grid(column=200,row=5)
etiapo5.grid(column=200,row=6)
etiapo6.grid(column=200,row=7)
etiapo7.grid(column=200,row=8)
etiapo8.grid(column=200,row=9)
etiapo9.grid(column=200,row=10)
etiapo10.grid(column=200,row=11)
etiapo11.grid(column=200,row=12)
etiapo12.grid(column=200,row=13)
etiapo13.grid(column=200,row=14)
etiapo14.grid(column=200,row=15)
etiapo15.grid(column=200,row=16)
etiapo16.grid(column=200,row=17)
etiapo17.grid(column=200,row=18)
etiapo18.grid(column=200,row=19)
etiapo19.grid(column=200,row=20)
etiapo20.grid(column=200,row=21)

ventana.mainloop()