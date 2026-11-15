'''
Ejercicio 1. Suma, recuento y media de una lista
Calcular, sin ninguna biblioteca,
la suma de las duraciones,
el número de películas y la duración media, redondeada a un decimal.
'''

duraciones = [90, 80, 105, 82, 94]

totalSumas = sum(duraciones);
numero= len(duraciones);
duracionMedia= round(totalSumas / numero,1);

print(f"Suma total es {totalSumas}, numero de peliculas {numero}, duracion media {duracionMedia}");

'''
Ejercicio 2. Recorrer una lista con una condición
Contar cuántas películas duran más de 85 minutos
, primero con un bucle for y un if,
y después en una sola línea con una lista por comprensión.
Mostrar también la lista de esas duraciones.
'''

'''
ojo con las tabulaciones, en python importan
'''
peliculas=0
for x in duraciones:
    if(x > 85):
        peliculas += 1
print(f"numero de peliculas mayor de 85 es:{peliculas}");

linea = [x for x in duraciones if x >85 ]
print(f"Misma condicion, mas de 85 en una linea {len(linea)}");


