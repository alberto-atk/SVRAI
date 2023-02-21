from random import choices

class Estado:
    def __init__(self,x,y,es_reward):
        self.x = x   
        self.y = y
        self.es_reward = es_reward
    def __str__(self) -> str:
        return "Estado: " + str(self.x) + " " + str(self.y) + " rw: " + str(self.es_reward)

class Entorno:
    estado_actual = Estado(-1,-1,False)
    recompensa = 0

    def __init__(self,id,estados:dict, acciones:dict):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual =  choices(population=list(estados),k=1)[0]

        
    def realizar_accion(self,accion):
        pesos = []
        if accion in acciones:
            #Generacion de los pesos para realizar un movimiento u otro
            for i in (list(self.acciones)):
                if i == accion:
                    pesos.append(0.7)
                else:
                    pesos.append(0.1)

            #Obtencion de la accion
            print(self.estado_actual)
            accionFinal = choices(population=list(acciones),k=1,weights=pesos)[0]
            print(accionFinal)
            if accionFinal == "up":
                self.estado_actual = Estado(self.estado_actual.x-1,self.estado_actual.y,self.estado_actual.es_reward)
            elif accionFinal == "right":
                self.estado_actual = Estado(self.estado_actual.x,self.estado_actual.y+1,self.estado_actual.es_reward)
            elif accionFinal == "left":
                self.estado_actual = Estado(self.estado_actual.x,self.estado_actual.y-1,self.estado_actual.es_reward)
            elif accionFinal == "down":
                self.estado_actual = Estado(self.estado_actual.x+1,self.estado_actual.y,self.estado_actual.es_reward)
            
            if self.estado_actual.x < 0:
                self.estado_actual.x = 0
            if self.estado_actual.y < 0:
                self.estado_actual.y = 0
            if self.estado_actual.x > 9:
                self.estado_actual.x = 9
            if self.estado_actual.y > 9:
                self.estado_actual.y = 9

            print(self.estado_actual)



acciones = {"left":0,"right":1,"up":2,"down":3}

estados = []
for i in range(10):
    for j in range(10):
        estados.append(Estado(i,j,False))

entorno = Entorno("ejercicio3",estados, acciones)
entorno.realizar_accion("up")