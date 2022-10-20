print("bienvenido")
print("escoje tu arma para iniciar")

print ("M16 (1)")
print("magnum (2)")
print("Catana (3)")
print("RPG (4)")
print("Barret (5)")

vida= 100
arma1= float(input())
curacion1= 15+vida
creditos= 0


import random
from re import A
daño1= random.randint (1,25)

if arma1== 1:
    print ("buena elección")
    

if arma1== 2:
    print("un arma para alguien con mucha agilidad")

if arma1== 3:
    print("el arma de todo un guerrero")

if arma1==4:
    print("Preparese para la destrucción")

if arma1== 5 :
    print("Un arma para alguien con buena precisión y amante del calibre 50")

print("Tambien necesitaras curación en caso de que sufras daños")
print("Toma estos vendajes")
print("Has conseguido 10 vendajes")
print("Tienes un medidor de vida que va de 0 a 100")
print("Si llegas a 0 el juego termina")
print("Suerte")

print("el objetivo es derrotar a todos los enemigos y sobrevivir a cualquier costo")

print (" te has encontrado con tu primer enemigo")
print("presiona (a) para atacar")

def act():
    accion= input()
    if accion==("a"):
        bot1= 25-daño1
        print("el enemigo esta a ", bot1, "de vida")
    if accion==("c"):
        vida= curacion1
        print("vida: ", vida)

act()

