#1)	Calculadora. Esta opción será un submenú de 10 opciones:
import abc

class calculadora:
    def __init__(self,numero1,numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        Sum = self.num1 + self.num2
        print("La suma de {}+{}={}".format(self.num1,self.num2,Sum))
    
    def resta(self):
        Res= self.num1 - self.num2
        print("La resta de {}-{}={}".format(self.num1,self.num2,Res))
    
    def multiplicacion(self):
        Multi= self.num1 * self.num2
        print("La multiplicacion de {}*{}={}".format(self.num1,self.num2,Multi))    

    def division(self):
        Div= self.num1 / self.num2
        print("La division de {}/{}={}".format(self.num1,self.num2,Div))
        
class CalEstandar(calculadora):
    def __init__(self,numero1,numero2):
        super().__init__(numero1, numero2)  
    
    def multiplicacion(self):
        Valor = self.num1 * self.num2
        return Valor 
    
    def exponente(self):
        Expo = self.num1**self.num2
        print("El exponente es:",Expo)
        
    def valorAbsoluto(self,numero):
       Valor = abs(numero)
       return Valor
    
class calCientifica(calculadora):
   Pi=3.1416
   def __init__(self,numero1,numero2):
       super().__init__(numero1,numero2) 
       
   def circunferencia (self):
       Pi=3.1416
       Circunferencia = 2 * Pi * self.num1 # circunferencia
       return Circunferencia
   
   def areaCirculo(self):
       Pi=3.1416
       Area = Pi * (self.num1 ** 2) # área del círculo
       return Area
   
   def areaCuadrado(self):
       Area = self.num2**2
       return Area

cal = calCientifica(2,4,6,8)
print(cal.circunferencia())
print(cal.areaCirculo())
print(cal.areaCuadrado())       
       