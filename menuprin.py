class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo 
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1...{}]:".format(len(self.opciones)))

men=Menu("Menu Principal",["1) Calculadora","2)Operacion Numeros","3)Tratamiento de Lista","4)Operacion de Cadenas","5)Salir"])
opc = men.menu()
