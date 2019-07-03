#Objetivo: Calcular el finonacci
#Autor: Fernanda Montoro
#Fecha: Lunes 1 de Julio del 2019

#---------------------------------
#Metodo para calcular el n-esimo termino de la serie de fibonacci
#---------------------------------

def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

#---------------------------------
#Funcion main
#---------------------------------
def main():
	num = int(input('Numero: '))
	print('\nLa serie hasta el', str(num), '° es:')
	for i in range(1, num + 1):
		print(str(fibonacci(i)), ' ' ,end = '')
	print('\n')

if __name__ == '__main__':
	main()
