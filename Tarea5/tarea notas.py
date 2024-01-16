def media_aritmetica(nota1,nota2,nota3):
    suma=nota1+nota2+nota3
    promedio=round((suma)/3)
    return promedio

def media_geometrica(nota1,nota2,nota3):
    multi= nota1*nota2*nota3
    media= round((multi)**(1/3))
    return media

def media_vuelta(media_aritmetica,nota3):
    nota= round((nota3*(media_aritmetica)**2)**(1/3))
    return nota

def aprobacion(media_aritmetica,media_geometrica,media_vuelta):
    if media_aritmetica >=55:
        return 1
    elif media_geometrica >=55:
        return 2
    elif media_vuelta >=55:
        return 3
    else:
        return 0


#Primero se definen las 4 funciones que se usaran en el programa( va desde la linea 1 a la linea 23
#En las lineas 45,46,47 y 53 se llaman las funciones correspondientes





pedir_notas = True
while pedir_notas:
    ramo = input("Ingrese el nombre del ramo: ")

    if ramo == "salir":
        pedir_notas = False
        print("Fin del programa - Desarrollado por Kiwi :D!")
    else:
        n1 = int(input("Ingrese la 1era nota: "))
        n2 = int(input("Ingrese la 2era nota: "))
        n3 = int(input("Ingrese la 3era nota: "))

        nf_aritmetica = media_aritmetica(n1,n2,n3)
        nf_geometrica = media_geometrica(n1,n2,n3)
        nf_vuelta = media_vuelta(nf_aritmetica,n3)

        print("Su nota final según la Media Aritmética es:", nf_aritmetica)
        print("Su nota final según la Media Geométrica es:", nf_geometrica)
        print("Su nota final según la Media Vuelta es:", nf_vuelta)

        nf_aprobacion = aprobacion(nf_aritmetica,nf_geometrica,nf_vuelta)

        if nf_aprobacion == 0:
            print("Lamentablemente no puedes aprobar con ninguna de las fórmulas :'c")
        elif nf_aprobacion == 1:
            print("Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 2:
            print("Si la NF del ramo se calcula usando la Media Geométrica, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 3:
            print("Si la NF del ramo se calcula usando la Media Vuelta, entonces apruebas", ramo, ":D")
