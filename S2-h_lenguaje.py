import os

def main():
    nombre = os.getenv("USERNAME")
    lenguaje_favorito = os.getenv("LANGUAGE")
    print(f"Hola, {nombre} desde GitHub usando {lenguaje_favorito} >_<")


if __name__ == "__main__":
   main()
