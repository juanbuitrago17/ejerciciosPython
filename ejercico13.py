# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:44:27 2022

@author: ciberplay-park
"""
"""
lista = [1, 2.5, 'DeCode', [5,6], 4]

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[3][1])
print(lista[1:3])
print(lista[0:4:2])
"""
"""
#unir dos lines en una
nombres = ['Daniel', 'Bernardo']
edades = [15, 35]
listas = [nombres, edades]
print(listas)
print(edades[1])
print(nombres[1], edades[1])
print(nombres[1], edades)
"""

ruta = ['Brayan', 'Carlos', 'Nicolas', 'Geyder', 'Juan', 'pablo' , 'diego', 'maria',9, 10, 14]
ruta1 =  [9,40,35,54,55]
"""
print(ruta)
print('\n')
print(ruta1)

print(ruta[5])
print(len(ruta))  #imprime la cantidad de elementos de la lista
print(len(ruta1))

print('\n')
print(ruta[-1]) #imprime el ultimo valor de la lista
print(ruta[0])
print(ruta[1])
print(ruta[-2])
print(ruta[-11])

print('\n')
print(ruta)
ruta[1] = "Gamba" #cambiar el valor de la posicion de la lista
print('\n')
print(ruta)
ruta[5] = "Buitrago"
print('\n')
print(ruta)
print('\n')
ruta.append(19) #agrega un elemento al final de la lista
ruta.append('sara')
print(ruta)
print(len(ruta))
"""
"""
print(ruta)
print('\n')

print(ruta.count(14)) # muestra cuantos numeros 14 hay
r = ruta.count('Brayan')
print(r)
#n = float(input('ingrese un numero parabuscar: '))
#print(ruta.count(n))
ruta += ['Hola'] #ingresa un dato en la ultima posicion
ruta += 'Hola'
print(ruta)
"""
"""
print(ruta)
ruta.extend(range(1,8)) #agrega al final un rango de numeros de 1 a 8
print(ruta)
print('\n')
print(ruta.index(14)) #imprime la posicion donde esta alojado el valor
ruta.insert(4, 'hola') #inserta un valor en una posicion determinada en la lista
print(ruta)
print(ruta.pop())#retorna el ultimo numero y lo borra
print(ruta)
"""
"""
#asignacion de tupla
y = 67.9
t = ('Esto es una cadena', 'b', 'c', 'a', 'd')
print(t)
print(len(t))
print(t[0]) #imprime de izquierda a derecha
print(t[-1]) #imprime de derecha a izquierda
print(t[0:4])#rango primer valor indica el inicio el segundo es el mx numero
print(type(y))
print(type(t))
"""
"""
t = ('a',)
print(t)
print(type(t))

t1 = ('a')
print(t)
print(type(t1))

print('\n')
y = 'b',
print(y)
print(type(y))

y1 = 'b'
print(y1)
print(type(y1))
"""
"""
t = ('python','desde cero')
print(t)

t1 = tuple('hola')
print(t1)
"""
"""
t = ('hola', 'b', 'c', 'g', 'h')
print(t)
t = t[0] + ' jajajaja'
print(t)

t = ('hola', 'b', 'c', 'g', 'h')
print(t)
t = 'care' + t[0]
print(t)
t = t[6] + ' perro hp'
print(t)
"""
t = ('Esto es una cadena', 'b', 'c', 'd', 'e')
print(t.index('d'))
print(t.count('d'))


print('\n')
txt = 'python es un lenguaje de programación facil de entender'
palabras = txt.split()
print(palabras)
print('\n')
l = list()
for subcadena in palabras:
    l.append((len(subcadena), subcadena))
print(l)