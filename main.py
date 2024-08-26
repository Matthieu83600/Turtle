import turtle

def escalier (taille, nb):
    t.forward(taille)
    for i in range(0, nb):
        t.left(90)
        t.forward(taille)
        t.right(90)
        t.forward(taille)

def carre (taille):
    for i in range (0, 4):
        t.forward(taille)
        t.right(90)

def carres(taille_depart, nb):
    for i in range (0, nb):
        taille = (i+1)*taille_depart
        carre(taille)

t = turtle.Turtle()

#escalier(50, 5)
#carre(100)
carres(10, 10)

turtle.done()