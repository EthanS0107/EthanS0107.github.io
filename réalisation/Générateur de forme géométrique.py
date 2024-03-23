# Créé par Ethan Serville, le 30/12/2015 en Python 3.2
from tkinter import *
from random import randint

def UnRond():
    B10.place(x=25,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    X=randint(0,400)
    Y=randint(0,400)
    Z=randint(0,200)
    Rand_color="#"+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]
    TBCercle.append(Grille.create_oval(X,Y,X+Z,Y+Z,fill=Rand_color))

def DixRond():
    B10.place(x=25,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    indice=0
    while indice in range(10):
        Rand_color="#"+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]
        X=randint(0,400)
        Y=randint(0,400)
        Z=randint(0,200)
        TBCercle.append(Grille.create_oval(X,Y,X+Z,Y+Z,fill=Rand_color))
        indice=indice+1

def CentRond():
    B10.place(x=25,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    indice=0
    while indice in range(100):
        Rand_color="#"+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]
        X=randint(0,400)
        Y=randint(0,400)
        Z=randint(0,200)
        TBCercle.append(Grille.create_oval(X,Y,X+Z,Y+Z,fill=Rand_color))
        indice=indice+1

def UnTriangle():
    B11.place(x=226,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    X=randint(0,400)
    Y=randint(0,400)
    D=randint(0,400)
    Z=randint(0,200)
    Rand_color="#"+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]
    TBTriangle.append(Grille.create_polygon(X,Y,D,X+Z,Y+Z,D+Z,fill=Rand_color))

def DixTriangle():
    B11.place(x=226,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    indice=0
    while indice in range(10):
        Rand_color="#"+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]
        X=randint(0,400)
        Y=randint(0,400)
        D=randint(0,400)
        Z=randint(0,200)
        TBTriangle.append(Grille.create_polygon(X,Y,D,X+Z,Y+Z,D+Z,fill=Rand_color))
        indice=indice+1

def CentTriangle():
    B11.place(x=226,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    indice=0
    while indice in range(100):
        Rand_color="#"+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]
        X=randint(0,400)
        Y=randint(0,400)
        D=randint(0,400)
        Z=randint(0,200)
        TBTriangle.append(Grille.create_polygon(X,Y,D,X+Z,Y+Z,D+Z,fill=Rand_color))
        indice=indice+1

def UnCarré():
    B12.place(x=427,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    X=randint(0,400)
    Y=randint(0,400)
    Z=randint(0,200)
    Rand_color="#"+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]+Tbbase16[randint(0,15)]
    TBCarré.append(Grille.create_rectangle(X,Y,X+Z,Y+Z,fill=Rand_color))

def DixCarré():
    B12.place(x=427,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    indice=0
    while indice in range(10):
        Rand_color="#"+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]
        X=randint(0,400)
        Y=randint(0,400)
        Z=randint(0,200)
        TBCarré.append(Grille.create_rectangle(X,Y,X+Z,Y+Z,fill=Rand_color))
        indice=indice+1

def CentCarré():
    B12.place(x=427,y=450)
    Tbbase16=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    indice=0
    while indice in range(100):
        Rand_color="#"+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]+Tbbase16[randint(0,14)]
        X=randint(0,400)
        Y=randint(0,400)
        Z=randint(0,200)
        TBCarré.append(Grille.create_rectangle(X,Y,X+Z,Y+Z,fill=Rand_color))
        indice=indice+1

def SuprimerRond():
    if len(TBCercle)==0:
        B10.place_forget()
    elif len(TBCercle) !=0 :
        Grille.delete(TBCercle.pop())
        if len(TBCercle)==0:
            B10.place_forget()
def SuprimerPolygonne():
    if len(TBTriangle)==0:
        B11.place_forget()
    elif len(TBTriangle) !=0 :
        Grille.delete(TBTriangle.pop())
        if len(TBTriangle)==0:
            B11.place_forget()

def SuprimerCarré():
    if len(TBCarré)==0:
        B12.place_forget()
    elif len(TBCarré) !=0 :
        Grille.delete(TBCarré.pop())
        if len(TBCarré)==0:
            B12.place_forget()


fen1= Tk()
fen1.title("dessin")
fen1.geometry("850x550")

TBCercle=[]
TBTriangle=[]
TBCarré=[]
Grille=Canvas(fen1,width=400,heigh=400,bg="black")
Grille.place(x=20,y=20)

#rond
B1=Button(fen1,text="CRÉER ROND",width=15,height=7,bg="black",fg="yellow",command=UnRond)
B1.place(x=430,y=25)
B2=Button(fen1,text="CRÉER ROND*10",width=15,height=7,bg="black",fg="orange",command=DixRond)
B2.place(x=430,y=160)
B3=Button(fen1,text="CRÉER ROND*100",width=15,height=7,bg="black",fg="red",command=CentRond)
B3.place(x=430,y=300)

#triangle
B4=Button(fen1,text="CRÉER POLYGON",width=15,height=7,bg="black",fg="yellow",command=UnTriangle)
B4.place(x=560,y=25)
B5=Button(fen1,text="CRÉER POLYGON*10",width=15,height=7,bg="black",fg="orange",command=DixTriangle)
B5.place(x=560,y=160)
B6=Button(fen1,text="CRÉER POLYGON*100",width=15,height=7,bg="black",fg="red",command=CentTriangle)
B6.place(x=560,y=300)

#carré
B7=Button(fen1,text="CRÉER RÉCTANGLE",width=15,height=7,bg="black",fg="yellow",command=UnCarré)
B7.place(x=690,y=25)
B8=Button(fen1,text="CRÉER RÉCTANGLE*10",width=15,height=7,bg="black",fg="orange",command=DixCarré)
B8.place(x=690,y=160)
B9=Button(fen1,text="CRÉER RÉCTANGLE*100",width=15,height=7,bg="black",fg="red",command=CentCarré)
B9.place(x=690,y=300)

#Boutton suprimer
B10=Button(fen1,text="SUPRIMER ROND",width=20,fg="purple",command=SuprimerRond)
B11=Button(fen1,text="SUPRIMER POLYGONNE",width=20,fg="purple",command=SuprimerPolygonne)
B12=Button(fen1,text="SUPRIMER CARRÉ",width=20,fg="purple",command=SuprimerCarré)

fen1.mainloop()