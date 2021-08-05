class Basico:
    def __init__(self):
        pass
    
    def numeroN(self,n):
        for i in range(1,n+1):
            print(i)  
            
    def multiplo(self,numero1,numero2):
        if numero1 % numero2 ==0:
            print("si es multiplo")
        else:
            print("no es multiplo")
           
    def DivisoresNumero(self,numero):
        for i in numero:
            if numero % i == 0:
                return i
        
    def primo(self,numero):
        contador = 0
        for i in range(1,numero+1):
            if (numero% i)==0:
                contador = contador + 1
        if contador==2:
            print ("el numero es primo")
        else: 
            print ("el numero no es primo")
            
    def perfecto(self,numero):
        suma=0  
        for i in range(1,numero):
            if(numero % i == 0):
                suma = +i
        if numero == suma:
            print ("el numero es perfecto")
        else:
            print("el numero no es perfecto")
class Intermedio (Basico):
    def __init__(self):
        pass
    
    def numeroN(self,numero):
        num = numero
        i = 1
        while i <= num:
            print (i)
            i = i + 1
            
    def factorial(self,numero):
        fact = 1
        while numero > 1:
            fact *= numero
            numero -= 1
        return fact
    
    def fibonacci(self,numero):
        i, j = 0,1
        while i < numero:
            print(i, end= ' ')
            i, j = i+j
        print()
        
    def primosGemelos (self,numero1,numero2):
        a = 0
        if numero1 > 0 and numero2 > 0 and numero1 != numero2:
            if numero1 > numero2:
                numero1 ^= numero2
                numero2 ^= numero1
                numero1 ^= numero2
            for i in range (numero1, numero2+1):
                creciente = 2
                esPrimo = True
                
                while esPrimo and creciente < i:
                    if i % creciente == 0:
                        esPrimo = False
                    else:
                        creciente += 1
                if esPrimo and not a:
                    a = i
                elif esPrimo and a:
                    b = i
                    if b-a == 2:
                        print("{} y {} son numeros primos gemelos".format(a, b))
                        a=i
                    
        else:
            if numero1 == numero2:
                print("Incorrecto los numeros son Iguales.")    
            else:
                print("Los numeros son incorrectos.")
                
    def amigos (self,numero):
        l=[]
        suma=0
        for i in numero:
            for j in range(1,i):
                for k in numero:
                    if i % j==0:
                        suma+=k
                        l.append(i)
                        l.append(k)
        return l
    