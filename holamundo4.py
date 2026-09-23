from pathlib import Path
from saludo import Saludo


if __name__ == '__main__':
    misaludo = Saludo()
    print(f"Hola mundo desde {Path(__file__).name} que está en {Path(__file__).parent}")
    print(f"Nombre del archivo sin extensión: {Path(__file__).stem}")
    print(f"Extensión del archivo: {Path(__file__).suffix}")
    misaludo.hola()