print("bienvenido")
print("escoje tu arma para iniciar")

print ("M16 (1)")
print("magnum (2)")
print("Catana (3)")
print("RPG (4)")
print("Barret (5)")

arma1= float(input())

if arma1==1:
    import random
    from re import A
    daño1= random.randint (1,25)


if arma1==2:
    import random
    from re import A
    daño1= random.randint (1,10)


if arma1==3:
    import random
    from re import A
    daño1= random.randint (5,30)


if arma1==4:
    import random
    from re import A
    daño1= random.randint (25,30)


if arma1==5:
    import random
    from re import A
    daño1= random.randint (2,20)

daño2= random.randint (5,25)

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


def pelea1():
    import random
    bot= random.randint(10,25)
    curas=10
    print("(a) atacar")
    print("(c) curarse")
    print("(e) escapar")

    print("vida del enemigo: ", bot)
    print("curaciones: ", curas)

    vida=100
    while bot>0 and vida>0 or accion!=("e"):
        accion= input()

        if accion==("e"):
            print("La probabilidad de escapar en de un 25%")
            import random
            escape= random.randint(1,4)
            if escape==1:
                print("escape exitoso")
                break
            if escape==2 or escape==3 or escape==4:
                print("fallaste")
                print("Hora de sufrir")
            

        if accion==("a"):
         bot= bot-daño1
         if bot>0:
            print("vida: ", vida)
            print("Vida restante del enemigo: ", bot)

        if bot>0:
            vida= vida-daño2
            print ("El enemigo te ha disparado")
            print("vida: ", vida)
        
        if accion==("c"):
            if vida<100 and curas>=1:
                vida=vida+15
                curas=curas-1
                print ("te has curado")
                print("curaciones: ",curas)
                print("Vida: ", vida)
            if vida>=100:
                print ("ya tienes el maximo de vida")
        
        if vida <=0:
            print ("Que bot")
            quit()
            
        if bot<=0:
            print ("enemigo derrotado")
            print ("vida: ", vida)
            print("curaciones: ",curas)
            import random
            bono= random.randint(50,150)
            global creditos
            creditos=0
            creditos=creditos + bono
            print ("creditos: ", creditos)
            break

pelea1()

print ("Bien hecho soldado")
print("Acabas de sobrevivir a tu primera pelea")
print("Si deseas ir al refugio puedes hacerlo para mejorar tus armas, pero no puedes quedarte ahi para siempre")

print("(q) Continuar")
print("(c) Curarse")
print("(r) Refugio")

desicion=input()
