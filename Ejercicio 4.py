#Realice un programa en Python que permita capturar en una lista las calificaciones
#de N alumnos y que le permita calcular e imprimir lo siguiente:
# -El promedio general de los alumnos
# -Numero de alumnos aprobados y número de alumnos reprobados (Si el alumno sacó una calificación menor a 70 se considera reprobado)
# -Porcentaje de alumnos aprobados y reprobados.
# -Número de alumnos cueya calificación fue mayor a 80

cal = []

def promedio():
    sum = 0.0
    
    for i in range(0, len(cal)):
        sum = sum + cal[i]

    prom = sum / len(cal)
    return prom

def aprobado():
    apro = 0
    repro = 0
    ochenta = 0

    for i in range(0, len(cal)):
        if cal[i] >= 70:
            if cal[i] >= 81:
                ochenta = ochenta + 1
            apro = apro + 1
        else:
            repro = repro + 1

    print('Aprobados: ', str(apro))
    print('Reprobados: ', str(repro))

    porapro = apro * 100 / len(cal)
    print('Porcentaje de aprobados: ', porapro)
    
    porrepro = repro * 100 / len(cal)
    print('Porcentaje de reprobados: ', porrepro)

    print('Alumnos con mas de 80:', ochenta)

    

def main():
    ciclo = True
    while ciclo == True:

        cal = float(input('Calificacion: '))
        cal.append(cal)
        otro = input('Ingresar otra calificacion? (s/n): ')
        if otro == 'n':
            ciclo = False

    else:
        print('Prmedio: ', str(promedio()))
        aprobado()
    
if __name__ == '__main__':
    main()