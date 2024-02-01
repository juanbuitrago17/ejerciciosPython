# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 08:33:10 2022

@author: ciberplay-park
"""
""" 
y = {} #se declara un diccionario vacio 
t =set() #se declara un conjunto vacio
print(y)
print(type(y)) #indica la clase dict, que es un diccionario
print(t)
print(type(t))#indica la clase set(), que es un conjunto
"""
"""
s1=set([1,2,3,5,6])
s2= set(range(10))
print(s1)
print(s2)
"""
"""
list = ({2,2,3,4})
print(list)
print(type(list))
print('\n')

x= set([1,2,3,4,4,3])
print(x)
print(type(x))
"""
"""
p = set('hola como esta, jajajhaja')
print(p)
print(len(p))

t = set(['hola', 'ruta', 'cielo'])
print('\n')
print(t)

g=set(['hoka', 'mama', 1.2, 3, 5, 'casa'])
print('\n')
print(g)
"""
"""
ruta=set(['maria', 'pablo', 'karen', 'joan', 'juan','juan','carlos', 'jose'])
print(ruta)
print(len(ruta))
for ruta1 in ruta:
    print(ruta1)
"""
"""
ruta = set([4,3,11,7,5,2,1,4])
print(ruta)
ruta.add(22.0008)
print(ruta)
ruta.add(6)
print(ruta)
x = float(input('ingrese un valor numerico: '))
ruta.add(x)
print(ruta)
"""
"""
ruta = set ([4,3,11,2,1,4,7,8])
print(ruta)
ruta.remove(3)
print(ruta)
ruta.clear()#con esto se borra todos los elementos del conjunto
print(ruta)
"""
"""
ruta=set(['maria', 'pablo', 'karen', 'joan', 'juan','juan','carlos', 'jose'])
print(ruta)
print(len(ruta))
cont = 0
for recorrer in ruta:
    print(f'En la posicion {cont} del conjunto llamdo ruta se guarda al siguiente valor: {recorrer}')
    cont = cont +1 
"""
"""
ruta = set([4,3,11,7,6,4,3,2,1])
print(ruta)
ruta1 = ruta.copy()
print('\n')
print(ruta)
print(ruta1)

print('\n')
ruta =set([4,3,5,11,3,4,4,])
ruta1 = set([5, 6,7,7,4,2,5,4])
print(ruta)
print(ruta1)
print(ruta.difference(ruta1))
"""
"""
group_a = {'Ana', 'Marcos', 'Carlos', 'Mario'}
group_b = {'Ana', 'Pedro', 'Carlos', 'Antonio'}
group_c = {'Ana', 'Antonio', 'Marcos', 'Pepe'}
all_students = group_a.union(group_b).union(group_c)
print(all_students)
for student in all_students:
    groups_in = []
    for letter, group in zip('ABC', [group_a, group_b, group_c]):
        if student in group:
             groups_in.append(letter)
             print(groups_in)
    groups_str = '-'.join(groups_in)
    plural = 's' if len(groups_in) > 1 else ''
    print(f'{student} en grupo{plural}: {groups_str}')
"""
def cargarnombres(alumnos):
    nombre=input('\nDigita el nombre: ')
    while nombre != 'x':
        alumnos.add(nombre)
        nombre=input('\nDigite el nombre: ')
    return alumnos
 
primaria = set()
secundaria= set()
 
print('alumnos de primaria')
primaria = cargarnombres(primaria)
 
print('alumnos de secundaria')
secundaria = cargarnombres(secundaria)
 
print('nombre de todos los alumnos')
for nombre in primaria&secundaria:
     print(nombre)

print('nombre de todos los alumnos')
for nombre in primaria-secundaria:
    print(nombre)
 
 