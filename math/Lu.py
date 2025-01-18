# import numpy as np

# def lu_factorization(A):
#     """
#     Realiza la factorización LU de una matriz cuadrada no singular A.
#     :param A: Matriz cuadrada de tamaño n x n (no singular).
#     :return: Matrices L y U tales que A = LU.
#     """
#     n = A.shape[0]
#     L = np.eye(n)  # Matriz identidad inicial para L
#     U = A.copy()   # Copia de A para trabajar en la matriz U

#     for i in range(n):
#         if U[i, i] == 0:
#             raise ValueError("La matriz es singular y no puede factorizarse en LU.")
        
#         for j in range(i + 1, n):
#             factor = U[j, i] / U[i, i]
#             L[j, i] = factor
#             U[j, i:] -= factor * U[i, i:]

#     return L, U

# # Ejemplo de uso
# A = np.array([[4.0, 3.0, 0.0],
#               [3.0, 7.0, -1.0],
#               [0.0, -1.0, 4.0]])

# L, U = lu_factorization(A)

# print("Matriz L (triangular inferior unitaria):")
# print(L.astype(int))
# print("\nMatriz U (triangular superior):")
# print(U.astype(int))

import numpy as np

def lu_factorization(A):
    """
    Realiza la factorización LU de una matriz cuadrada no singular A.
    :param A: Matriz cuadrada de tamaño n x n (no singular).
    :return: Matrices L y U (enteras) tales que A = LU.
    """
    n = A.shape[0]
    L = np.eye(n, dtype=int)  # Matriz identidad inicial para L (entera)
    U = A.astype(float)       # Trabajar en flotantes para operaciones

    for i in range(n):
        if U[i, i] == 0:
            raise ValueError("La matriz es singular y no puede factorizarse en LU.")
        
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = int(factor)  # Guardar en L como entero
            U[j, i:] -= factor * U[i, i:]

    # Redondear y convertir a enteros
    U = np.round(U).astype(int)
    return L, U

# Ejemplo de uso
A = np.array([[4, 3, 0],
              [3, 7, -1],
              [0, -1, 4]])

L, U = lu_factorization(A)

print("Matriz L (triangular inferior unitaria):")
print(L)
print("\nMatriz U (triangular superior):")
print(U)