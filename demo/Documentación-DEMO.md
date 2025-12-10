# Memoria Demo-Presentación:

### A la hora de enfrentar el desarrollo de lo que sería la presentación visual del proyecto, planteamos inicilamente varias posibilidades de enfoque, cada una con un relato acorde que le diese sentido a la perspectiva del análisis de los datos. Porque los datos son unos, concretos, pero el 'para qué lo uses' cambia el enfoque de la investigación y el análisis. 

__________________________

#### 1. PERSPECTIVA HUMANISTA:
Enfoque en el impacto de los datos en la vida de lxs empleadxs. La historia no es sobre optimización de costes, sino sobre la mejora de la experiencia laboral y la ética de la IA.

#### 2. Perspectiva de laboratorio de I+D:
Historia no es sobre dar consejos, sino sobre probar que la tecnología del sistema de gestión de talento funciona.

#### 3. Perspectiva del Inversor:
Historia sobre optimización de costes, impacto financiero de la retención.

#### 4. 4. Perspectiva como Consultoría Estratégica (…) 

___________________________


### Finalmente decidimos aunar las perspectivas humanistas y técnica, creando un contexto en el que partiendo de una base humanista que destaca la importancia de las personas tras los datos, llevamos a cabo un trabajo altamente técnico tanto para el análisis como para las transformaciones necesarias y las mejoras estructurales que redunden en una mayor calidad de la base técnica para la recogida de nuestros datos. 

### Una vez consensuado el efnoque, planteamos la estructura de nuestra presentación: Qué puntos tendríamos que abordar y de qué manera para exponer todo el trabajo llevado a cabo durante las semanas. Y esta fue nuestra estructura (e indagaciones) inicial: 



#### Estructura de la Presentación: Auditoría de Bienestar y Calidad de Datos:

##### 1. INICIO y Objetivo del proyecto: 

##### Retención del talento y satisfacción del personal (enfoque más técnico) + Captar la atención del Departamento de Ética y Cultura empresarial  (enfoque humanista). El problema ético del tratamiento de datos:

>*“ABC Corporation invierte en tecnología de talento, pero hoy, nuestra misión no es solo optimizar costes, sino auditar el bienestar de la empresa, que empieza con el buen estado/bienestar del dato…”*

>*“¿Estamos fallando en ver las señales de infelicidad? ¿Nuestra tecnología (IA) está creando un ambiente de trabajo justo y equitativo?”*

##### 2. SOMOS. Rol y Misión: Equipo de Auditoría de Bienestar./I+D.

“Somos el equipo de Investigación y Desarrollo encargado de asegurar que el análisis de datos se use para humanizar y dinamizar la gestión del talento, no solo para automatizarla. 

##### Nuestro objetivo: Calidad del dato = Calidad de vida

“Hemos auditado la fuente de datos de empleadxs que alimenta los futuros modelos de retención. Si este dato es defectuoso, la IA que se construya sobre él trabajará con sesgos y construirá con fallos de rendimiento”. 

##### 3. EL PROYECTO: LA AUDITORÍA TÉCNICA.

##### Calidad de Datos (Laboratorio I+D): Demostrar que la validez del análisis depende de la limpieza y una contextualización inteligente.

##### 3.1. Fase 1 y 2 (EDA): Cuestionar la fuente: 

Mostramos ejemplos de anomalías encontradas en columnas clave: Nulos, outliers y errores tipográficos:
df["standardhours"].value_counts(normalize=True, dropna=False)*100

'No podemos tomar decisiones justas sobre la jornada de un empleado si la tecnología no puede leerla correctamente. Tuvimos que indagar y buscarle explicación a un tanto por ciento tan significativo de nulos'.

##### 3.2. Fase 2 (Transformación): Hablar sobre conversiones, o estandarización de categorías. Ejemplos/propuestas:

'Nuestra auditoría encontró inconsistencias tipográficas en la columna maritalstatus, lo que significa que el dato no es fiable. Tuvimos que estandarizar la columna (limpieza) para garantizar la equidad del dato':
df["maritalstatus"] = df["maritalstatus"].str.replace("marreid", "married")

Propuesta Ética de Limpieza: Cómo tratar los datos sensibles (gender, etc.) para ser más inclusivos y éticos. 

##### Por qué limpiamos y cómo limpiamos (ética y calidad en el tratamiento de los datos).

'Sabemos que la plataforma de selección usa binarios (0 y 1), pero para la Auditoría de Bienestar, el equipo propuso transformar éticamente la columna gender de 0/1 a male/female y dejar la puerta abierta a categorías de género no binarias o no especificadas (non-binary/other?) para el futuro, asegurando que nuestra empresa sea más inclusiva que la propia tecnología que la soporta.'

##### 4. RESULTADOS. La evidencia del impacto: Mostrar las métricas de satisfacción y antigüedad. 

Fase 3 (Visualización) y 4 (Estadística): Mostrar Boxplots, Histogramas o Countplots.

1. Distribución de ``worklifebalance`` y ``relationshipsatisfaction``: ¿Dónde está la infelicidad?.

2. Relación entre ``totalworkingyears ``y ``attrition``: ¿Quién se va y por qué?

##### 5.CONCLUSIONES. 
##### Propuesta de Valor. La decisión estratégica: Resumir el hallazgo y el impacto de un dato de calidad.

###### Conclusión (El coste oculto de los datos rotos): 

“La **Auditoría de Bienestar** ha revelado que la baja calidad de los datos tiene un impacto **ético y económico** directo: nos impide ver la infelicidad y las grietas en el rendimiento. El error tipográfico en una jornada o el dato nulo en una satisfacción puede ser alguien de nuestro personal al que estamos dejando de prestar atención, puede que sea incluso recíproco.**La precisión técnica es un imperativo ético**”.

**Propuesta de valor:**

Fiabilidad del Modelo (I+D):

“Al limpiar y estandarizar la fuente, el equipo de I+D ha logrado un aumento del [X]% en la fiabilidad de las columnas de bienestar. 

Esto significa que si ABC Corporation utiliza este dataset saneado para entrenar un modelo de retención, ese modelo será más justo y preciso, reduciendo el riesgo de sesgo algorítmico”.

Hallazgo 'humano': 

'Nuestra visualización de ``worklifebalance`` muestra que el 60% de los empleados se concentra en los niveles 1 y 2. La IA solo puede optimizar el talento si sabe que el problema principal no es el salario, sino el desgaste. Esto es el insight humano que el dato limpio nos permite ver'.
		
**Mejora Continua:** 
Enlaza la limpieza de datos con la fiabilidad del futuro modelo de IA. 

'La IA es tan ética como los datos que la entrenan'. 

**Proponemos:** Mejorar el formulario de recogida de datos para evitar las anomalías encontradas y así entrenar modelos de retención más justos.

##### 6.NEXT STEPS:

**Refuerzo de la recolección de datos:** 

“Recomendamos implementar **validaciones estrictas en el back-end** del sistema de gestión de talento, eliminando la posibilidad de input erróneo. Por ejemplo, que la columna maritalstatus no pueda aceptar 'marreid' y el sistema fuerce el valor a 'Married' o que no permita dejar el valor nulo en categorías fundamentales”.

**Ampliación del marco ético:** 

“Implementar la **propuesta ética** de gender (incluir la opción 'Other' o 'Non-Binary') como estándar. Este paso no es solo limpieza, es una declaración activa de la política de inclusión de ABC Corporation, mejorando la moral y la imagen de marca”.

**Plan de auditoría continua:**

“La limpieza que hemos realizado en la Fase 2 es vital, pero es **solo el principio**. 

El riesgo de **data drift*** es constante porque **la cultura de una empresa es orgánica**. Por eso, proponemos la creación de un *Plan de Auditoría Continua*, para garantizar que los modelos de IA que se desarrollen tengan la garantía de la toma de decisiones basad en la realidad actual de nuestros empleados, no en la historia. Ésto transforma nuestra Fase 2 **de ser un "parche" a ser un "sistema de control de calidad" indispensable** para el futuro de la empresa”.

**data drift*: ocurre cuando las propiedades estadísticas de los datos cambian con el tiempo de forma inesperada (el mundo cambia, y los datos por ende. Es la principal razón por la que los modelos de Inteligencia Artificial (IA) y de Machine Learning pierden precisión después de un tiempo, incluso si fueron entrenados perfectamente).

##### 7.CIERRE: Agradecer y abrir el turno de preguntas.

'Hemos demostrado que la calidad de los datos es la base de la justicia empresarial.

Hemos ido más allá de la limpieza, transformando un dataset con inconsistencias en una fuente de verdad ética y fiable para *ABC Corporation*.

Al estandarizar los datos y proponer un plan de ETL automatizada, hemos **blindado la plataforma de talento contra el error humano y el data drift**. Ahora, su tecnología de retención tiene la confianza y la precisión que requiere.

Pero la inversión más importante no está en el software, sino en las personas. Nuestro trabajo asegura que, en la era de la IA, *ABC Corporation* tenga la capacidad de prestar atención a cada empleado individualmente, sin que su valor se pierda por un dato mal escrito o un valor nulo.

El éxito de su plataforma de talento no se medirá por la complejidad de sus algoritmos, sino por la precisión humana en la extracción de los datos que los alimentan'.

**Hemos saneado el dato; ahora,* ABC Corporation* puede sanar el talento.**

(Propuesta interna: Si usamos slides, podríamos finalizar con un slogan tipo: "Calidad del dato = Calidad de vida").


___________________
  
### Una vez definida la estructura que serviría de guión para crear el alma del proyecto, nos repartimos los roles para la creación del pitch de presentación de cada una. 

### Por el camino, y el EDA continuo que llevamos a cabo, vimos que los datos arrojaban información valiosa que nuestra presentación debía recoger y explicitar (porque, aunque quedara todo el análisis convenientemente recogido en el informe derivado, había una necesidad clara de destacarlo para que no quedara enterrado entre líneas y líneas de justificación del trabajo). Nos percatammos también, durante el proceso, de la necesidad de prestar atención a otras variables que incialmente pasaban más desapercibidas y que apoyaban nuestro punto de vista.  

### Así pues, construimos conjuntamente el hilo argumental que guiaría nuestra presentación y creamos el discurso de cada una (que dejamos aquí recogido como apoyo a la información visual de los slides de presentación).

_______________

#### PITCH DEMO:

SLIDE1: "Buenos días a todos. Hoy estamos aquí porque ABC Corporation no solo invierte en tecnología de talento, sino en algo aún más importante: en las personas que hay detrás de esa tecnología".

SLIDE2: "Y es que en Adalabers, creemos que el éxito de cualquier inversión empieza por el bienestar del dato. 
Nosotras somos el equipo de Investigación, Desarrollo y Auditoría de Bienestar de Adalab.
En concreto: 
- Clauda Cervantes como Auditora Principal
- Mayka Durán como Ingeniera de Datos
- Andrea R. Virgós como Analista especializada en Retencion y Bienestar
- Ona Zaragoza como analista de documentacion tecnica y automatizacion 
- Y yo misma, Patricia, como analista de visualizacion de resultados 

Queremos garantizar la retención del talento y la satisfacción laboral, preguntándonos: ¿Estamos interpretando las señales de infelicidad en los datos? ¿La IA que construimos hoy fomentará entornos laborales justos mañana?
Todo esto, dentro de un proyecto formativo real en la comunidad Adalab".

SLIDE3: "Hemos auditado rigurosamente los entornos laborales de ABC, usando metodologías robustas y Python para asegurar la limpieza y optimización de las bases de datos.

Y la conclusión es crítica: si el dato que nutre a los sistemas es defectuoso, la Inteligencia Artificial que se construya sobre él nacerá inevitablemente con sesgos y fallos de rendimiento. Un algoritmo sesgado pone en riesgo la equidad y la inversión.

En resumen, nuestro trabajo sienta la base para que la tecnología de ABC Corporation no solo sea eficiente, sino también ética y equitativa. 

Ahora os dejo con mi compañera Andrea, que contará sobre los objetivos del proyecto".

SLIDE3: "Hemos auditado rigurosamente los entornos laborales de ABC, usando metodologías robustas y Python para asegurar la limpieza y optimización de las bases de datos.

Y la conclusión es crítica: si el dato que nutre a los sistemas es defectuoso, la Inteligencia Artificial que se construya sobre él nacerá inevitablemente con sesgos y fallos de rendimiento. Un algoritmo sesgado pone en riesgo la equidad y la inversión.

En resumen, nuestro trabajo sienta la base para que la tecnología de ABC Corporation no solo sea eficiente, sino también ética y equitativa".

SLIDE4: "Orientamos nuestro proyecto bajo un enfoque dual: no solo buscamos la retención de talento, sino que sentamos las bases técnicas y éticas para el futuro de ABC Corporation.

Partimos de una tasa de retención meritoria, cierto, pero dado que la empresa construye herramientas inteligentes en las que ésto es crucial, nuestro primer paso fue auditar la materia prima: el dato.

Nos preguntamos: '¿Nuestra tecnología corre el riesgo de nacer con sesgos?', '¿Estamos fallando en escuchar a nuestro personal y sus necesidades concretas?' "

SLIDE5: "Nuestro primer objetivo fue la Auditoría y Saneamiento de la Materia Prima, el cimiento de todo valor futuro.

Para nosotras, la fórmula es clara: Calidad del dato equivale a Calidad de vida. Por ello, abordamos esta fase con el máximo rigor técnico.

A través de un riguroso y pormenorizado proceso de EDA y ETL, hemos saneado y estandarizado el dataset.

El resultado es una Base de Datos limpia y con estructura definida que actúa como una fuente de verdad para todos sus sistemas.

Este diseño es a prueba de data drift, lo que garantiza la posible evolución de los datos y la solidez de sus análisis futuros".

SLIDE6: "El segundo objetivo principal era la extracción de valor estratégico. Demostramos que la limpieza de datos es una necesidad ética para humanizar la gestión.

Si los datos son incorrectos, o están mal recogidos, estamos errando al escuchar las demandas de nuestro personal. Estamos tratándolos como números, no como personas.

Por ello, proporcionamos un Informe Visual Detallado que analiza los drivers clave de rotación.

Este análisis permite a ABC Corporation estudiar cómo proceder de cara a la mejora de las condiciones, lo que se traduce directamente en una mayor retención del talento.

Doy paso a mi compañera Claudia que nos hablará acerca de los retos que enfrentamos durante el proyecto".

SLIDE7: "Nuestro punto de partida fue analizar hasta qué punto los datos heredados reflejaban —o no— la realidad y la experiencia de las personas en la organización.

ABC Corporation ya había iniciado un esfuerzo valioso por recoger información, pero los registros mostraban variaciones, datos faltantes y contradicciones que podían afectar el análisis del bienestar. (esto puede pasar con cambios en personal, sobretodo en recursos humanos).

Por eso realizamos una revisión profunda: entender cómo se generan los datos y qué partes necesitaban más rigor para poder utilizarlos con confianza.

Este trabajo fue clave para asegurar que cualquier conclusión futura estuviera basada en un dato honesto y representativo".

SLIDE8: "Una vez identificados los retos, pasamos de observar a decidir.

Aplicamos criterios técnicos y éticos para limpiar, estandarizar y, cuando era necesario, descartar información que podía generar sesgos.

El objetivo no era 'arreglar' los datos, sino garantizar que reflejaran fielmente las condiciones reales del talento en la organización.

Con este proceso logramos una base sólida sobre la que sí es posible analizar bienestar y retención con rigor.

Ahora mi companera Mayka continuará con los insights clave: qué tendencias encontramos y cómo estos datos pueden orientar decisiones organizacionales".

SLIDE9: "Muchas gracias Claudia.

Como hemos visto, tras la limpieza de los datos, hemos realizado una serie de cruces y visualizaciones para entender las dinámicas internas de la compañía. 
Nuestros hallazgos no solo revelan tendencias, sino que apuntan a una dirección estratégica muy clara.

  1. La Fuga de Talento está Concentrada:

Como pueden ver, 5 de nuestros 9 departamentos están en modo puerta giratoria, con tasas de rotación que hacen pensar que algo está empujando a los empleados a buscar nuevos horizontes".

SLIDE10: "Otra forma de visualizar esta rotación puede ser el siguiente gráfico. Muestra claramente la cantidad de empleados que rotaron frente a los que no en cada departamento. 

Se puede observar que el departamento de 'research & development' es el más grande en términos  de número de empleados, pero también parece tener la mayor cantidad de rotación en números absolutos. 

Pero para comparar la 'tasa' de rotación entre departamentos de diferentes tamaños, sería más justo visualizar los porcentajes".

SLIDE11: "Así que, hemos metido en el mix este gráfico que nos regala una perspectiva fresquísima y más útil que solo contar cabezas:

 `Sales`: Lidera la carrera de la rotación, superando el 20%.

 `human resources`: Le pisa los talones, con una rotación también cercana al 20%.

`Research & Development`: Aunque pierde más empleados en bruto, tiene la tasa de rotación más baja, rondando el 15%.

  Conclusión:

Al ajustar los datos y mirar los porcentajes, concluimos que los departamentos de 'Sales' y 'human resources' tienen un probrema de rotación proporcionalmente mayor.

Esto nos ayuda a afinar la puntería para saber donde las estrategias de retención de talento son más urgentes".

SLIDE12: "Para seguir con nuestra búsqueda del bienestar, ahora hemos decidido centrarnos en el salario. 

Como podemos observar cada  'violín' está partido en dos: La mitad izquierda representa a los empleados que no rotaron  y la otra mitad  a los que sí.

En tres de los cuatro departamentos, la parte del violín de los que rotaron está visiblemente más concentrada en la zona de ingresos bajos. De ahí que sea más ancha en la parte inferior de la escala salarial.

Igualmente en el Departamento de `research & development` la tendencia también se cumple, la distribución de salarios en el lado de los que no rotaron es más amplia, alcanzando ingresos más altos. Sin embargo, los que rotaron también se concentran en la franja salarial inferior.

Este análisis departamental nos confirma que, si bien el 'performancerating' es clave para los aumentos, la estructura salarial de cada departamento juega un papel fundamental en la  rotación, lo que valida la hipótesis de que la compensación económica es un pilar central en la estrategia de retención de talento de la empresa".

SLIDE13: "El siguiente gráfico nos centramos en los aumentos de sueldo para cada nivel de 'Performance Rating'.

Como vemos claramente, existe una tendencia positiva clara:  a mayor evaluación de desempeño, mayor aumento salarial. La empresa **premia el desempeño con aumentos salariales**, lo que es una buena práctica.

Por tanto, recomendaríamos a la empresa a mantener esta política y comunicarla claramente para motivar a los empleados."

SLIDE14: "Ahora queremos mostrar como evolucionan los aumentos salariales en función de la antiguedad en la compañia.

Podemos observar que la línea de tendencia para performancerating = 4.0 sube ligeramente con los años en la empresa. Esto quiere decirnos que los empleados con alto desempeño ven un aumento gradual en su compensación a lo largo del tiempo. Los empleados con desempeño medio no ven un aumento significativo en su salario con la antigüedad.

Como comentamos en la anterior gráfica la empresa valora y recompensa el desempeño sobresaliente a lo largo del tiempo".

SLIDE15: "En esta visualización, no estamos viendo una sola variable, sino la interacción de tres factores críticos: la satisfacción laboral, el equilibrio entre la vida laboral y personal, y su impacto combinado en la rotación de personal.

Cada uno de los cuatro gráficos representa un nivel distinto de equilibrio vida-trabajo. Dentro de cada uno, las barras nos muestran cuántos empleados, para cada nivel de satisfacción, decidieron quedarse o irse. El análisis de estos gráficos nos lleva a una conclusión estratégica fundamental para la empresa:
   1. La insatisfacción laboral es el principal predictor de rotación. 
   2. El equilibrio vida-trabajo (WLB) actúa como un 'multiplicador de riesgo'. Un mal WLB acelera la rotación en todos los frentes, incluso entre el talento que está contento con sus tareas. 

Por tanto, para reducir la rotación de manera efectiva, la empresa no solo debe enfocarse en aumentar la satisfacción, sino que debe tratar las políticas de equilibrio vida-trabajo con la misma urgencia y prioridad.

Y con esta última reflexión doy paso a mi compañera Ona que nos hablará de los siguientes pasos que vamos a tomar".

SLIDE16: "Tomando el relevo de todo este trabajo, tenemos propuestas de futuro: 

El futuro son procesos automatizados.

Es un plan de auditoría continua.

Y es un refuerzo del sistema backend con validaciones estrictas y políticas claras para la gestión de la información".

SLIDE17: "Un refuerzo que parte del presente:

Utilizamos un lenguaje de programación de alto nivel, como es Python, que mantiene la estructura que hace efectivos protocolos de cribado, limpieza e implementa la ejecución de resultados.

Garantiza la futura automatización dirigida a la carga de bases de datos.

Un sistema que permite comunicarse con la información mediante la visualización,  en este caso hemos extraido las claves gracias a utilizar seaborn y matplotlib.

Esto sólo es posible si se dan ciertas condiciones para la continuidad:

La implementación de validaciones estrictas en el back-end del sistema de gestión de talento, eliminando la posibilidad de input erroneo.

Ampliar el abanico de opciones de respuesta, haciéndolo más exhaustivo al reflejar los modos de vida actuales."

SLIDE18: "Al estandarizar los datos garantizamos el camino a dinámicas de mejor competencia y mayor bienestar:

Con un Plan de ETL automatizado de principio a fin.

Con niveles avanzados de visualización, sumando dinamismo a la representación de datos complejos, entendible y efectista por cualquier potencial audiencia.

Con un plan de auditoría continua:

Que garantiza blindar la plataforma de gestión de talento contra el error humano y contra el data-drift al implementar sistemas de IA.

Y asimismo, tenemos la capacidad de acompañar tu negocio en su expansión con escalabilidad, replicando este mismo sistema en otras localizaciones globales.

Dicho esto, vamos con el cierre".

SLIDE19-20: "Muchas gracias Ona y a todo el equipo. 

Para cerrar, quiero dejarles con un pensamiento que resume el corazón de este proyecto:
Cada dato no es solo un registro; es una historia, una trayectoria y, sobre todo, una oportunidad.

Hemos demostrado que la calidad de los datos es la base de la justicia empresarial.

**Hemos saneado el dato; ahora,* ABC Corporation* puede sanar el talento.**

Pero nuestro compromiso no termina aquí. Seguiremos creando soluciones que conviertan los datos en herramientas para construir equipos más sanos, estables y más competentes.
Y abrimos ahora el turno de preguntas. Muchas gracias a todas".

______________________



### Para finalizar  con objeto de llevar un registro del proceso de trabajo en lo relativo a la presentación, desatacar que experimentamos como el proceso de EDA pasaba de ser un modo de trabajo a una filosfía que vertebraba todo nuestro desempeño, volviendo sobre nuestros pasos cuando se requería y cuidando al detalle cada uno de los mismos. Cada decisión justificada, cada paso, con significado. 

### Ésto lo denotamos cuando a raíz de la fase de las visualizaciones, modificando las gráficas y sus colores, asumimos una paleta cromática para unificar todo y evitar ruido visual extra. Así, lo que fue una elección casual de colores, se convirtió en el color corporativo, del cual quisimos hacer gala uniformándonos para la presentación. Lo que redundó en terminar de armar nuestro relato y dotarlo de una personalidad especial y diferenciada. 

