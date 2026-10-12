# Metodologías ágiles: Scrum, Kanban y Design Thinking

## Introducción y principios ágiles

Las metodologías ágiles son formas de ordenar el trabajon, que buscan que los proyectos puedan avanzar de manera ordenada y al mismo tiempo

Las metodologías ágiles no son apenas herramientas, son estrategias de marketing, gestión de servicios y más, que impulsan a las organizaciones a gestionar sus proyectos con rapidez y flexibilidad. Estas metodologías ayudan en el desarrollo de proyectos que necesitan mayor enfoque para adecuarse a las necesidades del cliente.

una metodología ágil es una muy buena forma de trabajar y organizar flujos, que divide los proyectos en partes, permite adaptarse sobre la marcha, complementa y resuelve etapas en poco tiempo

Trabajar de manera ágil no significa trabajar sin organización. Al contrario, busca organizar las actividades, dividir el trabajo, revisar los avances constantemente y permitir que el equipo pueda cambiar sus prioridades cuando sea necesario. El objetivo es conseguir resultados útiles y mantener una buena comunicación entre las personas que participan en el proyecto.

El enfoque ágil se basa en cuatro valores principales establecidos en el Manifiesto Ágil: 
1. Valoración de las personas y las relaciones sociales por encima de herramientas y procesos.
2. Colaboración directa con el cliente para mantener una relación más participativa y cercana.
3. Priorización funcional del producto por encima de la acumulación y exceso de documentación.
4. Responder de forma ágil y efectiva a los imprevistos y cambios que puedan haberse desarrollado en el plan inicial.

Estos principios permiten detectar problemas antes de que sean demasiado grandes, recibir comentarios durante el desarrollo y hacer cambios conforme se obtiene nueva información.

Existen diferentes formas de trabajar con ideas ágiles. Entre las más conocidas están Scrum, Kanban y Design Thinking. Scrum organiza el trabajo en periodos cortos llamados Sprints y es útil para proyectos que necesitan avances y revisiones frecuentes. Kanban utiliza un tablero para visualizar las tareas y controlar la cantidad de trabajo que se realiza al mismo tiempo, por lo que puede ser conveniente cuando las tareas llegan continuamente o las prioridades cambian. Design Thinking se concentra principalmente en comprender a las personas y sus necesidades antes de desarrollar una solución, por lo que es útil cuando todavía no se tiene completamente definido cuál es el problema o qué solución se necesita.

 - ventajas como una mayor facilidad para adaptarse a cambios, mejor comunicación, revisiones frecuentes y una mayor participación de las personas involucradas
- limitaciones Si existen demasiados cambios, el proyecto puede perder organización; si el equipo no se comunica correctamente, pueden aparecer problemas; y si se realizan demasiadas reuniones o revisiones, se puede perder tiempo. Por eso, existe un equilibrio entre flexibilidad y organización.

| Aspecto                   | Beneficio                                 | Limitación                                |
| ------------------------- | ----------------------------------------- | ----------------------------------------- |
| Cambios                   | Permite adaptarse a nuevas necesidades    | Demasiados cambios pueden desorganizar    |
| Comunicación              | Facilita el trabajo en equipo             | Requiere participación constante          |
| Entregas frecuentes       | Permite revisar los avances               | Puede requerir más revisiones             |
| Trabajo visual            | Permite conocer el estado de las tareas   | Un tablero mal organizado puede confundir |
| Participación del cliente | Ayuda a obtener un resultado más adecuado | Requiere tiempo del cliente               |

###  Scrum

Scrum es una forma de organizar el trabajo de un equipo mediante periodos cortos llamados Sprints. Durante cada Sprint se selecciona un conjunto de actividades y al terminar se busca obtener un resultado que pueda revisarse. Es útil principalmente cuando se desarrolla un proyecto que puede cambiar conforme se conocen mejor las necesidades.

#### En Scrum existen tres responsabilidades principales
 1. El **Product Owner** representa las necesidades del producto, organiza las prioridades y mantiene el Product Backlog. Un error frecuente es que intente controlar directamente todo el trabajo del equipo.
 2. El **Scrum Master** ayuda a que Scrum se utilice correctamente, facilita las reuniones y ayuda a resolver problemas que dificulten el trabajo. Un error común es verlo como un jefe que asigna todas las tareas. 
 3. El **Development Team** es el grupo encargado de realizar el trabajo necesario para crear el producto. Un problema frecuente sería que cada integrante trabaje por separado sin comunicarse con los demás.

#### Scrum utiliza tres elementos principales.

 1. El **Product Backlog** es una lista ordenada de todo lo que puede necesitar el producto. 
 2. El **Sprint Backlog** contiene el trabajo seleccionado para realizar durante el Sprint. Finalmente, 
 3. El **Increment** es el resultado del trabajo terminado que cumple con las condiciones establecidas.

También es importante diferenciar la **Definition of Done** de los **criterios de aceptación**. La Definition of Done establece las condiciones generales que debe cumplir un trabajo para considerarse terminado, mientras que los criterios de aceptación indican qué debe cumplir una función o tarea específica para ser aceptada.

###### Los eventos principales de Scrum son el Sprint, Sprint Planning, Daily Scrum, Sprint Review y Sprint Retrospective
 - El Sprint es el periodo durante el cual se realiza el trabajo y normalmente dura entre una y cuatro semanas. 
 - El Sprint Planning sirve para decidir qué trabajo se realizará. 
 - El Daily Scrum es una reunión breve, normalmente de 15 minutos, para revisar el avance y organizar el trabajo. 
 - La Sprint Review sirve para revisar el resultado obtenido y recibir comentarios. 
 - La Retrospective permite analizar cómo trabajó el equipo y qué puede mejorar. Un problema común es convertir estas reuniones en reuniones demasiado largas o utilizarlas para controlar individualmente a los integrantes

Scrum también puede utilizar diferentes medidas para conocer el avance. La **velocity** muestra aproximadamente cuánto trabajo completa un equipo durante un Sprint. El **burndown** permite observar cuánto trabajo falta por completar. El **WIP** representa el trabajo que está iniciado pero todavía no terminado. Estas medidas deben utilizarse para comprender y mejorar el trabajo, no para comparar equipos o castigar a las personas.

### 3. Kanban

Esta metodología nació en Toyota durante la década de 1940; esta marca automotriz japonesa explica que: “Kanban fue desarrollado por Taiichi Ono y su equipo, quienes se inspiraron en el sistema de los supermercados para optimizar la eficiencia y reducir el desperdicio en la producción. El término “Kanban” significa “tarjeta visual” en japonés, y se utilizaban tarjetas para controlar la producción en cada etapa del proceso, asegurando una producción alineada con la demanda y una respuesta ágil a los cambios en los pedidos

Un tablero Kanban sencillo para un equipo de desarrollo podría tener las columnas 
- Por hacer
- En proceso
- En revisión
- Terminado
Por ejemplo, se podría establecer un límite de tres tareas en "En proceso" y dos en "En revisión". Esto evita que el equipo comience demasiadas tareas al mismo tiempo sin terminar las anteriores.

```text
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  POR HACER  │ EN PROCESO  │ EN REVISIÓN │  TERMINADO  │
├─────────────┼─────────────┼─────────────┼─────────────┤
│   Tarea 1   │   Tarea 3   │   Tarea 5   │   Tarea 7   │
│   Tarea 2   │   Tarea 4   │             │   Tarea 8   │
│   Tarea 6   │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

Kanban utiliza diferentes medidas para conocer cómo está funcionando el trabajo. 
1. El **Lead Time** es el tiempo desde que se solicita una tarea hasta que se termina
2. El **Cycle Time** es el tiempo desde que el equipo comienza a trabajar en una tarea hasta que la termina
 3. El **Throughput** es la cantidad de tareas terminadas durante un periodo determinado

También pueden establecerse políticas para indicar cómo debe manejarse cada tarea. Por ejemplo, una regla puede indicar que una tarea solamente pasa a revisión cuando ya fue terminada y revisada. Además, existen diferentes clases de servicio. Un trabajo urgente puede tener prioridad porque necesita resolverse rápidamente; una tarea con fecha fija debe terminar antes de una fecha determinada; el trabajo normal puede seguir el proceso habitual; y una mejora puede realizarse para mejorar el sistema aunque no sea urgente.

Kanban puede ser especialmente útil cuando las tareas llegan continuamente, como en un equipo de soporte técnico que recibe tickets. También puede utilizarse cuando las prioridades cambian con frecuencia. A diferencia de Scrum, no necesita organizar obligatoriamente el trabajo en periodos fijos.

### 4. Design Thinking, aplicación y conclusión

- Design Thinking es una forma de buscar soluciones que comienza por comprender a las personas y el problema que tienen. Se puede utilizar en proyectos de software porque ayuda a conocer mejor lo que necesita el usuario antes de comenzar una solución.

Sus cinco etapas principales son 
1. Empatizar,se busca conocer las necesidades de las personas mediante entrevistas, observación
2. Definir, se organiza la información y se define el problema
3. Idear, se proponen diferentes soluciones
4. Prototipar, se crea un prototipo sencillo para representar una posible solución
5. Probar, se prueba el prototipo y se reciben opiniones para realizar mejoras


Un ejemplo sería crear una aplicación para ayudar a los estudiantes a organizar sus tareas. Primero se podría preguntar a varios estudiantes cómo organizan actualmente sus actividades y qué problemas tienen. Después se podría definir el problema como la dificultad para recordar las tareas y sus fechas de entrega. Posteriormente se propondrían ideas como un calendario, una lista de tareas y recordatorios. Como prototipo de baja fidelidad se podría realizar un dibujo de la pantalla principal:

```text
┌──────────────────────────┐
│       MIS TAREAS         │
├──────────────────────────┤
│ Matemáticas              │
│ ☐ Resolver ejercicios    │
│ Fecha: 10 de octubre     │
│                          │
│ Mecatrónica              │
│ ☐ Investigación          │
│ Fecha: 12 de octubre     │
│                          │
│      + AGREGAR TAREA     │
└──────────────────────────┘
```

Design Thinking puede utilizarse antes de Scrum o Kanban para comprender mejor el problema y saber qué se necesita desarrollar. Después, Scrum podría utilizarse para organizar el desarrollo por periodos de trabajo, mientras que Kanban podría utilizarse para visualizar las tareas y controlar su avance. De esta manera, los diferentes enfoques pueden complementarse.

 ### Conclusion
 las metodologías ágiles permiten organizar el trabajo de una manera más flexible y facilitan la adaptación a los cambios. Scrum, Kanban y Design Thinking tienen características diferentes, por lo que la elección depende del tipo de proyecto. En un contexto académico pueden ser útiles para organizar proyectos de la ewcuela, repartir tareas , revisar  y trabajar en equipo. También pueden utilizarse en proyectos de programación, mecatrónica y desarrollo de prototipos, donde es común realizar cambios después de probar los resultados.

Considero que conocer estas formas de trabajo puede ser útil tanto en la escuela como en la industria, nos muestran mejores y mas optimizadas maneras de ordenar informacion, revisar los resultados y ver que podemos mejorar
### Referencias

* Atlassian. (s. f.). *Roles de Scrum*. Atlassian. https://www.atlassian.com/es/agile/scrum/roles

* Cognodata. (s. f.). *Principios de la metodología Agile para el desarrollo de proyectos*. Cognodata. https://www.cognodata.com/blog/principios-metodologia-agile-desarrollo-proyectos/

* Scrum Alliance. (s. f.). *The Scrum Team*. Scrum Alliance. https://resources.scrumalliance.org/Article/scrum-team

* UNIR México. (s. f.). *Metodología Kanban: qué es, características y cómo funciona*. Universidad Internacional de La Rioja. https://mexico.unir.net/noticias/ingenieria/metodologia-kanban/

* Atlassian. (s. f.). *Roles de Scrum*. Atlassian. https://www.atlassian.com/es/agile/scrum/roles

* Cognodata. (s. f.). *Principios de la metodología Agile para el desarrollo de proyectos*. Cognodata. https://www.cognodata.com/blog/principios-metodologia-agile-desarrollo-proyectos/

* Scrum Alliance. (s. f.). *The Scrum Team*. Scrum Alliance. https://resources.scrumalliance.org/Article/scrum-team

* UNIR México. (s. f.). *Metodología Kanban: qué es, características y cómo funciona*. Universidad Internacional de La Rioja. https://mexico.unir.net/noticias/ingenieria/metodologia-kanban/
