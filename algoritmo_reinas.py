#Algoritmo_reinas.py
#
#Ricardo Pacheco Urias
#Abraham Sered Gómez Martínez
#Alexandra Iveth Rodriguez Castellanos
#Luis Arturo Dominguez Alatorre

#Función que resuelve el problema de las N reinas recibiendo un número (total de reinas en el tablero NxN) como parámetro
def resolver_n_reinas(n):
    
    # Función que checa si es seguro colocar una reina en una posición específica
    def es_seguro(tablero, fila, col):

        # Checa si hay una reina dentro de la misma fila
        for i in range(col):
            if tablero[fila][i] == 1:
                return False
            
        # Checa si hay una reina dentro de la diagonal que apunta a la esquina superior izquierda
        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False
        # Checa si hay una reina dentro de la diagonal que apunta a la esquina inferior izquierda
        for i, j in zip(range(fila, n), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False
            
        return True

    # Función recursiva que busca todas las soluciones al problema, toma un tablero y una columna como parámetros
    # Coloca una reina en una columna y luego se llama recursivamente para la siguiente columna, cuando encuentra
    # una solución válida la agrega al arreglo de soluciones
    def resolver(tablero, col):

        if col == n:
            soluciones.append([fila[:] for fila in tablero])
            return

        for i in range(n):
            if es_seguro(tablero, i, col):
                tablero[i][col] = 1
                resolver(tablero, col + 1)
                tablero[i][col] = 0

    soluciones = []
    #Pal tablero NxN
    tablero = [[0] * n for _ in range(n)]
    #Esto es pa empezar toda la operación desde la primera posicion de todo el tablero
    resolver(tablero, 0)
    
    if len(soluciones) == 0:
        print(f"No se encontraron soluciones para el problema de las {n} reinas.")
    else:
        print(f"Se encontraron un total de {len(soluciones)} soluciones al problema de las {n} reinas.")
        
        while True:
            print("¿Desea proceder con la impresión de soluciones?: SI: 1  NO: cualquier num")
            decision = int(input())
            if decision == 1:
                break
            else:
                return
                
        for idx, soluciones in enumerate(soluciones):
            print(f"Solución {idx + 1}:")
            for fila in soluciones:
                print(" ".join(map(str, fila)))
            print()


#Menú
print("-------PROBLEMA DE LAS N REINAS--------")
while True:
    print("Ingrese el número de reinas a resolver:")
    n = int(input())
    # Llamada a la función para resolver el problema con 8 reinas
    resolver_n_reinas(n)
    print("Desea hacer otra operación? SI: 1 - NO: cualquier num")
    decision = int(input())
    if decision == 1:
        continue
    else:
        break