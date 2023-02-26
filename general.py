from ej1 import *
from ej2 import *
from ej3 import *
from ej4 import *
import numpy as np

def ejercicio1():

    acciones = {"no_gira":0,"gira":1} #no gira y gira
    estados = {"bajo":0, "medio": 1,"alto": 2 }

    entorno = Entorno1("ejercicio1",estados, acciones)

    entorno.definir_movimientos(estados["alto"],acciones["gira"],estados["alto"])
    entorno.definir_movimientos(estados["alto"],acciones["no_gira"],estados["medio"])

    entorno.definir_movimientos(estados["medio"],acciones["gira"],estados["alto"])
    entorno.definir_movimientos(estados["medio"],acciones["no_gira"],estados["bajo"])

    entorno.definir_movimientos(estados["bajo"],acciones["gira"],estados["medio"])
    entorno.definir_movimientos(estados["bajo"],acciones["no_gira"],estados["bajo"])
    return entorno


def ejercicio2():
    acciones = {"gira_lento":0,"gira_rapido":1}
    estados = {"bajo":0, "medio": 1,"alto": 2, "superior":3}


    entorno = Entorno2("ejercicio2",estados, acciones)

    return entorno

def ejercicio3():
    acciones = {"left":0,"right":1,"up":2,"down":3}

    cuadricula = []
    for i in range(10):
        cuadricula.append([])
        for j in range(10):
            cuadricula[i].append(0)

    cuadricula[7][8] = 10
    cuadricula[2][7] = 3
    cuadricula[4][3] = -5
    cuadricula[7][3] = -10
    entorno = Entorno3("ejercicio3",cuadricula, acciones)

    return entorno

def ejercicio4():
    acciones = {"left":0,"right":1,"up":2,"down":3}


    entorno = Entorno4("ejercicio4", acciones)

    return entorno


def valueIterationEj3(env):
    def lookahead(U,s,a,gamma=0.8):
        suma = 0
        for sp in range(len(estados)):
            suma += R[s][a][sp] + gamma*np.sum(T[s][a][sp]*U[sp])
        return suma
    
    def backup(env,U,estado):
        return max([lookahead(U,estado,a) for a in list(env.acciones.values())])

    nS = len(env.estados)
    nA = len(env.acciones)

    estados = list(env.estados.values())
    acciones = list(env.acciones.values())
    T = np.zeros([nS, nA, nS])
    R = np.zeros([nS, nA, nS])
    for state_number,s in enumerate(estados):
        for a in acciones:
            p_trans,next_s,rew = env.nuevo_estado(s,a)
            T[state_number,a,next_s] += p_trans
            R[state_number,a,next_s] = rew
            T[state_number,a,:]/=np.sum(T[state_number,a,:])

    print("T: " + str(T))
    print("R: " + str(R))
    U = [0.0 for s in range(nS)]
    max_iters = 10000
    for i in range(max_iters):
        U = [backup(env,U,s) for s in range(nS)]
    print("U: " + str(U))

def valueIterationEjs12(env):
    def lookahead(U,s,a,gamma=0.8):
        suma = 0
        for sp in range(len(estados)):
            suma += R[s][a][sp] + gamma*np.sum(T[s][a][sp]*U[sp])
        return suma
    
    def backup(env,U,estado):
        return max([lookahead(U,estado,a) for a in list(env.acciones.values())])

    nS = len(env.estados)
    nA = len(env.acciones)

    estados = list(env.estados.values())
    acciones = list(env.acciones.values())
    T = np.zeros([nS, nA, nS])
    R = np.zeros([nS, nA, nS])
    for state_number,s in enumerate(estados):
        for a in acciones:
            p_trans,next_s,rew = env.nuevo_estado(s,a)
            T[state_number,a,next_s] += p_trans
            R[state_number,a,next_s] = rew
            T[state_number,a,:]/=np.sum(T[state_number,a,:])

    print("T: " + str(T))
    print("R: " + str(R))
    U = [0.0 for s in range(nS)]
    max_iters = 10000
    for i in range(max_iters):
        U = [backup(env,U,s) for s in range(nS)]
    print("U: " + str(U))

def qlearning(env):
    q_table = np.zeros([env.nestados, env.nacciones])
    import random

    # Hyperparameters
    alpha = 0.1
    gamma = 0.6
    epsilon = 0.1

    # For plotting metrics
    all_epochs = []
    all_penalties = []
    for i in range(1, 1001):
        state = env.reset()

        epochs, penalties, reward, = 0, 0, 0
        done = False
        
        while epochs < 1000:
            if random.uniform(0, 1) < epsilon:
                action = random.choice(list(env.acciones.values()) if isinstance(env.acciones,dict) else env.acciones) # Explore action space
            else:
                action = np.argmax(q_table[state]) # Exploit learned values
            next_state, reward, done = env.realizar_accion(action) 
            
            old_value = q_table[state, action]
            next_max = np.max(q_table[next_state])
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value

            if reward == -10:
                penalties += 1
            state = next_state
            epochs += 1
            if done == True:
                break
            
        if i % 100 == 0:
            print(f"Episode: {i}")

    print("Training finished.\n")


    total_epochs, total_penalties = 0, 0
    episodes = 100

    for _ in range(episodes):
        state = env.reset()
        epochs, penalties, reward = 0, 0, 0
        
        done = False
        
        while epochs < 1000:
            action = np.argmax(q_table[state])
            state, reward, done= env.realizar_accion(action)

            if reward == -10:
                penalties += 1

            epochs += 1
            if done == True:
                break

        total_penalties += penalties
        total_epochs += epochs

    print(f"Results after {episodes} episodes:")
    print(f"Average timesteps per episode: {total_epochs / episodes}")
    print(f"Average penalties per episode: {total_penalties / episodes}")
    return q_table

#valueIteration12(ejercicio2())
q_table = qlearning(ejercicio3())
print(q_table)

