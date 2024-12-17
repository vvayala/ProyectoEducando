## Proyecto Educando
_Samsung Innovation Campus 2024_

## 

## Tabla de contenidos
Tabla de contenidos

1. [Nombre](#Nombre)
2. [Descripción](#descripción)
3. [Arquitectura](#Arquitectura)
4. [Proceso](#Proceso)
5. [Funcionalidades](#Funcionalidades)
6. [Estado del proyecto](#EstadoDelProyecto)
7. [Agradecimientos](#Agradecimientos)



<h1 style="">ProyectoEducando</h1>

_Proyecto Samsung 2024_

## Descripción
El proyecto Educando tiene como objetivo principal evaluar las ventajas y desventajas del uso de software educativo en el desarrollo de los estudiantes.
Este software está diseñado con funcionalidades interactivas que faciliten el aprendizaje y permitan registrar el progreso de los usuarios.

## Objetivos
*	Desarrollar un software basado en Python, que permita mejorar el aprendizaje con el uso del programa.
*	El programa puede contar con una sección para permitir el registro de usuarios.
*	Puede contar con diferentes secciones: revisión de lecturas, sesión de entrenamiento, secciones de pruebas.
*	El software debe estar diseñado de tal forma que se registre el progreso de los usuarios.
*	Pruebas en grupos de control, realizar pruebas en dos grupos uno donde se muestre la forma tradicional de enseñanza es decir a través de lecturas y otro donde se muestren alternativas de enseñanza con el desarrollo de software. (registrar el tiempo de uso del programa en ambos grupos de control y luego comparar resultados, la sección de pruebas es opcional)




## Arquitectura

La arquitectura del proyecto incluye:
<ul>
  <li>
    Librerias Utilizadas
    <ul>
      <li>Pandas</li>
      <li>Seaborn</li>
      <li>Matplotlib.pyplo</li>
      <li>Customtkinter</li>
      <li>Datetime</li>
      <li>Time</li>
    </ul>
  </li>
  <li>
    Datasets utilizados
    <ul>
      <li>
        <a href="./Virtual_Reality_in_Education_Impact.csv">  Virtual_Reality_in_Education_Impact.csv</a>
      </li>
      <li>
        <a href="./education.csv">Education.csv</a>
      </li>
      <li>
        <a href="./students_adaptability_level_online_education.csv">Students_adaptability_level_online_education.csv</a>
      </li>
    </ul>
  </li>
</ul>

## Proceso
El desarrollo del proyecto se divide en las siguientes etapas:
<ul>
  <li>
    Fuente del Dataset:
    <ul>
      <li>
        Los datos utilizados provienen de estudios educativos relacionados con la adaptabilidad y el impacto de la realidad virtual en la educación
      </li>
    </ul>
  </li>
  <li>
    Limpieza de Datos:
    <ul>
      <li>
            Se utilizó la librería Pandas para procesar y limpiar los datos.
      </li>
    </ul>
  </li>
  <li>
    Manejo de Excepciones y Control de Errores:
    <ul>
      <li>
        Se implementaron técnicas en Python para garantizar la robustez del software.
      </li>
    </ul>
  </li>
</ul>

## Funcionalidades Basadas en el Análisis de Datos
<ul>
  <li>
    Evaluación de la Distribución de Edad y Adaptabilidad
    <ul>
      <li>Visualización de la distribución de edad de los estudiantes</li>
      <li>Análisis de cómo los diferentes grupos de edad afectan los niveles de adaptabilidad al aprendizaje en línea.</li>
    </ul>
  </li>


  <li>
    Relación entre Nivel Educativo y Adaptabilidad
    <ul>
      <li>Evaluación del nivel de adaptabilidad según niveles educativos (escuela, universidad, etc.)</li>
      <li>Identificación de factores educativos que afectan el rendimiento de los estudiantes</li>
    </ul>
  </li>

  <li>
    Impacto de Condiciones Externas en el Aprendizaje
    <ul>
      <li>Análisis del impacto de apagones eléctricos en la adaptabilidad al aprendizaje</li>
      <li>Estudio de cómo la condición financiera de los estudiantes influye en el acceso a diferentes tipos de internet</li>
    </ul>
  </li>

  <li>
    Análisis del Índice de Educación
    <ul>
      <li>Distribución y evolución del índice de educación (EI) a lo largo del tiempo</li>
      <li>Comparación entre población y el índice de educación, destacando relaciones significativas</li>
    </ul>
  </li>

  <li>
    Evaluación de Niveles Educativos
    <ul>
      <li>Cálculo del promedio de estudiantes en cada nivel educativo (kindergarten, escuela, universidad, etc.)</li>
      <li>Identificación de brechas entre niveles educativos mediante análisis de datos</li>
    </ul>
  </li>

  <li>
    Correlación entre Variables Educativas
    <ul>
      <li>Generación de un mapa de calor para visualizar las correlaciones entre variables numéricas clave, como población, índice de educación y niveles educativos</li>
    </ul>
  </li>
</ul>
    

## Análisis de Datos / Estadísticas

<div>
  <strong >Descripción:</strong>
  <p>
    En esta sección se analiza el nivel educativo mundial con base en índices de progreso
  </p>
</div>
<img src="./assets/graficos/indiceEducacion.png">

<div>
  <strong >Descripción:</strong>
  <p>Se muestra la distribución promedio de estudiantes según su nivel educativo</p>
</div>
<img src="./assets/graficos/promedioEducativo.png">

El análisis de adaptabilidad mide cómo los estudiantes responden a entornos virtuales de aprendizaje.


## Funcionalidad extra:

## Integración del proyecto en una aplicacion web
<p>  
Se desarrollo una interfaz amigable donde los estudiantes pueden poner en practica sus capacidades de lectura u otros objetivos
</p>

# Funcionalidades
El software incluye las siguientes secciones:

  * Registro de usuarios
  * Revisiones de lecturas
  * Sesiones de entrenamiento
  * Registro del progreso del usuario
  * Comparación de resultados
  * Registro del tiempo de uso


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

<!-- <br> -->
<p> 
Seccion de comparacion entre usuarios
</p>
<img src="./assets/comparacion.png">

<br>


## Tecnología / Herramientas usadas para el software
* Base de datos Relacional (SQL SERVER)
* Lenguaje de consultas SQL
* Lenguaje de programación Python

## Librerias
* Tkinter
* customtkinter 
* pyodbc
* json
* etc.



## Ejecutable del Software

> [!NOTE]
> crear .exe del programa

> [!IMPORTANT]
> Instalar la siguiente libreria
> pip install pyinstaller

> [!IMPORTANT]
> comando para crear el empaquetado de los archivos
> pyinstaller --onefile --windowed --add-data "cuentos;cuentos" login.py


##
## AGRADECIMIENTOS
> [!NOTE]
> Agradecemos a **Samsung Innovation Campus** y a todas las personas involucradas por su apoyo en el desarrollo del proyecto "Educando".  
> Este trabajo no habría sido posible sin el esfuerzo del equipo:  
> - Vilic Ayala Sandoval  
> - Moisés Isaac Molina Corado  
> - Carlos Fernando Pacheco Castro  
> - Tania Sofia Franco Flamenco  
> - Gabriel Armando Duran Cárcamo  
