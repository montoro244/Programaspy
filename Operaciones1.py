#Objetivo: Muestre como trabajanlos metodos o funciones en phyton
#Autor: Fernanda Montoro
#Fecha: 29 de junio 2019

#---------------------------------
#Funciòn para sumar dos enteros
#---------------------------------
def suma(num1, num2):
    return num1 + num2

#---------------------------------
#Funciòn para restar dos enteros
#---------------------------------
def resta(num1, num2):
    return num1 - num2

#---------------------------------
#Funciòn para multiplicar dos enteros
#---------------------------------
def mult(num1, num2):
    return num1 * num2

#---------------------------------
#Funciòn para dividir dos enteros
#---------------------------------
def divi(num1, num2):
    return num1 / num2

#---------------------------------
#Funciòn para comparar dos enteros
#---------------------------------
def compara(num1, num2):
    if (num1 > num2):
        print('El mayor es num1:', num1)
    elif (num1 < num2):
        print('El mayor es num2:', num2)
    else:
        print('Num1 y num2 son iguales', num1, ',', num2)

#---------------------------------
#Funcion para contar de num1 a num2
#---------------------------------
def cuenta(num1, num2):
    for i in range(num1, num2 + 1):
        print('valor de i:', i)

#---------------------------------
#Funcion main
#---------------------------------
def main():
    ciclo = True
    while(ciclo == True):

        n1 = int(input('Primer numero: '))
        n2 = int(input('Segundo numero: '))

#---------------------------------
#Invocamos las funciones
#---------------------------------
        print('\nLa suma es: ' + str(suma(n1, n2)))
        print('La resta es: ' + str(resta(n1, n2)))
        print('La multipliacion es: ' + str(mult(n1, n2)))
        print('La divicion es: ' + str(divi(n1, n2)))

#---------------------------------
#Funciones compara y cuenta
#---------------------------------
        compara(n1, n2)
        cuenta(n1, n2)
        
#---------------------------------
#Otro calculo
#---------------------------------
        cad = input('\nOtro calculo (s/n)? ')
        if (cad == 's' or cad == 'S'):
            ciclo = True
        else:
            ciclo = False

if __name__ == '__main__':
    main()