import os

def main():
    nombre = os.getenv("USERNAME")
    programa = os.getenv("LANGUAGE")
    print(f"Hola, {nombre} desde GitHub usando {programa} >_<")


if __name__ == "__main__":
   main()
