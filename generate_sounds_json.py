import os
import json
from pathlib import Path
from typing import List

def generate_sounds_json(
    base_dir: str,
    output_file: str = "sounds.json",
    mod_id: str = "minecraft",
    sound_extensions: List[str] = [".ogg"],
    overwrite: bool = False,
    verbose: bool = False
) -> None:
    """
    Generates a sounds.json file for Minecraft based on sound files in the specified directory.

    Args:
        base_dir (str): Base directory containing subdirectories of games (e.g., 'games/tetris').
        output_file (str): Name of the output JSON file (e.g., 'sounds.json').
        mod_id (str): Mod ID to use as the namespace prefix (e.g., 'razorquestsfabric').
        sound_extensions (List[str]): List of sound file extensions to include (e.g., ['.ogg', '.wav']).
        overwrite (bool): Whether to overwrite the output file if it exists.
        verbose (bool): Whether to print detailed progress information.
    """
    # Convert base_dir to Path object
    base_path = Path(base_dir).resolve()

    # Validate base directory
    if not base_path.exists():
        raise FileNotFoundError(f"Base directory '{base_path}' does not exist.")
    if not base_path.is_dir():
        raise NotADirectoryError(f"'{base_path}' is not a directory.")

    # Validate output file
    output_path = base_path / output_file
    if output_path.exists() and not overwrite:
        raise FileExistsError(f"Output file '{output_path}' already exists. Please choose a different name or allow overwriting.")

    # Initialize JSON structure
    sounds_json = {}

    # Recursively find all sound files in base directory and subdirectories
    for sound_file in base_path.rglob("*"):
        if sound_file.is_file() and sound_file.suffix.lower() in sound_extensions:
            # Get relative path from base_dir to sound file
            relative_path = sound_file.relative_to(base_path)
            # Create sound key (e.g., 'games.tetris.bajar_tetris')
            sound_key = str(relative_path.with_suffix("")).replace(os.sep, ".")
            # Create sound path for Minecraft (e.g., 'modid:games/tetris/bajar_tetris')
            sound_path = f"{mod_id}:{str(relative_path.with_suffix('')).replace(os.sep, '/')}"

            if verbose:
                print(f"Processing sound: {sound_key} -> {sound_path}")

            # Add to JSON structure
            sounds_json[sound_key] = {
                "sounds": [
                    {"name": sound_path}
                ]
            }

    # Check if any sounds were found
    if not sounds_json:
        print("Warning: No sound files found with the specified extensions.")

    # Save JSON to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sounds_json, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated '{output_file}' at '{output_path}' with {len(sounds_json)} sounds.")

def get_boolean_input(prompt: str, default: bool = False) -> bool:
    """Prompt for a yes/no input, return boolean based on user response."""
    default_str = "y" if default else "n"
    response = input(f"{prompt} (y/n, default: {default_str}): ").strip().lower()
    if response == "":
        return default
    return response in ("y", "yes", "true", "1")

def get_extensions_input() -> List[str]:
    """Prompt for sound file extensions, return a list of extensions."""
    response = input("Enter sound file extensions (e.g., .ogg .wav, default: .ogg): ").strip()
    if not response:
        return [".ogg"]
    return [ext.strip() for ext in response.split() if ext.strip().startswith(".")]

def main():
    print("Welcome to the Minecraft sounds.json generator!")
    print("Please provide the following information:\n")

    # Prompt for base directory
    base_dir = input("Base directory containing sound files (default: 'sounds'): ").strip()
    base_dir = base_dir if base_dir else "sounds"

    # Prompt for output file
    output_file = input("Output JSON file name (default: 'sounds.json'): ").strip()
    output_file = output_file if output_file else "sounds.json"

    # Prompt for mod ID
    mod_id = input("Mod ID for namespace prefix (default: 'minecraft'): ").strip()
    mod_id = mod_id if mod_id else "minecraft"

    # Prompt for sound extensions
    sound_extensions = get_extensions_input()

    # Prompt for overwrite option
    overwrite = get_boolean_input("Overwrite existing output file if it exists?", default=False)

    # Prompt for verbose mode
    verbose = get_boolean_input("Enable verbose output?", default=False)

    print("\nGenerating sounds.json with the following settings:")
    print(f"Base directory: {base_dir}")
    print(f"Output file: {output_file}")
    print(f"Mod ID: {mod_id}")
    print(f"Sound extensions: {', '.join(sound_extensions)}")
    print(f"Overwrite: {'yes' if overwrite else 'no'}")
    print(f"Verbose: {'yes' if verbose else 'no'}")
    print()

    try:
        generate_sounds_json(
            base_dir=base_dir,
            output_file=output_file,
            mod_id=mod_id,
            sound_extensions=sound_extensions,
            overwrite=overwrite,
            verbose=verbose
        )
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
