import os
import pandas as pd

# Ruta donde están los archivos .xls/.xlsx
DATA_PATH = "data/raw/"

# Categorías por palabras clave
CATEGORIAS = {
    "ventas": ["venta", "sales"],
    "compras": ["compra", "purchase"],
    "clientes": ["cliente", "customer"],
    "proveedores": ["proveedor", "supplier"],
    "articulos": ["articulo", "sku", "producto", "item"]
}

def clasificar_archivo(nombre_archivo):
    nombre_lower = nombre_archivo.lower()
    for categoria, palabras in CATEGORIAS.items():
        if any(palabra in nombre_lower for palabra in palabras):
            return categoria
    return "otros"

def explorar_archivo(path):
    try:
        df = pd.read_excel(path)
    except Exception as e:
        return {"error": str(e), "archivo": os.path.basename(path)}

    resumen = {
        "archivo": os.path.basename(path),
        "columnas": list(df.columns),
        "num_columnas": df.shape[1],
        "filas": df.shape[0],
        "nulos_totales": df.isnull().sum().sum(),
        "duplicados": df.duplicated().sum(),
        "columnas_nulas": df.isnull().sum().to_dict(),
        "tipos_dato": df.dtypes.astype(str).to_dict(),
        "columnas_con_años": [col for col in df.columns if "20" in col or "19" in col]
    }

    return resumen

# Recolectar todos los resumenes
resumenes = []

for archivo in os.listdir(DATA_PATH):
    if archivo.endswith(".xls") or archivo.endswith(".xlsx"):
        path_archivo = os.path.join(DATA_PATH, archivo)
        categoria = clasificar_archivo(archivo)
        resumen = explorar_archivo(path_archivo)
        resumen["categoria"] = categoria
        resumenes.append(resumen)

# Exportar como JSON
df_resumen = pd.DataFrame(resumenes)
df_resumen.to_json("outputs/reports/resumen_archivos.json", orient="records", indent=2)

# Mostrar en consola (debug)
import pprint
pprint.pprint(resumenes)

print("✅ Análisis completo. Archivo generado: outputs/reports/resumen_archivos.json")



