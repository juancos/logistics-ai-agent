import pandas as pd
import os

# Ruta del archivo de clientes
ARCHIVO_CLIENTES = "data/raw/clientes.xls"
# Verificar que el archivo existe
if not os.path.exists(ARCHIVO_CLIENTES):
    print(f"❌ Archivo no encontrado: {ARCHIVO_CLIENTES}")
    exit()

# Cargar el archivo .xls
try:
    df = pd.read_excel(ARCHIVO_CLIENTES)
    print("✅ Archivo cargado correctamente.")
except Exception as e:
    print(f"❌ Error al cargar el archivo: {e}")
    exit()
# Vista general
print("\n📊 Dimensiones del archivo:")
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

print("\n📌 Columnas del archivo:")
print(df.columns.tolist())

print("\n🧼 Tipos de datos:")
print(df.dtypes)

print("\n🔍 Primeras filas:")
print(df.head())

# 🔍 Valores nulos por columna
print("\n🧼 Valores nulos por columna:")
print(df.isnull().sum())

# 🧾 Porcentaje de nulos
print("\n📊 Porcentaje de nulos por columna:")
print((df.isnull().mean() * 100).round(2))

# 📦 Filas duplicadas
print("\n📦 Filas duplicadas:")
print(df.duplicated().sum())

# 🧬 Cardinalidad de columnas
print("\n🔢 Cardinalidad (valores únicos) por columna:")
print(df.nunique())

# 📊 Estadísticas descriptivas de columnas numéricas
print("\n📈 Estadísticas de columnas numéricas:")
print(df.describe())

# 🔤 Distribución de columnas categóricas
columnas_categoricas = df.select_dtypes(include='object').columns

print("\n🔤 Frecuencia de valores categóricos:")
for col in columnas_categoricas:
    print(f"\n📌 {col} (top 10):")
    print(df[col].value_counts().head(10))
