# def gaussian_elimination(A, b):
#     """
#     Resuelve el sistema de ecuaciones lineales Ax = b usando
#     eliminación gaussiana y sustitución hacia atrás.
    
#     Args:
#         A: Lista de listas representando una matriz cuadrada de tamaño n x n.
#         b: Lista representando un vector columna de tamaño n.
        
#     Returns:
#         x: Lista representando el vector solución de tamaño n.
#     """
#     n = len(A)  # Número de filas/columnas

#     # Convertir b a una lista para evitar modificaciones no deseadas
#     b = b[:]

#     # Eliminación gaussiana
#     for k in range(n):
#         # Pivotear si el elemento pivote es cero
#         if A[k][k] == 0:
#             for i in range(k + 1, n):
#                 if A[i][k] != 0:
#                     # Intercambiar filas
#                     A[k], A[i] = A[i], A[k]
#                     b[k], b[i] = b[i], b[k]
#                     break
#             else:
#                 raise ValueError("El sistema no tiene solución única (matriz singular).")

#         # Escalonar las filas
#         for i in range(k + 1, n):
#             factor = A[i][k] / A[k][k]
#             for j in range(k, n):
#                 A[i][j] -= factor * A[k][j]
#             b[i] -= factor * b[k]

#     # Sustitución hacia atrás
#     x = [0] * n
#     for i in range(n - 1, -1, -1):
#         suma = sum(A[i][j] * x[j] for j in range(i + 1, n))
#         x[i] = (b[i] - suma) / A[i][i]

# #  [int(num) for num in float_array]
#     return [int(num) for num in x]

# # Ejemplo de entrada
# A = [[2, -1, 1], [1, 3, 2], [1, 0, 0]]
# b = [2, 6, 1]

# # Llamar a la función y mostrar el resultado
# x = gaussian_elimination(A, b)
# print("x =", x)





# import numpy as np

# def gaussian_elimination(A, b):
#     """
#     Solve Ax = b using Gaussian elimination and back substitution.
#     """
#     n = len(b)
#     # Augment the matrix A with vector b
#     Ab = np.hstack((A, b.reshape(-1, 1)))

#     # Forward elimination
#     for i in range(n):
#         # Pivot to avoid division by zero
#         for k in range(i, n):
#             if Ab[k, i] != 0:
#                 Ab[[i, k]] = Ab[[k, i]]  # Swap rows
#                 break
#         else:
#             raise ValueError("Matrix is singular or nearly singular.")

#         # Make the diagonal element 1 and eliminate below
#         for j in range(i + 1, n):
#             factor = Ab[j, i] / Ab[i, i]
#             Ab[j, i:] -= factor * Ab[i, i:]

#     # Back substitution
#     x = np.zeros(n)
#     for i in range(n - 1, -1, -1):
#         x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:])) / Ab[i, i]

#     return x

# # Example Usage
# # A = np.array([[2.0, 1.0, -1.0],
# #               [-3.0, -1.0, 2.0],
# #               [-2.0, 1.0, 2.0]])
# # b = np.array([8.0, -11.0, -3.0])

# # Example Usage
# A = np.array([[2.0,-1.0,1.0],
#               [1.0,3.0,2.0],
#               [1.0,0.0,0.0]])
# b = np.array([2.0,6.0,1.0])

# x = gaussian_elimination(A.astype(float), b.astype(float))
# print("Solution:", x.astype(int))





############## Using nunpuy

import numpy as np

def gaussian_elimination_to_int(A, b):
    """
    Resuelve el sistema de ecuaciones lineales Ax = b usando eliminación gaussiana.
    Trabaja exclusivamente con enteros.
    :param A: Matriz cuadrada de coeficientes (n x n).
    :param b: Vector columna de términos independientes (n x 1).
    :return: Vector solución x con valores enteros.
    """
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

# # Ejemplo de uso
A = np.array([[2, -1, 1], [1, 3, 2], [1, 0, 0]])
b = np.array([2, 6, 1])

x = gaussian_elimination_to_int(A, b)

print("Vector solución x :", x)






# ### Whitout nunpy 

# def gaussian_elimination_to_int(A, b):
#     """
#     Resuelve un sistema de ecuaciones lienales Ax = b usando reduccion gaussiana 
#     con sustitucion hacia atras
#     :param A: Matriz Cuadrada n x n. 
#     :param: B: Vector columna b de tamaño n x b
#     :return: Vector solucion n x b 
    
#     """
#     # numero de filas
#     n = len(A)
#     A = [[float(val) for val in fila] for fila in A]

#     for i in range(n):
#         # Partial pivoting
#         if A[i][i] == 0:
#             for k in range(i + 1, n):
#                 if A[k][i] != 0:
#                     A[i], A[k] = A[k], A[i]  # Swap rows
#                     b[i], b[k] = b[k], b[i]
#                     break
#             else:
#                 raise ValueError("Matrix is singular or no unique solution exists.")

#         # Eliminate entries below the pivot
#         for j in range(i + 1, n):
#             factor = A[j][i] / A[i][i]
#             for k in range(i, n):
#                 A[j][k:] -= factor * A[i][k:]
#             b[j] -= factor * b[i]

#     # Back substitution
#     x = [0] * n
#     for i in range(n - 1, -1, -1):
#         x[i] = b[i]
#         for j in range(i + 1, n):
#             x[i] -= A[i][j] * x[j]
#         x[i] /= A[i][i]

#     return x

# Example of usage
# A = [[2, -1, 1],
#      [3, 3, 9],
#      [3, 3, 5]]

# b = [2, -1, 3]

# A = [[2, -1, 1], [1, 3, 2], [1, 0, 0]]
# b = [2, 6, 1]

# x = gaussian_elimination_to_int(A, b)
# print("Solution vector x:", x)