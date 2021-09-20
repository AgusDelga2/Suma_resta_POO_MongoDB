
class Suma:
    def __init__(self):
        #Atributos de la suma
        self.total = self._suma()

    #Metodo privado que retorna la suma
    def _suma(self):
        total = self.num1 + self.num2
        return total
    
   #Metodo para imprimir 
    def imprimirSuma(self):
        print(f'El resultado de la {type(self).__name__} es: {self.total}')
        


'''l = Suma(9, 4)
l._suma()
l.imprimir()'''
