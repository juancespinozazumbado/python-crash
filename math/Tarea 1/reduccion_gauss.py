import numpy as np

intro =  """
    Resuelve el sistema de ecuaciones lineales Ax = b usando eliminación gaussiana.
    Trabaja exclusivamente con enteros.
    :param A: Matriz cuadrada de coeficientes (n x n).
    :param b: Vector columna de términos independientes (n x 1).
    :return: Vector solución x con valores enteros.
    """
def gaussian_elimination_to_int(A, b):
   
    n = len(A)
    
    # Trabajamos inicialmente con flotantes para cálculos internos
    A = A.astype(float)
    b = b.astype(float)

    # Eliminación Gaussiana
    for i in range(n):
        # Pivoteo parcial para asegurar que A[i, i] no sea cero
        if A[i, i] == 0:
            for k in range(i + 1, n):
                if A[k, i] != 0:
                    A[[i, k]] = A[[k, i]]  # Intercambio de filas
                    b[[i, k]] = b[[k, i]]
                    break
            else:
                raise ValueError("La matriz es singular y no tiene solución única.")

        # Escalonar
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i] #eliminamos los puntos flotantes para evitrar modificaciones no deseadas

    # Convertir a enteros
    x = np.round(x).astype(int)
    return x


print(intro)
# # Ejemplo de uso
# A = np.array([[2, -1, 1], [1, 3, 2], [1, 0, 0]])
# b = np.array([2, 6, 1])
# salida esperada [ 1 1 1 ]

A = np.array([[2.0, -1.0, 1.0],
              [1.0,  3.0, 2.0],
              [1.0, -1.0, 2.0]])

b = np.array([8.0, 13.0, 5.0])
#Salida esperada [ 4 2 1 ]
print("Matriz: ", A)
print("Vector: ", b)

x = gaussian_elimination_to_int(A, b)

print("Vector solución x :", x)