#---------------------------------------------------------------------|
#                         FUNCIONES DEL PROGRAMA                      |
#---------------------------------------------------------------------|
def informacion_usuario(id_usuario):
    archivo = open('BX-Users.csv', 'r')
    for linea in archivo:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario == linea[0]:
            usuario = linea[0]
            if linea[2] == 'NULL':
                edad = 'No disponible'
            else:
                edad = linea[2]
            localidad = linea[1].strip().replace(' ','').split(',')
            for i in localidad:
                if i ==  'n/a':
                    localidad[localidad.index(i)] = 'No disponible'
            ciudad,estado,pais = localidad
    informacion_usuario = 'USUARIO: '+usuario+'\nEDAD: '+edad+'\nCIUDAD: '+ciudad.capitalize()+'\nESTADO: '+estado.capitalize()+'\nPAIS: '+pais.capitalize()
    archivo.close()
    print '--------------------------------------------------------------'
    print informacion_usuario
    return edad, pais

def obtener_libros_usuario(id_usuario):
    archivo = open('BX-Book-Ratings.csv','r')
    d = {}
    d_perfil = {}
    s = set()
    for linea in archivo:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario == linea[0]:
            d[linea[1]] = linea[2]
            s.add(linea[1])
            if linea[2] != '0':
                d_perfil[linea[1]] = linea[2]
    archivo.close()
    return d, d_perfil, s

def imprimir_libros_comprados(d,s,d_perfil,opcion):
    archivo = open('BX-Books.csv', 'r')
    c = 0
    x = 0
    for linea in archivo:
        linea = linea.strip().replace('"','').split(';')
        for i,j in d.items():
            if i == linea[0]:
                if j == '0':
                    if opcion == True:
                        print '- '+linea[1].title()+' de '+linea[2].title()+', sin valoracion'
                        val = False
                        x = +1
                else:
                    c += 1
                    if opcion == True:
                        print '- '+linea[1].title()+' de '+linea[2].title()+', con una valoracion de '+j
    archivo.close()
    if x == 1 and val == False:
        print 'El usuario ha valorado '+str(c)+' libros, con un promedio de valoracion de '+j
    else:
        prom = promedio_valoraciones(d_perfil)
        print '--------------------------------------------------------------'
        print 'El usuario ha valorado '+str(c)+' libros, con un promedio de valoracion de '+str(prom)
    solo_valoro_1 = False
    return solo_valoro_1

def obtener_opcion(d,s, d_perfil):
    opcion = raw_input('Desea imprimir listado de libros? (S/N): ')
    if opcion == 'S' or opcion == 's':
        opcion = True
        return imprimir_libros_comprados(d,s, d_perfil,opcion)
    elif opcion == 'N' or opcion == 'n':
        print 'No se imprimira listado ...'
        opcion = False
        return imprimir_libros_comprados(d,s, d_perfil,opcion)
    else:
        print 'Opcion invalida'
        obtener_opcion(d,s, d_perfil)

def obtener_opcion_2(lista):
    c = int(raw_input('Cuantas recomendaciones desea? (El max recomendaciones es de '+str(len(lista))+'): '))
    imprimir_libros_recomendados(lista, c)
    return None

def promedio_valoraciones(d):
    suma = 0
    cont = 0
    for i,j in d.items():
        suma += int(j)
        cont += 1
    return suma/cont

def corr_pearson(u1,u2,s1,s2):
    s = s1&s2
    r1 = media_rating(u1)
    r2 = media_rating(u2)
    suma = 0
    for i in s:
        suma += (float(u1[i])-float(r1))*(float(u2[i])-float(r2))
    if corr_auxiliar(u1,r1,s) != 0 and corr_auxiliar(u2,r2,s) != 0:
        total = suma/(corr_auxiliar(u1,r1,s)*corr_auxiliar(u2,r2,s))
    else:
        total = 0
    return total

def media_rating(d):
    suma = 0
    cont = 0
    for i in d.values():
        if i != '0':
            suma += int(i)
            cont += 1
    return suma/cont

def corr_auxiliar(u1,r1,s):
    suma = 0
    for i in s:
        suma += (float(u1[i])-r1)**2
    return suma**0.5

def pearson_ponderado(pearson,s_inter):
    umbral = 5
    if s_inter < umbral:
        pearson_pon = pearson*(s_inter/umbral)
    else:
        pearson_pon = pearson
    return pearson_pon

def obtener_vecinos(d,s,d_perfil,pais):
    lista_vecinos = []
    archivo1 = open('BX-Vecinos.csv', 'w')
    archivo2 = open('BX-Users.csv', 'r')
    for linea in archivo2:
        d2 = {}
        d2_perfil = {}
        s2 = set()
        linea = linea.strip().replace('"','').split(';')
        if linea[0] != 'User-ID':
            localidad = linea[1].strip().replace(' ','').split(',')
            if localidad[-1] == pais:
                d2,d2_perfil,s2 = obtener_libros_usuario(linea[0])
                s_inter = s&s2
                if len(d2_perfil) > 0 and len(s_inter) > 0:
                    pearson = corr_pearson(d,d2,s,s2)
                    pearson_pon = pearson_ponderado(pearson,s_inter)
                    if pearson > 0.1:
                        lista_vecinos.append(linea[0])
                        lista_escribir = []
                        for i,j in d2_perfil.items():
                            if i not in s_inter:
                                items = [i,j]
                                lista_aux = ';'.join(map(str,items))
                                lista_escribir.append(lista_aux)
                        lista_final = str(linea[0])+'|||'+str(pearson)+'|||'+'|'.join(lista_escribir)+'\n'
                        archivo1.write(lista_final)
                        print 'Vecino Encontrado'
    archivo1.close()
    archivo2.close()
    return lista_vecinos

def obtener_vecinos_sin_libros(d,s,d_perfil,pais):
    lista_vecinos = []
    archivo1 = open('BX-Vecinos.csv', 'w')
    archivo2 = open('BX-Users.csv', 'r')
    for linea in archivo2:
        d2 = {}
        d2_perfil = {}
        s2 = set()
        linea = linea.strip().replace('"','').split(';')
        if linea[0] != 'User-ID':
            localidad = linea[1].strip().replace(' ','').split(',')
            if localidad[-1] == pais:
                lista_vecinos.append(linea[0])
                lista_escribir = []
                d2,d2_perfil,s2 = obtener_libros_usuario(linea[0])
                if len(d2_perfil) > 0:
                    for i,j in d2_perfil.items():
                        items = [i,j]
                        lista_aux = ';'.join(map(str,items))
                        lista_escribir.append(lista_aux)
                    lista_final = str(linea[0])+'|||'+str(1.0)+'|||'+'|'.join(lista_escribir)+'\n'
                    archivo1.write(lista_final)
                    print 'Vecino Encontrado'
    archivo1.close()
    archivo2.close()
    return lista_vecinos

def posibles_libros(d):
    archivo = open('Bx-Vecinos.csv', 'r')
    posibles_libros = []
    for linea in archivo:
        Linea = linea.strip().split('|||')
        linea = Linea[2].split('|')
        for i in linea:
            print Linea[0]
            libro, val = i.split(';')
            if libro not in d.keys():
                posibles_libros.append(libro)
    archivo.close()
    return posibles_libros

def posibles_libros_edad(d, l):
    archivo = open('Bx-Vecinos.csv', 'r')
    posibles_libros = []
    for linea in archivo:
        Linea = linea.strip().split('|||')
        linea = Linea[2].split('|')
        for i in linea:
            libro, val = i.split(';')
            if libro not in d.keys() and Linea[0] in l:
                posibles_libros.append(libro)
    archivo.close()
    return posibles_libros

def usuarios_edad_similar(edad):
    archivo = open('Bx-Vecinos.csv', 'r')
    x = []
    for i in archivo:
        i = i.strip().split('|||')
        archivo2 = open('Bx-Users.csv')
        for j in archivo2:
            j = j.strip().replace('"', '').split(";")
            if j[0] == i[0]:
                if j[2] != "NULL" and (int(j[2]) >= int(edad)-15 and int(j[2]) <= int(edad)+15):
                    x.append(j[0])
        archivo2.close()
    archivo.close()
    return x
    
def estimacion_rating(l):
    d = {}
    for i in l:
        denominador = 0
        numerador= 0
        archivo = open('Bx-Vecinos.csv', 'r')
        for linea in archivo:
            id,corr, libros = linea.strip().split('|||')
            libros = libros.split('|')
            for j in libros:
                libro, val = j.split(';')
                if i == libro:
                    denominador += float(corr)*float(val)
                    numerador += float(corr)
            if numerador != 0:
                d[i] = round((denominador/numerador), 2)
        archivo.close()
    return d

def imprimir_libros_recomendados(d,c):
    l = []
    for i,j in d.items():
        if j != 10:
            l.append((j, i))
    l.sort()
    l.reverse()
    x = 0
    for i in l:
        val, libro = i
        archivo = open('BX-Books.csv', 'r')
        if x < c:
            for linea in archivo:
                linea = linea.strip().replace('"','').split(';')
                if libro == linea[0]:
                    print '-','"' + linea[1] + '"', 'de', linea[2] +',', 'con una valoracion de:', val,'||COD:',str(libro),'||'
                    x += 1
        archivo.close()
    return None
