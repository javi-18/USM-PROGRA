vacunas = {
"Sinovac":["11.111.111-1", "12.345.678-9"],
"Pfizer": ["8.978.657-3"],
"CanSino": ["13.789.456-k"]
}


dosis = {
"11.111.111-1":[55,(2021,4,11),(2021,5,10)],
"12.345.678-9":[47,(2021,6,3)],
"8.978.657-3":[79,(2021,3,23)],
"13.789.456-k":[40,(2021,5,18),(2021,6,10)]
}

dia=int(input("Día:"))
mes=int(input("Mes:"))
año=int(input("Año:"))
fecha = (año, mes, dia)
continuar=True

while continuar==True:
    rut=input("RUT:")
    if rut not in dosis:
        edad = int(input("Edad:"))

        dosis[rut] = [edad,(año, dia, mes)]
        vac = input("Tipo vacuna:")
        if vac not in vacunas:
            vacunas[vac] = rut
        else:
            vacunas[vac].append(rut)
    else:
        dosis[rut].append(fecha)
        for vacuna in vacunas:
            if rut in vacunas[vacuna]:
                print("Segunda dosis. Paciente debe ser inoculado con:", vacuna)
    mas_datos = input("¿Desea continuar? (s/n):")
    if mas_datos == "n":
        continuar = False

print("Edades con más personas con esquema de inoculación completo:")
vacunados = {}
for rut in dosis:
    if len(dosis[rut])>2:
        if dosis[rut][0] not in vacunados:
            vacunados[dosis[rut][0]] = 0
        vacunados[dosis[rut][0]] += 1
listo = []
for persona in vacunados:
    listo.append((persona,vacunados[persona]))

contador = 0
while contador < 3:
    i = 0
    cant = 0
    for edad, cuantos in listo:
        if cant< cuantos:
            cant = cuantos
            i = edad
    print(i, "años:", cant, "personas")
    listo.remove((i, cant))
    contador +=1

#para probar el codigo se uso el ejemplo del pdf