# ProyectoEducando
Proyecto Samsung 2024
Objetivos: Diseñar un software en Python que permita aprender de forma interactiva con el uso del programa.

●	Desarrollar un software basado en Python, que permita mejorar el aprendizaje con el uso del programa.
●	El programa puede contar con una sección para permitir el registro de usuarios.
●	Puede contar con diferentes secciones: revisión de lecturas, sesión de entrenamiento, secciones de pruebas.
●	El software debe estar diseñado de tal forma que se registre el progreso de los usuarios.
●	Pruebas en grupos de control, realizar pruebas en dos grupos uno donde se muestre la forma tradicional de enseñanza es decir a través de lecturas y otro donde se muestren alternativas de enseñanza con el desarrollo de software. (registrar el tiempo de uso del programa en ambos grupos de control y luego comparar resultados, la sección de pruebas es opcional)



# crear .exe del programa

Instalar la siguiente libreria
> pip install pyinstaller

comando para crear el empaquetado de los archivos
> pyinstaller --onefile --windowed --add-data "cuentos;cuentos" login.py
