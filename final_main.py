#Importamos las clsases suma y resta
import suma_resta as sr
#Importamos NumPy y Pandas
import numpy as np
import pandas as pd

if __name__ == '__main__':
    print('Principal se está ejecutando')
    
class Principal:
    def __init__(self):
        #Creamos el array
        self.array = np.array([[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]])
        print(self.array)
           
    def a_dataframe(self): #Creamos Dataframe a partir del array
        dataframe = pd.DataFrame(self.array)
        return dataframe
    
    
#Pruebas
l = Principal()
print(l.a_dataframe())

h = sr.Resta(9, 6)
h._resta()
h.imprimir()