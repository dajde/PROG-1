import turtle
import math
"""Nastavime pzadie, vygenerujeme si korytnacku, schovame ju a mastavime rychlost vykreslovania"""
turtle.delay(0)
bob = turtle.Turtle()
bob.speed(0)
bob.ht()

def polyline(t, n, length,angle):
    """Korytnacka vykresli ciaru v n krokoch, pricom v kazdom kroku ide o length dalej a
    natoci sa o angle dolava """
    for i in range (n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """ Najprv vypocitame dlzku obluku pomocou 2*pi*r a skratime ho len na nasu ziadanu dlzku
        n sa bude rovnat dlzke obluka podelenej styrmi, cize si ho rozdelime na n krokov, +3
        dlzku jedneho kroku vyratame z dlzky obluka podelenou poctom krokov
        uhol jedneho kroku podobne
    """
    arc_length = 2 * math.pi * r * abs(angle)/360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle/n)
    """Vykreslime ciaru  """
    polyline(t,n, step_length, step_angle)

def lupen(t,r,uhol):
    """ Lupen nakreslime tak, ze urobime jeden obluk, potom sa otocime naspat a urobime
    druhy obluk
    """
    for i in range(2):
        arc(bob,r,uhol)
        t.lt(180-uhol)

def kvet(t,n,r,uhol,farba):
    """ Vyratame uhol, o ktory sa korytnacka otoci po kazdom lupienku, pricom n je pocet lupienkov
    Nastavime farbu pera a vyplnenie lupienkov
    """
    angle = 360/n
    t.pencolor(farba)
    t.fillcolor(farba)
    t.begin_fill()
    """ Vykreslime n lupienkov, zakazdym sa otocime o vopred vyratany uhol, aby nam vysiel
    kvet do kruhu """
    for i in range(n):
        lupen(t,r,uhol)
        t.lt(angle)
    t.end_fill()
        
def stonka(t,dlzka,zakryvenie):
    """Nastavime farbu pera, nasmerujeme korytnacku najprv kolmo nahor, a neskor o polovicu uhla
    zakryvenia stonky, aby stonka nakoniec skoncila kolmo nad jej zaciatkom
    Stonka je obluk kruznice
    """
    t.pencolor("green")
    t.seth(90)
    t.lt(zakryvenie/2)
    arc(t,dlzka,-zakryvenie)

def listy(t,dlzka,sirka,uhol):
    """Nastavime farbicky"""
    t.pencolor("green")
    t.fillcolor("green")
    t.begin_fill()
    """Nastavime uhol kolmo nahor a nasledne bud pricitame alebo odcitame uhol, ktory maju zvierat so zemou
    otocime korytnacku o sirka/2 aby bol list v spravnom uhle
    vykreslime dva obluky, ktore tvoria nas list
    """
    for i in [-1,1]:
        t.seth(90+(i*uhol))
        t.rt(0+sirka/2)
        arc(t,dlzka,sirka)
        t.lt(180-sirka)
        arc(t,dlzka,sirka)

    t.end_fill()

def rastlina(xzaciatok,t,Nlupenov,r,Kuhol,Sdlzka,Szakryvenie,Lvelkost,Lsirka,Luhol,farba):
    """Posenieme xove suradnice a nastavime hrubku pera
    """
    t.width(3)
    t.pu()
    t.setpos(xzaciatok,0)
    t.pd()
    """ zavolame vsetky tri funkcie na vykreslenie celeho kvetu
    """
    listy(t,Lvelkost,Lsirka,Luhol)
    stonka(t,Sdlzka,Szakryvenie)
    kvet(t,Nlupenov,r,Kuhol,farba)
    """zaverecna zlta "bodka"
    """
    t.width(20)
    t.pencolor("yellow")
    t.fd(1)
    t.bk(1)

"""Vsetky tri funkcie zavolane v jednej,
    prva je o kvete
    druha stonka
    tretia listy
"""

rastlina(0,bob,Nlupenov=7,r=60,Kuhol=60,
         
         Sdlzka=400,Szakryvenie=20,
         
         Lvelkost=150,Lsirka=50,Luhol=90,farba="red")

rastlina(-200,bob,Nlupenov=10,r=40,Kuhol=80,
         
         Sdlzka=80,Szakryvenie=180,
         
         Lvelkost=100,Lsirka=50,Luhol=45, farba="blue")

rastlina(200,bob,Nlupenov=20,r=140,Kuhol=20,
         
         Sdlzka=350,Szakryvenie=45,
         
         Lvelkost=50,Lsirka=100,Luhol=60, farba="purple")

"""
Kvety z knihy:

7,60,60
10,40,80
20,140,20
"""




