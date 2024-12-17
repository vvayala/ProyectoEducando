## Tabla de contenidos
Tabla de contenidos

1. [Nombre](#Nombre)
2. [Descripción](#descripción)
3. [Arquitectura](#Arquitectura)
4. [Proceso](#Proceso)
5. [Funcionalidades](#Funcionalidades)
6. [Estado del proyecto](#EstadoDelProyecto)
7. [Agradecimientos](#Agradecimientos)



<h1 style="text-align:center; color:#f7a325;">ProyectoEducando</h1>

Proyecto Samsung 2024
Objetivos: Diseñar un software en Python que permita aprender de forma interactiva con el uso del programa.

*	Desarrollar un software basado en Python, que permita mejorar el aprendizaje con el uso del programa.
*	El programa puede contar con una sección para permitir el registro de usuarios.
*	Puede contar con diferentes secciones: revisión de lecturas, sesión de entrenamiento, secciones de pruebas.
*	El software debe estar diseñado de tal forma que se registre el progreso de los usuarios.
*	Pruebas en grupos de control, realizar pruebas en dos grupos uno donde se muestre la forma tradicional de enseñanza es decir a través de lecturas y otro donde se muestren alternativas de enseñanza con el desarrollo de software. (registrar el tiempo de uso del programa en ambos grupos de control y luego comparar resultados, la sección de pruebas es opcional)




## Arquitectura



* Arquitectura del proyecto + imagen

* Proceso de desarrollo:

-Fuente del dataset

-Limpieza de datos (img que lo valide)

-Manejo excepciones/control errores

-Estadísticos (Valores, gráficos, …)
<!-- > [!NOTE]
> El proyecto se fundamenta en el analisis de datos y tambien en la implementacion de un software educativo que los estudiantes pueden optar para su rendimiento -->

<div>
  <strong >Indice de educación</strong>
  <br>
</div>
<img src="./assets/graficos/indiceEducacion.png">

<div>
  <strong >Descripción:</strong>
  <p>En la siguiente grafica se puede visualizar un primedio de estudiantes por niveles educativos</p>
</div>
<img src="./assets/graficos/promedioEducativo.png">


## Funcionalidad extra:

## Integración del proyecto en una aplicacion web
<p>  
Se desarrollo una interfaz amigable donde los estudiantes pueden poner en practica sus capacidades de lectura
</p>

<p> 
Tenemos la primer ventana que consta de Validacion de usuarios
</p>
<img src="./assets/login.png">

<br>
<p> 
Ventana Principal donde se podra elegir la opcion a realizar con sus respectivas validaciones
</p>
<img src="./assets/home.png">

<br>
<p> 
Opcion de agregar nuevos usuarios
</p>
<img src="./assets/formUser.png">

<br>
<p> 
Seccion de Revisiones de lectura donde podra seleccionar la que guste leer
</p>
<img src="./assets/cuentos.png">
<p> 
Contenido de la lectura elegida
</p>
<img src="./assets/selectCuento.png">

<br>
<p> 
Seccion de Entrenamiento
</p>
<img src="./assets/entrenamiento.png">

<br>
<p> 
Seccion de progreso de usuario
</p>
<img src="./assets/progreso.png">

<br>
<p> 
Seccion de comparacion entre usuarios
</p>
<img src="./assets/comparacion.png">

<br>





## Tecnología /Herramientas usadas para el software
* Base de datos Relacion (SQL SERVER)
* Lenguaje de consultas SQL


## EJECUTABLE DEL SOFTWARE

> [!NOTE]
> crear .exe del programa

> [!IMPORTANT]
> Instalar la siguiente libreria
> pip install pyinstaller

> [!IMPORTANT]
> comando para crear el empaquetado de los archivos
> pyinstaller --onefile --windowed --add-data "cuentos;cuentos" login.py
