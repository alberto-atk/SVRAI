from random import choices

class Estado:
    def __init__(self,id):
        self.id = id   
    
    def __str__(self) -> str:
        return self.id

class Entorno1:
    movimientos = {}
    estado_actual = Estado("estado_indeterminado")
    recompensa = 0

    def __init__(self,id,estados:dict, acciones:dict):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual = estados[choices(list(estados), k=1)[0]]

    
    def definir_movimientos(self,estado1:Estado,accion,estado2:Estado):
        self.movimientos[(estado1,accion)] = estado2

    def realizar_accion(self,accion):
        self.estado_actual = self.movimientos[(self.estado_actual,accion)]
        if str(self.estado_actual) == "bajo":
            self.recompensa -= 1
        else:
            self.recompensa += 2
    
    def renderizar(self):
        print()
        auxDibujo = []
        for i in self.estados.values():
            if self.estado_actual == i:
                auxDibujo.append("  *")
            else:
                auxDibujo.append(" ")
        
        for i in range(len(self.estados)):
            print(auxDibujo[i], end="\t")
        print()
        for i in range(len(self.estados)):
            print(list(self.estados)[i], end="\t")
        print()




acciones = {"no_gira":0,"gira":1} #no gira y gira
estados = {"bajo":Estado("bajo"), "medio": Estado("medio"),"alto": Estado("alto") }

entorno = Entorno1("ejercicio1",estados, acciones)

entorno.definir_movimientos(estados["alto"],acciones["gira"],estados["alto"])
entorno.definir_movimientos(estados["alto"],acciones["no_gira"],estados["medio"])

entorno.definir_movimientos(estados["medio"],acciones["gira"],estados["alto"])
entorno.definir_movimientos(estados["medio"],acciones["no_gira"],estados["bajo"])

entorno.definir_movimientos(estados["bajo"],acciones["gira"],estados["medio"])
entorno.definir_movimientos(estados["bajo"],acciones["no_gira"],estados["bajo"])


#entorno.realizar_accion(acciones["no_gira"])
entorno.renderizar()
entorno.realizar_accion(acciones["no_gira"])
entorno.renderizar()
