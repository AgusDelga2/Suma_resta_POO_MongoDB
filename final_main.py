#Importamos las clsases suma y resta
import suma as s
import resta as r
#Importamos NumPy y Pandas
import numpy as np
import pandas as pd
    
class Principal(s.Suma):
    def __init__(self, array):
        #Creamos el array
        self.array = np.array(array)
        
        
    def a_dataframe(self): #Creamos Dataframe a partir del array
        df = pd.DataFrame(self.array)
        self.df = df.transpose()
        self.df.columns = ['PrimerN', 'SegundoN']
        self.df['Suma'] = 0
        self.df['Resta'] = 0
        #print (self.df)
        return self.df
    
    def suma_resta(self):
        for i in range(len(self.df)):
            x = int(self.df.iloc[i,0])
            y = int(self.df.iloc[i,1])
            #Herencia con Suma
            inst_suma = s.Suma.__init__(self, x, y)
            suma = s.Suma._suma(self)
            #Se agrega al df
            self.df.iloc[i,2] = suma
            
            #Relación de composicón con resta
            inst_resta = r.Resta(x, y)
            resta = inst_resta._resta()
            #Se Agrega al df
            self.df.iloc[i,3] = resta
             
        return self.df
    
    def imprimirDF(self):
        print('Pandas DF resultante de las operaciones:')
        print(self.df)
    
if __name__ == '__main__':
    print('Principal se está ejecutando')
    
    arr = [[45, 6, 8], [4, 7, 3]]
    l = Principal(arr)
    l.a_dataframe()
    l.suma_resta()
    l.imprimirDF()

#------------------------ANOTACIONES------------------------------ANOTACIONES-----------------------------ANOTACIONES--------------------------
'''
 No se puede hacer relacion de asociacion con Resta, ya que se debe crear un objeto fuera de la clase principal, 
poner como parámetros valores que se encuentran dentro del objeto de Principal, para luego desde el metodo en principal (suma_resta) 
llamar al metodo de resta desde el objeto que se creó fuera de la clase.
 En este caso, considero mejor la relacion de COMPOSICION, tambien considero que sería lo mejor para la clase suma.
 En un principio pense que no se podria porque el array es una variable local, pero luego vi que no es asi ya que es un
atributo de Principal y si se puede acceder a ella (a diferencia de las variables locales), pero de todas formas sigue sin ser la mejor opcion.
'''