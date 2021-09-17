class Resta:
    def __init__(self, num1, num2):
        #Atributos de la resta
        self.num1 = num1
        self.num2 = num2
        #Corroboramos que sean parámetros aptos
        if (type(num1) != int) or (type(num2) != int):
            print('Parametros no validos')
            self.num1 = int(input('Ingrese primer numero: '))
            self.num2 = int(input('Ingrese segundo numero: '))
        
        else:
            pass
    
    #Metodo privado que retorna la resta
    def _resta(self):
        self.total = self.num1 - self.num2
        return self.total
    
    #Metodo para imprimir 
    def imprimirResta(self):
        print(f'El resultado de la {type(self).__name__} es: {self.total}')
    
'''l = Resta(8, 9)
l._resta()
l.imprimir()'''