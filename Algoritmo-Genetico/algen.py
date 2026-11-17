import random

#Evolución paso a paso para maximizar la cantidad de unos (OneMax)

# --- FUNCIONES BASE ---
def calcular_fitness(individuo):
    return sum(individuo)

def crear_poblacion(cantidad_individuos, longitud_bits):
    poblacion = []
    for _ in range(cantidad_individuos):
        individuo = [random.randint(0, 1) for _ in range(longitud_bits)]
        poblacion.append(individuo)
    return poblacion

def seleccion_torneo(poblacion):
    individuo1 = random.choice(poblacion)
    individuo2 = random.choice(poblacion)
    fitness1 = calcular_fitness(individuo1)
    fitness2 = calcular_fitness(individuo2)
    if fitness1 > fitness2:
        return individuo1
    else:
        return individuo2

def cruce(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_corte] + padre2[punto_corte:]
    hijo2 = padre2[:punto_corte] + padre1[punto_corte:]
    return hijo1, hijo2

def mutacion(individuo, tasa_mutacion=0.05):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            if individuo[i] == 0:
                individuo[i] = 1
            else:
                individuo[i] = 0
    return individuo

# --- PARÁMETROS FIJOS ---
TAMANO_POBLACION = 20
LONGITUD_BITS = 15
GENERACIONES = 50
TASA_MUTACION = 0.05

# --- EJECUCIÓN PRINCIPAL ---
# Quitamos el if st.button() y ejecutamos directo
print("Iniciando ...\n")

poblacion = crear_poblacion(TAMANO_POBLACION, LONGITUD_BITS)
historial_fitness = []

for generacion in range(GENERACIONES):
    nueva_poblacion = []
    
    while len(nueva_poblacion) < TAMANO_POBLACION:
        padre1 = seleccion_torneo(poblacion)
        padre2 = seleccion_torneo(poblacion)
        
        hijo1, hijo2 = cruce(padre1, padre2)
        
        hijo1 = mutacion(hijo1, TASA_MUTACION)
        hijo2 = mutacion(hijo2, TASA_MUTACION)
        
        nueva_poblacion.extend([hijo1, hijo2])
        
    poblacion = nueva_poblacion
    
    # Registrar el mejor fitness de esta generación
    mejor_individuo = max(poblacion, key=calcular_fitness)
    mejor_puntaje = calcular_fitness(mejor_individuo)
    historial_fitness.append(mejor_puntaje)
    
    # Imprimir el progreso en la terminal en lugar de la barra de progreso
    print(f"Generación {generacion + 1:02d} | Mejor fitness: {mejor_puntaje:02d}/{LONGITUD_BITS} | Individuo: {mejor_individuo}")

print("\nEvolucion finalizada.")
print(f"Mejor individuo final: {mejor_individuo} (Fitness: {mejor_puntaje}/{LONGITUD_BITS})")