#Función que calcule el promedio de las notas dadas

def promedio(alumno1, alumno2, alumno3):
    suma = alumno1 + alumno2 + alumno3
    return suma/3

media = promedio(7, 8, 9)
print("La media de las notas es: ", media)

# Teniendo la función definida, podemos calcular la media de distintas clases

media = promedio(5, 8, 6)
print("La media de las notas es: ", media)

# Pero existe el problema de que si necesitamos agregar una nueva nota, el programa nos larga error. 
# Esto sucede porque la función solo espera tres argumentos 

#---------------------------------------------------------------------#
# Solución -> pensar las notas como una lista
#---------------------------------------------------------------------#

def promedio2(clase):
    return sum(clase) / len(clase)

clase = [7,8,9]
media = promedio2(clase)
print("La media de la clase es:", media)

# Y si necesitamos poner una nota mas solo deberíamos agregar el nuevo dato a la lista "clase"
clase = [7,8,9,5]
media = promedio2(clase)
print("La media de la segunda clase es:", media)








