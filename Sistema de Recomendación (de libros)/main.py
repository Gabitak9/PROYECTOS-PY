# '--------------------------------------------------------------'
# '|     BIENVENIDO AL SISTEMA DE RECOMENDACION DE LIBROS       |'
# '|                          (V 3.0)                           |'
# '--------------------------------------------------------------'

#----------------------------------------------------------------|
#                 IMPORTAMOS MODULOS NECESARIOS                  |
#----------------------------------------------------------------|
from Tkinter import *

#----------------------------------------------------------------|
#                   FUNCIONES DEL PROGRAMA                       |
#----------------------------------------------------------------|
def informacion_usuario():
    archivo2 = open('BX-Book-Ratings.csv','r')
    d = {}
    d_perfil = {}
    s = set()
    for linea in archivo2:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario.get() == linea[0]:
            d[linea[1]] = linea[2]
            if linea[2] != '0':
                d_perfil[linea[1]] = linea[2]
                s.add(linea[1])
    archivo2.close()
    archivo = open('BX-Users.csv', 'r')
    for linea in archivo:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario.get() == linea[0]:
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
    lblInformacion_Usuario1=Label(v,text='INFORMACION USUARIO',font=('Verdana',8,'bold')).place(x=200,y=230)
    lblInformacion_Usuario2=Label(text= '\nUSUARIO: '+usuario+'\nEDAD: '+edad+'\nCIUDAD: '+ciudad.capitalize()+'\nESTADO: '+estado.capitalize()+'\nPAIS: '+pais.capitalize()+'\n',font=('Verdana',8)).place(x=120,y=245)
    btnAccion1=Button(v,text='LISTADO DE LIBROS COMPRADOS',font=('Verdana',8),command=imprimir_libros_comprados).place(x=300,y=260)
    if len(s) > 5:
        btnAccion2=Button(v,text='LISTADO DE LIBROS RECOMENDADOS',font=('Verdana',8),command=libros_sugeridos).place(x=300,y=285)
    elif len(s) <= 5:
        btnAccion2=Button(v,text='LISTADO DE LIBROS RECOMENDADOS',font=('Verdana',8),command=libros_sugeridos_2).place(x=300,y=285)
    btnAccion3=Button(v,text='TOP 20 DE LA COMUNIDAD',font=('Verdana',8),command=top_libros).place(x=300,y=310)
    archivo.close()
    return None

def top_libros():
    lbl1=Label(text='TOP 20 (COMUNIDAD)',font=('Verdana',8,'bold')).place(x=900,y=230)
    lstLibros=Listbox(v,font=('Verdana',8),background='White',width='80',height='6')
    archivo1=open('BX-Book-Ratings.csv','r')
    d = {}
    for linea in archivo1:
        linea = linea.strip().replace('"','').split(';')
        if linea[0] != 'User-ID' and linea[2] != '0':
            if linea[1] not in d:
                c = float(1)
                d[linea[1]] = [float(linea[2]),c]
            else:
                c = 1
                d[linea[1]] = [d[linea[1]][0]+float(linea[2]),float(d[linea[1]][1])+c]
    archivo1.close()
    lista = []
    for i,j in d.items():
        if j[1] > 30:
            prom = round(j[0]/j[1],2)
            lista.append((prom,i))
    lista.sort()
    lista.reverse()
    c = 0
    lista_top = []
    while c < 20:
        lista_top.append(lista[c])
        c += 1
    c = 0
    for i in lista_top:
        archivo1=open('BX-Books.csv','r')
        for linea in archivo1:
            linea = linea.strip().replace('"','').split(';')
            if linea[0] == i[1]:
                lstLibros.insert(c,str('"'+linea[1])+'" de '+str(linea[2])+' con un promedio de valoracion de: '+str(i[0]))
                c += 1
        archivo1.close()
    lstLibros.place(x=700,y=250)

def imprimir_libros_comprados():
    lbl1=Label(text='LIBROS COMPRADOS',font=('Verdana',8,'bold')).place(x=250,y=390)
    lstLibros=Listbox(v,font=('Verdana',8),background='White',width='90',height='20')
    archivo2 = open('BX-Book-Ratings.csv','r')
    d = {}
    d_perfil = {}
    s = set()
    for linea in archivo2:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario.get() == linea[0]:
            d[linea[1]] = linea[2]
            s.add(linea[1])
            if linea[2] != '0':
                d_perfil[linea[1]] = linea[2]
    archivo2.close()
    if len(d) != 0:
        archivo1 = open('BX-Books.csv', 'r')
        c = 0
        for linea in archivo1:
            linea = linea.strip().replace('"','').split(';')
            for i,j in d.items():
                if i == linea[0]:
                    if j == '0':
                        lstLibros.insert(c, '- "'+linea[1].title()+'" de '+linea[2].title()+', Sin valoracion')
                    else:
                        lstLibros.insert(c, '- "'+linea[1].title()+'" de '+linea[2].title()+', Con una valoracion de '+j)
                        c += 1
        archivo1.close()
    else:
        c = 0
    prom = promedio_valoraciones(d_perfil)
    lstLibros.place(x=20,y=410)
    lbl2=Label(text='\nEL USUARIO HA VALORADO '+str(c)+' LIBROS\nCON UN PROMEDIO DE VALORACION DE: '+str(prom),font=('Verdana',7)).place(x=200,y=335)

def libros_sugeridos():
    lbl1=Label(text='LIBROS SUGERIDOS',font=('Verdana',8,'bold')).place(x=800,y=390)
    btnAccion1=Button(v,text='RECOMENDAR',font=('Verdana',8),command=imprimir_libros).place(x=1090,y=385)

def libros_sugeridos_2():
    lbl1=Label(text='LIBROS SUGERIDOS',font=('Verdana',8,'bold')).place(x=800,y=390)
    btnAccion1=Button(v,text='RECOMENDAR',font=('Verdana',8),command=imprimir_libros_2).place(x=1090,y=385)
    
def imprimir_libros_2():
    lstLibros2=Listbox(v,font=('Verdana',8),background='White',width='90',height='20')
    archivo = open('BX-Users.csv', 'r')
    for linea in archivo:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario.get() == linea[0]:
            usuario = linea[0]
            edad = linea[2]
            localidad = linea[1].strip().replace(' ','').split(',')
            ciudad,estado,pais = localidad
    archivo.close()
    s_usuario = set()
    s_edad = set()
    s_localidad = set()
    archivo2 = open('Bx-Users.csv','r')
    for linea2 in archivo2:
        linea2 = linea2.strip().replace('"','').split(';')
        localidad2 = linea2[1].strip().replace(' ','').split(',')
        if edad == linea2[-1]:
            s_edad.add(linea2[0])
        if localidad[-1] == localidad2[-1]:
            s_localidad.add(linea2[0])
    archivo2.close()
    d = {}
    archivo1 = open('BX-Book-Ratings.csv','r')
    for linea in archivo1:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario.get() == linea[0]:
            s_usuario.add(linea[1])
        if linea[0] != 'User-ID' and linea[2] != '0':
            if linea[1] not in d and (linea[0] in s_edad or linea[0] in s_localidad):
                c = float(1)
                d[linea[1]] = [float(linea[2]),c]
            elif linea[1] in d and (linea[0] in s_edad or linea[0] in s_localidad):
                c = float(1)
                d[linea[1]] = [d[linea[1]][0]+float(linea[2]),float(d[linea[1]][1])+c]
    archivo1.close()
    lista = []
    for i,j in d.items():
        #UMBRAL QUE SE DEBE AJUSTAR
        if j[1] > 30:
            prom = round(j[0]/j[1],2)
            lista.append((prom,i))
    lista.sort()
    lista.reverse()
    c = 0
    lista_top = []
    for i in lista:
        if i[1] not in s_usuario:
            while c < int(cantidad_de_libros.get()):
                lista_top.append(lista[c])
                c += 1
    c = 0
    for i in lista_top:
        archivo3=open('BX-Books.csv','r')
        for linea in archivo3:
            linea = linea.strip().replace('"','').split(';')
            if linea[0] == i[1]:
                lstLibros2.insert(c,str('"'+linea[1])+'" de '+str(linea[2])+' con una valoracion de: '+str(i[0])+' |||COD:'+str(linea[0])+'|||')
                c += 1
        archivo3.close()
    lstLibros2.place(x=680,y=410)
    

def imprimir_libros():
    lstLibros2=Listbox(v,font=('Verdana',8),background='White',width='90',height='20')
    lstLibros2.place(x=680,y=410)
    d = {}
    d_perfil = {}
    s = set()
    archivo1 = open('BX-Book-Ratings.csv','r')
    for linea in archivo1:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario.get() == linea[0]:
            d[linea[1]] = linea[2]
            s.add(linea[1])
            if linea[2] != '0':
                d_perfil[linea[1]] = linea[2]
    archivo1.close()
    archivo2 = open('Bx-Vecinos_'+str(id_usuario.get())+'.csv', 'r')
    posibles_libros = []
    for linea in archivo2:
        Linea = linea.strip().split('|||')
        linea = Linea[2].split('|')
        for i in linea:
            libro, val = i.split(';')
            if libro not in d.keys():
                posibles_libros.append(libro)
    archivo2.close()
    diccionario_posibles_libros = {}
    for i in posibles_libros:
        denominador = 0
        numerador= 0
        archivo2 = open('Bx-Vecinos_'+str(id_usuario.get())+'.csv', 'r')
        for linea in archivo2:
            id,corr, libros = linea.strip().split('|||')
            libros = libros.split('|')
            for j in libros:
                libro, val = j.split(';')
                if i == libro:
                    denominador += float(corr)*float(val)
                    numerador += float(corr)
            if numerador != 0:
                estimacion = round((denominador/numerador), 2)
                if estimacion != float(10):
                    diccionario_posibles_libros[i] = estimacion
        archivo2.close()
    lista_ordenar = []
    for i,j in diccionario_posibles_libros.items():
        lista_ordenar.append((j, i))
    lista_ordenar.sort()
    lista_ordenar.reverse()
    x = 0
    for i in lista_ordenar:
        val, libro = i
        archivo = open('BX-Books.csv', 'r')
        if x < int(cantidad_de_libros.get()):
            for linea in archivo:
                linea = linea.strip().replace('"','').split(';')
                if libro == linea[0]:
                    lstLibros2.insert(x,'- "'+linea[1]+'" de '+linea[2]+' con una valoracion de: '+str(val)+' |||COD:'+str(linea[0])+'|||')
                    x += 1
        archivo.close()

def obtener_vecinos(d,s,d_perfil):
    lista_vecinos = []
    archivo1 = open('BX-Vecinos.csv', 'w')
    archivo2 = open('BX-Users.csv', 'r')
    for linea in archivo2:
        d2 = {}
        d2_perfil = {}
        s2 = set()
        linea = linea.strip().replace('"','').split(';')
        if linea[0] != 'User-ID':
            d2,d2_perfil,s2 = obtener_libros_usuario(linea[0])
            s_inter = s&s2
            if len(d2_perfil) > 0 and len(s_inter) > 0:
                pearson = corr_pearson(d,d2,s,s2)
                pearson_pon = pearson_ponderado(pearson,s_inter)
                print pearson_pon
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
    archivo1.close()
    archivo2.close()
    return lista_vecinos
    
def obtener_edad(id_usuario):
    archivo = open('BX-Users.csv', 'r')
    for linea in archivo:
        linea = linea.strip().replace('"','').split(';')
        if id_usuario == linea[0]:
            if linea[2] == 'NULL':
                edad = 'No disponible'
            else:
                edad = linea[2]

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

def promedio_valoraciones(d):
    suma = 0
    cont = 0
    for i,j in d.items():
        suma += int(j)
        cont += 1
    if len(d) == 0 and cont == 0:
        return 0
    else:
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

def media_rating(d):
    suma = 0
    cont = 0
    for i in d.values():
        if i != '0':
            suma += int(i)
            cont += 1
    return suma/cont

#----------------------------------------------------------------|
#                  CREANDO VENTANA DEL PROGRAMA                  |
#----------------------------------------------------------------|
#Caracteristicas Ventana
v=Tk()
v.geometry("1000x700")
v.title("SISTEMA DE RECOMENDACION DE LIBROS V.3.0")

#Texto Inicial
Banner=PhotoImage(file='banner.gif')
lblImagen=Label(v,image=Banner).pack()
Logo=PhotoImage(file='LogoPremium.gif')
lblImage=Label(v,image=Logo).place(x=0,y=0)

#----------------------------------------------------------------|
#                     EJECUTANDO PROGRAMA                        |
#----------------------------------------------------------------|
lblUsuario=Label(text='CODIGO DE USUARIO:',font=('Verdana',8)).pack()
#Se crea variable id_usuario para obtener informacion de este
id_usuario=StringVar()
id_usuario.set('Ingrese codigo ...')
txtUsuario=Entry(v,textvariable=id_usuario,background='White',font=('Verdana',8)).pack()
#Boton que llama a la funcion de obtener_informacion
edad = obtener_edad(id_usuario.get)
btnAccion=Button(v,text='INGRESAR',font=('Verdana',8),command=informacion_usuario).pack()
lbl1=Label(text='------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------').pack()
cantidad_de_libros=StringVar()
cantidad_de_libros.set('Ingrese cantidad ...')
txtCantidad=Entry(v,textvariable=cantidad_de_libros,background='White',font=('Verdana',8)).place(x=940,y=390)
#Ejecutando ventana
v.mainloop()
