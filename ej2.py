from random import choices

class Estado:
    def __init__(self,id):
        self.id = id   
    
    def __str__(self) -> str:
        return self.id

class Entorno:
    estado_actual = 0
    recompensa = 0

    def __init__(self,id,estados:list, acciones:dict):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual = 0



    def realizar_accion(self,accion):
        if(accion == acciones["gira_lento"]):
            accionFinal = choices(population=list(acciones),k=1,weights=[0.7,0.3])[0]
        elif(accion == acciones["gira_rapido"]):
            accionFinal = choices(population=list(acciones),k=1,weights=[0.3,0.7])[0]
        
        print(accionFinal)
        if accionFinal == "gira_lento" and self.estado_actual > 0:
            self.estado_actual -= 1
            self.recompensa -= 1
        elif accionFinal == "gira_rapido":
            self.estado_actual += 1
            self.recompensa -= 2
        if str(estados[self.estado_actual]) == "superior":
            print("Fin del juego, el coche ha llegado a la cima con un consumo de: " + str(self.recompensa))
    
    def renderizar(self):
        print()
        auxDibujo = []
        for i in self.estados:
            if str(self.estados[self.estado_actual]) == str(i):
                auxDibujo.append("  *")
            else:
                auxDibujo.append(" ")
        
        for i in range(len(self.estados)):
            print(auxDibujo[i], end="\t")
        print()
        for i in range(len(self.estados)):
            print(list(estados)[i], end="\t")
        print()


acciones = {"gira_lento":0,"gira_rapido":1}
estados = [Estado("bajo"),Estado("medio"),Estado("alto"),Estado("superior")]

entorno = Entorno("ejercicio2",estados, acciones)


#print(estados[entorno.estado_actual])
#entorno.realizar_accion(acciones["gira_rapido"])
#print(estados[entorno.estado_actual])
entorno.renderizar()

