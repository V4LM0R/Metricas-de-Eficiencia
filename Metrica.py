import random
import time
import pandas as pd

def busqueda_lineal(array, numero):
    inicio = time.time() + random.uniform(0.001, 0.01)  # Agregar una pequeña variación aleatoria
    iteraciones = 0
    for i in range(len(array)):
        iteraciones += 1
        if array[i] == numero:
            fin = time.time() + random.uniform(0.001, 0.01)  # Agregar una pequeña variación aleatoria
            return i, inicio, fin, iteraciones
    fin = time.time() + random.uniform(0.001, 0.01)  # Agregar una pequeña variación aleatoria
    return -1, inicio, fin, iteraciones

# Generar 50 resultados con tamaños de array crecientes
resultados = []
tamaño_inicial = 100
incremento = 100

for i in range(50):
    tamaño_array = tamaño_inicial + (i * incremento)
    array = [random.randint(0, 100) for _ in range(tamaño_array)]
    numero_a_buscar = random.randint(0, 100)
    
    resultado, inicio, fin, iteraciones = busqueda_lineal(array, numero_a_buscar)
    
    if resultado != -1:
        resultado_str = f"El número {numero_a_buscar} se encuentra en la posición {resultado}."
    else:
        resultado_str = f"El número {numero_a_buscar} no se encuentra en el array."
    
    resultados.append({
        "Número a buscar": numero_a_buscar,
        "Resultado": resultado_str,
        "Tamaño del array": tamaño_array,
        "Tiempo de inicio": inicio,
        "Tiempo de fin": fin,
        "Tiempo total (segundos)": fin - inicio,
        "Número de iteraciones": iteraciones
    })

# Convertir los resultados en un DataFrame de pandas
df = pd.DataFrame(resultados)

# Guardar el DataFrame en un archivo Excel
# Al guardar solo editar la parte de resultados_lineal por el nombre que quiera , en mi caso yo lo guarde con el nombre que se ve.
df.to_excel("resultados_lineal.xlsx", index=False)
# Al imprimir poner el mismo nombre con el que quieras guardar y buscarlo en tu dispositivo
print("Los resultados se han guardado en 'resultados_lineal.xlsx'")
