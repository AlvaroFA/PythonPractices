import pandas as pd

nombres = ["Hildegard von Bingen", "Barbara Strozzi", "Fanny Mendelssohn",
           "Clara Schumann", "Lili Boulanger"]
years = [1098, 1619, 1805, 1819, 1893]

'''
Ejercicio 4. Series con índice
Crear una Series con el año de nacimiento de cinco compositoras,
usando sus nombres como índice. Mostrar el año de Clara Schumann (por su etiqueta)
 y las compositoras nacidas después de 1800.
'''

datos= pd.Series(years, index=nombres)
print(f"{datos}");
print("La compositora Clara Schumann", datos["Clara Schumann"])
print(f"compositoras nacidas después de 1800 {datos[datos>1800]}")

'''
Ejercicio 5. Creación de DataFrame a partir de un diccionario
Crear un DataFrame con los datos del diccionario
y mostrar su tamaño (filas y columnas), los nombres de las columnas y el tipo de dato de cada una.
'''

datos_peliculas = {
    "titulo": ["Baila, muchacha, baila", "El autoestopista", "Cleo de 5 a 7",
               "Las margaritas", "La ascensión"],
    "direccion": ["Dorothy Arzner", "Ida Lupino", "Agnès Varda",
                  "Věra Chytilová", "Larisa Shepitko"],
    "anio": [1940, 1953, 1962, 1966, 1977],
    "duracion": [90, 71, 90, 76, 111],
    "color": [False, False, False, True, False],
}

fuente=pd.DataFrame(datos_peliculas)
print(f"El tamaño del dataframe es {fuente.shape}")
print(f"los tipos de datos son {fuente.dtypes}")
print(f"los nombre de las columnas son: {list(fuente.columns)}")

'''
Ejercicio 6. Selección de columnas y filas
Con la tabla de películas, mostrar: la columna titulo;
las columnas titulo y anio; la fila de etiqueta 2 con loc;
y el valor de la última fila en la columna direccion con iloc.
'''
peliculas = pd.DataFrame({
    "titulo": ["Baila, muchacha, baila", "El autoestopista", "Cleo de 5 a 7",
               "Las margaritas", "La ascensión"],
    "direccion": ["Dorothy Arzner", "Ida Lupino", "Agnès Varda",
                  "Věra Chytilová", "Larisa Shepitko"],
    "anio": [1940, 1953, 1962, 1966, 1977],
    "duracion": [90, 71, 90, 76, 111],
})

print(f"Titulos: {peliculas["titulo"]}")
print(f"Peliculas: {peliculas[["titulo","anio"]]}")
print(f"Anio: {peliculas[["titulo","anio"]]}")
print(f"Ultima Directora:{peliculas.iloc[-1]["direccion"]}")

'''
Mostrar el título y el año de las películas estrenadas
antes de 1960 o de más de 100 minutos.
Después, contar cuántas duran entre 75 y 95 minutos, ambos incluidos.
'''
filtro = peliculas[(peliculas["anio"] <  1960) | (peliculas["duracion"] >  100)]
print(f"Peliculas que cumple condiciones {filtro}")

contador = (peliculas["duracion"].between(75,95)).sum();
print(f"Peliculas que duran entre 75 y 95 minutos {contador}")

'''
Ejercicio 8. ORdenación y quedarse con las mayores
Ordenar los libros de más a menos préstamos y mostrar los tres primeros.
Obtener el mismo resultado con un solo método que devuelve directamente las filas con los valores más altos.
'''

libros = pd.DataFrame({
    "titulo": ["Una habitación propia", "La campana de cristal", "Frankenstein",
               "Orgullo y prejuicio", "Nada", "El género en disputa"],
    "prestamos": [34, 29, 41, 38, 26, 9],
})

print(f"el listado de los libros ordenados son: {libros.sort_values("prestamos", ascending=False).head(3)}");
print(f"el listado de los libros ordenados con un metodo solo son: {libros.nlargest(3,"prestamos")}");

'''
Ejercicio 9. Columnas calculadas
Añadir a la tabla dos columnas: siglo, calculada a partir del año (1929 pertenece al siglo 20),
 y paginas_por_prestamo, redondeada a un decimal. Mostrar el título y las dos columnas nuevas.
'''

libracos = pd.DataFrame({
    "titulo": ["Una habitación propia", "Frankenstein", "Los pazos de Ulloa", "Nada"],
    "anio": [1929, 1818, 1886, 1945],
    "paginas": [160, 280, 384, 296],
    "prestamos": [34, 41, 18, 26],
})

libracos["siglos"] = (libracos["anio"] // 100)+1;
libracos["paginasPrestamo"] = (libracos["paginas"] / libracos["prestamos"]).round(1);
print(f"los siglos de los libros son {libracos}")

'''
Ejercicio 10. Leer un describe
Obtener el resumen de la columna paginas con describe,
redondeado a un decimal.
A partir de la salida, indicar si hay algún libro mucho más largo que el resto.
'''

paginas = pd.Series([160, 224, 288, 912, 320, 280, 432, 296],
                    index=["Una habitación propia", "La señora Dalloway",
                           "La campana de cristal", "El segundo sexo",
                           "El género en disputa", "Frankenstein",
                           "Orgullo y prejuicio", "Nada"], name="paginas");

print(f"resumen de la columna paginas: {paginas.describe().round(1)}");
print(f"libro mas largo: {paginas.idxmax()}");


'''
Ejercicio 11. Frecuencias de variable categórica
Contar cuántos libros hay de cada género y calcular la proporción de cada uno, redondeada a tres decimales. Indicar la moda.
'''
genero = pd.Series(["ensayo", "novela", "novela", "novela", "poesía",
                    "ensayo", "ensayo", "novela", "novela", "poesía"]);

valores=genero.value_counts();
print(f"{valores}");
valoresDecimales=genero.value_counts(normalize=True).round(3);
print(f"{valoresDecimales}");
moda= genero.mode();
print("Moda:", genero.mode()[0])
print(f"{moda}")

'''
Ejercicio 12. Resumen por grupos
Calcular el número de libros,
la media y la mediana de préstamos de cada género, con la media redondeada a un decimal.
'''

libros = pd.DataFrame({
    "genero": ["ensayo", "novela", "novela", "poesía", "ensayo",
               "novela", "ensayo", "novela"],
    "prestamos": [34, 21, 29, 8, 15, 41, 9, 26],
})

resultado = libros.groupby("genero").agg(["count","mean","median"]).round(1);
print(f"{resultado.round(1)}")
resultado_ordenado = resultado.sort_values(by=("prestamos","count"),ascending=False)

print(f"{resultado_ordenado.round(1)}")
