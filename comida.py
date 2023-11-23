class Comida():
    #test de cambio para git
    def __init__(self, salado_dulce: str) -> str:
        self.salado_dulce = salado_dulce

        if (self.salado_dulce == "dulce") or (self.salado_dulce == "salado"):
                print(f"Su selección fue {self.salado_dulce.capitalize()}")
        else:   
                print(f"Error en la selección, debe indicar Dulce o Salado")


seleccion = input("Seleccione Dulce o Salado: ")
seleccion = seleccion.lower()
Comida(seleccion)