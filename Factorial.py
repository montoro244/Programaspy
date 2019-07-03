#Objetivo: Calcular el factorial de un numero
#Autor: Fernanda Montoro
#Fecha: Lunes 1 de Julio del 2019

#---------------------------------
#Metodo recursivo
#---------------------------------
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

#---------------------------------
#Funcion main
#---------------------------------
def main():
	num = int(input('Numero: '))
	print('El factorial es: ', str(factorial(num)))

if __name__ == '__main__':
	main()
