import os
import json
from pathlib import Path

def generate_sounds_json(base_dir, output_file="sounds.json"):
    """
    Genera un archivo sounds.json para Minecraft basado en los archivos de sonido en el directorio especificado.
    
    Args:
        base_dir (str): Directorio base que contiene subdirectorios de juegos (ej. 'games/tetris').
        output_file (str): Nombre del archivo JSON de salida (ej. 'sounds.json').
    """
    # Estructura del JSON
    sounds_json = {}
    
    # Convertir base_dir a objeto Path
    base_path = Path(base_dir)
    
    # Recorrer cada subdirectorio (juego) en el directorio base
    for game_dir in base_path.iterdir():
        if game_dir.is_dir():  # Asegurarse de que es un directorio
            game_name = game_dir.name  # Ej. 'tetris'
            
            # Recorrer archivos de sonido en el directorio del juego
            for sound_file in game_dir.glob("*.ogg"):  # Buscar archivos .ogg
                # Obtener el nombre del archivo sin la extensión
                sound_name = sound_file.stem  # Ej. 'bajar_tetris'
                
                # Crear la clave para el sonido en el JSON
                sound_key = sound_name
                
                # Crear la ruta relativa para Minecraft (ej. 'geowaremod:games/tetris/bajar_tetris')
                sound_path = f"geowaremod:games/{game_name}/{sound_name}"
                
                # Agregar al JSON
                sounds_json[sound_key] = {
                    "sounds": [
                        {"name": sound_path}
                    ]
                }
    
    # Guardar el JSON en el archivo de salida
    output_path = base_path / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sounds_json, f, indent=2, ensure_ascii=False)
    
    print(f"Archivo {output_file} generado exitosamente en {output_path}")

if __name__ == "__main__":
    # Directorio base con los sonidos
    base_directory = r"C:\GitHubProjects\GeoWare\GeoWareMod\src\main\resources\assets\geowaremod\sounds\games"
    
    # Generar el sounds.json
    generate_sounds_json(base_directory)