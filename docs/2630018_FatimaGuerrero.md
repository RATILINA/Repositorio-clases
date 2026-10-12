# Investigación sobre Tipos de Robots Móviles

## Conceptos básicos
### ¿Qué es un robot móvil?

Un robot móvil es una máquina capaz de moverse de un lugar a otro, para moverse utiliza sistema como ruedas, orugas o patas, En el caso de los robots móviles con ruedas, el movimiento depende de la forma en que están colocadas y controladas las ruedas

### ¿Qué diferencia existe entre un robot móvil y un robot manipulador fijo?

Un robot móvil puede cambiar de posición dentro de un lugar , mientras que un robot fijo se mantiene sujeto a una base y utiliza principalmente sus articulaciones para mover una herramienta u objeto

Por ejemplo, un robot móvil puede recorrer un almacén, mientras que un brazo robótico fijo puede permanecer instalado para manipular piezas.

### ¿Qué función cumple el sistema de locomoción?

El sistema de movimiento permite que el robot se desplace, Está formado por elementos como ruedas, motores, mecanismos de dirección y controladores. Su diseño determina si el robot puede avanzar, retroceder, girar o moverse a los lados

### ¿Qué significa que un robot tenga movilidad omnidireccional?

Significa que el robot puede desplazarse en cualquier dirección sobre una superficie plana y, además, puede cambiar su orientación sin importar de la dirección en la que se está desplazando.

Por ejemplo, puede moverse hacia la izquierda sin tener que girar primero.

### ¿Qué relación existe entre la disposición de las ruedas y los movimientos que puede realizar el robot?

La posición, orientación y tipo de ruedas determinan las restricciones de movimiento del robot. Una configuración diferencial permite avanzar, retroceder y girar, pero no desplazarse directamente de lado. En cambio, las ruedas omni y Mecanum permiten generar movimiento lateral debido a sus rodillos.

### ¿Dónde se utilizan los robots móviles?

- lmacenes y centros de distribución
- Fábricas
- Hospitales
- Laboratorios
- Agricultura
- Exploración
- Transporte de materiales
- nvestigación y educación
- Vehículos autónomos

## Robot diferencial con rueda de castor
La configuración diferencial con rueda de castor utiliza normalmente dos ruedas motrices independientes y una o más ruedas de apoyo que no proporcionan tracción.

Las dos ruedas principales tienen motores cada una, por lo que cada una puede girar a una velocidad diferente. Esta configuración es una de las más sencillas y utilizadas en robótica móvil.

### ¿Cómo están colocadas las ruedas motrices?

Las dos ruedas motrices se encuentran aproximadamente sobre el mismo eje, una a la izquierda y otra a la derecha del robot.

### ¿Para qué sirve la rueda de castor?

La rueda de castor, también llamada rueda loca, sirve principalmente para sostener parte del peso del robot y mantenerlo estable. Normalmente puede girar libremente y no tiene un motor propio.

### ¿Cómo avanza en línea recta?

Las dos ruedas motrices giran hacia adelante aproximadamente a la misma velocidad.

Como ambas producen velocidades similares, el robot avanza aproximadamente en línea recta.

### ¿Cómo gira a la izquierda o derecha?

Si una rueda gira más rápido que la otra, el robot describe una curva.

Rueda izquierda más lenta + derecha más rápida - gira a la izquierda.
        Rueda derecha más lenta + izquierda más rápidagira a la derecha.
### ¿Qué sucede cuando una rueda gira más rápido que la otra?

El robot deja de avanzar en línea recta y comienza a describir una trayectoria curva. La diferencia entre las velocidades determina qué tan cerrada es la curva.

### ¿Cómo gira sobre su propio eje?

Las dos ruedas giran en sentidos opuestos y con velocidades similares:

Izquierda ←
Derecha →

Una rueda empuja el robot hacia un lado y la otra hacia el contrario, haciendo que el centro del robot permanezca aproximadamente en el mismo lugar mientras gira.

### Ventajas
1. Diseño sencillo
2. Solo necesita dos motores para las ruedas principales.
3. Control relativamente fácil.
4. Bajo costo.
5. Es apropiado para aprender control de robots móviles.
6. Puede girar sobre su propio eje.
### Limitaciones
1. No puede desplazarse directamente hacia los lados.
2. Las ruedas deben mantener contacto adecuado con el suelo.
3. Las diferencias entre los motores y el deslizamiento pueden producir errores de odometría.
4. No es tan apropiado como un sistema omnidireccional para espacios donde se requiere movimiento lateral.
### Aplicaciones

- Robots educativos.
- Robots de investigación.
- Robots de servicio.

![Robot diferencial con rueda de castor](https://researchgate.net)

                 SENTIDO DE AVANCE
                         ↑
                         │
                ┌─────────────────┐
                │                 │
                │     ROBOT       │
                │                 │
                └─────────────────┘
                   O           O
              Rueda izq.   Rueda der.
                   │           │
                   └─────┬─────┘
                         │
                    ● Rueda
                    de castor

             ↻ Eje de giro aproximado
              (entre las ruedas motrices)
 
| RUEDA DERECHA| RUEDA IZQUIERDA |MOVIMIENTO|
|-|-|-|
|AVANZA|AVANZA|AVANZA EN LINEA RECTA|
|AVANZA|DETENIDA|GIRA A LA IZQUIERDA|
|DETENIDA|AVANZA|GIRA A LA DERECHA|
|RETROCEDE|AVANZA|GIRA EN SU PPROPIO EJE|
|AVANZA|RETROCEDE|SENTIDO CONTRARIO SORE SU MISMO EJE|
|RETROCEDE|RETROCEDE|AVANZA EN LINEA RECTA|

## Robots omnidireccionales con ruedas Omni
Una rueda Omni es una rueda especial que tiene pequeños rodillos alrededor de su periferia.

Estos rodillos pueden girar libremente en una dirección diferente a la dirección principal de giro de la rueda.

### ¿Cómo está construida?

Una rueda Omni está formada principalmente por:

Un cuerpo o núcleo circular.
Un eje central.
Pequeños rodillos distribuidos alrededor del perímetro.
Elementos que permiten que los rodillos giren libremente.
¿Para qué sirven los pequeños rodillos?

Permiten que la rueda ruede normalmente en una dirección, pero que pueda deslizarse con mucha menor resistencia en otra dirección.

Esto elimina una de las restricciones de una rueda convencional.

Una rueda convencional no puede desplazarse lateralmente sin arrastrarse. En una rueda Omni, los rodillos permiten ese movimiento lateral.

### ¿En qué dirección puede generar fuerza?

La rueda genera principalmente fuerza en la dirección de avance de su rueda.

### ¿Por qué puede deslizarse libremente en otra dirección?

Porque los pequeños rodillos giran libremente. En vez de obligar a toda la rueda a deslizarse sobre el suelo, los rodillos giran y permiten el desplazamiento lateral.

### ¿Cómo permite esto movimientos especiales?

Al colocar varias ruedas Omni con diferentes orientaciones, las fuerzas producidas por cada rueda pueden combinarse.

Así, el robot puede generar:

- Movimiento hacia adelante.
- Movimiento hacia atrás.
- Movimiento lateral.
- Movimiento diagonal.
- Rotación.
- Configuración de tres ruedas Omni

Una configuración común utiliza tres ruedas Omni distribuidas alrededor del robot aproximadamente cada 120°. Esta distribución permite controlar las tres variables principales de movimiento en el plano: desplazamiento en X, desplazamiento en Y y rotación.

### Distribución

![Robot omnidireccional con 3 ruedas Omni](https://udemycdn.com)

                         ↑
                         │
                    ┌───────┐
                    │ Rueda │
                    │   1   │
                    └───┬───┘
                        │
                        │
                  ┌───────────┐
                 /             \
                /     ROBOT     \
               /       ●         \
              /                   \
             O                     O
          Rueda 2              Rueda 3
             ↖                     ↗
Las tres ruedas están separadas aproximadamente 120° entre sí.

### Movimiento hacia adelante y atrás

Las velocidades de las tres ruedas se coordinan para producir una componente de movimiento hacia adelante.

### Movimiento lateral

Al cambiar las velocidades de las tres ruedas, las fuerzas resultantes se combinan para producir una componente lateral.

### Movimiento diagonal

Se pueden combinar simultáneamente las componentes longitudinal y lateral.

### Giro sobre su propio eje

Las tres ruedas pueden girar de manera coordinada para producir un momento alrededor del centro del robot.

### ¿Qué ocurre si las tres ruedas giran a diferentes velocidades?

La combinación de sus velocidades determina el movimiento final. El robot puede desplazarse y girar al mismo tiempo.

La relación entre las velocidades de las ruedas y el movimiento del robot se estudia mediante la cinemática 

## Configuración de cuatro ruedas Omni
En una configuración de cuatro ruedas Omni se colocan normalmente las ruedas cerca de las cuatro esquinas del chasis.

       FRENTE
    O──────────O
    │          │
    │  ROBOT   │
    │          │
    O──────────O
        FRENTE
  
Cada rueda aporta una componente de fuerza. El controlador combina las velocidades de las cuatro ruedas para conseguir el movimiento deseado.

### Diferencias respecto a tres ruedas

### Tres ruedas:

- Menor número de motores.
- Estructura compacta.
- Las ruedas están aproximadamente a 120°.
- Puede generar movimiento omnidireccional.

### Cuatro ruedas:

- Distribución más parecida a una plataforma rectangular.
- Puede proporcionar mayor estabilidad y capacidad de carga.
- Requiere controlar cuatro ruedas.
- El control cinemático es más complejo.  

## Robot omnidireccional con ruedas Mecanum
Las ruedas Mecanum son ruedas especiales que tienen varios rodillos alrededor de su perímetro. Los rodillos están montados aproximadamente a 45° respecto al plano de la rueda, dependiendo del diseño.

### ¿Cómo están construidas?

Una rueda Mecanum contiene:

- Un cuerpo circular.
- Un eje central.
- Varios rodillos.
- Rodillos inclinados.
- Estructura que permite que los rodillos giren libremente.
### ¿Qué diferencia existe entre Mecanum y Omni?

La diferencia principal está en la orientación de los rodillos.

En una Omni convencional, los rodillos permiten principalmente el deslizamiento lateral respecto a la rueda.

En una Mecanum, los rodillos están inclinados aproximadamente 45°, por lo que la fuerza generada por cada rueda tiene componentes en diferentes direcciones. Al combinar las cuatro ruedas se obtiene movimiento omnidireccional.

### ¿Por qué generalmente se utilizan cuatro?

Porque cuatro ruedas permiten colocar las ruedas en las cuatro esquinas de una plataforma rectangular y combinar sus velocidades para producir desplazamiento longitudinal, lateral y rotación.

### Orientación
             FRENTE
        ↗              ↖
       [FI]            [FD]

       [TI]            [TD]
        ↖              ↗
             ATRÁS

| Movimiento      | Delantera izquierda | Delantera derecha | Trasera izquierda | Trasera derecha |
| --------------- | ------------------- | ----------------- | ----------------- | --------------- |
| Avanzar         | ↑                   | ↑                 | ↑                 | ↑               |
| Retroceder      | ↓                   | ↓                 | ↓                 | ↓               |
| Izquierda       | ↓                   | ↑                 | ↑                 | ↓               |
| Derecha         | ↑                   | ↓                 | ↓                 | ↑               |
| Girar izquierda | ↓                   | ↑                 | ↓                 | ↑               |
| Girar derecha   | ↑                   | ↓                 | ↑                 | ↓               |

## Robot con dirección Ackermann

La geometría Ackermann es una configuración de dirección utilizada en automóviles y en algunos robots móviles tipo vehículo

### ¿Qué ruedas proporcionan la dirección?

Normalmente las ruedas delanteras.

### ¿Qué ruedas pueden proporcionar tracción?

Dependiendo del diseño, pueden proporcionar tracción:

Las ruedas traseras.
Las delanteras.
Las cuatro ruedas.
### ¿Por qué las ruedas interiores y exteriores no giran con el mismo ángulo?

Durante una curva, cada rueda sigue una trayectoria circular diferente.

- La rueda interior recorre una circunferencia de menor radio, mientras que la exterior recorre una circunferencia de mayor radio.

Por eso:

Ángulo de rueda interior > ángulo de rueda exterior.

Esta geometría permite reducir el deslizamiento de las ruedas durante una curva.

### ¿Qué es el radio de giro?

Es la distancia aproximada entre el centro instantáneo de giro y el vehículo o una referencia determinada del vehículo.

Cuanto menor sea el radio de giro, más cerrada será la curva.

### ¿Por qué no puede desplazarse directamente hacia un costado?

Porque sus ruedas convencionales están diseñadas para rodar principalmente en la dirección hacia la que apuntan. No tienen los rodillos laterales de una rueda Omni o Mecanum.

Por lo tanto, el robot necesita orientar las ruedas y avanzar o retroceder para cambiar su posición.

Semejanza con un carro 
### La principal semejanza es que ambos:

- Utilizan dirección de las ruedas delanteras.
- Siguen trayectorias curvas.
- Tienen un radio de giro.
- No pueden moverse lateralmente directamente.
- Necesitan avanzar o retroceder para cambiar de posición.
### Ejemplos

Se utiliza en:

Robots tipo automóvil.
Vehículos autónomos.
Robots para investigación de conducción autónoma.
Vehículos de competencia.
Plataformas educativas de conducción autónoma.

| Configuración        | Número típico de ruedas | Movimiento lateral | Giro sobre su eje | Complejidad mecánica | Complejidad de control | Aplicaciones                          |
| -------------------- | ----------------------: | ------------------ | ----------------- | -------------------- | ---------------------- | ------------------------------------- |
| Diferencial + castor |                       3 | No                 | Sí                | Baja                 | Baja                   | Educación, almacenes, investigación   |
| Omni de 3 ruedas     |                       3 | Sí                 | Sí                | Media                | Media                  | Plataformas omnidireccionales         |
| Omni de 4 ruedas     |                       4 | Sí                 | Sí                | Media                | Media-alta             | Plataformas móviles                   |
| Mecanum              |                       4 | Sí                 | Sí                | Media-alta           | Alta                   | Almacenes, competencia, investigación |
| Ackermann            |                       4 | No                 | No                | Media                | Media                  | Vehículos autónomos                   |

## ¿Cuál elegiría en cada caso?
Robot pequeño para aprender programación y control

### Diferencial + castor.

Es sencillo porque solamente se necesitan controlar dos ruedas motrices independientes.

Robot para un almacén con espacios reducidos

### Mecanum.

Puede desplazarse lateralmente y cambiar rápidamente de dirección sin tener que realizar grandes maniobras.

### Omnidireccional o Mecanum.

Plataforma que necesita moverse lateralmente sin cambiar su orientación

Ambas permiten generar movimiento lateral.

### Ackermann
 Vehículo autónomo similar a un automóvil



Su comportamiento se parece al de un carro

Robot para una competencia donde sea necesario cambiar rápidamente de dirección

### Mecanum

Su capacidad de desplazamiento lateral y diagonal puede ser muy útil cuando se necesita maniobrar rápidamente


### Diferencial + castor

Robot móvil sencillo que utilice únicamente dos motores

Es la opción más adecuada porque utiliza dos motores independientes para las ruedas motrices

## Análisis del movimiento
Diferencial
### ¿Qué debe hacer cada rueda para que el robot gire sobre su propio eje?

Las dos ruedas deben girar en sentidos opuestos y con velocidades aproximadamente iguales.

### Por ejemplo:

Izquierda:  ←
Derecha:    →

La rueda izquierda intenta desplazar el robot hacia un lado y la derecha hacia el contrario. Como ambas velocidades tienen magnitudes similares, las componentes lineales se cancelan y queda principalmente un movimiento de rotación.

### Omni
¿Por qué los rodillos permiten generar movimiento lateral?

Porque los rodillos pueden girar libremente en una dirección perpendicular a la dirección principal de rodadura de la rueda.

Esto disminuye la resistencia al desplazamiento lateral. Al combinar varias ruedas orientadas de diferentes maneras, sus fuerzas se suman y producen una velocidad lateral del chasis.

### Mecanum
¿Por qué puede desplazarse lateralmente aunque ninguna rueda esté orientada directamente hacia el costado?

Porque los rodillos de las ruedas están inclinados.

Cada rueda genera una fuerza cuya dirección puede descomponerse en diferentes componentes. Al hacer que las cuatro ruedas giren a velocidades y sentidos determinados, algunas componentes se cancelan y otras se suman.

La suma de esas componentes produce una fuerza lateral sobre el robot.

### Ackermann
¿Por qué necesita avanzar o retroceder para cambiar de posición lateral?

Porque sus ruedas convencionales no pueden rodar libremente hacia los lados.

es como un carro, su traccion le permite moverse a los lados, pero al igual que los carros tiene
que retrocerder  o avanzar para hacerlo

## Aplicación en un robot real
TurtleBot3 Burger

Un ejemplo real es el TurtleBot3 Burger, desarrollado por ROBOTIS como plataforma educativa y de investigación para ROS.

Nombre

- TurtleBot3 Burger

- Fabricante
 ROBOTIS

- Tipo de locomoción
 Diferencial de dos ruedas motrices.

ROBOTIS especifica que TurtleBot3 utiliza una plataforma de dos ruedas con accionamiento diferencial.

Número y tipo de ruedas
- 2 ruedas motrices.
- 1 rueda de castor.
- Actuadores

Utiliza dos actuadores DYNAMIXEL XL430-W250, uno para cada rueda. Estos actuadores cuentan con control de velocidad y un encoder para conocer la posición del eje.

El TurtleBot3 Burger utiliza:

- Sensor láser de distancia de 360°.
IMU.
Encoders de los actuadores.

- El sensor láser permite obtener información del entorno para tareas como navegación 
Se utiliza principalmente para:

- Educación.
- Investigación.
- Navegación autónoma.

Desarrollo de aplicaciones robóticas.
### ¿Por qué es adecuada esta configuración?

La configuración diferencial es adecuada porque el TurtleBot3 está diseñado como plataforma compacta y educativa. Utilizar únicamente dos ruedas motrices permite simplificar el control del movimiento, mientras que la rueda de castor proporciona apoyo.

Además, las dos ruedas pueden controlarse independientemente, por lo que el robot puede avanzar, girar y realizar giros sobre su propio eje

## Conclusion
Durante la investigación, la configuración que me pareció más sencilla de comprender fue la diferencial con rueda de castor, principalmente porque utiliza dos ruedas motrices que pueden controlarse de manera independiente. Al aumentar, disminuir o invertir la velocidad de cada rueda se puede entender fácilmente cómo cambia el movimiento del robot, y es la configuracion para mi mas facil de hacer

La configuración que ofrece mayor libertad de movimiento es la omnidireccional, Estas configuraciones permiten moverse en mas direciones y sentidos, además de poder girar sobre su propio eje.

También comprendí que no existe una sola configuración de ruedas adecuada para todos los robots porque cada aplicación tiene necesidades diferentes. Un robot para aprender programación puede necesitar un sistema sencillo, mientras que un robot de almacén puede necesitar moverse lateralmente en espacios reducidos. Por otro lado, un vehículo autónomo que se comporte como un automóvil necesita una configuración Ackermann. Por eso la elección de la locomoción depende del espacio de trabajo, el tipo de movimiento requerido, la carga, la estabilidad, el costo y la complejidad del control.

## Referencias


1. **Lynch, Kevin M. & Park, Frank C.** (2017). *Modern Robotics: Mechanics, Planning, and Control*. Cambridge University Press. Capítulo 13: *Wheeled Mobile Robots*.
   https://modernrobotics.northwestern.edu/

2. **Tagliavini, Luigi; Colucci, Giovanni; Botta, Andrea; Cavallone, Paride; Baglieri, Lorenzo & Quaglia, Giuseppe.** (2022). *Wheeled Mobile Robots: State of the Art Overview and Kinematic Comparison Among Three Omnidirectional Locomotion Strategies*. Journal of Intelligent & Robotic Systems.
   https://doi.org/10.1007/s10846-022-01745-7

3. **ROS 2 Control.** (s. f.). *Wheeled Mobile Robot Kinematics*. Documentación técnica sobre la cinemática de robots móviles diferenciales, omnidireccionales y Ackermann.
   https://control.ros.org/master/doc/ros2_controllers/doc/mobile_robot_kinematics.html

4. **ROBOTIS.** (s. f.). *TurtleBot3 – Features and Specifications*. Documentación oficial de TurtleBot3.
   https://emanual.robotis.com/docs/en/platform/turtlebot3/features/

5. **ROBOTIS.** (s. f.). *TurtleBot3 DYNAMIXEL*. Documentación técnica de los actuadores utilizados en TurtleBot3.
   https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_dynamixel/

6. **ROBOTIS.** (s. f.). *LDS-02 / LDS-03 Laser Distance Sensor*. Documentación técnica de los sensores láser utilizados en TurtleBot3.
   https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_lds_02/

7. **Movement Performance Analysis of Mecanum Wheeled Omnidirectional Mobile Robot.** (2019). *IEEE International Conference on Mechatronics and Automation (ICMA)*.
   https://doi.org/10.1109/ICMA.2019.8816397


