# Tarea 1: Resoluci´on de Sistemas de Ecuaciones Lineales
### Docente: Dylan Benavides C

## MA0323: Metodos numericos 

### Reduccion gaussiana consustitucion hacia atras

definicion del algoritmo 

```bash
    Resuelve el sistema de ecuaciones lineales Ax = b usando eliminación gaussiana.
    Trabaja exclusivamente con enteros.
    :in A: Matriz cuadrada de coeficientes (n x n).
    :in b: Vector columna de términos independientes (n x 1).
    :return: Vector solución x con valores enteros.
```


ejemplo del uso: 
 - agremos una matriz n x n y un vector n x 1

```python
A = np.array([[2, -1, 1], [1, 3, 2], [1, 0, 0]])
b = np.array([2, 6, 1])
```

### Factorizacion LU

