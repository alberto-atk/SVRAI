from random import choices

class Estado:
    def __init__(self,id):
        self.id = id   
    
    def __str__(self) -> str:
        return self.id

class Entorno2:
    estado_actual = 0
    recompensa = 0

    def __init__(self,id,estados:list, acciones:dict):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual = 0
        self.nestados = len(estados)
        self.nacciones = len(acciones)

    def reset(self):
        acciones = {"gira_lento":0,"gira_rapido":1}
        estados = [Estado("bajo"),Estado("medio"),Estado("alto"),Estado("superior")]
        self.__init__("ejercicio2",estados,acciones)
        return self.estado_actual

    def nuevo_estado(self,estado,accion):
        if(accion == self.acciones["gira_lento"]):
            accionFinal = choices(population=list(self.acciones),k=1,weights=[0.7,0.3])[0]
        elif(accion == self.acciones["gira_rapido"]):
            accionFinal = choices(population=list(self.acciones),k=1,weights=[0.3,0.7])[0]
        
        nuevo_estado = 0
        if accionFinal == "gira_lento":
            nuevo_estado = 0
            self.recompensa -= 1
            if accion == accionFinal:
                return 0.7, nuevo_estado, -1
            else:
                return 0.3, nuevo_estado, -1
        elif accionFinal == "gira_rapido":
            if estado == 3:
                return 1.0, estado,-2
            nuevo_estado = estado + 1
            self.recompensa -= 2
            if accion == accionFinal:
                return 0.7, nuevo_estado, -2
            else:
                return 0.3, nuevo_estado, -2


    def realizar_accion(self,accion):
        if(accion == self.acciones["gira_lento"]):
            accionFinal = choices(population=list(self.acciones),k=1,weights=[0.7,0.3])[0]
        elif(accion == self.acciones["gira_rapido"]):
            accionFinal = choices(population=list(self.acciones),k=1,weights=[0.3,0.7])[0]
        
        if accionFinal == "gira_lento" and self.estado_actual > 0:
            self.estado_actual -= 1
            self.recompensa -= 1
        elif accionFinal == "gira_rapido":
            self.estado_actual += 1
            self.recompensa -= 2
        if str(self.estados[self.estado_actual]) == "superior":
            return self.estado_actual, self.recompensa, True
        return self.estado_actual, self.recompensa, False
        
    
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
            print(list(self.estados)[i], end="\t")
        print()

"""
acciones = {"gira_lento":0,"gira_rapido":1}
estados = [Estado("bajo"),Estado("medio"),Estado("alto"),Estado("superior")]

entorno = Entorno2("ejercicio2",estados, acciones)


#print(estados[entorno.estado_actual])
#entorno.realizar_accion(acciones["gira_rapido"])
#print(estados[entorno.estado_actual])
entorno.renderizar()

"""