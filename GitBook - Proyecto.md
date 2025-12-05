# Módulo 3: Optimización de Talento

Recuerda que este proyecto es un ejercicio académico, ante la duda pregunta a tus profesores.

## 1. Resumen.

En el entorno empresarial altamente competitivo de hoy en día, la toma de decisiones informadas es esencial para el éxito a largo plazo. La retención de empleados y la satisfacción en el trabajo son cuestiones críticas para cualquier organización, ya que afectan directamente a la productividad, la moral y la rentabilidad.

Con el objetivo de reducir la rotación de empleados y mejorar la satisfacción en el trabajo la empresa **ABC Corporation**, nos han contratado para desarrollar un proyecto de análisis de datos. Nuestra misión es **identificar factores clave que influyen en la satisfacción en el trabajo y, en última instancia, en la retención de empleados**.

En este proyecto, presentaremos los resultados de nuestro análisis exploratorio de datos y analizaremos los resultados para proporcionar a ABC Corporation** información valiosa** que informe sus decisiones estratégicas.

**¿Quién es ABC Corporation?**

ABC Corporation, fundada en 1980 en California, es una consultora tecnológica especializada en ofrecer soluciones de inteligencia artificial (IA) y aprendizaje automático (*machine learning*) a empresas de diversos sectores. Su enfoque principal radica en automatizar y optimizar procesos empresariales mediante tecnologías de vanguardia.

La empresa se distingue por tener un equipo multidisciplinario que abarca expertos en UX/UI, marketing, analistas, científicos de datos y otros campos relevantes. Esta diversidad permite una sinergia única entre conocimientos técnicos especializados y perspectivas variadas, lo que les permite ofrecer soluciones personalizadas adaptadas a las necesidades individuales de cada cliente.

EL último proyecto donde ha estado implicado la empresa ha sido la optimización de procesos de selección de personal, para ello la empresa ha desarrollado una plataforma de selección inteligente, donde los empleados pueden analizar automáticamente los CV de las posibles candidatas, identificar sus habilidades clave para finalmente clasificar los candidatos según su idoneidad para determinados roles. Además, han creado un sistema de recomendación para sugerir a los reclutadores los mejores candidatos.

## Fases del proyecto

**Fase 1: Análisis Exploratorio de Datos(EDA).**

Antes de llevar a cabo el proyecto es crucial comprender mejor el conjunto de datos y sus características. Para ello deberás hacer un análisis exploratorio detallado del conjunto de datos para familiarizarte con ellos y entender que información tenemos.

**Fase 2: Transformación de los datos.**

Esto puede incluir la limpieza de datos, la normalización, la conversión de tipos de datos y la aplicación de reglas empresariales específicas. Las transformaciones se realizarán mediante funciones de Python que se aplicarán a los datos extraídos. Algunas de las transformaciones que podrías hacer son:

* La columna Gender tiene valores de 0 y 1, los cuales son pocos intuitivos. Los podrías reemplazar por "Male" y "Female", o "M" y "F" por ejemplo.
* Algunas columnas, como la columna DailyRate son columnas que incluyen valores numéricos decimales. Pero en el DataFrame aparece como columna de tipo string. Deberás hacer los cambios necesarios para convertirla en columna de tipo numérica.
* Evaluar si hay valores duplicados y analizar si tiene sentido eliminarlos o mantenerlos.
* Valores inconsistentes, por ejemplo en la columna DistanceFromHome tiene valores negativos.
* Errores tipográficos en algunos valores de las columnas categóricas. Por ejemplo, en la columna MaritalStatus en vez de "Married" en algunas filas aparece "Marreid".
* Columnas redundantes, es decir, columnas que nos dan la misma información expresada de forma diferente.

**Fase 3: Visualizando los datos.**

El objetivo de esta fase será proporcionar a **ABC Corporation** un informe detallado del contexto general de la empresa utilizando visualizaciones en Python. Este informe permitirá una comprensión más profunda de la situación actual y servirá como base para la toma de decisiones informadas.

Deberás generar **un informe completo que incluirá las visualizaciones junto con análisis descriptivos (se presentará el día de la demo)**. Las visualizaciones ayudarán a resaltar **tendencias, áreas de mejora y fortalezas dentro de la empresa**.

**Fase 4: Diseño de BBDD e Insercción de los Datos (estructura).**

En esta fase tiene como objetivo la creación y la inserción de datos en una base de datos desde el punto de vista de su arquitectura o estructura, es decir, definir como seria su BBDD final. Los aspectos principales de esta fase del proyecto son:

1. **Diseño de la Estructura de la Base de Datos:** Deberás definir la estructura de la base de datos. Esto incluye identificar las tablas necesarias y sus relaciones, así como definir las claves primarias y foráneas.
2. **Creación de la Base de Datos:** Deberás crear la base de datos utilizando las herramientas aprendidas en el módulo 2.
3. **Inserción de Datos Iniciales:** Deberás insertar los datos de los empleados de la empresa en la base de datos.

**Fase 5: Creación de una ETL.(Bonus)**

En esta fase del proyecto, deberás crear un archivo .py que llevará a cabo la extracción, transformación y carga (ETL) de datos. El objetivo de esta etapa es automatizar la inserción de datos en la base de datos relacional y garantizar que la información se actualice de manera consistente y también automatizar el proceso de transformación de la información antes de la inserción en la BBDD. Los pasos que deberás seguir en esta fase son:

1. **Extracción de Datos:** En esta primera parte de la ETL, las alumnas desarrollarán una función para extraer datos desde las fuentes de datos previamente definidas. Estas fuentes pueden incluir hojas de cálculo, archivos CSV, bases de datos externas o cualquier otro formato de datos relevante. El objetivo es obtener datos frescos y relevantes que se cargarán en la base de datos.
2. **Transformación de Datos:** Deberás desarrollar una función (o varias) para aplicar todas las transformaciones necesarias para garantizar la integridad y la calidad de los datos (estas transformaciones serán las mismas que en la fase 2).
3. **Creación de la Base de Datos:** En esta etapa, crearás una función con el código para la creación de la BBDD diseñada en la fase 3.
4. **Carga de Datos:** Después de la creación de las tablas, desarrollaras funciones que permitan la inserción de datos transformados en la base de datos. Esto garantizará que la base de datos esté siempre actualizada con la información más reciente.

**NOTA** Todo este código deberá estar en funciones y en archivos .py.

## Los Datos.

Las columnas que os encontraréis en el DataFrame son:

* **Age**: Edad del empleado.
* **Attrition**: Indica si el empleado dejó la empresa (Yes/No).
* **BusinessTravel**: Frecuencia de viajes laborales (e.g., travel\_rarely).
* **DailyRate**: Tarifa diaria estimada para clientes, calculada en base al salario.
* **Department**: Departamento en el que trabaja el empleado.
* **DistanceFromHome**: Distancia en millas o kilómetros desde el hogar al trabajo.
* **Education**: Nivel educativo del empleado en escala numérica.
* **EducationField**: Campo de estudio académico del empleado.
* **employeecount**: Valor constante de "1", indicando un solo empleado por registro.
* **employeenumber**: Número de identificación del empleado.
* **EnvironmentSatisfaction**: Nivel de satisfacción con el ambiente laboral.
* **Gender**: Género del empleado.
* **HourlyRate**: Tarifa por hora calculada.
* **JobInvolvement**: Nivel de compromiso del empleado en el trabajo.
* **JobLevel**: Nivel jerárquico del puesto del empleado.
* **JobRole**: Función o rol específico del empleado.
* **JobSatisfaction**: Satisfacción general en el puesto.
* **MaritalStatus**: Estado civil (e.g., Single, Married).
* **MonthlyIncome**: Ingreso mensual estimado en base al salario anual.
* **MonthlyRate**: Tarifa mensual estimada en función de la tarifa diaria.
* **NUMCOMPANIESWORKED**: Número de empresas previas en las que ha trabajado.
* **OverTime**: Indica si el empleado trabaja horas extras (Yes/No).
* **PercentSalaryHike**: Incremento porcentual en el salario.
* **PerformanceRating**: Evaluación de desempeño en una escala numérica.
* **RelationshipSatisfaction**: Satisfacción con relaciones interpersonales en el trabajo.
* **StandardHours**: Clasificación de jornada (Full Time/Part Time).
* **StockOptionLevel**: Nivel de opciones sobre acciones asignadas.
* **TOTALWORKINGYEARS**: Años totales de experiencia laboral.
* **TrainingTimesLastYear**: Número de sesiones de entrenamiento en el último año.
* **WORKLIFEBALANCE**: Nivel de balance entre vida personal y laboral.
* **YearsAtCompany**: Años en la empresa actual.
* **YearsInCurrentRole**: Años en el rol actual.
* **YearsSinceLastPromotion**: Años desde la última promoción recibida.
* **YEARSWITHCURRMANAGER**: Años trabajando con el mismo gerente.
* **DateBirth**: Año de nacimiento del empleado.
* **Salary**: Salario anual calculado para el empleado.
* **RoleDepartament**: Combinación de rol y departamento.
* **NUMBERCHILDREN**: Número de hijos del empleado (si está disponible).
* **RemoteWork**: Indica si el empleado trabaja de forma remota (Yes/No).


## Objetivos

1. Consolidar los conocimientos de Python y SQL.
2. Utilizar control de versiones en equipo para aprender las ventajas y conflictos que genera.
3. Implementar Scrum como marco de referencia para el desarrollo del producto, basándonos siempre en los valores de *Agile* como puntos clave del trabajo en equipo y la mejora continua.
4. Mejorar la comunicación entre los miembros del equipo.
5. Mejorar vuestras habilidades de comunicación en público al exponer el proyecto en la sesión final.

## Planificación del proyecto.

### *sprints*

Para la realización de este proyecto trabajaremos en 2 *sprints* (2 iteraciones). Siguiendo los principios ágiles, estableceremos pequeños ciclos iterativos de forma que al final de cada uno generemos valor perceptible por nuestros usuarios. Dedicaremos el primer día a la planificación del *sprint* (*sprint planning*) y el resto a trabajar en el desarrollo del proyecto. Al final de cada *sprint* haremos un *Sprint Review* del proyecto para presentar los resultados conseguidos y recoger *feedback*.

También haremos una retro corta revisando los *working agreements* que hemos acordado al inicio del proyecto y añadiendo cualquier otro *feedback* que nos permita mejorar el proyecto.

Al final del segundo **sprint** (que coincidirá con el final del proyecto y del módulo), haremos una sesión de presentación más completa, más allá de lo que sería un *Sprint Review*.

### Criterios de aceptación

* Crear la infraestructura necesaria: repositorio en GitHub y con acceso para todos los miembros del equipo.
* Extraer datos de distintas fuentes de datos y creación de una Base de Datos.
* Tener la extracción de datos, creación de la base de datos e inserción de datos automatizada en funciones(obligatorio) y clases(optativo).
* Tener en el repositorio de GitHub todo el código del desarrollo del proyecto.

### Historias de usuario

Para la gestión del proyecto, usaremos historias de usuario. Las historias de usuario son descripciones breves y concretas de las funcionalidades o características que un usuario espera encontrar en un producto o sistema. Recordemos que, las historias de usuario son una herramienta importante para asegurarse de que el equipo de desarrollo (es decir, nosotras) entienda las necesidades de los usuarios y construya el producto de manera efectiva.

Algunas de las historias de usuario que podemos definir son:

1. Exploración del DataFrame para entender que datos hay.
2. Realización del EDA para identificar que transformaciones hay que hacer a los datos.
3. Transformación de los datos.
4. Decidir que visualizaciones hacer.

## Entrega

El formato de entrega de este proyecto será mediante la subida de este a la plataforma de GitHub. Para subirlo, se creará un repositorio en vuestro perfil. El nombre del repositorio deberá estar compuesto de las siguientes partes, todo ello separado por guiones:

* La palabra: proyecto-da.
* Número de la promoción: promo-X.
* Número del módulo: modulo-3.
* Número del equipo: team-X.

Por ejemplo:

* project-da-promo-47-modulo-3-team-1
* project-da-promo-47-modulo-3-team-3

En lo relacionado en las fechas de los *sprints* pueden verlo en vuestros calendarios

En las *sprint review* se revisará que se hayan solucionado todas las tareas técnicas asociadas a la entrega de esos *sprints*, si algo quedara pendiente se arrastraría al siguiente *sprint*.

## 6. Presentación

El último día del módulo presentaréis la versión final de este proyecto a vuestras compañeras y al equipo de Adalab. Cada equipo realizará una presentación de 10 minutos y posteriormente habrá 5 minutos de *feedback* por parte del público. En este caso, la audiencia podría ser más variada pues no sólo estarán los profesores.

El objetivo es que practiquéis la realización de las demos de los proyectos que habéis desarrollado, explicándolo desde un punto de vista técnico y también desde la perspectiva de producto, mejorando además vuestras habilidades de exposición, objetivo de desarrollo profesional del curso.

Para que la presentación salga bien es imprescindible una buena preparación. Por ello, durante el primer *sprint* del módulo tendréis que asignar responsabilidades dentro del equipo relacionadas con la preparación de ésta. Algunos tips para preparaos este demo son:

* Todas las participantes del equipo deben hablar en la presentación (sin práctica no hay mejora).

* Identificar los objetivos de la presentación: Debemos tener claro qué es lo que queremos lograr con la presentación. ¿Queremos demostrar la funcionalidad de un producto? ¿Queremos mostrar los resultados de un experimento? ¿Queremos atraer inversores? Dependiendo del objetivo, deberemos enfocar la presentación de manera distinta.
* Conoce a tu audiencia: La presentación debe estar adaptada al tipo de audiencia que se espera. Si se presentara ante posibles inversores, la presentación debe estar enfocada en los beneficios y la rentabilidad del producto. Si es una presentación para usuarios, deberá enfocarse en la usabilidad y la facilidad de uso.
* Debéis ser claras y concisas: La presentación debe ser fácil de entender y no debe ser demasiado larga. Es importante presentar la información de manera clara y concisa. Debemos tener en cuenta que los detalles técnicos pueden ser interesantes, pero no deberían opacar la idea principal.
* Demostrad la funcionalidad del producto: Si la presentación es para demostrar un producto, es importante que demostremos su funcionalidad. Podemos hacerlo mediante un video o demostrando el producto en vivo. Es importante asegurarse de que el producto funciona correctamente antes de la presentación.
* Resaltad los aspectos más importantes: En cualquier presentación, hay aspectos que son más importantes que otros. Debéis resaltar los aspectos que sean más relevantes para su objetivo. Por ejemplo, si queréis atraer inversores, deberéis resaltar los beneficios y la rentabilidad del producto.
* Practicad la presentación: Es importante que practiquéis la presentación varias veces antes del evento. Debéis aseguraos de que la presentación esté bien estructurada y que os sentís cómodas hablando frente a la audiencia.
* Preparad respuestas a preguntas frecuentes: Es probable que la audiencia tenga preguntas después de la presentación. Debéis preparaos para responder preguntas frecuentes y tener la información necesaria a mano.

Además de esto, para mejorar vuestras habilidades de exposición en público y hacer la presentación más rica, podréis incorporar otros elementos adicionales (son solo ideas, sentíos libres de innovar y ser creativas):

* Dejar muy claro quién ha sido vuestro cliente y qué fue lo que os pidió.
* Explicar qué necesidades cubre o qué problemas soluciona el producto, cuál es el beneficio principal que aporta y qué lo hace único comparado con otros productos parecidos del mercado.
* Aportaciones "únicas y diferenciadoras" de cada equipo al proyecto.
* Cómo ha sido la organización del equipo, el reparto de tareas y la coordinación a la hora de trabajar todas en el mismo código.
* Cuál de las tareas o los puntos ha sido el que más esfuerzo ha requerido.
* Cuál de las tareas o partes del producto es la que hace que el equipo esté más orgulloso.
* Las tecnologías qué habéis utilizado y para qué sirven, y algunas partes del código que habéis desarrollado que merezca la pena resaltar.
* La presentación debe tener un "buen inicio y un buen cierre" que nos haga a todos estar atentos y aplaudir... ahí os dejamos que echéis a volar vuestra imaginación.
* No habléis en primera persona de lo que habéis hecho, hablad del equipo.
* No mencionéis problemas, sino "retos" que os han hecho aprender y crecer.
ChatGPT said:
Aquí tienes una descripción breve, clara y profesional del proyecto, en español, ideal para resumirlo en un README, slide o presentación:

Descripción breve del proyecto
Este proyecto tiene como objetivo analizar y optimizar la gestión del talento en ABC Corporation mediante técnicas de análisis de datos, visualización y diseño de bases de datos. A partir de un conjunto de datos de Recursos Humanos, llevamos a cabo un análisis exploratorio, transformamos y limpiamos la información, generamos visualizaciones clave y diseñamos la arquitectura de una base de datos relacional para centralizar y estructurar los datos del personal. Como fase adicional, desarrollamos un proceso ETL automatizado en Python para la extracción, transformación y carga de los datos.
El proyecto se desarrolla siguiendo metodologías ágiles (Scrum) y buenas prácticas de control de versiones, con el objetivo final de presentar resultados claros que ayuden a comprender los factores que influyen en la satisfacción laboral y la retención del talento dentro de la organización.

---
### Resumen conciso

Este proyecto analiza datos de Recursos Humanos de ABC Corporation para identificar factores que influyen en la satisfacción laboral y la retención del talento. 

Incluye un análisis exploratorio, limpieza y transformación de datos, generación de visualizaciones y diseño de una base de datos relacional.

Además, se desarrolla un proceso ETL automatizado en Python para asegurar la actualización y coherencia de la información. 

El trabajo se realiza siguiendo metodologías ágiles y buenas prácticas de control de versiones.

### Más conciso aún

Proyecto centrado en analizar y transformar datos de Recursos Humanos para identificar factores que influyen en la satisfacción y retención del personal en ABC Corporation.

Incluye EDA, limpieza, visualizaciones, diseño de base de datos y un proceso ETL en Python, aplicado con un enfoque ágil.
