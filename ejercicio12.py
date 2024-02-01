# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 08:50:02 2022

@author: ciberplay-park
"""
"""
palabra = str(input("Dijite la primera palabra: "))
palabra1 = str(input('Dijite la segunda palabra: '))

if palabra < palabra1:
    print('tu palabra ' + palabra + ' viene antes de ' + palabra1)
    print(f'tu palabra {palabra} viene antes de {palabra1}')
elif palabra > palabra1:
    print('tu palabra ' + palabra + ' viene despues de ' + palabra1)
    print(f'tu palabra {palabra} viene despues de {palabra1}')
else :
    print('tu palabra ' + palabra + ' ves igual ' + palabra1)
    print(f'tu palabra {palabra} es igual {palabra1}')
"""
"""
print('------------CONVERTIR EN MAYUSCULAS--------')
print('\n')
palabra = str(input('Dijite palabra a convertir: '))
print(palabra.upper())
print('\n')
print('------------convertir en minuscula--------')
print('\n')
palabra1 = str(input('Dijite palabra a convertir: '))
palabra_final = palabra1.lower()
print(palabra_final)
"""
"""
palabra = 'noche'
p_letra = palabra.find('h')
print('la letra esta en la posicion: ' +str(p_letra))
print('la letra esta en la posicion: ', palabra, ', esta en la posicion: ', p_letra)
print('la letra esta en la posicion: '+ str(palabra)+ ', esta en la posicion: '+ str(p_letra))
print(f'la palabra que busca en la palabra {palabra} esta en la posicion: {p_letra}')
print('la letra esta en la posicion: ', palabra, ', esta en la posicion: ', palabra.find('o'))
"""
"""
palabra = str(input('Dijite la palabra: '))
letra = str(input('Dijite la letra a buscar: '))
p_letra = palabra.find(letra)
print('la letra esta en la posicion: ', letra, 'en la palabra ', palabra, ', esta en la posicion: ', p_letra)
print(f'la letra que buscas es {letra}, de la palabra {palabra}, esta en la posicion {p_letra}')
print('\n')
print('la letra que busca es ' , letra, ' en la palabra', '(', palabra, ')' , ', esta en la posicion:', palabra.find(letra))
"""
"""
print('metodo strip()')
palabra = '     holas     '
print(palabra)
quitar_espa = palabra.strip()
print(quitar_espa)
print(palabra.strip())
print('\n')
print(palabra.strip() + ' si quita los espacios')

print('\nmetodo rtrip()')
texto = '     campeon     '
print(texto)
texto_sinespa = texto.rstrip()
print(texto_sinespa)
print(texto.rstrip())
print('\n')
print(texto.rstrip() + ' si quita los espacios')


print('\nmetodo ltrip()')
texto2 = '    buena la banda     '
print(texto2)
texto2_espa = texto2.lstrip()
print(texto2_espa)
print(texto2.lstrip())
print('\n')
print(texto2.lstrip() + ' si quita los espacios')
"""

"""
texto = 'el precio del dolar esta muy elevado por ello todo lo electrónico subio de precio'
p_espacio = texto.find('m')
print(p_espacio)

p_esp_nuevo = texto.find('r',p_espacio)
print(p_esp_nuevo)
"""
"""
diccionario = {"total": 26}
print(diccionario)

diccionario2 = dict(total = 34)
print(diccionario2)
"""
"""
usuario = {
    'nombre': 'nombre de usuario',
    'edad': 23,
    'no medallas' : 10,
    'casa': {
        'programacion': True,
        'casa': False,
        }
    }
print(usuario)
print(usuario['no medallas'] + 20)
print(usuario['casa']['casa'])
"""
"""
diccionario= dict()
print(diccionario)

diccionario['marca']= 'carro'
print(diccionario)

diccionario['precio']= 30000
print(diccionario)
  
valor=input('Dijite el valor: ')
diccionario['automovil']= valor
print(diccionario)
"""
"""
diccionario={ 'rafael':3, 'santiago':4, 'carlos':5}
print(diccionario)
keys= diccionario.keys()
print(keys)
print(diccionario.keys())
valor=diccionario.values()
print(valor)
print(diccionario.values())
"""
"""
diccionario = {
    'nombre': 'sara',
    'nombre2': 'juan',
    }
print(diccionario)
print(type(diccionario))


diccionario ={ 'rafael':3, 'santiago':4, 'carlos':5}
diccionario.clear()
print(diccionario)

diccionario={ 'rafael':3, 'santiago':4, 'carlos':5}
diccionario1 =diccionario.copy()
print(diccionario1)
"""
"""
secuencia= {'hola' , 'casa', 'picos'}
versiones= dict.fromkeys(secuencia)

print('nuevo diccionario ' + str(versiones))
print('nuevo diccionario %s' % str(versiones))
print('nuevo diccionariuo {}' .format(versiones))

versiones = dict.fromkeys(secuencia, 0.1)
print('nuevo diccionario ' + str(versiones))
print('nuevo diccionario %s' % str(versiones))
"""