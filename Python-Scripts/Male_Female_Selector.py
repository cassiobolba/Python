# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
# sklearn é uma suit de packges para machine learning e Big Data. Tree é o package de DECISION TREE 
from sklearn import tree

# primeiro criam-se as duas variáveis que serão comparadas
x = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],
     [166,65,40],[190,90,47],[175,64,39],[177,70,40],
     [159,55,38],[171,75,42],[181,85,43]]

y =  ['male','female','female','female','male','male'
      ,'male','female','male','female','male']

# depois cria-se uma variavel para chamar dentro de Tree, o modulo decisiontreequalifier
clf = tree.DecisionTreeClassifier()

# em uma segunda variavel de reclassifica o clf  (que tem o modulo DECISIONTREECLASSIFIER) como fit(x,y) que é outro modulo
clf = clf.fit(x,y)

# o codigo esta pronto para receber um valor e atraves do fit e decision tree qualifier, decidir se o valor é de homem ou mulher
prediction = clf.predict([[150,80,42]])

print(prediction)