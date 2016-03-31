print("                   menu ")
tupla =("arroz","leche","tuna","cereal","jugo")
print(tupla)
def capturar():
        global lista
lista=[]

print ("cuantos articulos va a tener su lista: ")
n=input()
n=int(n)

for i in range(0,n):
    print("favor ingrese los articulos que desea segun el menu  ",i)
    elemento=input()
    lista.insert(i,elemento)
def ver():
    print(lista)

def agregar():
    print("favor ingrese el articulo que desea agregar segun el menu")
    elemento=input()
    print ("en que indice desea agregarlo:  ")
    indice  = input()
    indice=int(indice)
    longitud=len(lista)
    longitud=int(longitud)
    if (indice>longitud or indice<0):
        print (" el indice debe estar entre el 0 y ",longitud)
    else:
        lista.insert(indice,elemento)
        print ("elemento agregado")
    def ver():
           print(lista)


def eliminar():

        print ("articulo que desea eliminar:  ")
        indice = input()
        indice=int(indice)
        longitud=len(lista)
        longitud=int(longitud)
        if (compra>longitud-1 or compra<0):
            print ("la compra debe entre el 0 y",longitud-1)

        else:
            del lista[indice]
            print("elemento eliminado")
def principal():
    option="1"
    while(option!="6")  :
        print ("lista de opciones")
        print("1. captura")
        print("2. ver")
        print("3. agregar")
        print("4.eliminar")
        print("5.salir")

        print ("elija una opcion")
        option=input()
        if (option=="1"):
            capturar()
        elif (option=="2"):
             ver()
        elif (option=="3"):
              agregar()
        elif (option=="4"):
              eliminar()
        elif (option=="5"):
              print ("FIN DEL PROGRAMA")
        else:
              print ("incorrecto vuelva a escojer otra opcion")
principal()    