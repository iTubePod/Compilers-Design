#Hector Mauricio Gonzalez Coello
#A01328258
#ITC

from globalTypes import *
from lexer import *

f = open('sample.txt', 'r')
programa = f.read()
progLong = len(programa)
programa = programa + '$'
posicion = 0
globales(programa, posicion, progLong)
token, tokenString = getToken(True)
while (token != TokenType.ENDFILE):
    token, tokenString = getToken(True)
