#Ejercicio1

with open("/Users/ismaelcorralalonso/Desktop/archivo.txt", "r", encoding="latin-1") as fichero:
    for linea in fichero:
        print(linea.strip())

#Ejercicio2

with open("/Users/ismaelcorralalonso/Desktop/archivo.txt", "r", encoding="latin-1") as fichero:
    lineas = fichero.readlines()
    print("Número de filas:", len(lineas))


#Ejercicio3

with open("/Users/ismaelcorralalonso/Desktop/archivo.txt", "r", encoding="latin-1") as fichero:
    texto = fichero.read()
    palabras = len(texto)
    print(palabras)


#Ejercicio4

with open("/Users/ismaelcorralalonso/Desktop/archivo.txt", "r", encoding="latin-1") as fichero:
    texto = fichero.read()
    clave = 0
    for palabra in texto.split():
        if palabra.lower() == "el":
            clave += 1

print(f"Hay {clave} ocurrencias de la palabra 'el'.")


#Ejercicio5

with open("/Users/ismaelcorralalonso/Desktop/archivo.txt", "r", encoding="latin-1") as fichero:
    texto = fichero.read()  # Falta paréntesis
    palabras = texto.split()
    palabras_cortas = [palabra for palabra in palabras if len(palabra) < 4]

    print(f"Hay {len(palabras_cortas)} palabras de menos de 4 caracteres")
    

#Ejercicio 5 modificado 

def contar_palabras_cortas(ruta_archivo, longitud_maxima):
    try:
        with open(ruta_archivo, "r", encoding="latin-1") as fichero:
            texto = fichero.read()
            palabras = texto.split()
            palabras_cortas = [palabra for palabra in palabras if len(palabra) < longitud_maxima]
            return len(palabras_cortas)
    except FileNotFoundError:
        print(f"El archivo en la ruta {ruta_archivo} no se encontró.")
        return 0    
ruta = "/Users/ismaelcorralalonso/Desktop/archivo.txt"
longitud = 4
cantidad = contar_palabras_cortas(ruta, longitud)
print(f"Hay {cantidad} palabras de menos de {longitud} caracteres en el archivo.")



#Ejercicio6

with open("/Users/ismaelcorralalonso/Desktop/archivo.txt", "r", encoding="latin-1") as fichero:
    for linea in fichero:
        linea_buscada = linea.strip()
        if "EL MUNDO ES REDONDO" in linea_buscada:
            print("#".join(linea_buscada))


#Ejercicio7

import string

for letra in string.ascii_uppercase:
    archivos = f"{letra}.txt"
    with open(archivos, "w", encoding="utf-8") as f: 
        f.write(f"Este archivo es {archivos}")

print("Creados los archivos")


#Ejercicio8

with open ("python.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Texto.\n")
    Nuevo_texto = archivo.write("Nuevo texto añadido.\n")

with open ("python.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    print(texto)


#Ejercicio9

def frencuencia_palabras(archivo):
    with open("/Users/ismaelcorralalonso/Desktop/archivo.txt", "r", encoding="latin-1") as fichero:
        texto = fichero.read().lower()
        palabras = texto.split()
        frecuencia = {}

        for palabra in palabras: 
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    
    return frecuencia
archivo = "/Users/ismaelcorralalonso/Desktop/archivo.txt"
frecuencias = frencuencia_palabras("/Users/ismaelcorralalonso/Desktop/archivo.txt")
for palabra, veces in frecuencias.items():
    print(f"{palabra}: {veces}")


#Ejercicio10

archivo = "/Users/ismaelcorralalonso/Desktop/archivo.txt"

try:
    with open(archivo, "r", encoding="utf-8") as f:
        print(f"El archivo '{archivo}' existe.")
except FileNotFoundError:
    print(f"El archivo '{archivo}' no existe.")


#Ejercicio2.1

import pandas as pd

df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")


print("Primeras cinco filas:")
print(df.head())
print("Ultimas cinco filas:")
print(df.tail())


#Ejercicio2.2

import pandas as pd

df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")
df.fillna(0, inplace=True)
print(df)


#Ejercicio2.3

import pandas as pd 
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")
df = df.dropna(subset=["price"])
coche = df.loc[df["price"].idxmax()]
print(coche[["company", "price"]])

#Ejercicio2.4

import pandas as pd 
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")
toyota = df[df["company"].str.lower() == "toyota"]
print(toyota)

#Ejercicio2.5
import pandas as pd 
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")
coches_empresa = df["company"].value_counts()
print(coches_empresa)

#Ejercicio2.6

import pandas as pd
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")
precio_alto = df.groupby("company") ["price"].idxmax()
coche_caro = df.loc[precio_alto]
print(coche_caro)

#Ejercicio2.7

import pandas as pd 
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")
df["average-mileage"] = pd.to_numeric(df["average-mileage"], errors="coerce")
media_km = df.groupby("company")["average-mileage"].mean()
print(media_km)

#Ejercicio2.8

import pandas as pd
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/datos definitivos t.5.csv", sep=";", encoding="latin-1")
orden_precio = df.sort_values(by="price")
print(orden_precio)

#Ejercicio2.9

import pandas as pd 

GermanCars = {"Company": ["Ford", "Mercedes", "BMV", "Audi"],
              "Price": [23845, 171995,125925, 71400]}
JapaneseCars = {"Company": ["Toyota", "Honda", "Nissan", "Mitsubishi"],
                "Price": [29995, 23600, 61500, 58900]}

df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(JapaneseCars)

df_juntos = pd.concat([df_german, df_japanese])
print(df_juntos)

#Ejercicio2.10

import pandas as pd 

Car_Price = {"Company": ["Toyota", "Honda", "BMV", "Audi"],
             "Price": [23845, 17995, 135925, 71400]}
Car_horsepower = {"Company": ["Toyota", "Honda", "BMV", "Audi"],
                  "Horsepower": [141, 80, 182, 160]}
df_carprice = pd.DataFrame(Car_Price)
df_powerhorse = pd.DataFrame(Car_horsepower)
df_juntos = pd.merge(df_carprice, df_powerhorse, on="Company")
print(df_juntos)

#Ejercicio3.1

import numpy as np
array = np.random.randint(0, 100, size=(4, 2), dtype=np.uint16)
print("Array:\n", array)
print("Dimensiones:", array.ndim)
print("Forma:", array.shape)
print("Tamaño de cada elemento (bytes):", array.itemsize)

#Ejercicio3.2
import numpy as np
matriz = np.arange(100, 200, 10).reshape(5, 2)
print(matriz)   

#Ejercicio3.3
import numpy as np
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
tercera_columna = sampleArray[:, 2]
print(tercera_columna)  

#Ejercicio3.4
import numpy as np
sampleArray = np.array([[3, 6,9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
resultado = sampleArray[1::2, ::2]
print(resultado)  

#Ejercicio3.5
import numpy as np
array1 = np.array([[5,6,9], [21,18,27]])
array2 = np.array([[15,33,24], [4,7,1]])
suma = (array1 + array2)
print(suma)
cuadrado = np.square(suma)
print(cuadrado) 

#Ejercicio3.6
import numpy as np
matriz = np.arange(10, 34).reshape(8, 3)
submatrices = np.array_split(matriz, 4)
for i, submatriz in enumerate(submatrices):
    print(f"Submatriz {i+1}:\n{submatriz}\n")   

#Ejercicio3.7
import numpy as np
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]]) 
caso1 = sampleArray[sampleArray[2].argsort()]
print(caso1) 
caso2 = sampleArray[sampleArray[:, 2].argsort()]  
print(caso2)

#Ejercicio3.8
import numpy as np
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
max_eje0 = np.max(sampleArray, axis=0)
min_eje1 = np.min(sampleArray, axis=1)
print("Maximo del eje 0:", max_eje0)
print("Minimo del eje 1:", min_eje1)    

#Ejercicio3.9
import numpy as np        
sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
newColumn = np.array([[10, 10, 10]])
modificado = np.delete(sampleArray, 1, axis=1)
nuevo = np.insert(modificado, 1, newColumn, axis=1)
print(nuevo)

#Ejercicio4.1
import pandas as pd
import matplotlib.pyplot as plt    
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
plt.plot(df["month_number"], df["total_profit"], marker='o')
plt.title("Beneficios totales por mes")
plt.xlabel("Número de mes")
plt.ylabel("Beneficio total")
plt.grid()
plt.show()  

#Ejercicio4.2
import pandas as pd
import matplotlib.pyplot as plt    
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
plt.plot(df["month_number"], df["total_units"], linestyle='--', color='red', marker='o', linewidth=3, label="Unidades vendidas")
plt.title("Unidades vendidas por mes")
plt.xlabel("Número de mes")
plt.ylabel("Número de unidades vendidas")
plt.legend(loc='lower right')
plt.grid()
plt.show()

#Ejercicio4.3
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
plt.plot(df["month_number"], df["facecream"], marker='o', label="Face Cream")
plt.plot(df["month_number"], df["facewash"], marker='o', label="Face Wash")
plt.plot(df["month_number"], df["toothpaste"], marker='o', label="Toothpaste")
plt.plot(df["month_number"], df["bathingsoap"], marker='o', label="Bathing Soap")
plt.plot(df["month_number"], df["shampoo"], marker='o', label="Shampoo")
plt.plot(df["month_number"], df["moisturizer"], marker='o', label="Moisturizer")
plt.title("Ventas de productos por mes")
plt.xlabel("Número de mes")
plt.ylabel("Número de unidades vendidas")
plt.legend() 
plt.show()

#Ejercicio4.4
import pandas as pd     
import matplotlib.pyplot as plt 
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
plt.scatter(df["month_number"], df["toothpaste"], color='blue', marker='o')
plt.title("Ventas de pasta de dientes por mes")
plt.xlabel("Número de mes")
plt.ylabel("Unidades vendidas de pasta de dientes")
plt.grid(True, linestyle='-')
plt.show()    

#Ejercicio4.5
import pandas as pd    
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
bar_width = 0.35
months = df["month_number"]
facecream_sales = df["facecream"]
facewash_sales = df["facewash"] 
index = range(len(months))  
plt.bar(index, facecream_sales, bar_width, label="Face Cream", color='b')
plt.bar([i + bar_width for i in index], facewash_sales, bar_width, label="Face Wash", color='r')
plt.xlabel("Número de mes")
plt.ylabel("Unidades vendidas")
plt.title("Ventas de crema facial y lavado facial por mes")
plt.xticks([i + bar_width / 2 for i in index], months)
plt.legend()
plt.show()  

#Ejercicio4.6
import pandas as pd     
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
plt.bar(df["month_number"], df["bathingsoap"], color='blue')
plt.title("Ventas de jabón por mes")
plt.xlabel("Número de mes")
plt.ylabel("Unidades vendidas de jabón")
plt.savefig("/Users/ismaelcorralalonso/Desktop/ventas_jabon.png")
plt.show()  

#Ejercicio4.7
import pandas as pd    
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
plt.hist(df["total_profit"], bins=5, color='green', edgecolor='black')
plt.title("Histograma de beneficios totales por mes")
plt.xlabel("Beneficio total")
plt.ylabel("Frecuencia")
plt.show()  

#Ejercicio4.8
import pandas as pd    
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
total_sales = {
    "Face Cream": df["facecream"].sum(),
    "Face Wash": df["facewash"].sum(),
    "Toothpaste": df["toothpaste"].sum(),
    "Bathing Soap": df["bathingsoap"].sum(),
    "Shampoo": df["shampoo"].sum(),
    "Moisturizer": df["moisturizer"].sum()
}       
labels = total_sales.keys()
sizes = total_sales.values()    
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Porcentaje de ventas totales por producto en el último año")
plt.axis('equal')
plt.legend(loc="lower right")
plt.show()  

#Ejercicio4.9
import pandas as pd    
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
fig, ax = plt.subplots()
ax.plot(df["month_number"], df["bathingsoap"], marker='o', color='purple')
ax.set_title("Ventas de jabón de baño por mes")
ax.set_xlabel("Número de mes")
ax.set_ylabel("Unidades vendidas de jabón de baño")
plt.show()  

#Ejercicio4.10
import pandas as pd    
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/ismaelcorralalonso/Desktop/mat ejercicios.csv", sep=";", encoding="latin-1")
plt.stackplot(df["month_number"],
              df["facecream"],
              df["facewash"],
              df["toothpaste"],
              df["bathingsoap"],
              df["shampoo"],
              df["moisturizer"],
              labels=["Face Cream", "Face Wash", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"])
plt.title("Ventas de productos por mes")
plt.xlabel("Número de mes")
plt.ylabel("Unidades vendidas")
plt.legend(loc='upper left')
plt.show()  






