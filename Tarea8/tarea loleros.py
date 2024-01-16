características = [
('kawaii',10), ('leal',20), ('acusete',-10), ('avaro',-15), ('respetuoso',20),
('otaku',25),('lolero',25),('furro',-50),('vtuver',25),('mechero',-30)
]

amigos = [('Sneki',('leal','kawaii','vtuver')),
          ('Otaku-taku',('otaku','avaro','lolero','leal')),
          ('Maiga',('paciente','otaku','leal')),
          ('Mojojojo',('mechero','kawaii','Furro','lolero')),
          ('Seiya',('leal','acusete')),
          ('Vegeta',('otaku','avaro')),
          ('Kalila',('lolero','kawaii')),
          ('Grogu',('avaro','kawaii','lolero','otaku')),
          ('Freezer',('acusete','furro','otaku','lolero'))
]


def obtener_valor_caracteristica(características, buscada):
    for c, puntaje in características:
        if buscada == c:
            return puntaje
    return 0


def puntaje_amigo(amigo, características):
    total = 0
    _, caract = amigo
    for cualidad in caract:
        total += obtener_valor_caracteristica(características, cualidad)
    return total




print("Equipo seleccionado:")

mayor = float("-inf")
nombre_mayor=""
mayor1cualis = ""
for amigo in amigos:
    nombre, cualidades = amigo
    for cualidad in cualidades:
        if cualidad == "lolero":
            if mayor < puntaje_amigo(amigo, características):
                mayor = puntaje_amigo(amigo, características)
                nombre_mayor = nombre
                mayor1cualis = cualidades

print(nombre_mayor+",", mayor,"puntos")
amigos2 = list(amigos)
amigos2.remove((nombre_mayor,mayor1cualis))

nombre_mayor2 = ""
mayor2 = 0
for amigo2 in amigos2:
    nombre2, cualidades2 = amigo2
    for cualidad2 in cualidades2:
        if cualidad2 == "lolero":
            if mayor2 < puntaje_amigo(amigo2, características):
                mayor2 = puntaje_amigo(amigo2, características)
                nombre_mayor2 = nombre2
                mayor1cualis2 = cualidades2
print(nombre_mayor2+",", mayor2,"puntos")
