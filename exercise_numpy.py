import numpy as np

titulos = ["Cleo de 5 a 7", "La felicidad", "Sin techo ni ley",
           "Los espigadores y la espigadora", "Caras y lugares"]
duraciones = [90, 80, 105, 82, 94]

''''
Ejercicio 3. Operaciones con un array de NumPy
Convertir la lista en un array de NumPy, pasar
 todas las duraciones a horas con una sola operación (redondeadas a dos decimales)
 y obtener la media, el máximo y la posición del máximo. Con esa posición, mostrar el título de la película más larga.
'''

datos=np.array(duraciones);
print(datos)

horas = np.round((datos/60),2);
print(f"lista de peliculas en horas {horas}");
media = np.mean(datos);
maximo= np.max(datos);
posicionMaxima = np.argmax(horas);

print(f"media de duracion en horas {media}, el valor maximo es {maximo}, la posicion maxima es {posicionMaxima}");
print(f"La pelicula es {titulos[posicionMaxima]}");
print("La más larga, metodo abreviado:", titulos[horas.argmax()]);

