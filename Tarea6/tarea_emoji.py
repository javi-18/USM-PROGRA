mensaje= input("Ingrese texto:")
reemplazo=True
while reemplazo:
    signif= input("Ingrese significados:")
    signif= signif.upper()
    if mensaje=="$" or mensaje=="*":
        reemplazo=False
        
    else:
        i=0
        s=0
        traduccion=""
        emoji=""
        while i<len(mensaje):
            
                
            if signif==mensaje[i:i+len(signif)]:
                traduccion+=signif
                i+= len(signif)
                
            else:
                traduccion+=mensaje[i]
                i+=1
            if signif[i:i+len(signif)]=="*":
                emoji+=signif
                traduccion=emoji+mensaje
            else:
                signif[i:]
                traduccion= mensaje
                s+=1
                
        print("Texto traducido:",traduccion)
        
    mensaje=traduccion        


 
 
 
 
