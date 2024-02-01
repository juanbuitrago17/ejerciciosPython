# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 09:56:51 2022

@author: ciberplay-park
"""

"""
Escribir dos funciones que permitan calcular:

1. La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
2. La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
3. Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, 
convertir a horas,minutos y segundos o salir del programa.

"""
"""
def segundos(h,m,s):
    return h*3600 + m*60 +s

def comvertir_hms(s):
    h =s // 3600
    s =s - h*3600
    m =s // 60
    s =s - m*60
    seg = s
    return h,m,seg
while True:
    print('\n')
    print('1 - convertir a segundos.')
    print('2 - convertir a horas, minutos y segundos.')
    print('3 - salir.')
    datos = input('Digite la operacion a realizar: ')
    if datos == '1':
        hora = int(input('\nIngrese las horas: '))
        minu = int(input('\nIngrese las minutos: '))
        segund = int(input('\nIngrese las segundos: '))
        print('\nlas horas, minutos y segundos ingresados corresponden' ,segundos(hora,minu,segund), 'segundos')
   elif
"""
"""
import numpy as np

matriz = np.zeros((5,3))
print(matriz)
print('\n')
b = np.ones((4,6))
print(b)
print('\n')
c= np.full((6,5),16)
print(c)
print('\n')
d= np.eye(3)
print(d)
print('\n')
e=np.random.random((4,3))
print(e)
"""
import numpy as np

a = np.array([[1,2,3],[4,5,6],[9,10,11]])
print(a)
print('\n')
b = a[0:3, 0:3]
print(b)
print('\n')
c=a[0:2, 1:3]
print(c)
