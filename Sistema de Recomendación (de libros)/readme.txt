----------------------------------------------------------------------------
|                    PROBLEMA 2:  SISTEMA DE RECOMENDACION                 |
----------------------------------------------------------------------------

1. INTEGRANTES
      (Nombre)	            (Rol)
- Renato Olavarr�a	| 201573088-1
- Camila Mu�oz		| 201573085-7
- Gabriela Sep�lveda 	| 201573012-1

2. LIBRERIAS NECESARIAS
- Tkinter

3. COMENTARIOS ADICIONALES
- No olvide incluir el DATASET en la misma carpeta en que ejecutar� el c�digo
- Se incluyen los archivos de vecinos de los usuarios 1, 79441, 113345 y 151546

- Respecto al funcionamiento del programa:
* Cuando se ingresan usuarios con muy pocas valoraciones se pasa autom�ticamente a un
m�todo que no calcula los libros con los vecinos-correlacion pearson; si no que busca
un listado de listo de acuerdo a la edad y ubicacion del usuario. (Actualmente este
umbral es de 5 libros, en la linea 41 y 43 puede modificar este valor, pero cn ese valor
se obtuvieron resultados positivos).
* Respecto al punto anterior se debe destacar que cuando son usuarios de ubicaciones 
menos comunes, es dificil hallar libros que hayan sido valorados m�s de unas 15 veces
(Q fue el umbral que se propuso para considerar al libro, y evitar aquellos q tienen altas
valoraciones m�s solo han sido evaluados una vez); por lo que se recomienda modificar este
umbral(disminuirlo) para obtener mejores resultados cuando son pa�ses con pocos usuarios.
* Por un tema de tiempo el programa con interfaz gr�fica no hace el an�lisis de vecinos, si
no que trabaja sobre los archivos que creaba la primera versi�n (Sin interfaz gr�fica). De-
bido a la complejidad del problema y el poco tiempo disponible se decidi� hacer esto. Por
tanto se incluye en una carpeta aparte el programa inicial para calcular los vecinos.
(Recuerde incluir el dataset tambien en la carpeta de este programa auxiliar)