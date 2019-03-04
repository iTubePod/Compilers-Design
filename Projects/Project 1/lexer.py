#Hector Mauricio Gonzalez Coello
#A01328258
#ITC

from globalTypes import *

#global function as required in reuirements document
def globales(code, position, length):
    global programa
    global posicion
    global progLong
    global progLine
    programa = code
    posicion = position
    progLong = length
    progLine = 1

#get enum values helper
def getTypeFromToken(token, imprime, tokenSize):
    try:
        return (printTokenType(TokenType(token), token, imprime, tokenSize))
    except:
        return(printTokenType(TokenType.ID, token, imprime, tokenSize))

#getToken function as required in reuirements document
def getToken(imprime = True):
    #print("inside getToken")
    global posicion, progLine

    #ingnoring blank characters
    while(programa[posicion] == '\n' or programa[posicion] == ' ' or programa[posicion]== '\t'):
        if(programa[posicion] == '\n'):
            progLine+=1
        posicion += 1

    #parsing comments
    if(programa[posicion] == '/'):
        if(programa[posicion+1] == '*'):
            while(True):
                posicion += 1
                if(programa[posicion] == '*'):
                    if(programa[posicion+1] == '/'):
                        posicion+= 2
                        print("(COMMENT)")
                        break

    #continue read in case we had a comment
    while(programa[posicion] == ' ' or programa[posicion] == '\n' or programa[posicion]== '\t'):
        posicion += 1

    #Token switch
    if(programa[posicion] == '$'):
        return (printTokenType(TokenType.ENDFILE, '$', imprime, 1))
    elif(programa[posicion] == '+'):
        return (printTokenType(TokenType.PLUS, '+', imprime, 1))
    elif(programa[posicion] == '-'):
        return (printTokenType(TokenType.MINUS, '-', imprime, 1))
    elif(programa[posicion] == ';'):
        return (printTokenType(TokenType.SEMICOLON, ';', imprime, 1))
    elif(programa[posicion] == ','):
        return (printTokenType(TokenType.COMMA, ',', imprime, 1))
    elif(programa[posicion] == '('):
        return (printTokenType(TokenType.OPEN_PARENTHESIS, '(', imprime, 1))
    elif(programa[posicion] == ')'):
        return (printTokenType(TokenType.CLOSE_PARENTHESIS, ')', imprime,1 ))
    elif(programa[posicion] == '['):
        return (printTokenType(TokenType.OPEN_BRACKETS, '[', imprime, 1))
    elif(programa[posicion] == ']'):
        return (printTokenType(TokenType.CLOSE_BRACKETS, ']', imprime, 1))
    elif(programa[posicion] == '{'):
        return (printTokenType(TokenType.OPEN_KEYS, '{', imprime, 1))
    elif(programa[posicion] == '}'):
        return (printTokenType(TokenType.CLOSE_KEYS, '}', imprime, 1))
    elif(programa[posicion] == '<'):
        if(programa[posicion+1] == '='):
            return (printTokenType(TokenType.LESS_THAN_EQUAL_TO, '<=', imprime, 2))
        return (printTokenType(TokenType.LESS_THAN, '<', imprime, 1))
    elif(programa[posicion] == '>'):
        if(programa[posicion+1] == '='):
            return (printTokenType(TokenType.GREATER_THAN_EQUAL_TO, '>=', imprime, 2))
        return (printTokenType(TokenType.GREATER_THAN, '>', imprime, 1))
    elif(programa[posicion] == '*'):
        return (printTokenType(TokenType.ASTERISK, '*', imprime, 1))
    elif(programa[posicion] == '/'):
        return (printTokenType(TokenType.SLASH, '/', imprime, 1))
    elif(programa[posicion] == '='):
        if(programa[posicion+1] == '='):
            return (printTokenType(TokenType.EQUAL, '==', imprime, 2))
        return (printTokenType(TokenType.ASSIGNMENT, '=', imprime, 1))
    elif(programa[posicion] == '!'):
        if(programa[posicion+1] == '='):
            return (printTokenType(TokenType.DIFFERENT, '!=', imprime, 2))
        else:
            return(printTokenType(TokenType.ERROR, 'error', imprime, 2, "Error en la formación de una expresión", posicion))
    #Checking if the current pos is a number
    elif(programa[posicion].isdigit()):
        tokenSize = 1
        token = programa[posicion]
        while(True):
            if(programa[posicion+tokenSize].isdigit()):
                token += programa[posicion + tokenSize]
                tokenSize +=1
            elif(programa[posicion + tokenSize].isalpha()):
                pos = posicion + tokenSize
                errorpos = posicion + tokenSize
                while(True):
                    if(programa[posicion+tokenSize] == ' ' or programa[posicion+tokenSize] == '\n' or programa[posicion+tokenSize] == '\t'):
                        if(programa[posicion+tokenSize] == '\n'):
                            progLine+=1
                        return(printTokenType(TokenType.ERROR, 'error', imprime, tokenSize, "Error en la formación de un entero", errorpos))
                    else:
                        tokenSize += 1
            else:
                break
        return(printTokenType(TokenType.NUM, token, imprime, tokenSize))
    #chekcking if the current pos is a character
    elif(programa[posicion].isalpha()):
        tokenSize = 1
        token = programa[posicion]
        while(True):
            if(programa[posicion+tokenSize].isalnum()):
                token += programa[posicion + tokenSize]
                tokenSize +=1
            else:
                break
        return (getTypeFromToken(token, imprime, tokenSize))
    else:
        return(printTokenType(TokenType.ERROR, 'error', imprime, 1))


def printTokenType(TokenType, TokenVal, imprime, tokenLen, error = "", tokenSize = 0):
    global posicion
    posicion += tokenLen
    if(TokenVal == 'error'):
        generateError(error, tokenSize, progLine)
    if(imprime):
        print("({}, {})".format(TokenType, TokenVal))
    return(TokenType, TokenVal)

def generateError(error, posicion, line):
    linePos = posicion
    print("Línea {}: ".format(line), error)
    while(True):
        linePos -= 1
        if(programa[linePos] == '\n'):
            break
    pointer = linePos
    while(True):
        linePos += 1
        if(programa[linePos] == '\n'):
            break
        print(programa[linePos], end= "")
    print("\n")
    while(True):
        if(pointer == posicion-1):
            print("^")
            break
        else:
            print(" ", end="")
        pointer +=1