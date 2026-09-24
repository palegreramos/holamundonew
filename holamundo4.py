from pathlib import Path
#from saludos import Saludar (con esta línea se escribiría Saludar() en vez de saludos.Saludar())
import saludos

if __name__ == '__main__':
    misaludo = saludos.Saludar()
    print(f"Hola mundo desde {Path(__file__).name} que está en {Path(__file__).parent}")
    print(f"Nombre del archivo sin extensión: {Path(__file__).stem}")
    print(f"Extensión del archivo: {Path(__file__).suffix}")
    print(misaludo.hola())