# Investigación sobre sensores y actuadores
## Conceptos básicos
### ¿Qué es un sensor?

Un censor es un dispositivo que detecta o mide una característica del entorno, como temperatura, luz, distancia, presión, humedad, posición o movimiento, y convierte esa información en una señal que puede interpretar un sistema de control, esa señal se puede interpretar como 00 y 1 o como 0v y 5v

### ¿Qué es un actuador?

Un actuador es un dispositivo que recibe una señal de control y la convierte en una acción física Puede producir movimiento, fuerza, desplazamiento, giro,

un actuador permite que una máquina haga algo.

### Diferencia entre sensor y actuador

La principal diferencia

- El sensor detecta o mide una variable
- El actuador realiza una acción física

Por ejemplo, en una puerta automática, un sensor puede detectar que una persona se encuentra frente a la puerta y un motor puede abrirla

### Función dentro de un sistema mecatrónico

Los sensores propocionan información al sistema de control, mientras que los actuadores hacen las acciones que el sistema dice . Por eso ambos son elementos importantes de un sistema mecatrónico. En sistemas de automatización se utilizan sensores, actuadores y sistemas de control para coordinar el funcionamiento de máquinas y procesos

Ejemplo: puerta automática

Sensor: sensor fotoeléctrico o de proximidad

 ¿Qué detecta? 

Detecta que una persona u objeto se encuentra frente a la puerta.

Actuador: motor eléctrico

 ¿Qué acción realiza? 
 
 Hace girar el mecanismo que abre la puerta

Funcionamiento general:

Persona → Sensor → Controlador → Motor → Puerta abierta

- Los sensores fotoeléctricos pueden detectar objetos mediante la interrupción o reflexión de luz y convertir ese cambio en una señal eléctrica.

 ## Investigación de sensores
 | Tipo de sensor             | Variable que mide                     | Principio de funcionamiento                                                                                  | Ejemplo                  | Aplicación                               |
| -------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------ | ---------------------------------------- |
| **Temperatura**            | Temperatura                           | Cambia una propiedad eléctrica, como la resistencia o el voltaje, de acuerdo con la temperatura              | LM35                     | Control de temperatura en equipos        |
| **Luz**                    | Intensidad luminosa                   | Un material fotosensible cambia sus propiedades eléctricas cuando recibe luz                                 | Fotoresistencia (LDR)    | Encendido automático de lámparas         |
| **Proximidad**             | Presencia o cercanía de un objeto     | Detecta cambios en un campo electromagnético, capacitancia, magnetismo o mediante otros métodos sin contacto | OMRON E2E                | Detección de piezas metálicas            |
| **Distancia**              | Distancia entre el sensor y un objeto | Emite una señal, como ultrasonido, y mide el tiempo o cambio de la señal recibida                            | HC-SR04                  | Robot móvil                              |
| **Presión**                | Presión de un gas o líquido           | La presión provoca una deformación o cambio eléctrico que puede medirse                                      | Sensor de presión BMP280 | Sistemas neumáticos y medición ambiental |
| **Humedad**                | Humedad relativa                      | Detecta cambios en las propiedades eléctricas de un material debido a la cantidad de vapor de agua           | DHT22                    | Estaciones meteorológicas                |
| **Posición**               | Posición o desplazamiento             | Detecta la posición mediante resistencia, magnetismo, luz u otro método                                      | Potenciómetro            | Control de posición                      |
| **Velocidad o movimiento** | Velocidad, giro o aceleración         | Detecta cambios de posición a través del tiempo o aceleración                                                | Encoder rotatorio        | Control de motores                       |
| **Fuerza o peso**          | Fuerza o peso                         | Una deformación mecánica produce un cambio en una señal eléctrica                                            | Celda de carga           | Básculas electrónicas                    |

 ## Clasificación de sensores
 ### Sensores analógicos y digitales
#### Sensores analógicos

Un sensor es analógico cuando su salida puede variar continuamente dentro de un rango.
Por ejemplo podría entregar:

0v, 1v, 2v, 3v, 4v, 5v

La característica que permite clasificarlo como analógico es que la señal puede tomar muchos valores diferentes y continuos.


#### Sensores digitales

Un sensor es digital cuando entrega información mediante datos digitales.

Por ejemplo:

0 = no detecta

1 = detecta

La característica principal es que su información se representa mediante estados definidos o datos digitales.

### Sensores de contacto y sin contacto
#### Sensores de contacto

Necesitan tocar físicamente el objeto para detectar algo.

Ejemplo: interruptor de límite.

La característica que los coloca en esta categoría es que existe contacto físico entre el sensor y el objeto.

#### Sensores sin contacto

Detectan un objeto sin tocarlo.

Ejemplo: sensor inductivo de proximidad.

La característica principal es que utilizan como un campo electromagnético, luz, ultrasonido o capacitancia, para detectar el objeto a distancia. OMRON señala que los sensores de proximidad realizan detección sin contacto y convierten la presencia o movimiento del objeto en una señal eléctrica.

### Sensores activos y pasivos
#### Sensores activos

Un sensor activo necesita alimentación externa para funcionar y realizar su proceso de medición o detección.

Por ejemplo, un sensor ultrasónico necesita energía para emitir una señal y después recibir el eco.

#### Sensores pasivos

Un sensor pasivo obtiene la información a partir de una propiedad física del fenómeno que está midiendo y no necesita generar una señal de excitación para realizar la detección.

Ejemplo: una termopar puede generar una pequeña tensión debido a la diferencia de temperatura.

La característica que permite clasificarlos es principalmente si necesitan generar o aplicar energía externa para realizar la medición.

### Investigacion de actuadores
| Actuador                | Energía utilizada | Movimiento           | Ventaja                                   | Limitación                                               | Aplicación            |
| ----------------------- | ----------------- | -------------------- | ----------------------------------------- | -------------------------------------------------------- | --------------------- |
| **Motor DC**            | Eléctrica         | Rotatorio            | Sencillo y económico                      | El control de posición requiere elementos adicionales    | Ruedas de robots      |
| **Servomotor**          | Eléctrica         | Rotatorio controlado | Permite controlar posición con precisión  | Tiene mayor dificultad y costo que un motor DC sencillo | Brazo robótico        |
| **Motor paso a paso**   | Eléctrica         | Rotatorio por pasos  | Permite controlar el movimiento por pasos | Puede perder pasos bajo ciertas condiciones              | Impresoras 3D         |
| **Solenoide**           | Eléctrica         | Lineal               | Diseño sencillo y respuesta rápida        | Recorrido normalmente corto                              | Cerraduras y válvulas |
| **Cilindro neumático**  | Aire comprimido   | Lineal               | Rápido y adecuado para automatización     | Necesita sistema de aire comprimido                      | Líneas de producción  |
| **Cilindro hidráulico** | Fluido hidráulico | Lineal               | Produce grandes fuerzas                   | Sistema más pesado y requiere mantenimiento              | Maquinaria pesada     |

### Comparación de actuadores
#### Motor DC vs. servomotor

Un motor DC sencillo gira mientras recibe energía, pero normalmente no sabe por sí mismo en qué posición se encuentra.

Un servomotor utiliza control y retroalimentación para mantener o alcanzar una posición determinada.

Elegiría un motor DC: para mover las ruedas de un robot móvil, donde principalmente necesito que las ruedas giren.

Elegiría un servomotor: para mover una articulación robótica donde necesito que el eje llegue a un ángulo específico.

#### Servomotor vs. motor paso a paso

El servomotor utiliza retroalimentación para controlar la posición y puede corregir errores.

El motor paso a paso mueve el eje mediante pasos determinados.

Elegiría un servomotor: para una articulación que necesita mantener una posición con precisión.

Elegiría un motor paso a paso: para una impresora 3D o máquina CNC donde se necesita realizar desplazamientos controlados por pasos.

#### Actuador neumático vs. actuador hidráulico

Ambos utilizan fluidos para generar movimiento lineal, pero el neumático utiliza normalmente aire comprimido y el hidráulico utiliza un fluido a presión.

Elegiría un actuador neumático: para empujar rápidamente piezas ligeras en una línea de producción.

Elegiría un actuador hidráulico: para levantar o mover cargas muy pesadas porque puede producir grandes fuerzas.

## Sensores y actuadores en un sistema real
### Sistema : robot móvil

Un robot móvil necesita sensores para su entorno y actuadores para desplazars

### Sensores
Sensor ultrasónico de distancia: detecta qué tan cerca está un obstáculo
Encoder: permite conocer el movimiento o giro de las ruedas
Sensor de luz: podría utilizarse para detectar cambios de iluminación si el robot necesita orientarse o realizar alguna tarea relacionada con la luz.
### Actuadores
Motores DC: hacen girar las ruedas.
Servomotor: podría utilizarse para mover una cámara o sensor en diferentes direcciones.

| Elemento           | Función                                     |
| ------------------ | ------------------------------------------- |
| Sensor ultrasónico | Detectar obstáculos                         |
| Encoder            | Medir el giro de las ruedas                 |
| Sensor de luz      | Detectar intensidad luminosa                |
| Motor DC           | Mover las ruedas                            |
| Servomotor         | Orientar una cámara o sensor                |
| Controlador        | Procesar la información y decidir qué hacer |

             ROBOT MÓVIL

       ┌──────────────────────┐
       │       SENSORES       │
       │                      │
       │  Distancia ─────┐    │
       │  Encoder ───────┤    │
       │  Luz ───────────┤    │
       └─────────────────┼────┘
                         ↓
                ┌────────────────┐
                │  CONTROLADOR   │
                │   (Arduino/    │
                │      PLC)      │
                └───────┬────────┘
                        │
                        ↓
              ┌──────────────────┐
              │    ACTUADORES    │
              │                  │
              │   Motores DC     │
              │   Servomotor     │
              └────────┬─────────┘
                       ↓
                 MOVIMIENTO
                  DEL ROBOT
                       │
                       ↓
                NUEVA SITUACIÓN
                       │
                       └────→ Sensores

## Selección de componentes                       

| Situación                                                              | Sensor o actuador seleccionado              | Razón                                                                                      |
| ---------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Detectar si una persona se encuentra frente a una puerta automática    | **Sensor fotoeléctrico**                    | Puede detectar una persona sin necesidad de contacto físico mediante luz                   |
| Medir la temperatura dentro de un salón                                | **Sensor de temperatura** | Está diseñado para medir temperatura y puede proporcionar una señal eléctrica proporcional |
| Detectar el nivel de agua de un depósito                               | **Sensor de nivel**                         | Está diseñado específicamente para detectar cuándo el agua alcanza determinada altura      |
| Mover una rueda de un robot móvil                                      | **Motor DC**                                | Produce movimiento rotatorio y es adecuado para mover ruedas                               |
| Controlar con precisión el ángulo de una pequeña articulación robótica | **Servomotor**                              | Permite controlar la posición angular del eje                                              |
| Empujar una pieza en una línea de producción                           | **Cilindro neumático**                      | Produce movimiento lineal y puede empujar rápidamente una pieza                            |
| Medir la distancia entre un robot y una pared                          | **Sensor ultrasónico**                      | Puede medir la distancia entre el robot y un obstáculo sin contacto                        |
| Detectar si una habitación está iluminada                              | **Fotoresistencia LDR**                     | Su resistencia cambia dependiendo de la cantidad de luz que recibe                         |


## conclusion

la diferencia de un dato de variable y una accion fisica es que el dato es como temperatura o nivel o luminosidad , ese es un dato simplemente y una accion fisica ya es actual, se necesitan entre los dos para ya poder hacer un sistema, claro tomando en cuenta un controlador que codifique las variables, un sistema mecatronico actua de esa manera, actua de acuerdo a señales
mi actuador favorito creo que son los cilindros o pistones,se me hizo interesante la manera en que actuan y que pueden actuar con mayor fuerza y que tienen diferente longitudes

## Referencias

* OMRON Industrial Automation. (s. f.). *Overview of Proximity Sensors*. OMRON. [https://www.ia.omron.com/support/guide/41/overview.html](https://www.ia.omron.com/support/guide/41/overview.html?url=sourcetech411&utm_source=chatgpt.com)

* OMRON Industrial Automation. (s. f.). *Overview of Photoelectric Sensors*. OMRON. [https://www.ia.omron.com/support/guide/43/introduction.html](https://www.ia.omron.com/support/guide/43/introduction.html?utm_source=chatgpt.com)

* Arduino. (2024). *Analog Input*. Arduino Documentation. [https://docs.arduino.cc/built-in-examples/analog/AnalogInput/](https://docs.arduino.cc/built-in-examples/analog/AnalogInput/?utm_source=chatgpt.com)

* Arduino. (s. f.). *Analog Input Pins*. Arduino Documentation. [https://github.com/arduino/docs-content/blob/main/content/learn/02.microcontrollers/02.analog-input/analog-input.md](https://github.com/arduino/docs-content/blob/main/content/learn/02.microcontrollers/02.analog-input/analog-input.md?utm_source=chatgpt.com)

* Texas Instruments. (s. f.). *Temperature Sensors*. TI. [https://www.ti.com/product-category/sensors/temperature/overview.html](https://www.ti.com/product-category/sensors/temperature/overview.html?utm_source=chatgpt.com)

* Texas Instruments. (s. f.). *Sensors*. TI. [https://www.ti.com/product-category/sensors/overview.html](https://www.ti.com/product-category/sensors/overview.html?utm_source=chatgpt.com)

* Parker Hannifin Corporation. (s. f.). *Safety Guide for Selecting and Using Hydraulic, Pneumatic Cylinders and Their Accessories*. Parker. [https://www.parker.com/content/dam/Parker-com/Literature/Literature-Files/pneumatic/Literature/Actuator-Cylinder/MSG_PDN_0981P-P8S-Sensor-FINAL.pdf](https://www.parker.com/content/dam/Parker-com/Literature/Literature-Files/pneumatic/Literature/Actuator-Cylinder/MSG_PDN_0981P-P8S-Sensor-FINAL.pdf?utm_source=chatgpt.com)

* Parker Hannifin Corporation. (s. f.). *Pneumatic Division 3D CAD Library*. Parker. [https://discover.parker.com/PDNCadLibrary](https://discover.parker.com/PDNCadLibrary?utm_source=chatgpt.com)
