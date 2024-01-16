Valor_prop=int(input("Valor propiedad en UF(1500-13000):"))
Pie=int(input("Ingrese el % del pie (20%-45%):"))
Plazo=int("Ingrese Plazo (20,25,30):"))
Vivienda=int(input("Tipo vivienda Casa(1) o Departamento(2):"))
Estado= int(input("Estado vivienda Nueva(1) o Usada(2):"))
if Valor_prop <1500 and >13000 :
    print("ERROR:Valor fuera de rango")

    else:
        if Pie<20 and >45 :
            print("ERROR:Valor fuera de rango")
            else:
                if Plazo!=20 or Plazo!=25 or Plazo!=30 :
                    print("ERROR:Valor fuera de rango")
                    else:
                        if Vivienda!=1 and Vivienda!=2:
                            print("ERROR:Valor fuera de rango")
                            else:
                                
                        
    elif Valor_prop>=1500 and <=13000:
        Valor_a_pagar= Valor_prop-(Valor_prop*pie)
        
            
    
    
