# EcoBoat
Bienvenidos al repositorio de EcoBoat.



## Software

En la carpeta de "Software" se encontrarán con varios archivos:

- EcoBoat1.0: Es el código principal, donde se ejecuta el funcionamiento del barco y todas las librerías utilizadas para dicho fin.
- Motores: Es la librería (desarrollada por el equipo de EcoBoat) que se utiliza para controlar los motores.
- SensoresUS: Es la librería (desarrollada por el equipo de EcoBoat) que utilizamos para realizar las mediciones con los sensores Ultrasónicos.
- RedNeuronal: Es la librería (desarrollada por el equipo de EcoBoat) que contiene el código de la Red Neuronal (No incluye la parte del entrenamiento).
- Módulo_Master: Es el programa utilizado para recibir la información y transferirla mediante sockets a la Interfaz de Usuario.
- Interfaz de Usuario: En esta carpeta se encuentran los códigos de la interfaz de usuario.
- Simulación: En esta carpeta encontrarán todo lo relacionado al entrenamiento de la Red Neuronal.
  - Aplicación Ejecutable: Aquí se encuentra la aplicación de la cual se obtienen los datos de entrenamiento para la red, es decir, la red aprende de las acciones realizadas en dicha aplicación.
  - Código fuente: Contiene el programa de la simulación y entrenamiento de la Red Neuronal.
  - trainData: En esta carpeta se guardan los archivos con la información de entrenamiento.

## Hardware

En esta carpeta se encuentran los diseños de todas las placas utilizadas:

- Circuito de Control de Marcha: Circuito utilizado para controlar los 3 motores del EcoBoat
- Fuente de 12V a 5V: regulador de tensión de 12 a 5V.
- Regulador de Carga: Es el circuito que controla la carga de la batería utilizando un panel solar.
- SensoresUS: Esta placa cumple la función de sincronizar la toma de datos de los sensores Ultrasónicos.
- Diagrama de Interconexión de circuitos: Es un diagrama que muestra como se conectan todas las placas del proyecto.

