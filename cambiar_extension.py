import os

# Ruta de la carpeta donde están los archivos
carpeta = "C:/GitHubProjects/GeoWare/GeoWareMod/src/main/resources/assets/geowaremod/sounds/games"  # Cambia esto por la ruta de tu carpeta

# Función para cambiar la extensión de los archivos
def cambiar_extension(carpeta):
    # Recorre todos los archivos y subcarpetas
    for raiz, directorios, archivos in os.walk(carpeta):
        for archivo in archivos:
            # Verifica si el archivo tiene extensión .OGG
            if archivo.endswith(".OGG"):
                # Construye la ruta completa del archivo
                ruta_antigua = os.path.join(raiz, archivo)
                # Crea el nuevo nombre con extensión .ogg
                nuevo_nombre = os.path.splitext(archivo)[0] + ".ogg"
                ruta_nueva = os.path.join(raiz, nuevo_nombre)
                
                # Renombra el archivo
                os.rename(ruta_antigua, ruta_nueva)
                print(f"Renombrado: {ruta_antigua} -> {ruta_nueva}")

# Ejecuta la función
cambiar_extension(carpeta)
print("¡Proceso completado!")