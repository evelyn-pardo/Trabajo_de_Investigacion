class Lista():
    
    def __init__(self,lista=[]):        
        self.li = lista
    
    def presentarLista(self):
         for item in self.li:            
            print(item)    
    
    def buscarLista(self,valor):
        for item in self.li:
            if valor == item:
                print(item)    
                
    def listaFactorial(self,num):
        import math
        li = []
        for c in range(1,num):
            fact = math.factorial(c)
            self.li.append(fact)
        return li

    def insertarLista(self,valor,posicion):
        self.li.insert(posicion, valor)
    
    
    def eliminarLista(self,valor):
        for item in self.li:
            self.li.remove(valor)
    
    def retornaValorLista(self,posicion):
        num = self.li.pop(posicion)
        return num
    
    def copiarTuplaLista(self,tupla):
        li2 = []
        for item in tupla:
            self.li.append(tupla[item])