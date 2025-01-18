intro = """
    Realiza la factorización LU de una matriz cuadrada no singular A.
    :param A: Matriz cuadrada de tamaño n x n (no singular).
    :return: Matrices L y U tales que A = LU.
    """

def lu_factorizacion(A):
    
    n = len(A)

    # Inicializa matrices L y U
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    # Descompocision LU
    for i in range(n):
        # Llenar fila U
        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        # Llenar columna L
        L[i][i] = 1  # Diagonal de 1s
        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] //= U[i][i]

    return L, U

### Imprimir matriz
def print_matriz(M):
    for fila in M:
      print(fila)
    

# Caso de ejemplo
A =  [[4, 3, 0],
     [3, 7, -1],
     [0, -1, 4]]

L, U = lu_factorizacion(A)

print(intro)

print("Matriz trinagular: ")
print_matriz(A)

print("\nMatriz L (Triangular inferior):")
print_matriz(L)

print("\nMatriz U (Triangulo superior):")
print_matriz(U)
