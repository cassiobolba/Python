# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:52:02 2018

@author: Cassio
"""

cassio = 'love_to_all'

#print(cassio)

print(cassio[8:])

bolba = '_but_not_all'

cassio_bolba = cassio + bolba

print(cassio_bolba)

type(sum)

type(cassio_bolba)

def aoquadrado (x):
    y = x * x
    return(y)
    
print('O quadrado de 5 é '+ str(aoquadrado(5)))
print

## CREATING FUNCTIONS

def square(x):
   x = 0       # assign a new value to the parameter x
   y = x * x
   return y

x = 2
z = square(x)
print(z)

#################

def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = 0
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)

########### FUNCTION INSIDE FUNCTION
def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c

a = -5
b = 2
c = 10
result = sum_of_squares(a, b, c)
print(result)

## FUNÇÕES PROGRAMAÇÃO 

## calculo de distância entre dois pontos
def distance(x1, y1, x2, y2):
    var1 = x2 - x1
    var2 = y2 - y1
    var3 = var1**2 + var2**2
    result = var3**0.5
    return result

## caculo de area de um circulo
def area_cir(raio):
    area = 3.14 * raio**2
    return area

## calculo area do circulo usando distancio como raio
def area_cir_dist(x1, y1, x2, y2):
    radius = distance(x1, y1, x2, y2)
    result = area_cir(radius)
    return result


print (area_cir_dist(1,2,3,4))

## Modulo 5 - 

import math
print(math.pi)

import random
d20 = random.randrange(1,21)
print(d20)


