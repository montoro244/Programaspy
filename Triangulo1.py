#Objetivo: Identifica tipo de triangulo y su perimetro
#Autor: Fernanda Montoro
#Fecha: 1 de julio 2019

#------------------------------------------
#Funciòn para identificar tipo de triangulo
#-------------------------------------------
def compara(l1, l2, l3):
    if l1 == l2:
        if l1 == l3:
            tipo = 0
        else:
            tipo = 1
    elif l1 == l3 or l2 == l3:
        tipo = 1
    else:
        tipo = 2
    return tipo

#---------------------------------
#Funciòn para calcular perimetro
#---------------------------------
def perimetro(l1, l2, l3):
    perimetro = l1 + l2 + l3
    return perimetro


def main():

    tipos = ['equilatero', 'isosceles', 'escaleno']

    ciclo = True
    while ciclo == True:

        lado1 = float(input('Lado 1: '))
        lado2 = float(input('Lado 2: '))
        lado3 = float(input('Lado 3: '))

        print('\nEl triangulo es de tipo:', tipos[compara(lado1, lado2, lado3)])
        print('El perimetro del triangulo es:', perimetro(lado1, lado2, lado3))


        r = input('\nOtro calculo (s/n)? ')
        if r == 'n' or r == 'N':
            ciclo = False


if __name__ == '__main__':
    main()