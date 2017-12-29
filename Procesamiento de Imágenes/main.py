# -*- coding: cp1252 -*-
#-----------------------------------------------------------------------
#                   IMPORTAMOS MODULOS NECESARIOS                      |
#-----------------------------------------------------------------------
from PIL import Image, ImageTk
import PIL.Image
import numpy
from Tkinter import *

#-----------------------------------------------------------------------
#                             FUNCIONES                                |
#-----------------------------------------------------------------------

def mostrar_imagen():
    
    #Creando ventana para previsualizar imagen cargada
    lblcv = Label(text='IMAGEN CARGADA',font=('Governor',9),foreground='#6d6e70').place(x=16,y=135)
    cv=Canvas(v,width=400,height=400)
    cv.place(x=10,y=150)
    cv.create_rectangle(10,10,390,390)
    
    #Cargando imagen con ayuda de la libreria PIL para soportar todos los formatos de imagen
    photo = PIL.Image.open(id_imagen.get())
    photo.thumbnail((374,374), PIL.Image.ANTIALIAS) #Modificamos tamaño
    photo = ImageTk.PhotoImage(photo)
    label = Label(image=photo)
    label.image = photo
    label.place(x=22,y=162)
    
    #Convirtiendo imagen a archivo para su manipulacion
    imagen = PIL.Image.open(id_imagen.get())
    imagen = imagen.convert('RGB')
    matrizNumpy = numpy.array(imagen)
    archivo = open('Archivo_temporal_imagen', 'w')
    for fila in matrizNumpy:
        for pixel in fila :
            for componente in pixel :
                archivo.write(' ' + str(componente))
            archivo.write(',')
        archivo.write('\n')
    archivo.close()

    #Agregando Opciones
    btnAccion = Button(v,text='EDITAR IMAGEN',font=('Governor',10),background='#01a8a6',foreground='White',command=mostrar_opciones).place(x=135,y=550)
    lblinstrucciones = Label(text='Para acceder a las opciones de edicion,\nproceda a seleccionar -EDITAR IMAGEN-',font=('Verdana',7),foreground='#6d6e70').place(x=85,y=570)

    return True

def mostrar_opciones():

    lbl1 = Label(text='OPCIONES DE EDICION',font=('Governor',10),foreground='#6d6e70').place(x=450,y=135)
    lbl2 = Label(text='Seleccione la(s) opcion(es) que desea aplicar a la imagen',font=('Verdana',7),foreground='#6d6e70').place(x=450,y=150)

    #Opciones de Rotacion
    lbl3 = Label(text='ROTAR', font=('Verdana',8, 'bold'),foreground='#6d6e70').place(x=450,y=170)
    check1 = Checkbutton(text='90*',font=('Verdana',7),foreground='#6d6e70',variable=rotar_90,onvalue=1,offvalue=0).place(x=455,y=185)
    check2 = Checkbutton(text='180*',font=('Verdana',7),foreground='#6d6e70',variable=rotar_180,onvalue=1,offvalue=0).place(x=455,y=200)
    check3 = Checkbutton(text='270*',font=('Verdana',7),foreground='#6d6e70',variable=rotar_270,onvalue=1,offvalue=0).place(x=455,y=215)

    #Opciones de Espejo
    lbl4 = Label(text='ESPEJO', font=('Verdana',8,'bold'),foreground='#6d6e70').place(x=450,y=238)
    check4 = Checkbutton(text='Horizontal',font=('Verdana',7),foreground='#6d6e70',variable=espejo_horizontal,onvalue=1,offvalue=0).place(x=455,y=255)
    check5 = Checkbutton(text='Vertical',font=('Verdana',7),foreground='#6d6e70',variable=espejo_vertical,onvalue=1,offvalue=0).place(x=455,y=270)

    #Opciones de Efectos Visuales
    lbl5 = Label(text='EFECTOS VISUALES', font=('Verdana',8,'bold'),foreground='#6d6e70').place(x=450,y=295)
    check6 = Checkbutton(text='Escala de Grises',font=('Verdana',7),foreground='#6d6e70',variable=escala_grises,onvalue=1,offvalue=0).place(x=455,y=312)
    check11 = Checkbutton(text='Blanco y Negro',font=('Verdana',7),foreground='#6d6e70',variable=blanco_y_negro,onvalue=1,offvalue=0).place(x=455,y=327)
    check7 = Checkbutton(text='Negativo',font=('Verdana',7),foreground='#6d6e70',variable=negativo,onvalue=1,offvalue=0).place(x=455,y=342)
    check8 = Checkbutton(text='Rojo sobre Grises',font=('Verdana',7),foreground='#6d6e70',variable=rojo_sobre_grises,onvalue=1,offvalue=0).place(x=455,y=357)
    check9 = Checkbutton(text='Azul sobre Grises',font=('Verdana',7),foreground='#6d6e70',variable=azul_sobre_grises,onvalue=1,offvalue=0).place(x=455,y=372)
    check10 = Checkbutton(text='Verde sobre Grises',font=('Verdana',7),foreground='#6d6e70',variable=verde_sobre_grises,onvalue=1,offvalue=0).place(x=455,y=387)
    
    #Opciones de Filtros
    lbl9 = Label(text='FILTROS', font=('Verdana',8,'bold'),foreground='#6d6e70').place(x=450,y=415)
    check16 = Checkbutton(text='Filtro Color',font=('Verdana',7),foreground='#6d6e70',variable=filtro_color,onvalue=1,offvalue=0).place(x=455,y=435)
    lbl10 = Label(text='(Rojo=1, Azul=2, Verde=3, Morado=4, Celeste=5, Amarillo=6)',font=('Verdana',7,'italic'),foreground='#6d6e70').place(x=455,y=450)
    barra3 = Scale(v,font=('Verdana',7),orient=HORIZONTAL,width=10,length=100,from_=1,to=6,foreground='#686868',variable=opcion).place(x=555,y=420)
    check18 = Checkbutton(text='Filtro Bandera Chile',font=('Verdana',7),foreground='#6d6e70',variable=bandera_chile,onvalue=1,offvalue=0).place(x=455,y=465)
    check19 = Checkbutton(text='Filtro Bandera Francia',font=('Verdana',7),foreground='#6d6e70',variable=bandera_francia,onvalue=1,offvalue=0).place(x=455,y=480)
    check20 = Checkbutton(text='Filtro 4 Colores',font=('Verdana',7),foreground='#6d6e70',variable=cuatro_colores,onvalue=1,offvalue=0).place(x=455,y=495)
    check21 = Checkbutton(text='Filtro 4 Imagenes',font=('Verdana',7),foreground='#6d6e70',variable=cuatro_imagenes,onvalue=1,offvalue=0).place(x=455,y=510)
    check23 = Checkbutton(text='Colo-Colo ',font=('Verdana',7),foreground='#6d6e70',variable=colo_colo,onvalue=1,offvalue=0).place(x=455,y=525)
    check24 = Checkbutton(text='U. De Chile ',font=('Verdana',7),foreground='#6d6e70',variable=u_dechile,onvalue=1,offvalue=0).place(x=555,y=525)
    
    #Opciones de Filtro Especial
    lbl10 = Label(text='FILTRO ESPECIAL', font=('Verdana',8,'bold'),foreground='#6d6e70').place(x=450,y=540)
    check22 = Checkbutton(text='Filtro Especial',font=('Verdana',7),foreground='#6d6e70',variable=filtro_especial,onvalue=1,offvalue=0).place(x=455,y=560)
    barra4 = Scale(v,label='Color',font=('Verdana',7),orient=HORIZONTAL,width=10,length=100,from_=1,to=6,foreground='#686868',variable=opcion_color).place(x=455,y=580)
    barra5 = Scale(v,label='Intensidad',font=('Verdana',7),orient=HORIZONTAL,width=10,length=100,from_=0,to=255,foreground='#686868',variable=opcion_intensidad).place(x=555,y=580)
    
    #Opciones de Reflexion
    lbl6 = Label(text='REFLEXION', font=('Verdana',8, 'bold'),foreground='#6d6e70').place(x=600,y=170)
    check12 = Checkbutton(text='Derecha',font=('Verdana',7),foreground='#6d6e70',variable=reflexion_der,onvalue=1,offvalue=0).place(x=605,y=185)
    check13 = Checkbutton(text='Izquierda',font=('Verdana',7),foreground='#6d6e70',variable=reflexion_izq,onvalue=1,offvalue=0).place(x=605,y=200)
    
    #Opciones de Contraste
    lbl7 = Label(text='CONTRASTE', font=('Verdana',8, 'bold'),foreground='#6d6e70').place(x=600,y=238)
    check14 = Checkbutton(text='Intensidad',font=('Verdana',7),foreground='#6d6e70',variable=contraste,onvalue=1,offvalue=0).place(x=605,y=253)
    barra1 = Scale(v,font=('Verdana',7),orient=HORIZONTAL,width=10,length=100,from_=-100,to=100,foreground='#686868',variable=rango).place(x=700,y=238)

    #Opciones de Desenfoque
    lbl8 = Label(text='DESENFOQUE', font=('Verdana',8, 'bold'),foreground='#6d6e70').place(x=600,y=295)
    check15 = Checkbutton(text='Radio',font=('Verdana',7),foreground='#6d6e70',variable=desenfoque,onvalue=1,offvalue=0).place(x=605,y=310)
    barra2 = Scale(v,font=('Verdana',7),orient=HORIZONTAL,width=10,length=100,from_=1,to=6,foreground='#686868',variable=radio).place(x=700,y=295)

    #Opciones de new coleccion
    lb20 = Label(text='NEW COLLECTION', font=('Verdana',8, 'bold'),foreground='#6d6e70').place(x=600,y=352)
    check24 = Checkbutton(text='Cambio de color',font=('Verdana',7),foreground='#6d6e70',variable=cambio_color,onvalue=1,offvalue=0).place(x=605,y=367)
    barra4 = Scale(v,font=('Verdana',7),orient=HORIZONTAL,width=10,length=100,from_=1,to=5,foreground='#686868',variable=opcion_cambio).place(x=740,y=352)

    #Boton para aplicar edicion
    btnAccion = Button(v,text='APLICAR EFECTOS',font=('Governor',12),background='#01a8a6',foreground='White',command=editar_imagen).place(x=530,y=650)

    #Creando ventana para previsualizar imagen cargada
    lblcv = Label(text='IMAGEN MODIFICADA',font=('Governor',9),foreground='#6d6e70').place(x=900,y=135)
    cv=Canvas(v,width=400,height=400)
    cv.place(x=900,y=150)
    cv.create_rectangle(10,10,390,390)

    return True

def editar_imagen():

    #Obtener matriz de la imagen
    archivo = open('Archivo_temporal_imagen','r')
    matriz = []
    for i in archivo:
        lista = []
        fila = []
        lista = i.strip(",\n").split(',')
        for pixel in lista :
            aux = pixel.split()
            for e in range(3) :
                aux[e] = int(aux[e])
            fila.append(aux)
        matriz.append(fila)
    archivo.close()

    #Se procederá a revisar cada opcion marcada por el usuario, si la opcion se encuentra marcada, se aplica el efecto en la imagen.
    if rotar_90.get() == 1:
        inverso=[]
        largo=len(matriz[0])
        tamano1=0
        matriz.reverse()
        while tamano1<largo:
            lista1=[]
            for fila in matriz:
                lista1.append(fila[tamano1])
            inverso.append(lista1)
            tamano1+=1
        matriz = inverso
        
    if rotar_180.get() == 1:
        matriz.reverse()
        inverso=[]
        for fila in matriz:
            fila.reverse()
            inverso.append(fila)
        matriz = inverso
        
    if rotar_270.get() == 1:
        inverso=[]
        largo=len(matriz[0])
        tamano1=0
        matriz.reverse()
        while tamano1<largo:
            lista1=[]
            for fila in matriz:
                lista1.append(fila[tamano1])
            inverso.append(lista1)
            tamano1+=1
        inverso.reverse()
        inverso2=[]
        for fila in inverso:
            fila.reverse()
            inverso2.append(fila)
        matriz = inverso2
        
    if espejo_vertical.get() == 1:
        matriz.reverse()
        
    if espejo_horizontal.get() == 1:
        for fila in matriz:
            fila = fila.reverse()

    if reflexion_der.get() == 1:
        largo = int(len(matriz[0])/2)
        lista1=[]
        for columna in matriz:
            lista1.append(columna[largo:])
        listafinal=[]
        for i in lista1:
            q = list(i)
            q.reverse()
            listafinal.append(q+i)       
        matriz = listafinal

    if reflexion_izq.get() == 1:
        largo = int(len(matriz[0])/2)
        lista1=[]
        for columna in matriz:
            lista1.append(columna[:largo])
        listafinal=[]
        for i in lista1:
            q = list(i)
            q.reverse()
            listafinal.append(i+q)       
        matriz = listafinal

    if contraste.get() == 1:
        tono = 250*rango.get()/100
        listafinal=[]
        for columna in matriz:
            listabits = []
            for bits in columna:
                rojo,verde,azul = bits[0],bits[1],bits[2]
                rojo = rojo+tono
                verde = verde+tono
                azul= azul+tono
                listabits.append([rojo,verde,azul])
            listafinal.append(listabits)
        matriz = listafinal

    if desenfoque.get() == 1:
        alto = len(matriz)
        for fila in matriz:
            ancho = len(fila)
            indice1 = matriz.index(fila)
            if indice1 > radio.get() and indice1 < (alto-radio.get()):
                for i in fila:
                    indice = fila.index(i)
                    if indice > radio.get() and indice < (ancho-radio.get()):
                        contador_ancho = 0
                        contador_alto = 0
                        suma_a = 0
                        suma_b = 0
                        suma_c = 0
                        cont = 0
                        while contador_ancho < radio.get():
                            while contador_alto < radio.get():
                                cont = cont+1
                                suma_a = suma_a+matriz[indice1-contador_ancho][indice-contador_alto][0]+matriz[indice1+contador_ancho][indice+contador_alto][0]
                                suma_b = suma_b+matriz[indice1-contador_ancho][indice-contador_alto][1]+matriz[indice1+contador_ancho][indice+contador_alto][1]
                                suma_c = suma_c + matriz[indice1-contador_ancho][indice-contador_alto][2]+matriz[indice1+contador_ancho][indice+contador_alto][2]
                                contador_ancho += 1
                                contador_alto += 1
                        i[0] = suma_a/(cont*2)
                        i[1] = suma_b/(cont*2)
                        i[2] = suma_c/(cont*2)
        
    if escala_grises.get() == 1:
        for fila in matriz:
            for i in fila:
                tono_gris = (i[0]+i[1]+i[2])/3
                i[0] = tono_gris
                i[1] = tono_gris
                i[2] = tono_gris
        
    if negativo.get() == 1:
        for fila in matriz:
            for i in fila:
                i[0] = abs(i[0]-255)
                i[1] = abs(i[1]-255)
                i[2] = abs(i[2]-255)

    if rojo_sobre_grises.get() == 1:
        for fila in matriz:
            for i in fila:
                if i[0] > i[1] and i[0] > i[2]:
                    None
                else:
                    tono_gris = (i[0]+i[1]+i[2])/3
                    i[0] = tono_gris
                    i[1] = tono_gris
                    i[2] = tono_gris
                    
    if azul_sobre_grises.get() == 1:
        for fila in matriz:
            for i in fila:
                if i[2] > i[0] and i[2] > i[1]:
                    None
                else:
                    tono_gris = (i[0]+i[1]+i[2])/3
                    i[0] = tono_gris
                    i[1] = tono_gris
                    i[2] = tono_gris

    if verde_sobre_grises.get() == 1:
        for fila in matriz:
            for i in fila:
                if i[1] > i[0] and i[1] > i[2]:
                    None
                else:
                    tono_gris = (i[0]+i[1]+i[2])/3
                    i[0] = tono_gris
                    i[1] = tono_gris
                    i[2] = tono_gris

    if blanco_y_negro.get() == 1:
        for fila in matriz:
            for i in fila:
                promedio = (i[0]+i[1]+i[2])/3
                if promedio > 100:
                    i[0] = 255
                    i[1] = 255
                    i[2] = 255
                elif promedio <= 100:
                    i[0] = 1
                    i[1] = 1
                    i[2] = 1

    if filtro_color.get() == 1:
        for fila in matriz:
            for i in fila:
                promedio = (i[0]+i[1]+i[2])/3
                if opcion.get() == 1:
                    i[0] = promedio+50
                    i[1] = promedio
                    i[2] = promedio
                elif opcion.get() == 2:
                    i[0] = promedio
                    i[1] = promedio
                    i[2] = promedio+50
                elif opcion.get() == 3:
                    i[0] = promedio
                    i[1] = promedio+50
                    i[2] = promedio
                elif opcion.get() == 4:
                    i[0] = promedio+50
                    i[1] = promedio
                    i[2] = promedio+50
                elif opcion.get() == 5:
                    i[0] = promedio
                    i[1] = promedio+50
                    i[2] = promedio+50
                elif opcion.get() == 6:
                    i[0] = promedio+50
                    i[1] = promedio+50
                    i[2] = promedio

    if bandera_chile.get() == 1:
        largo = len(matriz)
        mitad_largo = largo/2
        ancho = len(matriz[0])
        mitad_ancho = ancho/2
        n = 0
        if mitad_ancho>50:
            n=50
        for fila in matriz[:mitad_largo]:
            for i in fila[:mitad_ancho-n]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio
                i[1] = promedio
                i[2] = promedio+100
            for i in fila[mitad_ancho-n:]:
                i[0] = i[0] + 100
                i[1] = i[1] + 100
                i[2] = i[2] + 100
        for fila in matriz[mitad_largo+1:]:
            for i in fila:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio+100
                i[1] = promedio
                i[2] = promedio

    if bandera_francia.get() == 1:
        largo = (len(matriz[0])/3)
        medio = largo + largo
        for fila in matriz:
            for i in fila[:largo+1]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio
                i[1] = promedio
                i[2] = promedio + 100
            for i in fila[largo+1:medio+1]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio + 100
                i[1] = promedio + 100
                i[2] = promedio + 100
            for i in fila[medio+1:]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio + 100
                i[1] = promedio
                i[2] = promedio

    if colo_colo.get() == 1:
        largo = (len(matriz[0])/2)
        medio = largo+largo
        for fila in matriz:
            for i in fila[:largo]:
                i[0] += 100
                i[1] += 100 
                i[2] += 100
            for i in fila[largo:]:
                promedio = ((i[0]+i[1]+i[2])/3) - 100
                i[0] = promedio 
                i[1] = promedio
                i[2] = promedio

    if u_dechile.get() == 1:
        largo = (len(matriz[0])/2)
        medio = largo+largo
        for fila in matriz:
            for i in fila[:largo]:
                promedio = ((i[0]+i[1]+i[2])/3) 
                i[0] = promedio 
                i[1] = promedio
                i[2] = promedio + 100
            for i in fila[largo:]:
                promedio = ((i[0]+i[1]+i[2])/3) 
                i[0] = promedio + 100
                i[1] = promedio 
                i[2] = promedio
    
    if cuatro_colores.get() == 1:
        largo = len(matriz)
        mitad_largo = largo/2
        ancho = len(matriz[0])
        mitad_ancho = ancho/2
        for fila in matriz[:mitad_largo+1]:
            for i in fila[:mitad_ancho+1]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio
                i[1] = promedio
                i[2] = promedio + 100
            for i in fila[mitad_ancho+1:]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio + 100
                i[1] = promedio
                i[2] = promedio
        for fila in matriz[mitad_largo+1:]:
            for i in fila[:mitad_ancho+1]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio
                i[1] = promedio + 100
                i[2] = promedio
            for i in fila[mitad_ancho+1:]:
                promedio = (i[0]+i[1]+i[2])/3
                i[0] = promedio + 100
                i[1] = promedio + 100
                i[2] = promedio

    if cuatro_imagenes.get():
        listafinal=[]
        for columna in matriz:
            listabits=[]
            for bits in columna:
                rojo,verde,azul=bits[0],bits[1],bits[2]
                promedio=(rojo+verde+azul)/3
                azul=promedio+100
                listabits.append([promedio,promedio,azul])
            for bits in columna:
                rojo,verde,azul=bits[0],bits[1],bits[2]
                promedio=(rojo+verde+azul)/3
                azul=promedio+150
                verde=promedio+150
                listabits.append([promedio,verde,azul])
            listafinal.append(listabits)
        for columna in matriz:
            listabits=[]
            for bits in columna:
                rojo,verde,azul=bits[0],bits[1],bits[2]
                promedio=(rojo+verde+azul)/3
                rojo=promedio+100
                listabits.append([rojo,promedio,promedio])
            for bits in columna:
                rojo,verde,azul=bits[0],bits[1],bits[2]
                promedio=(rojo+verde+azul)/3
                azul=promedio+100
                rojo=promedio+100
                listabits.append([rojo,promedio,azul])
            listafinal.append(listabits)
        matriz = listafinal
    
    if filtro_especial.get() == 1:
        for fila in matriz:
            for i in fila:
                if opcion_color.get() == 1:
                    i[0] = i[0] + opcion_intensidad.get() + opcion_intensidad.get()
                    i[1] = i[1] + opcion_intensidad.get()
                    i[2] = i[2] + opcion_intensidad.get()
                elif opcion_color.get() == 2:
                    i[0] = i[0] + opcion_intensidad.get()
                    i[1] = i[1] + opcion_intensidad.get()
                    i[2] = i[2] + opcion_intensidad.get() + opcion_intensidad.get()
                elif opcion_color.get() == 3:
                    i[0] = i[0] + opcion_intensidad.get() 
                    i[1] = i[1] + opcion_intensidad.get() + opcion_intensidad.get()
                    i[2] = i[2] + opcion_intensidad.get()
                elif opcion_color.get() == 4:
                    i[0] = i[0] + opcion_intensidad.get() + opcion_intensidad.get()
                    i[1] = i[1] + opcion_intensidad.get()
                    i[2] = i[2] + opcion_intensidad.get() + opcion_intensidad.get()
                elif opcion_color.get() == 5:
                    i[0] = i[0] + opcion_intensidad.get() 
                    i[1] = i[1] + opcion_intensidad.get() + opcion_intensidad.get()
                    i[2] = i[2] + opcion_intensidad.get() + opcion_intensidad.get()
                elif opcion_color.get() == 6:
                    i[0] = i[0] + opcion_intensidad.get() + opcion_intensidad.get()
                    i[1] = i[1] + opcion_intensidad.get() + opcion_intensidad.get()
                    i[2] = i[2] + opcion_intensidad.get()

    if cambio_color.get() == 1:
        for fila in matriz:
            for i in fila:
                rojo,verde,azul=i[0],i[1],i[2]
                if opcion_cambio.get() == 1:
                    i[0] = azul
                    i[1] = rojo
                    i[2] = verde
                elif opcion_cambio.get() == 2:
                    i[0] = verde
                    i[1] = azul
                    i[2] = verde
                elif opcion_cambio.get() == 3:
                    i[0] = rojo
                    i[1] = azul
                    i[2] = verde
                elif opcion_cambio.get() == 4:
                    i[0] = verde
                    i[1] = rojo
                    i[2] = azul
                elif opcion_cambio.get() == 5:
                    i[0] = azul
                    i[1] = verde
                    i[2] = rojo
                

    #Guardar la imagen
    arr = numpy.array(matriz)
    imagen = PIL.Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
    nombre_imagen = id_imagen.get().split('.')[0]
    imagen.save(nombre_imagen+'_modificada.png')

    #Boton para visualizar cambios
    btnAccion = Button(v,text='VISUALIZAR CAMBIOS',font=('Governor',12),background='#01a8a6',foreground='White',command=visualizar_cambios).place(x=1000,y=560)
    
    return None

def visualizar_cambios():
    
    #Cargando imagen con ayuda de la libreria PIL para soportar todos los formatos de imagen
    nombre_imagen = id_imagen.get().split('.')[0]
    photo2 = PIL.Image.open(nombre_imagen+'_modificada.png')
    photo2.thumbnail((374,374), PIL.Image.ANTIALIAS) #Modificamos tamaño
    photo2 = ImageTk.PhotoImage(photo2)
    label = Label(image=photo2)
    label.image = photo2
    label.place(x=912,y=162)

    return None

#-----------------------------------------------------------------------
#                           VENTANA PROGRAMA                           |
#-----------------------------------------------------------------------

#INICIANDO VENTANA
v = Tk()
v.geometry("1300x700")
v.title("PROCESADOR DE IMAGENES v.1.0")
Banner = PhotoImage(file='banner2.gif')
lblBanner = Label(v,image=Banner).place(x=0,y=0)

#AGREGANDO BOTONES PRINCIPALES
lbl1 = Label(text='ARCHIVO A EDITAR:',font=('Governor',8),foreground='#6d6e70').place(x=640,y=50)

#CREANDO VARIABLES QUE SE OCUPARAN DESPUES
rotar_90 = IntVar()
rotar_180 = IntVar()
rotar_270 = IntVar()
espejo_horizontal = IntVar()
espejo_vertical = IntVar()
reflexion_der = IntVar()
reflexion_izq = IntVar()
contraste = IntVar()
desenfoque = IntVar()
escala_grises = IntVar()
negativo = IntVar()
rojo_sobre_grises = IntVar()
azul_sobre_grises = IntVar()
verde_sobre_grises = IntVar()
blanco_y_negro = IntVar()
filtro_color = IntVar()
bandera_chile = IntVar()
bandera_francia = IntVar()
cuatro_colores = IntVar()
cuatro_imagenes = IntVar()
colo_colo = IntVar()
u_dechile = IntVar()
cambio_color = IntVar()
filtro_especial = IntVar()

#variables auxiliares
matriz = IntVar()
rango = IntVar()
radio = IntVar()
opcion_cambio = IntVar()
opcion = IntVar()
opcion_color = IntVar()
opcion_intensidad = IntVar()

#VARIABLE PARA INGRESAR IMAGEN
id_imagen = StringVar()
id_imagen.set('Ingrese nombre ...')
txtimagen = Entry(v,textvariable=id_imagen,background='White',font=('Verdana',8)).place(x=770,y=50)
btnAccion = Button(v,text='CARGAR',font=('Governor',8),background='#01a8a6',foreground='White',command=mostrar_imagen).place(x=920,y=50)


#EJECUTANDO VENTANA
v.mainloop()
