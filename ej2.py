from random import choices

class Entorno2:
    estado_actual = 0
    recompensa = 0

    """
    Función que inicializa el entorno
    """
    def __init__(self,id,estados, acciones):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual = 0
        self.nestados = len(estados)
        self.nacciones = len(acciones)
        self.P = self.generar_tabla_p()

    """
    Función que devuelve el entorno a condiciones iniciales
    """
    def reset(self):
        acciones = {"gira_lento":0,"gira_rapido":1}
        estados = {"bajo":0, "medio": 1,"alto": 2, "superior":3}
        self.__init__("ejercicio2",estados,acciones)
        return self.estado_actual


    """
    Función que obtiene el estado futuro, dado un estado y una acción.
    """  
    def nuevo_estado(self,estado,accion):
        #Obtención de la acción final en función de las probabilidades
        if(accion == self.acciones["gira_lento"]):
            accionFinal = choices(population=list(self.acciones),k=1,weights=[0.7,0.3])[0]
        elif(accion == self.acciones["gira_rapido"]):
            accionFinal = choices(population=list(self.acciones),k=1,weights=[0.3,0.7])[0]
        
        nuevo_estado = 0
        if accionFinal == "gira_lento":
            nuevo_estado = 0
            self.recompensa -= 1
            #Si la accion final es la misma que la pasada por parámetros, se devuelve probabilidad de 0,7
            if accion == accionFinal:
                return 0.7, nuevo_estado, -1
            else:
                return 0.3, nuevo_estado, -1
        elif accionFinal == "gira_rapido":
            #Si esta en el estado superior, no puede subir mas
            if estado == 3:
                return 1.0, estado,-2
            nuevo_estado = estado + 1
            self.recompensa -= 2
            if accion == accionFinal:
                return 0.7, nuevo_estado, -2
            else:
                return 0.3, nuevo_estado, -2


    """
    Función auxiliar para generar las el contenido (acciones) de la tabla p 
    """  
    def nuevo_estado_tabla_p(self,estado,accion):
        fila_tabla = []
        nuevoEstado = 0
        for i in self.acciones.values():
            nuevoEstado = self.nuevo_estado(estado,i)[1]
            if i == accion:
                fila_tabla.append((0.7,nuevoEstado,-2))
            else:    
                fila_tabla.append((0.3,nuevoEstado,-1))
        return fila_tabla


    """
    Función para generar la tabla P necesaria en algunos algoritmos
    """  
    def generar_tabla_p(self):
        P = {}
        for i in range(len(self.estados)):
            acciones = {}
            for accion in self.acciones.values():
                acciones[accion] = self.nuevo_estado_tabla_p(i,accion) 
            P[i] = acciones
        return P


    """
    Función que realiza la acción pasada por parámetros sobre el entorno
    """
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
        if self.estados["superior"] == self.estado_actual:
            return self.estado_actual, self.recompensa, True
        return self.estado_actual, self.recompensa, False
        
    """
    Función que muestra gráficamente el estado del entorno
    """
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