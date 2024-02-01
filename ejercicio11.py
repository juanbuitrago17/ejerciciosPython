# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 08:40:17 2022

@author: ciberplay-park
"""
"""
z = 7
x = 1
while z > 0:
 print(' ' * z + '*' * x + ' ' * z)
 x+=2
 z-=1
"""
"""
text = "Python"
i = 0
while i < len(text):
 print(text[:i + 1])
 i += 1
"""
"""
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
 print('k=', k, ', v=', v)
"""
"""
for num in range(0, 11, 2):
 print(num)
 """
"""
def longitud(x:int):
  cont = 0
  for cont in range(cont,x):
   print(cont)
  return cont
longitud(20)

"""
"""
coleccion = 50
for e in range(coleccion):
 if e == 8:
  break
 print(e)
"""
coleccion = 50
for e in range (coleccion):
 if e %2 !=0:
  continue
 print(e)