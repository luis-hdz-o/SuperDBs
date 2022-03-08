import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import tensorflow as tf 
from sklearn.model_selection import train_test_split

###



print("Leyendo CSV")
df= pd.read_csv("fechas.csv", delimiter = ',')
# df = pd.read_csv(url, index_col=False, delimiter = ',')


# df.fechacompra = pd.to_datetime(df["fechacompra"]).dt.strftime('%Y-%m-%d %H:%M:%S')

#cambiar el formato de las demás columnas
# df=df.astype({'precioventa':'float64'})

sns.scatterplot(df['fechacompra'], df['precioventa'])
# plt.show()

#Carga de datos
print("Seleccionando las columnas")
X= df['fechacompra']
Y= df['precioventa']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, shuffle=True)


#dataset
print("Creando el Modelo")
model= tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#Compilando
print ("Compilando el modelo")
model.compile(optimizer= tf.keras.optimizers.Adam(1), loss= 'mean_squared_error')

#Entrenando el modelo
print("Entrenando el modelo")
epochs_hist= model.fit(x_train, y_train, epochs= 100)

#Evaluar modelo
print("Evaluando el modelo entrenado")
print("Keys:")
print(epochs_hist.history.keys())

#GRafico
plt.plot(epochs_hist.history['loss'])
plt.title("Progreso de perdida durante nuestre entrenamiento del modelo")
plt.xlabel("Epoch")
plt.ylabel("Training Loss")
plt.legend("Training Loss")
plt.show()

Temp_C= 50
Temp_F= model.predict([Temp_C])
print("Temperatura de Prediccion: "+  str(Temp_F))
# Temp_F = 9/5 * Temp_C + 32
# print("Temperatura de Ecucion: "+ str(Temp_F))