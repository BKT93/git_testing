def leap_year(year):  # Definimos la función
    return

year = 2020  # Aquí podemos trabajar con la variable fija y a continuación realizar la validación con type

# ---------------------------------------------------------------------------------------------------------------------
# year=int(input("Introduzca un año: ") ---> también podemos trabajar con un input y asignar el valor a la variable year
# ---------------------------------------------------------------------------------------------------------------------

if type(year) == int:  # Realizamos la validación para comprobar que el dato sea de tipo entero
    if year % 4 != 0:
        print(f"El año {year} no es bisiesto")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"El año {year} es bisiesto")
    elif year % 400 == 0 and year % 100 != 0:
        print(f"El año {year} es bisiesto")
    elif year % 100 == 0:
        print(f"El año {year} no es bisiesto")
else:  # En caso de que se haya ingresado un número no entero
    print(f"{year} no es un año. Por favor introduzca un año.")
