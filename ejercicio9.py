# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 10:25:59 2022

@author: ciberplay-park
"""

n=int(input('digite el numero de su nota: '))
if n>=1 and n<=20:
    if n>=1 and n<=9:
        print('su nota es: E')
    else:
        if n>=10 and n<=12:
            print('su nota es: D')
        else:
            if n>=13 and n<=15:
                print('su nota es: C')
            else:
                if n>=16 and n<=18:
                    print('su nota es: B')
                else:
                    print('su nota es: A')
else:
    print('su nota es incorecta, vuelva y dijite su nota')
                    
                  
              
              
