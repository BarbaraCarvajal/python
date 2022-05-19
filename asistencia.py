"""
El Profesor ha decidido bonificar a los alumnos que tengan menos inasistencias al curso:

Inasistencia        Bonificación 
Mas de 10              0% 
Más de 7 hasta 10      3% 
Más de 4 hasta 7       5% 
4 o menos              10%

Debe solicitar al inicio la cantidad de alumnos del curso. 
El programa debe entregar: 
• La nota reajustada de cada alumno 
 
Además, debe validar: 
• El número de inasistencias debe ser mayor o igual a 0. 
• Las  notas  son  en  escala  chilena  (de  1,0  a  7,0).  Considere  valores  con 
decimales.

"""

alumnos=int(input("¿La información de cuántos alumnos ingresará?"))

for x in range(1,alumnos+1):
    nombre = input(f"Alumno {x}: ")
    nota = float(input("Nota: "))
    inasistencias = int(input("Numero de inasistencias: "))

    if inasistencias >10:
        print(f"La nota final de {nombre} es: {nota}, por haber tenido {inasistencias} inasistencias, no vuelvas a faltar!")
    elif inasistencias >7 and inasistencias <=10:
        bonificacion = nota *1.03
        print(f"La nota final de {nombre} es: {bonificacion:.2f}, por haber tenido {inasistencias} inasistencias,falta menos a la proxima!!")
    elif inasistencias >4 and inasistencias <=7:
        bonificacion = nota *1.05
        print(f"La nota final de {nombre} es: {bonificacion:.2f}, por haber tenido {inasistencias} sigue asi! pero no faltes :C!!")
    elif inasistencias >=0 and inasistencias <4:
        bonificacion = nota *1.10
        print(f"La nota final de {nombre} es: {bonificacion:.2f}, por haber tenido {inasistencias} sigue asi! Felicitaciones!!")
