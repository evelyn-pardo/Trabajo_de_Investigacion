class Cadena:
    def __init__(self,cadena):
        self.cadena = cadena

    def recorrerCadena(self):
        return

    def buscarCaracter(self,buscado):
        enc=False
        for pos,ele in enumerate(self.cadena):
            if ele == buscado:
                enc=True
                break
        if enc ==True:return pos
        else:return -1

    def  listaPosiciones(self,caracter):
        
            pass

    def listaPalabras(self):
        return

    def cadenaLista(self):
        return

    def insertarDato(self,cadena,buscado,posicion):
        if posicion <= len(cadena):
            izquierda = cadena[:posicion]
            derecha = cadena[posicion + 1:]
            return "{} {} {}".format(izquierda,buscado,derecha)
        else:
            return "La posicion donde se quiere ingresar el texto no existe"

    def eliminarOcurrencias(self,buscado):
        for x in range(len(buscado)):
            cadenaO = cadena.replace(buscado[x],"")
            return cadenaO

    def retornaValor(self,posicion):
        posicion= self.cadena[-1]
        self.cadena =self.cadena[0:-1]
        return posicion

    def concatenarCadena(self,dato):
        return"{} {}".format(cadena,dato)


cadena = 'Podemos salir a cenar '
lista = ["Este","es","el","lugar", "de cenar"]
Cad = Cadena(cadena)
Cad.recorrerCadena()
for c in cadena:
    print(c)
buscado="a"
resp = Cad.buscarCaracter(buscado)
print(resp)
l = cadena.split()
print (l)
ca = ' '.join(lista)
print(ca)
buscado = "el viernes"
posicion = 22
print(Cad.insertarDato(cadena,buscado,posicion))
print(Cad.eliminarOcurrencias("a"))
buscado="cenar"
print(cadena)
print(Cad.concatenarCadena("despues"))
print(Cad.retornaValor(1))
