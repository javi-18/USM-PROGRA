


def avistamientos_por_región(nombre_archivo):
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    plantilla= "En el mes {0} de {1} hubo{2} de avistamientos confirmados de un total{3}\n"
    cant_archivos=0
    contador=0
    d ={}
    for linea in archivo:
        datos=linea.strip().split(";")
        fecha,región,informados,ovnis,aviones,satélites,otros=datos
        año,mes=fecha.split("-")
        informados=int(informados)
        ovnis=int(ovnis)
        porcentaje=round((ovnis/informados)*100,2) +str("%")
        if región not in d:
            d[región]=[]
        tupla=(mes,año,porcentaje)
        d[región].append(tupla)
    archivo.close()

    for región in d:
        d[región].sort()
        d[región].reverse()
        nuevo=open(región+".txt","w")
        if contador <=3:
            for info in d[región]:
                mes,año,porcentaje=info
                line=plantilla.format(mes,año,porcentaje)
                nuevo.write(line)
            contador+=1
            cant_archivos+=1
        nuevo.close()
    return cant_archivos            





