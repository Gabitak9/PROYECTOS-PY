#IMPORTAMOS LIBRERIAS QUE NOS PERMITIRAN GRAFICAR Y OTRAS FUNCIONES
import matplotlib.pyplot as plt
from matplotlib.pylab import hist, show

print '--------------------------------------------------------------'
print '|      BIENVENIDO AL DETECTOR DE PLAGIOS (V.Beta 1.4)        |'
print '|                   Que desea realizar?                      |'
print '|        Opcion 1: Detectar plagio entre dos textos          |'
print '|    Opcion 2: Detectar plagio entre parrafos de un texto    |'
print '--------------------------------------------------------------'

#FUNCIONES DEL PROGRAMA
def iniciar_programa():
    opcion = raw_input('(MARQUE LA OPCION -NUMERO- CORRESPONDIENTE Y PRESIONE ENTER): ')
    if opcion == '1':
        opcion_e = '1'
        print 'Ha escogido la Opcion 1'
        return opcion_e
    elif opcion == '2':
        opcion_e = '2'
        print 'Ha escogido la Opcion 2'
        return opcion_e
    else:
        print 'Opcion Invalida'
        iniciar_programa()

def obtener_opcion():
    opcion = raw_input('(MARQUE LA OPCION -NUMERO- CORRESPONDIENTE Y PRESIONE ENTER): ')
    if opcion == '1':
        opcion_e = '1'
        print 'Creando archivo de Distancia Euclidiana ...'
        return opcion_e
    elif opcion == '2':
        opcion_e = '2'
        print 'Creando archivo de Distancia Coseno ...'
        return opcion_e
    elif opcion == '3':
        opcion_e = '3'
        print 'Creando archivos de Distancia Euclidiana y Distancia Coseno ...'
        return opcion_e
    else:
        print 'Opcion Invalida'
        obtener_opcion()

def obtener_opcion2():
    opcion = raw_input(str('MARQUE LA OPCION CORRESPONDIENTE (S/N) Y PRESIONE ENTER): '))
    if opcion == 's' or opcion == 'S':
        opcion_e2 = 's'
        print 'Creando grafico ...'
        return opcion_e2
    elif opcion == 'n' or opcion == 'N':
        opcion_e2 = 'n'
        print 'No se realizara el grafico'
        return opcion_e2
    else:
        print 'Opcion Invalida'
        obtener_opcion2()        

def obtener_lista_diccionarios_por_parrafo(archivo_analizar):
    archivo = open(archivo_analizar, 'r')
    lista = []
    for linea in archivo:
        d = {}
        if linea != '\n':
            parrafo = linea.strip().lower().replace(',','').replace(',','').replace(':','').replace(';','').replace('?','').replace('!','').replace('(','').replace(')','')
            parrafo = parrafo.split(' ')
            for palabra in parrafo:
                c_2 = parrafo.count(palabra)
                d[palabra] = c_2
            lista.append(d)
    archivo.close()
    return lista

def obtener_diccionario_palabras_total_archivo(archivo_analizar):
    archivo = open(archivo_analizar, 'r')
    d = {}
    for linea in archivo:
        if linea != '\n':
            parrafo = linea.strip().lower().replace(',','').replace(',','').replace(':','').replace(';','').replace('?','').replace('!','').replace('(','').replace(')','')
            parrafo = parrafo.split(' ')
            for palabra in parrafo:
                if palabra in d:
                    palabras_total = int(parrafo.count(palabra)) + int(d[palabra])
                    d[palabra] = palabra_total
                else:
                    palabra_total = parrafo.count(palabra)
                    d[palabra] = palabra_total
    archivo.close()
    return d

def distancia_euclidiana(diccionario1,diccionario2):
    suma = 0
    conjunto_palabras = set(diccionario1)|set(diccionario2)
    for palabra in conjunto_palabras:
        total_dic1 = float(0)
        total_dic2 = float(0)
        if palabra in diccionario1:
            total_dic1 = float(diccionario1[palabra])
        if palabra in diccionario2:
            total_dic2 = float(diccionario2[palabra])
        suma = suma + ((total_dic1 - total_dic2)**2)
    return float(suma)**0.5

def distancia_coseno(diccionario1,diccionario2):
    suma = 0
    d0 = {}
    deucli_1 = float(distancia_euclidiana(diccionario1,d0))
    deucli_2 = float(distancia_euclidiana(diccionario2,d0))
    conjunto_palabras = set(diccionario1)|set(diccionario2)
    for palabra in conjunto_palabras:
        total_dic1 = 0
        total_dic2 = 0
        if palabra in diccionario1:
            total_dic1 = float(diccionario1[palabra])
        if palabra in diccionario2:
            total_dic2 = float(diccionario2[palabra])
        suma = suma + (total_dic1*total_dic2)
    division = float(suma)/float(deucli_1*deucli_2)
    distancia = abs(1-division)
    return distancia

def cantidad_de_parrafos(archivo_analizar):
    archivo = open(archivo_analizar, 'r')
    parrafos_archivo = 0
    for linea in archivo:
        if linea != '\n':
            parrafos_archivo += 1
    archivo.close()
    return int(parrafos_archivo)

def porcentaje_plagio(valor):
    porcentaje = float(100) - (float(100)*float(valor))
    porcentaje_redondeado = '%.2f' % round(porcentaje)
    return porcentaje_redondeado

def analisis_resultado_2archivos(archivo_resultados):
    archivo = open(archivo_resultados, 'r')
    lista = []
    for linea in archivo:
        linea_a_leer = linea.strip().split(':')
        for dato in linea_a_leer:
            lista.append(float(dato))
    promedio = sum(lista)/len(lista)
    if promedio > 20:
        return 'Los textos son diferentes'
    elif promedio <= 20 and promedio > 10:
        return 'Los textos tienen similitudes, podria tratarse de un plagio'
    elif promedio <= 10 and promedio > 0:
        return 'Los textos son muy parecidos, se trata de un plagio'
    elif promedio == 0:
        return 'Uno de los textos es una copia del otro'
    archivo.close()

def analisis_resultado_1archivo(archivo_resultados):
    archivo = open(archivo_resultados, 'r')
    parrafo = 1
    lista = []
    for linea in archivo:
        linea_a_leer = linea.strip().split(':')
        if linea != '\n':
            for dato in linea_a_leer:
                conjunto = {parrafo,(linea_a_leer.index(dato)+1)}
                if conjunto not in lista:
                    lista.append(conjunto)
                    if float(dato) > 20:
                        if parrafo != linea_a_leer.index(dato)+1:
                            print 'Los parrafos '+str(parrafo)+' y '+str(linea_a_leer.index(dato)+1)+' son diferentes'
                    elif float(dato) <= 20 and float(dato) > 10:
                        if parrafo != linea_a_leer.index(dato)+1:
                            print 'Los parrafos '+str(parrafo)+' y '+str(linea_a_leer.index(dato)+1)+' tienen similitudes, podria tratarse de un plagio'
                    elif float(dato) <= 10 and float(dato) > 0:
                        if parrafo != linea_a_leer.index(dato)+1:
                            print 'Los parrafos '+str(parrafo)+' y '+str(linea_a_leer.index(dato)+1)+' son muy parecidos, se trata de un plagio'
                    elif float(dato) == 0:
                        if parrafo != linea_a_leer.index(dato)+1:
                            print 'El parrafo '+str(parrafo)+' es una copia del parrafo '+str(linea_a_leer.index(dato)+1)
        parrafo += 1
    archivo.close()

def obtener_datos_tabular(archivo_resultados):
    archivo = open(archivo_resultados, 'r')
    lista = []
    i = 0
    for linea in archivo:
        linea_a_leer = linea.strip().split(':')
        c = len(linea_a_leer)
        i = i + 1
        normalizador = i
        while i<c:
            lista.append(linea_a_leer[i])
            i = i+1
        i = normalizador
    return lista

#INICIANDO PROGRAMA
opcion_e = iniciar_programa()

#SE OBTIENEN LOS PARRAFOS DE CADA ARCHIVO
if opcion_e == '1':
    variable = 'opcion1'
    archivo_a_analizar_1 = str(raw_input('Ingrese nombre del archivo 1: '))
    archivo_a_analizar_2 = str(raw_input('Ingrese nombre del archivo 2: '))
    parrafos_archivo1 = cantidad_de_parrafos(archivo_a_analizar_1)
    parrafos_archivo2 = cantidad_de_parrafos(archivo_a_analizar_2)
    print 'Su archivo de texto 1 tiene '+str(parrafos_archivo1)+' parrafos'
    print 'Su archivo de texto 2 tiene '+str(parrafos_archivo2)+' parrafos'
elif opcion_e == '2':
    variable = 'opcion2'
    archivo_a_analizar_1 = str(raw_input('Ingrese nombre del archivo: '))
    parrafos_archivo1 = cantidad_de_parrafos(archivo_a_analizar_1)
    print 'Su archivo de texto tiene '+str(parrafos_archivo1)+' parrafos'

#SE OBTIENE LISTA DE DICCIONARIOS/DICCIONARIO POR CADA ARCHIVO
if variable == 'opcion1':
    diccionarios_1 = obtener_diccionario_palabras_total_archivo(archivo_a_analizar_1)
    lista_diccionarios_1 = obtener_lista_diccionarios_por_parrafo(archivo_a_analizar_1)
    diccionarios_2 = obtener_diccionario_palabras_total_archivo(archivo_a_analizar_2)
    lista_diccionarios_2  = obtener_lista_diccionarios_por_parrafo(archivo_a_analizar_2)
elif variable == 'opcion2':
    lista_diccionarios = obtener_lista_diccionarios_por_parrafo(archivo_a_analizar_1)

print '--------------------------------------------------------------'
print '|                Que desea realizar ahora?                   |'
print '|   - Opcion 1: Calcular plagio con Distancia Euclidiana     |'
print '|    - Opcion 2: Calcular plagio con Distancia Coseno        |'
print '|    - Opcion 3: Calcular plagio con ambas distancias        |'
print '--------------------------------------------------------------'
opcion_e = obtener_opcion()

#SE ACCEDE A CADA OPCION Y SE CREA UN ARCHIVO CON LOS RESULTADOS DE CADA ANALISIS
if opcion_e == '1':
    if variable == 'opcion1':
        archivo_tabla_eucli = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'w')
        for dic_parrafo_archivo1 in lista_diccionarios_1:
            lista_eucli = []
            for dic_parrafo_archivo2 in lista_diccionarios_2:
                eucli = distancia_euclidiana(dic_parrafo_archivo1, dic_parrafo_archivo2)
                lista_eucli.append(eucli)
            linea_escribir_eucli = ':'.join(map(str,lista_eucli))+'\n'
            archivo_tabla_eucli.write(linea_escribir_eucli)
        print 'Archivo de Distancia Euclidiana creado con exito'
        archivo_tabla_eucli.close()
        print 'Segun el analisis de Distancia Euclidiana ...'
        print analisis_resultado_2archivos('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt')
    elif variable == 'opcion2':
        archivo_tabla_eucli = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'.txt', 'w')
        for dic_parrafo in lista_diccionarios:
            lista_eucli = []
            for dic_parrafo_2 in lista_diccionarios:
                eucli = distancia_euclidiana(dic_parrafo, dic_parrafo_2)
                lista_eucli.append(eucli)
            linea_escribir_eucli = ':'.join(map(str,lista_eucli))+'\n'
            archivo_tabla_eucli.write(linea_escribir_eucli)
        print 'Archivo de Distancia Euclidiana creado con exito'
        archivo_tabla_eucli.close()
        print 'Segun el analisis de Distancia Euclidiana ...'
        print analisis_resultado_1archivo('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'.txt')

elif opcion_e == '2':
    if variable == 'opcion1':
        archivo_tabla_coseno = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'w')
        for dic_parrafo_archivo1 in lista_diccionarios_1:
            lista_coseno = []
            for dic_parrafo_archivo2 in lista_diccionarios_2:
                coseno = distancia_coseno(dic_parrafo_archivo1, dic_parrafo_archivo2)
                lista_coseno.append(coseno)
            linea_escribir_coseno = ':'.join(map(str,lista_coseno))+'\n'
            archivo_tabla_coseno.write(linea_escribir_coseno)
        archivo_tabla_coseno.close()
        print 'Archivo de Distancia Coseno creado con exito'
        porcentaje = float(porcentaje_plagio(distancia_coseno(diccionarios_1,diccionarios_2)))
        if porcentaje < 25:
            print 'Los archivos de texto son diferentes'
        if porcentaje >= 25 and porcentaje <50:
            print 'Los archivos de textos presentan similitudes'
        elif porcentaje >= 50 and porcentaje < 75:
            print 'Los archivos son muy parecidos, podria tratarse de un plagio'
        elif porcentaje >= 75 and porcentaje < 100:
            print 'Los archivos son practicamente iguales, se trata de un plagio'
        elif porcentaje == 100:
            print 'Los archivos son iguales'
        print 'El porcentaje de plagio es de '+str(porcentaje_plagio(distancia_coseno(diccionarios_1,diccionarios_2)))+'%'
        archivo_tabla_coseno.close()
    elif variable == 'opcion2':
        archivo_tabla_coseno = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'.txt', 'w')
        for dic_parrafo in lista_diccionarios:
            lista_coseno = []
            for dic_parrafo_2 in lista_diccionarios:
                coseno = distancia_coseno(dic_parrafo, dic_parrafo_2)
                lista_coseno.append(coseno)
            linea_escribir_coseno = ':'.join(map(str,lista_coseno))+'\n'
            archivo_tabla_coseno.write(linea_escribir_coseno)
        archivo_tabla_coseno.close()
        print 'Archivo Distancia Coseno creado con exito'

elif opcion_e == '3':
    if variable == 'opcion1':
        archivo_tabla_eucli = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'w')
        archivo_tabla_coseno = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'w')
        for dic_parrafo_archivo1 in lista_diccionarios_1:
            lista_eucli = []
            lista_coseno = []
            for dic_parrafo_archivo2 in lista_diccionarios_2:
                eucli = distancia_euclidiana(dic_parrafo_archivo1, dic_parrafo_archivo2)
                coseno = distancia_coseno(dic_parrafo_archivo1, dic_parrafo_archivo2)
                lista_eucli.append(eucli)
                lista_coseno.append(coseno)
            linea_escribir_eucli = ':'.join(map(str,lista_eucli))+'\n'
            linea_escribir_coseno = ':'.join(map(str,lista_coseno))+'\n'
            archivo_tabla_eucli.write(linea_escribir_eucli)
            archivo_tabla_coseno.write(linea_escribir_coseno)
        print 'Archivo de Distancia Euclidiana creado con exito'
        print 'Archivo de Distancia Coseno creado con exito'
        archivo_tabla_eucli.close()
        archivo_tabla_coseno.close()
        print 'Segun el analisis de Distancia Euclidiana ...'
        print analisis_resultado_2archivos('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt')
        print 'Segun el analisis de Distancia Coseno ...'
        porcentaje = float(porcentaje_plagio(distancia_coseno(diccionarios_1,diccionarios_2)))
        if porcentaje < 50:
            print 'Los archivos de textos presentan similitudes, podria tratarse de un plagio'
        elif porcentaje >= 50 and porcentaje < 75:
            print 'Los archivos son muy parecidos, podria tratarse de un plagio'
        elif porcentaje >= 75 and porcentaje < 100:
            print 'Los archivos son practicamente iguales, se trata de un plagio'
        elif porcentaje == 100:
            print 'Los archivos son iguales'
        print 'El porcentaje de plagio es de '+str(porcentaje_plagio(distancia_coseno(diccionarios_1,diccionarios_2)))+'%'
    elif variable == 'opcion2':
        archivo_tabla_eucli = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'.txt', 'w')
        archivo_tabla_coseno = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'.txt', 'w')
        for dic_parrafo in lista_diccionarios:
            lista_eucli = []
            lista_coseno = []
            for dic_parrafo_2 in lista_diccionarios:
                eucli = distancia_euclidiana(dic_parrafo, dic_parrafo_2)
                coseno = distancia_coseno(dic_parrafo, dic_parrafo_2)
                lista_eucli.append(eucli)
                lista_coseno.append(coseno)
            linea_escribir_eucli = ':'.join(map(str,lista_eucli))+'\n'
            linea_escribir_coseno = ':'.join(map(str,lista_coseno))+'\n'
            archivo_tabla_eucli.write(linea_escribir_eucli)
            archivo_tabla_coseno.write(linea_escribir_coseno)
        archivo_tabla_eucli.close()
        archivo_tabla_coseno.close()
        print 'Archivos creados con exito'

print 'Desea graficar los resultados?\n- Si\n- No'
opcion_e2 = obtener_opcion2()

#CREAMOS LA VENTANA DEL GRAFICO
plt.figure('Detector de Plagios')
plt.rc('font', size = 18)
plt.suptitle('Histograma de Analisis de Plagio')
plt.rc('font', size = 12)
plt.minorticks_on()
plt.grid(True)

#CREANDO EL GRAFICO
if opcion_e2 == 's':
    if opcion_e == '1':
        plt.plot(1,2)
        if variable == 'opcion1':
            archivo = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'r')
            data = []
            for linea in archivo:
                linea_a_leer = linea.strip().split(':')
                for dato in linea_a_leer:
                    data.append(dato)
        elif variable == 'opcion2':
            archivo = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'.txt', 'r')
            data = obtener_datos_tabular('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'.txt')
        cantidad_valores = len(data)
        plt.hist(map(float,data),cantidad_valores, (0,30))
        plt.xlabel('Distancia Euclidiana entre parrafos')
        plt.ylabel('Frecuencia')
        archivo.close()
    elif opcion_e == '2':
        plt.plot(1,2)
        if variable == 'opcion1':
            archivo = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'r')
            data = []
            for linea in archivo:
                linea_a_leer = linea.strip().split(':')
                for dato in linea_a_leer:
                    data.append(dato)
        elif variable == 'opcion2':
            archivo = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'.txt', 'r')
            data = obtener_datos_tabular('Tabla_coseno_'+str(archivo_a_analizar_1)+'.txt')
        cantidad_valores = len(data)
        plt.hist(map(float,data),cantidad_valores, (0,1))
        plt.xlabel('Distancia Coseno entre parrafos')
        plt.ylabel('Frecuencia')
        archivo.close()
    elif opcion_e == '3':
        plt.subplot(1,2,1)
        if variable == 'opcion1':
            archivo = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'r')
        elif variable == 'opcion2':
            archivo = open('Tabla_euclidiana_'+str(archivo_a_analizar_1)+'.txt', 'r')
        data = []
        for linea in archivo:
            linea_a_leer = linea.strip().split(':')
            for dato in linea_a_leer:
                data.append(dato)
        cantidad_valores = len(data)
        plt.hist(map(float,data),cantidad_valores, (0,30))
        plt.xlabel('Distancia Euclidiana entre parrafos')
        plt.ylabel('Frecuencia')
        archivo.close()
        plt.subplot(1,2,2)
        if variable == 'opcion1':
            archivo = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'_'+str(archivo_a_analizar_2)+'.txt', 'r')
        elif variable == 'opcion2':
            archivo = open('Tabla_coseno_'+str(archivo_a_analizar_1)+'.txt', 'r')
        data2 = []
        for linea in archivo:
            linea_a_leer = linea.strip().split(':')
            for dato in linea_a_leer:
                data2.append(dato)
        cantidad_valores = len(data2)
        plt.hist(map(float,data2),cantidad_valores, (0,1))
        plt.xlabel('Distancia Coseno entre parrafos')
        plt.ylabel('Frecuencia')
        archivo.close()
    show()
