import pandas as pd

# Crear un DataFrame usando un diccionario
data = {
    "Nombre": ["Ana", "Luis", "Juan", "María"],
    "Edad": [23, 30, 35, 28],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
}

df = pd.DataFrame(data)
df_Ana = df[df["Nombre"] =="Edad"]

print(df)
