# Memoria de Proyecto ABC Corporation: Gestión del Talento

       . breve descripción

### Índice

- [1. Estructura/Etiquetas](#1-estructura-y-etiquetas)

- [2. Patrones generales](#2-patrones)

- [3. Análisis Exploratorio de Datos (EDA)](#3-análisis-exploratorio-de-datos-eda)

- [4. Cambios ejecutados](#4-cambios-ejecutados)

- [5. Nuestras cuestiones sobre los datos](#5-nuestras-cuestiones-sobre-los-datos)

- [6. Visualización como respuesta](#6-visualización-como-respuesta:)

## 1. Estructura y etiquetas

Los [datos proporcionados](Análisis_y_transformación_datos\raw_data.csv) para el proyecto de análisis presenta índices como columnas:

- [Age](#age) F
- [Attrition](#attrition) ✔
- [Business Travel](#businesstravel) ✔
- [Daily Rate](#dailyrate) ✔
- [Department](#department) NaN
- [Distance From Home](#distancefromhome) F
- [Education](#education) ✔
- [Education Field](#educationfield) NaN
- [Employee Count](#employeecount) <font color="green">♻</font>
- [Employee Number](#employeenumber) ✔
- [Environment Satisfaction](#environmentsatisfaction) Por reflexionar (formato)
- [Gender](#gender)
- [Hourly Rate](#hourlyrate) NaN por calcular
- [Job Involvement](#jobinvolvement) Por reflexionar (formato)
- [Job Level](#joblevel) ✔
- [Job Role](#jobrole) NaN
- [Job Satisfaction](#jobsatisfaction) Por reflexionar (formato)
- [Marital Status](#maritalstatus) NaN
- [Monthly Income](#monthlyincome) NaN por calcular
- [Monthly Rate](#monthlyrate) Nan por calcular
- [Number of Companies Worked](#numcompaniesworked) ✔
- [Over 18](#over18) <font color="green">♻</font>
- [Overtime](#overtime) NaN
- [Percent Salary Hike](#percentsalaryhike) ✔
- [Performance Rating](#performancerating) NaN
- [Relationship Satisfaction](#relationshipsatisfaction) A reflexionar
- [Standard Hours](#standardhours) ✔
- [Stock Option Level](#stockoptionlevel) ✔
- [Total Working Years](#totalworkingyears)
- [Training Times Last Year](#trainingtimeslastyear) ✔
- [Work Life Balance](#worklifebalance) NaN
- [Years at Company](#yearsatcompany) ✔
- [Years in Current Role](#yearsincurrentrole) NaN
- [Years Since Last Promotion](#yearssincelastpromotion) ✔
- [Years with Current Manager](#yearswithcurrmanager) ✔
- [Same as Monthly Income](#sameasmonthlyincome) <font color="green">♻</font>
- [Date of Birth](#datebirth) ✔
- [Salary](#salary) NaN por calcular
- [Role Department](#roledepartament) <font color="green">♻</font>
- [Number of Children](#numberchildren) <font color="green">♻</font>
- [Remote Work](#remotework) F

---

## 2. Patrones

|       Tipo | Descripción |
| ----------- | ----------- |
| Generales     | Datos personales anonimizados sobre empleados (edad, rango, departamento, género, tipo de contrato...), con presencia de valores nulos.<br><br> Escalas de valoración (ambiente laboral, satisfacción con el trabajo) sin estandarizar (0-5, 0-50).<br><br> Columnas duplicadas (1).<br><br> Filas con valores duplicados en toda su serie de columnas.|
| Valores nulos   | Distribución dispersa de valores nulos en general.<br><br> Columnas que contienen únicamente valores nulos (1).<br><br> Valores nulos en columnas atribuidas a conceptos salariales.|
Valores objeto | Entradas de escritura irregular (alternan aleatoriamente mayúsculas y minúsculas)<br><br> Valores que se agrupan indebidamente por errores ortográficos.<br><br> Espaciado extra|
Valores numéricos | Valores numericos relativos a información salarial junto a símbolos de divisa: ``$``, que impide realizar cálculos con ellos.<br><br> Presentan ``,`` en su formato, que dificulta el procesamiento de los datos, en lugar de ``.``.<br><br> Formato negativo para expresar distancias.

nulos para apuntar en otro lado: pero su distribución admite el cálculo del valor faltante relacionando las cantidades presentes en las otras columnas.

---

## 3. Análisis Exploratorio de Datos (EDA)

### age

| Tipo | Indica Edad del empleado|
| ----------- | ----------- |
| dtype: object | 35ㅤ5.24<br>31ㅤ5.24<br>34ㅤ5.13<br>29ㅤ4.89<br>36ㅤ4.71<br>32ㅤ3.93<br>30ㅤ3.87<br>38ㅤ3.81<br>33ㅤ3.75<br>(...)<br>43ㅤ2.50<br>fifty-fiveㅤ0.06<br>twenty-sixㅤ0.06<br>thirty-sevenㅤ0.06.<br><br> Valores únicos: **54**<br>Número de registros: **1678**|
---
ㅤ     
**Propuesta de mejora:**

       Homogeneizar al mismo formato numérico, float o int.

**Propuestas ejecutadas:**

- ?

---
---

### attrition

| Tipo | Indica si el empleado dejó la empresa (Yes/No) |
| ----------- | ----------- |
| dtype: object |Noㅤ83.79<br>Yesㅤ16.21<br><br>Valores únicos: **2**<br>Número de registros: **1678**.|

---
ㅤ     
Sin anomalías. Mantener sin cambios.
ㅤ     

---
---

### businesstravel

|  Tipo  |   Indica Frecuencia de viajes   |
| ----------- | ----------- |
| dtype: object | NaNㅤㅤㅤㅤㅤㅤ 47.74<br>travel_rarelyㅤㅤㅤ36.71<br>travel_frequentlyㅤ10.01<br>non-travelㅤㅤㅤㅤ 5.54<br><br>Valores únicos: **3**<br>Número de registros: **1678**|

---
ㅤ     
**Nota:**     
Comprobar si el ``NaN`` tiene más valores ``NaN`` asociados al mismo empleado.

**Propuesta de mejora:**

       Sustituir NaN por non-travel, según la información proporcionada por el PO.
ㅤ     
**Propuesta ejecutada:**

- Se ha sustituido (**2**) valores ``NaN`` por ``non-travel``.
ㅤ     
ㅤ     
---
---

### dailyrate

|    Tipo  |   Tarifa diaria estimada para clientes, calculada en base al salario   |
| ----------- | ----------- |
| dtype: int64 | 556.256661ㅤㅤ19.43<br>290.035510ㅤㅤ18.36<br>1032.487286ㅤㅤ8.94<br>1582.771346ㅤㅤ3.28<br>1973.984127ㅤㅤ2.26<br>(...)<br>531.452381ㅤㅤ  0.06<br>295.388889ㅤㅤ 0.06<br>294.873016ㅤㅤ 0.06<br>116.484127ㅤㅤ 0.06<br><br>Valores únicos: **673**<br>Número de registros: **1678**|

---
ㅤ     
**Propuesta de mejora:**

       Usar round() para estandarizar la precisión.
       
Asegurarse de aplicar el mismo criterio a todas las columnas numéricas relativas al salario en el dataset (puntuación y redondeo).

**Propuesta ejecutada:**

- Sustitución de ``,`` por ``.``.
- Redondeado a dos decimales.
- Calcular datos faltantes.

ㅤ

---
---

### department

|    Tipo  |  Departamento donde trabaja el empleado   |
| ----------- | ----------- |
| dtype: object | NaNㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ 81.41<br>Research & Developmentㅤ12.10<br>Sales ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ 5.54<br>Human Resourcesㅤㅤㅤㅤㅤ0.95<br><br>Valores únicos: **3**<br>Número de registros: **1678**|
---
ㅤ     
**Propuesta de mejora:**

       > Estandarizar a minúculas todos los nombres.
 
       > Comparar los valores nulos con las columnas que incluyen datos aparentemente reiterados, pueden contener este valor en ausencia de estar presentes en esta columna.

Columna referenciada: [roledepartament](#roledepartment)

       > Sustituir espacios innecesarios al inicio, final y entre las palabras del valor (' Human Resources ') por valores estandarizados y sin espacios innecesarios.
ㅤ
Dados los pocos departamentos que hay, inferiremos el valor de los nulos de la relación entre los valores presentes y los valores de la columna [jobrole](#jobrole).

**Propuesta ejecutada:**

- Estandarización: formato letras minúsculas.
- El espaciado extra ha sido eliminado.
- Incluimos información en ``department``, en función a los valores de la columna ``jobrole``
- Modificamos ``NaN`` por ``Desconocido``.

---
---

### distancefromhome

|    Tipo  |   Distancia en millas o kilómetros desde el hogar al trabajo   |
| ----------- | ----------- |
| dtype: int64 | 2 ㅤ 13.59<br>1 ㅤ 12.46<br>9ㅤㅤ5.30<br>10 ㅤ 5.13<br>8ㅤㅤ5.07<br>-21ㅤ0.12<br>-43ㅤ0.12<br>-28ㅤ0.12<br>-39ㅤ0.06<br>-40ㅤ0.06 <br><br> Valores únicos: **69**<br>Número de registros: **1678**|
---
ㅤ     
**Propuesta de mejora:**

       Convertimos en absolutos para eliminar valores numéricos negativos.

**Propuesta ejecutada:**

       Sin ejecución.
---
---

### education

(dtype: int64)
*Nivel educativo del empleado en escala numérica*
|    Tipo   |   Nivel educativo del empleado en escala numérica  |
| ----------- | ----------- |
| dtype: int64| 3ㅤ38.68<br>4ㅤ27.47<br>2ㅤ19.19<br>1ㅤ11.08<br>5ㅤ3.58<br><br> Valores únicos: **5**<br>Número de registros: **1678**|

Sin anomalías. Mantener sin cambios.

⚑ Incluir en un glosario el significado de la escala de valores.

---
---

### educationfield
|    Tipo   |   Campo académico del empleado   |
| ----------- | ----------- |
| dtype: object | NaNㅤㅤㅤㅤㅤㅤㅤ46.13<br>Life Sciences ㅤㅤㅤ 21.87<br>Medical ㅤㅤㅤㅤㅤ 17.04<br>Marketing ㅤㅤ ㅤㅤ  6.32<br>Technical Degreeㅤㅤ4.17<br>Otherㅤㅤㅤㅤㅤㅤㅤ3.75<br>Human Resources ㅤ 0.72 <br><br> Valores únicos: **6**<br>Número de registros: **1678**|
---
ㅤ     
**Propuesta de mejora:**

       > Estandarizar a minúculas todos los nombres.

       > Comparar los valores nulos con las columnas que incluyen datos aparentemente reiterados, pueden contener este valor en ausencia de estar presentes en esta columna.

Columna referenciada: [department](#department).

**Propuestas ejecutadas:**

- Las letras minúsculas ahora son el estándar.
- El espaciado extra ha sido eliminado.

---
---

### employeecount
|    Tipo   | Valor constante de ``1``, indicando un solo empleado por registro  |
| ----------- | ----------- |
| dtype: int64| 1ㅤㅤ100.0 <br><br> Valores únicos: **1**<br>Número de registros: **1678**|
---
ㅤ     
Este campo es redundante, cada registro corresponde a un único empleado (valor siempre igual a 1).

**Propuesta de mejora:**

       Eliminar columna

**Propuestas ejecutadas:**

- ?

---
---

### employeenumber
|    Tipo   |   Identificación del empleaㅤㅤdo   |
| ----------- | ----------- |
| dtype: int64 |528ㅤㅤ0.12<br>300ㅤㅤ0.12<br>168ㅤㅤ0.12<br>644ㅤㅤ0.12<br>271ㅤㅤ0.12<br>(...)<br>1594ㅤㅤ0.06<br>1595ㅤㅤ0.06<br>1596ㅤㅤ0.06<br>1597ㅤㅤ0.06<br>1614ㅤㅤ0.06 <br><br>Valores únicos: **1614**<br>Número de registros: **1678**<br><br>Registros duplicados: **64**|
---

ㅤㅤ   
**Propuesta de mejora:**

       > Consultar la presencia de valores nulos al PO.

       > Gestión de duplicados.

**Propuestas ejecutadas:**

- ?

---

### environmentsatisfaction

|    Tipo   |   Nivel de satisfacción con el ambiente laboral   |
| ----------- | ----------- |
| dtype: int64 |4ㅤㅤ28.50<br>3ㅤㅤ28.44<br>1ㅤㅤ18.46<br>2ㅤㅤ18.40<br>12ㅤㅤ0.43<br>35ㅤㅤ0.37<br>13ㅤㅤ0.37<br>24ㅤㅤ0.31<br>47ㅤㅤ0.31<br>14ㅤㅤ0.31<br>41ㅤㅤ0.25<br>42ㅤㅤ0.25<br>46ㅤㅤ0.25<br>36ㅤㅤ0.25<br>48ㅤㅤ0.25<br>20ㅤㅤ0.19<br>22ㅤㅤ0.19<br>11ㅤㅤ0.19<br>18ㅤㅤ0.19<br>45ㅤㅤ0.19<br>(...)<br>10ㅤㅤ0.06<br>26ㅤㅤ0.06<br>43ㅤㅤ0.06<br><br> Valores únicos: **38**<br>Número de registros: **1614** |
---
ㅤㅤ   
**Propuesta de mejora:**

       > Plantearnos si podemos igualar el rango de la escala al resto de escalas de valoración que tenemos, por ejemplo: 
       
       Decidir acortar las distancias entre 0 y 50 pasándolos a float entre 0-5 (0.1, 0.3, 0.4... 3.3, 4.5, 4.9)

**Propuestas ejecutadas:**

- ?

---
---

### gender

|    Tipo   |   Género asignado del empleado   |
| ----------- | ----------- |
| dtype: int64 | 0ㅤㅤ60.13<br>1ㅤㅤ9.87<br><br> Valores únicos: **2**<br>Número de registros: **1678** |
---
ㅤㅤ   
No está documentado qué significa cada valor (ej: 0 = Femenino, 1 = Masculino)

ㅤㅤ   
**Propuesta de mejora:**

       > Definir explícitamente el significado de cada valor.

       > Consultar las referencias con PO.

**Nota:**     
No incluye opciones no binarias o diversidad de género, podría ser interesante que se pudieran añadir más valores y tenerlo en cuenta de cara a la presentación como next steps/sugerencias para la empresa.


**Propuestas ejecutadas:**

- 0, másculino. 1, femenino.

---
---

### hourlyrate

|    Tipo   |   Tarifa por hora calculada   |
| ----------- | ----------- |
| dtype: float64 | NaNㅤㅤㅤㅤ75.51<br>36.254439ㅤㅤ4.53<br>69.532083ㅤㅤ4.47<br>129.060911 ㅤ 2.44<br>197.846418     0.83<br>(...)<br>108.230159     0.06<br>247.477183     0.06<br>67.424603      0.06<br>34.821429      0.06<br>133.159722     0.06 <br><br> Valores únicos: **194**<br>Número de registros: **1678** |
---

ㅤㅤ   

La mayor parte de los valores son nulos. ¿Es un error de recolección o hay empleados sin tarifa asignada?

Los valores tienen hasta 10 decimales (ej: 69.53208262).

ㅤㅤ   
**Propuesta de mejora:**

       > Redondear a 2 decimales (estándar para monedas).

       > Compararlo con el nivel del puesto.

       > Inferir valor de nulos calculando el 'hourlyrate' = 'dailyrate' /8.

ㅤㅤ   
**Propuestas ejecutadas:**

- Calculo de valores faltantes

---

### jobinvolvement

(dtype: int64)
*Nivel de compromiso del empleado en el trabajo*

       Valores = array([3, 2, 4, 1])

Mantener sin cambios.

O:

       NOTA: como next steps, poder definir y documentar explícitamente el significado de cada valor: 
       ej: 1: 'Bajo compromiso',
       2: 'Compromiso moderado',
       3: 'Compromiso alto',
       4: 'Compromiso excepcional'

¿Incluimos 0 y 5 en la escala aunque no aparezcan en la recolección de puntuaciones?

Podemos dejarlo perfectamente como está e incluir un GLOSARIO en el que se indiquen las equivalencias.

---

### joblevel

(dtype: int64)
*Nivel jerárquico del puesto del empleado*

       Valores = array([5, 4, 3, 2, 1])

Sin anomalías.

- ¿Incluimos sus equivalencias en glosario?

---

### jobrole

(dtype: object)
Función o rol específico del empleado

       Valores = array([' resEArch DIREcToR ', ' ManAGeR ', ' ManaGER ', ...,
       ' sAlES ExECUTivE ', ' SaLes ExecUtIVe ',
       ' mAnUfactURInG DiRECTOr '], dtype=object)

Objetos como valores con escritura irregular.

Propuesta de mejora:

- Convertir a minuscula todos los nombres
``df["jobrole"] = df["jobrole"].str.lower()``

       Ejemplo:
       array([' research director ', ' manager ', ' sales executive ',
       ' manufacturing director ', ' research scientist ',
       ' healthcare representative ', ' laboratory technician ',
       ' sales representative ', ' human resources ']

- Eliminar espaciado innecesario entre palabras.

Propuestas ejecutadas:

- Estandarización: formato letras minúsculas.
- El espaciado extra ha sido eliminado.

---

### jobsatisfaction

(dtype: int64)
*Satisfacción general en el puesto*

       Valores = array([3, 4, 1, 2])

Mantener sin cambios.  

O:

       NOTA: como next steps, poder definir y documentar explícitamente el significado de cada valor: 
       ej: 1: 'Insatisfecho',
       2: 'Poco satisfecho',
       3: 'Satisfecho',
       4: 'Muy satisfecho'

¿Incluimos 0 y 5 en la escala aunque no aparezcan en la recolección de puntuaciones?

Podemos dejarlo perfectamente como está e incluir un GLOSARIO en el que se indiquen las equivalencias.

---

### maritalstatus

(dtype: object)
*Estado civil (e.g., Single, Married)*

       Values total 1678 | Unique 5 + NaN | dtype - objects. (incluye NaN - 675 - muchos) Null - TBD

              NaN         675
              Married     419
              Single      343
              Divorced    194
              Marreid      36
              divorced     11

Propuesta de mejora:

- lower() todos
´´df["maritalstatus"] = df["maritalstatus"].str.lower()´´
- replace ``Marrieid`` por ``Married``
``df["maritalstatus"] = df["maritalstatus"].str.replace("marreid", "married")``
- Null - TBD

Propuestas ejecutadas:

- Estandarización: formato letras minúsculas.
- Sustituidas incorrecciones ortográficas.

---

### monthlyincome

(dtype: object)
*Ingreso mensual estimado en base al salario anual*

       Values U1678 | Unique 493 + NaN | dtype - int. (incluye NaN - 498 - muchos) |  **Null - TBD**

              muestra de valores:
              NaN          489
              2342,59$     228
              4492,84$     227

Propuesta de mejora:

- Usar ``replace()`` ``,`` por ``.`` y usar ``replace()`` ``$`` por ``""``:
``df["monthlyincome"] = df["monthlyincome"].str.replace("$", "", regex=False).str.replace(",", ".", regex=False)``

       -->regex false - pandas puede pensar que es una funcion regex
- Cambiar a numérico de tipo float:
``df["monthlyincome"] = df["monthlyincome"] = pd.to_numeric(df["monthlyincome"], errors="coerce")``

       --> errors="coerce" asegura que, si no se cumple, convierte en NaN
       
       ie. 40 esta como 'forty'
              muestra monthlyincome limpio:
              0       16280.83
              1            NaN
              2            NaN
              3       14307.50
              4       12783.92

- Relleno de nulos = 'monthlyincome = salary / 12'

Propuestas ejecutadas:

- Calculo de valores faltantes

---

### monthlyrate

(dtype: object)
*Tarifa mensual estimada en función de la tarifa diaria*

       Values 1678 | Unique 673 | NaN 0 | dtype Object  

Propuesta de mejora:

- Mismo que en ``monthlyincome``
``df["monthlyrate"] = df["monthlyrate"].str.replace("$", "", regex=False).str.replace(",", ".", regex=False)``

       -->regex false - pandas puede pensar que es una funcion regex
- ``df["monthlyrate"] = df["monthlyrate"] = pd.to_numeric(df["monthlyrate"], errors="coerce")``

       --> errors="coerce" asegura que si no se cumple convierte en NaN
       
       ie. 40 esta como 'forty'

### numcompaniesworked

(dtype: int64)
*Número de empresas previas en las que ha trabajado*

       Valores = array([7, 0, 1, 3, 2, 4, 8, 9, 5, 6])

       Values 1678 | Unique 10 (0-9) | NaN 0 | dtype int

- Entendemos que son empleos en compañías anteriores.

De cara al volcado a SQL:

- ¿Igual podemos llamarlo experiencia previa en empresas? ¿Score empleos previos?

---

### over18

(dtype: object)
*columna no definida*

       Valores = array(['Y', nan], dtype=object)

       Values 1678 | dtype Object | Unique 1 | NaN 1 (938 valores NaN -- muchos, la mayoria)

No existe valor N (No), solo Y (Yes) o NaN.

Interpreto que es muy incompleto, con 56% NaN, para darle peso en el analysis global.

       Muestra de valores y counts:
       NaN    938
       Y      740

Propuesta de mejora:

- Gestión de nulos.
- Inferir que los nulos, en ausencia de No, pueden tener ese valor.
- Consultar con nuestro enlace de proyecto, Pilar.

---

### overtime

(dtype: object)
*Indica si el empleado trabaja horas extras (Yes/No)*

       Valores = array(['No', nan, 'Yes'], dtype=object)

Propuesta de mejora:

- Gestión de nulos.
- ¿Atribuir ``NaN`` como ``Desconocido`` y darle valor a la información de quien tiene un claro Yes?
- Consultar con nuestro enlace de proyecto, Pilar.

Propuestas ejecutadas:

- Cambio ``nan`` por ``unknown``

---

### percentsalaryhike

(dtype: int64)
*Incremento porcentual en el salario*

       Valores = array([13, 14, 11, 19, 12, 25, 16, 17, 22, 23, 20, 15, 21, 24, 18])

Propuesta de mejora:
Mantener sin cambios.

---

### performancerating

(dtype: object)
*Evaluación de desempeño en una escala numérica*

       Valores = array(['3,0', '4,0', nan], dtype=object)

Propuesta de mejora:

- Reemplazar ``,`` por ``.``:
``df["performancerating"] = df["performancerating"].str.replace(',', '.')``
- Rellenar los vacíos con 0:
``df["performancerating"] = df["performancerating"].fillna(0)``
- Convertir a float:
``df["performancerating"] = df["performancerating"].astype(float)``

       Ejemplo:
       array([3., 4., 0.]) // dtype('float64')

- Otra sugerencia: para evitar que el nuevo valor ``0`` baje la media del *performance rating*, sustituir por ``Desconocido``.

---

### relationshipsatisfaction

(dtype: int64)
*Satisfacción con relaciones interpersonales en el trabajo*

       Valores = array([3, 1, 4, 2])

Propuesta de mejora:
Mantener sin cambios.  

O:

       NOTA: como next steps, poder definir y documentar explícitamente el significado de cada valor: 
       1: 'Insatisfecho',
       2: 'Poco satisfecho',
       3: 'Satisfecho',
       4: 'Muy satisfecho'

¿Incluimos 0 y 5 en la escala aunque no aparezcan en la recolección de puntuaciones?

Podemos dejarlo perfectamente como está e incluir un GLOSARIO en el que se indiquen las equivalencias.

---

### standardhours

(dtype: object)
*Clasificación de jornada (Full Time/Part Time)*

       Valores = array(['Full Time', nan, 'Part Time'], 
       dtype=object)

Faltan valores: ``NaN``.
standardhours tiene 927 'part time', 400 full time y 351 nulos
-por qué faltan las horas estándar a 351 registros?
-error de registro? categoría ausente para alguna trabajadora?
-dependiendo de lo que sea: 1)Reemplazar nulos por otra catergoría 'desconocido'; 2)Eliminar nulos

Propuesta de mejora:

- Mirar la relacion con otras columnas para asegurarnos si el nulo es por falta de informacion, o por otro tipo de clasificacion de jornada (ej: 'Freelance'?, 'Otro', 'No Especificado'). EJ:
 ``df['standardhours'] = df['standardhours'].replace(np.nan, 'No especificado')``
 ``df['standardhours'] = df['standardhours'].str.lower()`` # convertir todo a minúsculas para normalizar todas categorías

Propuestas ejecutadas:

- Cambio de ``nan`` a ``full time``

---

### stockoptionlevel

(dtype: int64)
*Nivel de opciones sobre acciones asignadas.*

       Valores numéricos ([0, 1, 2, 3])

Propuesta de mejora:
Mantener sin cambios.

---

### totalworkingyears

(dtype: object)
*Años totales de experiencia laboral*

       Valores = array([nan, '34,0', '22,0', '28,0', '20,0', '21,0', '33,0', '40,0',
       '18,0', '25,0', '15,0', '17,0', '26,0', '16,0', '24,0', '14,0',
       '23,0', '27,0', '19,0', '11,0', '38,0', '37,0', '13,0', '12,0',
       '29,0', '10,0', '36,0', '35,0', '9,0', '31,0', '32,0', '8,0',
       '7,0', '30,0', '6,0', '5,0', '4,0', '3,0', '2,0', '1,0', '0,0'],
      dtype=object)

Propuesta de mejora:

- Reemplazar ``,`` por ``.``
``df["totalworkingyears"] = df["totalworkingyears"].str.replace(',', '.')``
- Posibilidad de cambiar a 0 Gestión de nulos:
``df["totalworkingyears"] = df["totalworkingyears"].fillna(0)``
- Convertir a float:
``df["totalworkingyears"] = df["totalworkingyears"].astype(float)``

       Resultado: array([ 0, 34, 22, 28, 20, 21, 33, 40, 18, 25, 15, 17, 26, 16, 24, 14, 23, 27, 19, 11, 38, 37, 13, 12, 29, 10, 36, 35,  9, 31, 32,  8,  7, 30, 6,  5,  4,  3,  2,  1])

- Comprobar si el nulo en años de experiencia laboral es dispar con la columna [numcompaniesworked](#numcompaniesworked). Está comprobado y la conclusión es: dejar los valores nulos y los datos float

---

### trainingtimeslastyear

(dtype: int64)
*Número de sesiones de entrenamiento en el último año.*

       Valores numéricos ([5, 3, 2, 0, 1, 4, 6])

Sin anomalías.

---

### worklifebalance

(dtype: object)
*Nivel de balance entre vida personal y laboral.*

       Valores = array(['3,0', nan, '2,0', '4,0', '1,0'], dtype=object)
Hay 114 nulos

Propuesta de mejora:

- Reemplazar la ``,`` por ``.``:
``df["worklifebalance"] = df["worklifebalance"].str.replace(',', '.')``
- Gestión de nulos
- Posibilidad de cambiar a 0 Gestión de nulos:
``df["worklifebalance"] = df["worklifebalance"].fillna(0)``
- Convertir a float:
``df["worklifebalance"] = df["worklifebalance"].astype(float)``
- Ahora sí, pasar a entero sin miedo:
``df["worklifebalance"] = df["worklifebalance"].astype(int)``

       Resultado: array([3, 0, 2, 4, 1])

---

### yearsatcompany

(dtype: int64)
*Años en la empresa actual.*

       Valores = array([20, 33, 22, 19, 21, 18, 24, 31, 26, 16, 23, 15, 17, 32, 14, 13, 25, 12, 11, 37, 40, 36, 27, 29, 10,  9, 30,  8,  7, 34,  6,  5,  4,  2, 3,  1,  0])

Sin anomalías.

- Sería interesante comparar los años en la empresa actual con los valores nulos en la columna [totalworkingyears](#numcompaniesworked) para comprobar qué relato/perfil nos devuelve.

---

### yearsincurrentrole

(dtype: object)

       Valores = array([nan, '13,0', '12,0', '11,0', '7,0', '6,0', '4,0', '3,0', '2,0',
       '1,0', '0,0'], dtype=object)
Hay 1643 nulos

Propuesta de mejora:

- Reemplazar la ``,`` por ``.``:
``df["yearsincurrentrole"] = df["yearsincurrentrole"].str.replace(',', '.')``
- Rellenar los vacíos con 0
``df["yearsincurrentrole"] = df["yearsincurrentrole"].fillna(0)``
- Convertir a float:
``df["yearsincurrentrole"] = df["yearsincurrentrole"].astype(float)``
-Ahora sí, pasar a entero sin miedo:
``df["yearsincurrentrole"] = df["yearsincurrentrole"].astype(int)``

       Resultado:
       array([ 0, 13, 12, 11,  7,  6,  4,  3,  2,  1])
  
---

### yearssincelastpromotion

(dtype: int64)

       Valores = [15, 11,  5,  2,  4,  7,  0,  1, 13, 14,  8, 12,  3,  6, 10,  9]

Mantener sin cambios.

---

### yearswithcurrmanager

(dtype: int64)
*Años trabajando con el mismo gerente.*

       Valores = [15,  9,  6,  8,  7, 11, 10, 12,  4,  0,  5, 17,  2, 14,  1, 13,  3, 16]

Mantener sin cambios.

---

### sameasmonthlyincome

(dtype: object)
*columna sin especificar*

       Valores = Datos tipo objeto, con simbolo en "Español" para los decimales y además incluido en el dato el simbolo $

Propuesta de mejora:

- Cambiar la ``,`` por ``.``, eliminar también el simbolo ``$``. Por último cambiar el valor objeto a float

``df["sameasmonthlyincome"] = df["sameasmonthlyincome"].str.replace(',', '.')``

``df["sameasmonthlyincome"] = df["sameasmonthlyincome"].str.replace('$', '', regex=False)``

``df["sameasmonthlyincome"] = df["sameasmonthlyincome"].astype(float)``

- Comprobar si esta columna es una copia redundante de [monthlyincome](#monthlyincome), si en efecto lo es, eliminar.

Propuestas ejecutadas:

- Eliminación de columna

---

### datebirth

(dtype: int64)
*Año de nacimiento del empleado*

       Valores = [1972, 1971, 1981, 1976, 1977, 1975, 1964, 1982, 1967, 1985, 1968, 1983, 1965, 1988, 1978, 1990, 1987, 1989, 1970, 1980, 1963, 1991, 1986, 1974, 1984, 1973, 1979, 1993, 1994, 1992, 1969, 1966, 1996, 1995, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005]

Sin anomalías.

---

### salary

(dtype: object)
*Salario anual calculado para el empleado*

       Valores = Datos tipo objeto, con simbolo en "Español" para los decimales y además incluido en el dato el simbolo $

Propuesta de mejora:

- Cambiar la ``,`` por ``.``, eliminar también el simbolo ``$``. Por último cambiar el valor tipo objeto a float

``df["salary"] = df["salary"].str.replace(',', '.')``

``df["salary"] = df["salary"].str.replace('$', '', regex=False)``

``df["salary"] = df["salary"].astype(float)``

- Relleno de nulos = 'salary = monthlyincome * 12'

Propuestas ejecutadas:

- Calculo de valores faltantes

---

### roledepartament

(dtype: object)
*Combinación de rol y departamento.*

       Valores = array([nan, ' manager  -  research & development ',
       ' healthcare representative  -  research & development ',
       ' sales executive  -  sales ',
       ' laboratory technician  -  research & development ',
       ' manufacturing director  -  research & development ',
       ' research scientist  -  research & development ',
       ' research director  -  research & development ',
       ' human resources  -  human resources ', ' manager  -  sales ',
       ' sales representative  -  sales ',
       ' manager  -  human resources '], dtype=object)

Propuesta de mejora:

- df["roledepartament"] = df["roledepartament"].str.lower()

       [nan, ' manager  -  research & development ',
       ' healthcare representative  -  research & development ',
       ' sales executive  -  sales ',
       ' laboratory technician  -  research & development ',
       ' manufacturing director  -  research & development ',
       ' research scientist  -  research & development ',
       ' research director  -  research & development ',
       ' human resources  -  human resources ', ' manager  -  sales ',
       ' sales representative  -  sales ',
       ' manager  -  human resources ']

- ¿Comprobar si esta columna es redundante o si contiene los datos que faltan en [department](#department) y [jobrole](#jobrole)?
- ¿Destinarla a eliminación una vez reubicados todos los valores?
- Hemos realizado comparación y determinamos que la columna debe ser eliminada.

Propuestas ejecutadas:

- Eliminación de columna

---

### numberchildren

(dtype: float64)
*Número de hijos del empleado*

       Valores = [nan]

Propuesta de mejora:

- Posible columna a eliminar.
- Incluir comentarios para MySQL

Propuestas ejecutadas:

- Eliminación de columna

---

### remotework

(dtype: object)
*Indica si el empleado trabaja de forma remota (Yes/No).*

       Valores =[ 'Yes', '1', 'False', '0', 'True']

Todos son objetos aunque haya número de por medio. Quizás el 0 signifique Si/Yes y el 1 signifique No. También es posible que el True sea igual a Si/Yes y el False sea No

Propuesta de mejora:

- Unificar datos.

## 4. Cambios ejecutados

       Hipervínculo + parte crucial del código que soluciona
       Y así sucesivamente

---

## 5. Nuestras cuestiones sobre los datos

*Presentación de preguntas de Patri + enfoque de Andrea*

---

## 6. Visualización como respuesta

**A continuación, la información que hemos obtenido en consecuencia:**

       Visualizaciones 