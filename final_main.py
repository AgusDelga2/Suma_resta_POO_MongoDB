#Importamos las clsases suma y resta
import suma_resta as sr
#Importamos NumPy y Pandas
import numpy as np
import pandas as pd

class Main:
    def __init__(self):
        #Creamos el array
        self.array = np.arange(22).reshape(2, 11)
        print(self.array)
           
    def a_dataframe(self): #Creamos Dataframe a partir del array
        dataframe = pd.DataFrame(self.array, columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'h'])
        return dataframe

#Pruebas
l = Main()
print(l.a_dataframe())

h = sr.Resta(9, 6)
h._resta()
h.imprimir()