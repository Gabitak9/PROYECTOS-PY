#!/usr/bin/python
import numpy as np

print '--------------------------------------------------------------'
print '|     BIENVENIDO AL SISTEMA DE RECOMENDACION DE LIBROS       |'
print '|                          (V 1.3)                           |'
print '|          Proceda a ingresar el codigo del usuario          |'
print '--------------------------------------------------------------'

from funciones import * 
    
#---------------------------------------------------------------------|
#                      INICIANDO PROGRAMA                             |
#---------------------------------------------------------------------|

id_usuario = str(raw_input('Codigo del usuario: '))

#-------------------------PRIMERA FASE--------------------------------|
#            (Informacion Usuario, Perfil usuario)

#Verificaremos que el usuario existe
archivo = open('BX-Users.csv', 'r')
s = set()
for linea in archivo:
    linea = linea.strip().replace('"','').split(';')
    s.add(linea[0])
archivo.close()
while id_usuario not in s:
    id_usuario = str(raw_input('El usuario no existe, ingrese nuevamente codigo del usuario: '))
#Si el usuario existe procedemos a imprimir su informacion
edad, pais = informacion_usuario(id_usuario)

#Se obtienen los libros que el usuario ha comprado, cuales ha valorado y el prom de valoracion
print '--------------------------------------------------------------'
print 'Obteniendo libros que el usuario ha comprado ...'
print '--------------------------------------------------------------'
d,d_perfil,s = obtener_libros_usuario(id_usuario)
libros_comprados = str(len(s))
print 'El usuario ha comprado '+str(len(s))+' libros'
if libros_comprados != '0':
    obtener_opcion(d,s, d_perfil)
    print '--------------------------------------------------------------'
    cero_libros = False
else:
    print '--------------------------------------------------------------'
    print 'Como el usuario no ha comprado ningun libro se recomendaran los mejores evaluados dentro de su pais'
    cero_libros = True

#-------------------------SEGUNDA FASE--------------------------------|
#                 (Obtencion vecinos del usuario)

#Llamamos a la funcion que permite obtener los vecinos del usuario y almacenamos
#estos vecinos con sus respectivos libros valorados en un diccionario.
if cero_libros == False:
    print 'Obteniendo vecinos ...'
    if len(s) < 2:
        a = obtener_vecinos_sin_libros(d,s,d_perfil,pais)
    else:
        a = obtener_vecinos(d,s,d_perfil,pais)
    print '--------------------------------------------------------------'
else:
    a = obtener_vecinos_sin_libros(d,s,d_perfil,pais)
    print '--------------------------------------------------------------'
    
#Una vez obtenido los usuarios a fin procedemos a obtener los posibles libros recomendados
print 'Obteniendo listado de libros recomendados ...'
if edad != 'No disponible':
    lista_edad_similar = usuarios_edad_similar(edad)
    posibles_libros_recomendados = posibles_libros_edad(d, lista_edad_similar)
else:
    posibles_libros_recomendados = posibles_libros(d)

#Ahora calcularemos la estimacion de rating para cada posible libro recomendado
libros_recomendados = estimacion_rating(posibles_libros_recomendados)

#Imprimimos la cantidad de libros que el usuario desea
print 'Se han obtenido '+str(len(libros_recomendados))+' libros acorde a los gustos del usuario.'
print '--------------------------------------------------------------'
c = obtener_opcion_2(libros_recomendados)
