#Objetivo: Muestra el funcionamiento de las listas en python
#Autor: Fernanda Montoro
#Fecha: Martes 2 de Julio del 2019

#---------------------------------
#Declaramos una lista de manera global
#---------------------------------
lista = []

#---------------------------------
#Metodo para parar la ejecucion del programa
#---------------------------------

def parar():
	paro = input('')
#---------------------------------
#Metodo para agregar un dato a la lista
#---------------------------------
def agregar(d):
	lista.append(d)
#---------------------------------
#Metodo para buscar un dato en la lista y muesta su posicion
#---------------------------------
def buscar(d):
	if d in lista:
		print('El dato esta en la posicion: ', str(lista.index(d)))
	else:
		print('Dato no encontrado')
	parar()

#---------------------------------
#Metodo para eliminar un dato de la lista
#---------------------------------
def eliminar(d):
	if d in lista:
		lista.remove(d)
		print('Dato eliminado')
	else:
		print('Dato no encontrado')
	parar()

#---------------------------------
#Metodo para imprimir todos los datos de la lista
#---------------------------------
def imprimir():
	j = 0
	for i in lista:
		print('Dato: ', j, ',', i)
		j = j +1
	parar()

#---------------------------------
#Metodo principal
#---------------------------------
def main():
	
	ciclo = True
	while ciclo == True:

		print('--- Script para trabajar con listas ---\n')
		print('0. Salir')
		print('1. Agrega elementos a la lista')
		print('2. Buscar un elemento en la lista')
		print('3. Eliminar un elemento de la lista')
		print('4. imprimir\n')

		opcion = int(input('Opcion: '))

		if opcion == 0:
			ciclo = False
		elif opcion == 1:
			dato = input('\nDato: ')
			agregar(dato)
		elif opcion == 2:
			dato = input('\nDato: ')
			buscar(dato)
		elif opcion == 3:
			dato = input('\nDato: ')
			eliminar(dato)
		elif opcion == 4:
			imprimir()
		else:
			print('ERROR: Opcion no valida')
			parar()
			

			
if __name__ == '__main__':
	main()
