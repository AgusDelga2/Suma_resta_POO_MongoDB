#Importamos las clsases suma y resta
from suma import Suma
from resta import Resta
#Importamos NumPy y Pandas
import numpy as np
import pandas as pd
from pymongo import MongoClient # import mongo client to connect  

        

class Principal(Suma):
    
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
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #INTENTANDO APLICAR HERENCIA: suma= self._suma(x, y), TypeError: _suma() takes 1 positional argument but 3 were given
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            inst_suma = Suma.__init__(self, x, y)
            suma = Suma._suma(self)
            #Se agrega al df
            self.df.iloc[i,2] = suma
            
            #Relación de composicón con resta
            inst_resta = Resta(x, y)
            resta = inst_resta._resta()
            #Se Agrega al df
            self.df.iloc[i,3] = resta
             
        return self.df
    
    def imprimirDF(self):
        print('Pandas DF resultante de las operaciones:')
        print(self.df)
        
    def to_mongo(self):
        # Instancia de mongoclient
        client = MongoClient('localhost')  
        print(1)
        # Creando database
        db = client['finaldb']
        #Creando documento
        col = db['suma_resta_mongo']
        #Insertamos el pandas df en el documento
        db.suma_resta.insert(self.df)
        #Print coleccion
        print(db.suma_resta_mongo.find())
        
if __name__ == '__main__':
    print('Principal se está ejecutando')
    
    arr = [[45, 6, 8], [4, 7, 3]]
    tabla = Principal(arr)
    tabla1 = tabla.a_dataframe()
    print(tabla1)
    tabla.suma_resta()
    tabla.imprimirDF()
    #tabla.to_mongo()

#------------------------ANOTACIONES------------------------------ANOTACIONES-----------------------------ANOTACIONES--------------------------
'''
 No se puede hacer relacion de asociacion con Resta, ya que se debe crear un objeto fuera de la clase principal, 
poner como parámetros valores que se encuentran dentro del objeto de Principal, para luego desde el metodo en principal (suma_resta) 
llamar al metodo de resta desde el objeto que se creó fuera de la clase.
 En este caso, considero mejor la relacion de COMPOSICION, tambien considero que sería lo mejor para la clase suma.
 En un principio pense que no se podria porque el array es una variable local, pero luego vi que no es asi ya que es un
atributo de Principal y si se puede acceder a ella (a diferencia de las variables locales), pero de todas formas sigue sin ser la mejor opcion.
'''

'''tabla_dict = tabla1.to_dict()
print (tabla_dict)'''
