from random import randint
class EstoyProbandoWeas:
    def __init__(self, nombre: str, numero: int) -> None:
        self.nombre = nombre
        self.puntos = numero
        pass
    def gambling(self, repeticiones):
        for i in range(repeticiones):
            self.puntos = self.puntos*randint(0,10) # el peor sistema de gambing, una perdida total = perdida para siempre 
            if self.puntos == 0:
                print("lo perdi todo")
            else:
                print(f"omg ahora tengo {self.puntos}")
        print(f"quede con {self.puntos}")
        pass
    def __str__(self) -> str:
        return f"olaa soy {self.nombre}"
