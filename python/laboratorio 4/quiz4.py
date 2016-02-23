class perro:

    puntos_de_vida = 5
    puntos_de_alegria = 5

    def caminar(self):
        puntos_de_vida = puntos_de_vida -2
        puntos_de_alegria = puntos_de_alegria -1

    def correr(self):
        puntos_de_vida = puntos_de_vida -4
        puntos_de_alegria = puntos_de_alegria +3

    def dormir(self):
        puntos_de_vida = puntos_de_vida +1
        puntos_de_alegria = puntos_de_alegria -3

    def jugar(self):
        puntos_de_vida = puntos_de_vida -3
        puntos_de_alegria = puntos_de_alegria +4

    def comer(self):
        puntos_de_vida = puntos_de_vida +5
        puntos_de_alegria = puntos_de_alegria = +1

lassie = perro()
lassie.dormir()
lassie.juegue()
lassie.comer()
lassie.juegue()
lassie.camine()
lassie.duerma()
lassie.corra()
lassie.duerma()
lassie.duerma()
lassie.coma()

x=5
y=5
contador = 0
lassie = perro(5,5)

while contador != 10: