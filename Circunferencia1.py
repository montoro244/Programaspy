#Objetivo: Calcula el area y diametro de una circunferencia e importar la libraria
#Autor: Fernanda Montoro
#Fecha: 1 de julio 2019

import math

#---------------------------------
#Funciòn para calcular area
#---------------------------------
def calculaArea(r):
    area = math.pi*(math.pow(r, 2))
    return area

#---------------------------------
#Funciòn para calcular diametro
#---------------------------------

def calculaDiametro(r):
    diametro = r * 2
    return diametro

#----------------------------------------------------------
#Funcion principal
#----------------------------------------------------------
def main():
    
    ciclo = True
    while ciclo == True:

        
        print('-- Script para calcular el Area de circulo')
        radio = float(input('\nIntroduce el valor del radio: '))

#----------------------------------------------------------
#Invoca metodos
#----------------------------------------------------------
        print('\nEl area es: ', str(calculaArea(radio)))
        print('El diametro es: ', str(calculaDiametro(radio)))

        r = input('\nOtro calculo (s/n)? ')
        if r == 'n' or r == 'N':
            ciclo = False


if __name__ == '__main__':
    main()