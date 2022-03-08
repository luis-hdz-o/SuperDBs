import pandas as pd

students = [{
    "name": "Jorge", 
    "surname":"Perez", 
    "age":24, 
    "weight":50, 
    "height":170 
},{
    "name":"Pepe",
    "surname":"Garcia",
    "age":27,
    "weight":60,
    "height":175 
},{
    "name":"Aria", 
    "surname":"Jimenez", 
    "age":26,
    "weight":70,
    "height":180
},{
    "name":"Maria",
    "surname":"Ruz", 
    "age":25,
    "weight":75,
    "height":181
},{
    "name":"Maria",
    "surname":"Ruz", 
    "age":25,
    "weight":75,
    "height":181
},{
    "name":"Luisa",
    "surname":"Perez", 
    "age":24,
    "weight":50,
    "height":170
},{
    "name":"Luisa",
    "surname":"Perez", 
    "age":24,
    "weight":50,
    "height":170
}]

df= pd.DataFrame(students)
#print(df)
#print(df.head())
#print(df.duplicated().sum)
#print(df.name.value_counts())
#print(df.name.unique())

nombres= {
    'name': 'Nombre',
    'surname': 'Apellido'
}
df= df.rename(columns=nombres)
print("##############")
print(df.head())

print(df.shape)
print(df.info())
print(df.describe())
