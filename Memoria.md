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

- [Age](#age)
- [Attrition](#attrition)
- [Business Travel](#businesstravel)
- [Daily Rate](#dailyrate)
- [Department](#department)
- [Distance From Home](#distancefromhome)
- [Education](#education)
- [Education Field](#educationfield)
- [Employee Count](#employeecount)
- [Employee Number](#employeenumber)
- [Environment Satisfaction](#environmentsatisfaction)
- [Gender](#gender)
- [Hourly Rate](#hourlyrate)
- [Job Involvement](#jobinvolvement)
- [Job Level](#joblevel)
- [Job Role](#jobrole)
- [Job Satisfaction](#jobsatisfaction)
- [Marital Status](#maritalstatus)
- [Monthly Income](#monthlyincome)
- [Monthly Rate](#monthlyrate)
- [Number of Companies Worked](#numcompaniesworked)
- [Over 18](#over18)
- [Overtime](#overtime)
- [Percent Salary Hike](#percentsalaryhike)
- [Performance Rating](#performancerating)
- [Relationship Satisfaction](#relationshipsatisfaction)
- [Standard Hours](#standardhours)
- [Stock Option Level](#stockoptionlevel)
- [Total Working Years](#totalworkingyears)
- [Training Times Last Year](#trainingtimeslastyear)
- [Work Life Balance](#worklifebalance)
- [Years at Company](#yearsatcompany)
- [Years in Current Role](#yearsincurrentrole)
- [Years Since Last Promotion](#yearssincelastpromotion)
- [Years with Current Manager](#yearswithcurrmanager)
- [Same as Monthly Income](#sameasmonthlyincome)
- [Date of Birth](#datebirth)
- [Salary](#salary)
- [Role Department](#roledepartament)
- [Number of Children](#numberchildren)
- [Remote Work](#remotework)

---

## 2. Patrones

|  Generales  |
| ----------- |
| Datos personales anonimizados sobre empleados (edad, rango, departamento, género, tipo de contrato...), con presencia de valores nulos.
|Escalas de valoración (ambiente laboral, satisfacción con el trabajo) sin estandarizar (0-5, 0-50).
|Columnas duplicadas (1).
|Columnas que contienen únicamente valores únicos (1).
|Filas con valores duplicados en toda su serie de columnas.|

---
---
ㅤ     

|  Valores nulos  |
| ----------------|
|Distribución dispersa de valores nulos en general.
|Valores nulos en columnas atribuidas a conceptos salariales.
|Nulos cuya distribución admite el cálculo del valor faltante relacionando las cantidades presentes en las otras columnas.|

---
---
ㅤ     


|  Valores Objeto |
| ----------------|
| Entradas de escritura irregular (alternan aleatoriamente mayúsculas y minúsculas).
|Valores que se agrupan indebidamente por errores ortográficos.
|Espaciado extra|

---
---
ㅤ     

| Valores Numéricos |
| ------------------|
| Valores numericos relativos a información salarial junto a símbolos de divisa: ``$``, que impide realizar cálculos con ellos.
|Presentan ``,`` en su formato, que dificulta el procesamiento de los datos, en lugar de ``.``
| Formato negativo para expresar distancias.

---
---

ㅤ     

## 3. Análisis Exploratorio de Datos (EDA)

### age

|    dtype: object  |   Índica la edad del empleado   |
|-----------|---------------|
||
||**Top 5:**
||35  ㅤㅤ5.24%
||31  ㅤㅤ5.24%
||34  ㅤㅤ5.13%
||29  ㅤㅤ4.89%
||36  ㅤㅤ4.71%
||<br>
||**Bottom 5:**
||thirty-one  0.06%
||thirty  ㅤㅤ0.06%
||fifty-fiveㅤ0.06%
||twenty-six  0.06%
||thirty-seven  0.06%
||<br>
||**Media:** 36.94
||**Mediana:** 36.0
||**Moda:** 31.0
||<br>
||Valores únicos: **54**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **1624**|
---
ㅤ     
ㅤ
**Propuesta de mejora:**

       Homogeneizar al mismo formato numérico, float o int.

ㅤ     
**Propuestas ejecutadas:**

- Se ha estandarizado a valores numéricos enteros.

ㅤ     
---
---

### attrition

|    dtype: object  |   Indica si el empleado dejó la empresa (Yes/No)   |
|-----------|---------------|
||
||No  ㅤㅤㅤ83.79
||Yes  ㅤㅤㅤ16.21
||<br>
||<br>
||Valores únicos: **2**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **1676**|
---

ㅤ     
Sin anomalías. Mantener sin cambios.
ㅤ

---
---

### businesstravel

|    dtype: object  |   Indica frecuencia de viajes  |
|-----------|---------------|
||
||NaN  ㅤㅤㅤㅤㅤㅤ47.74
||travel_rarelyㅤㅤㅤ36.71
||travel_frequentlyㅤ10.01
||non-travelㅤㅤㅤㅤ5.54
||<br>
||<br>
||Valores únicos: **3**
||Número de registros: **1678**
||Valores nulos: **801**
||Registros duplicados: **1675**|
---

ㅤ     
**Nota:**     
Comprobar si estos valores nulos tienen más valores nulos asociados al mismo empleado.

**Propuesta de mejora:**

       > Sustituir 'NaN' por 'non-travel', según la información proporcionada por el PO.
ㅤ
**Propuesta ejecutada:**

- Se han sustituido (**801**) valores ``NaN`` por ``non-travel``.

ㅤ     


---
---

### dailyrate

|    dtype: float64  |   Tarifa diaria estimada para clientes, calculada en base al salario    |
|-----------|---------------|
||
||**Top 5:**
||556.2566609977324  19.43%
||290.03550973654063  18.36%
||1032.4872861766066  8.94%
||1582.7713464696226  3.28%
||1973.9841269841268  2.26%
||<br>
||**Bottom 5:**
||531.452380952381  0.06%
||295.3888888888889  0.06%
||294.8730158730159  0.06%
||116.484126984127  0.06%
||1108.920634920635  0.06%
||<br>
||**Media:** 668.07
||**Mediana:** 556.25
||**Moda:** 556.25
||<br>
||Valores únicos: **673**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **1005**|
---
ㅤ
**Propuesta de mejora:**

       Usar round() para estandarizar la precisión.
       
Asegurarse de aplicar el mismo criterio a todas las columnas numéricas relativas al salario en el dataset (puntuación y redondeo).

**Propuesta ejecutada:**

- Sustitución de ``,`` por ``.``.
- Redondeado a dos decimales.

ㅤ

---
---

### department

|    dtype: object  |   Departamento donde trabaja el empleado   |
|-----------|---------------|
||
|| NaNㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ81.41
|| Research & Developmentㅤ12.1
|| Salesㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ5.54
|| Human Resourcesㅤㅤㅤㅤ 0.95
||<br>
||<br>
||Valores únicos: **3**
||Número de registros: **1678**
||Valores nulos: **1366**
||Registros duplicados: **1675**|
---

---
ㅤ
**Propuesta de mejora:**

       > Estandarizar a minúculas todos los nombres.
 
       > Comparar los valores nulos con las columnas que incluyen datos aparentemente reiterados, pueden contener este valor en ausencia de estar presentes en esta columna.

Ir a columna de referencia: [roledepartament](#roledepartment)

       > Sustituir espacios innecesarios al inicio, final y entre las palabras del valor (' Human Resources ') por valores estandarizados y sin espacios innecesarios.
ㅤ
Dados los pocos departamentos que hay, podemos inferir el valor de los nulos de la relación entre los valores presentes y los valores de la columna [jobrole](#jobrole).

**Propuesta ejecutada:**

- Estandarización: formato letras minúsculas.
- El espaciado extra ha sido eliminado.
- Incluimos información faltante en relación a los valores presentes y relacionados de la columna ``jobrole``
- Modificamos ``NaN`` por ``unknown``.

---
---

### distancefromhome

|    dtype: int64  |   Distancia desde el hogar al trabajo  |
|-----------|---------------|
||
||**Top 5:**
||2ㅤㅤ13.59%
||1ㅤㅤ12.46%
||9ㅤ ㅤ 5.3%
||10ㅤㅤ5.13%
||8  ㅤ ㅤ5.07%
||<br>
||**Bottom 5:**
||-21  ㅤ 0.12%
||-43  ㅤ 0.12%
||-28  ㅤ 0.12%
||-39  ㅤ 0.06%
||-40  ㅤ 0.06%
||<br>
||**Media:** 4.50
||**Mediana:** 5
||**Moda:** 2
||<br>
||Valores únicos: **69**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **1609**|
---
---
ㅤ
**Propuesta de mejora:**

       Convertimos en absolutos para eliminar valores numéricos negativos.

**Propuesta ejecutada:**

- Los valores negativos han sido transformados.

ㅤ
---

---

### education

|    dtype: int64  |   Nivel Educativo (Escala Numérica)  |
|-----------|---------------|
||
||3ㅤㅤ38.68
||4ㅤㅤ27.47
||2ㅤㅤ19.19
||1ㅤㅤ11.08
||5ㅤㅤ 3.58
||<br>
||**Media:** 2.93
||**Mediana:** 3
||**Moda:** 3
||<br>
||Valores únicos: **5**
||Número de registros: **1678**
||Valores nulos: **0**
---
ㅤ     
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

       > Estandarizar a formato minúculas todos los nombres.

       > Comparar los valores nulos con las columnas que incluyen datos aparentemente reiterados, pueden contener este valor en ausencia de estar presentes en esta columna.

**Propuestas ejecutadas:**

- Estandarización: formato letras minúsculas.
- El espaciado extra ha sido eliminado.
- Imputar por ``unknown`` los valores nulos.

---
---

### employeecount

|    Tipo   | Valor constante de ``1``, indicando un solo empleado por registro  |
| ----------- | ----------- |
| dtype: int64| 1ㅤㅤ100.0 <br><br> Valores únicos: **1**<br>Número de registros: **1678**|

---

ㅤ     
Este campo es redundante, cada registro corresponde a un único empleado (valor siempre igual a 1).

ㅤ     
**Propuesta de mejora:**

       > Eliminar columna
ㅤ     
**Propuestas ejecutadas:**

- La columna ha sido eliminada.

ㅤ     

---
---

### employeenumber

|    dtype: int64  |   Número de Identificación del empleado  |
|-----------|---------------|
||
||**Top 5:**
||528ㅤㅤ0.12%
||300ㅤㅤ0.12%
||168ㅤㅤ0.12%
||644ㅤㅤ0.12%
||271ㅤㅤ0.12%
||<br>
||**Bottom 5:**
||1594ㅤㅤ0.06%
||1595ㅤㅤ0.06%
||1596ㅤㅤ0.06%
||1597ㅤㅤ0.06%
||1614ㅤㅤ0.06%
||<br>
||**Media:** 809.85
||**Mediana:** 813.5
||**Moda:** 9
||<br>
||Valores únicos: **1614**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **64**|
---

ㅤ     

**Propuesta de mejora:**

       > Gestión de duplicados.
ㅤ     
**Propuestas ejecutadas:**

- Se han eliminado los (**64**) registros duplicados en los identificadores únicos.

- También presentaban duplicidades en las filas asociadas del resto de columnas: han sido elimnadas también.

ㅤ     

---

### environmentsatisfaction

|    dtype: int64  |   environmentsatisfaction   |
|-----------|---------------|
||
||**Top 5:**
||4ㅤㅤ28.78%
||3ㅤㅤ28.07%
||2ㅤㅤ18.83%
||1ㅤㅤ18.24%
||12ㅤㅤ0.42%
||<br>
||**Bottom 5:**
||39ㅤㅤ0.06%
||49ㅤㅤ0.06%
||10ㅤㅤ0.06%
||26ㅤㅤ0.06%
||43ㅤㅤ0.06%
||<br>
||**Media:** 4.26
||**Mediana:** 3
||**Moda:** 4
||<br>
||Valores únicos: **38**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **1640**|
---

---
ㅤㅤ
**Propuesta de mejora:**

       > Plantearnos si podemos igualar el rango de la escala al resto de escalas de valoración que tenemos, por ejemplo: 
       
       Decidir acortar las distancias entre 0 y 50 pasándolos a float entre 0-5 (0.1, 0.3, 0.4... 3.3, 4.5, 4.9)

       Tratar los datos altos imputandolos como valores con décimas, es decir, 24 será un 2,4 y para estandarizar con la mayoría de respuestas (93,8%) lo imputaremos a 2.

**Propuestas ejecutadas:**

- Buscamos redondear al primer número de cada valor alto (outlier) ``df["columna"] = ((df["columna"] + 5) // 10).astype(int)``

---
---

### gender

|    dtype: int64  |   gender   |
|-----------|---------------|
||
||0ㅤㅤ60.13
||1ㅤㅤ39.87
||<br>
||<br>
||Valores únicos: **2**
||Número de registros: **1678**
||Valores nulos: **0**|
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
| dtype: float64 | NaNㅤㅤㅤㅤ75.51<br>36.254439ㅤㅤ4.53<br>69.532083ㅤㅤ4.47<br>129.060911 ㅤ 2.44<br>197.846418     0.83<br>(...)<br>108.230159     0.06<br>247.477183     0.06<br>67.424603      0.06<br>34.821429      0.06||133.159722     0.06 <br><br> Valores únicos: **194**<br>Número de registros: **1678** |

---

ㅤㅤ

La mayor parte de los valores son nulos. Puede ser un error de recolección o la existencia de empleados sin tarifa asignada

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

|    Tipo   |   Nivel de compromiso del empleado en el trabajo   |
|-----------|---------------|
| dtype: int64 |3ㅤㅤ59.3||2ㅤㅤ25.09||4ㅤㅤ10.13||1ㅤㅤ5.48<br><br>Valores únicos: **4**<br>Número de registros: **1678**

---

ㅤㅤ
Escala de valoración.

Sin anomalías. Mantener sin cambios.

**Propuesta de mejora:**

       > Definir y documentar explícitamente el significado de cada valor: 
       ej: 1: 'Bajo compromiso',
       2: 'Compromiso moderado',
       3: 'Compromiso alto',
       4: 'Compromiso excepcional'
       
       Podemos incluir 0 y 5 en la escala, aunque no aparezcan en las puntuaciones registradas, por convención y estándar.

ㅤㅤ
⚑ Incluir en un glosario el significado de la escala de valores.

---
---

### joblevel

|    Tipo   |   Nivel jerárquico del puesto del empleado   |
|-----------|---------------|
| dtype: int64 |2ㅤㅤ36.83
||1ㅤㅤ36.47
||3ㅤㅤ15.2
||4 ㅤㅤ 6.79
||5 ㅤㅤ 4.71<br><br>Valores únicos: **5**<br>Número de registros: **1678**|

---

ㅤㅤ
Escala de rangos.

Sin anomalías. Mantener sin cambios.

⚑ Incluir en un glosario el significado de los rangos.

ㅤㅤ

---
---

### jobrole

|    Tipo   |   jobrole   |
|-----------|---------------|
| dtype: object | mANager ㅤㅤ0.3<br><br> mAnageR ㅤㅤ0.18<br> ManagEr ㅤㅤ0.18<br> mAnaGeR ㅤㅤ0.18<br> ManageR ㅤㅤ0.18<br> MANAgER ㅤㅤ0.18<br>maNaGeR ㅤㅤ0.18<br> SALes RePREsEntAtivE ㅤㅤ0.12<br>SALes exeCUtiVE ㅤㅤ0.12<br> LAboRaTorY teChniCiaN ㅤㅤ0.12<br> reseaRCH DIrectOr ㅤㅤ0.12<br> ManUFaCtURInG dIReCToR ㅤㅤ0.12<br> MaNAgeR ㅤㅤ0.12<br> mANAgER ㅤㅤ0.12<br> ManAgEr ㅤㅤ0.12<br>(...)<br> hEAltHCarE REpreSentaTiVe ㅤㅤ0.06<br> mANUFacTURInG DIREctoR ㅤㅤ0.06<br>heALtHCArE RepRESENTATIVE ㅤㅤ0.06<br> maNUFacturing DiRector ㅤㅤ0.06<br><br>Valores únicos: **1579**<br>Número de registros: **1678**<br>Registros duplicados: **99**|

---

 ㅤㅤ  
Registros con valores de escritura irregular que no se agrupan como debieran: aparecen como 1579 registros únicos.

Tras una estandarización el resultado es que los registros únicos son 9:

       [' research director ', ' manager ', ' sales executive ', ' manufacturing director ', ' research scientist ', ' healthcare representative ', ' laboratory technician ', ' sales representative ', ' human resources ']
 ㅤㅤ  
**Propuesta de mejora:**

       > Estandarizar a formato letras minúsculas.

       > Eliminar espaciado innecesario entre palabras.

 ㅤㅤ  
**Propuestas ejecutadas:**

- Estandarización a formato letras minúsculas.
- El espaciado extra ha sido eliminado.

---
---

### jobsatisfaction

|    Tipo   |   Satisfacción general en el puesto   |
|-----------|---------------|
| dtype: int64 |4ㅤㅤ32.06
||3ㅤㅤ29.62
||1ㅤㅤ19.43
||2ㅤㅤ18.89<br><br>Valores únicos: **4**<br>Número de registros: **1678**|

---

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

(dtype: object) **PENDIENTE**
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

(dtype: object) **PENDIENTE**
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

(dtype: object) **PENDIENTE**
*Tarifa mensual estimada en función de la tarifa diaria*

       Values 1678 | Unique 673 | NaN 0 | dtype Object  

Propuesta de mejora:

- Mismo que en ``monthlyincome``
``df["monthlyrate"] = df["monthlyrate"].str.replace("$", "", regex=False).str.replace(",", ".", regex=False)``

       -->regex false - pandas puede pensar que es una funcion regex
- ``df["monthlyrate"] = df["monthlyrate"] = pd.to_numeric(df["monthlyrate"], errors="coerce")``

       --> errors="coerce" asegura que si no se cumple convierte en NaN
       
       

### numcompaniesworked

(dtype: int64) **PENDIENTE**
*Número de empresas previas en las que ha trabajado*

       Valores = array([7, 0, 1, 3, 2, 4, 8, 9, 5, 6])

       Values 1678 | Unique 10 (0-9) | NaN 0 | dtype int

- Entendemos que son empleos en compañías anteriores.

De cara al volcado a SQL:

- ¿Igual podemos llamarlo experiencia previa en empresas? ¿Score empleos previos?

---

### over18

(dtype: object) **PENDIENTE**
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

(dtype: object) **PENDIENTE**
*Indica si el empleado trabaja horas extras (Yes/No)*

       Valores = array(['No', nan, 'Yes'], dtype=object)

Propuesta de mejora:

- Gestión de nulos.
- ¿Atribuir ``NaN`` como ``Desconocido`` y darle valor a la información de quien tiene un claro Yes?
- Consultar con nuestro enlace de proyecto, Pilar.

Propuestas ejecutadas:

- Cambio ``nan`` por ``unknown``

---

### percentsalaryhike **PENDIENTE**

(dtype: int64)
*Incremento porcentual en el salario*

       Valores = array([13, 14, 11, 19, 12, 25, 16, 17, 22, 23, 20, 15, 21, 24, 18])

Propuesta de mejora:
Mantener sin cambios.

---

### performancerating **PENDIENTE**

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

(dtype: int64) **PENDIENTE**
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

(dtype: object) **PENDIENTE**
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

(dtype: int64) **PENDIENTE**
*Nivel de opciones sobre acciones asignadas.*

       Valores numéricos ([0, 1, 2, 3])

Propuesta de mejora:
Mantener sin cambios.

---

### totalworkingyears

(dtype: object) **PENDIENTE**
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

(dtype: int64) **PENDIENTE**
*Número de sesiones de entrenamiento en el último año.*

       Valores numéricos ([5, 3, 2, 0, 1, 4, 6])

Sin anomalías.

---

### worklifebalance

|    Tipo   |   worklifebalance   |
|-----------|---------------|
| dtype: object |3,0ㅤㅤ56.38<br>2,0ㅤㅤ22.29<br>4,0 ㅤㅤ 9.65<br>NaNㅤㅤ6.79<br>1,0 ㅤㅤ 4.89<br><br>Valores únicos: **4**<br>Número de registros: **1678**

---

ㅤㅤ
**Propuesta de mejora:**

       > Reemplazar ',' por '.'.

       > Gestionar nulos, sustituir nulos por mediana

       > Convertir valores a tipo 'float'.

**Propuestas ejecutadas:**

- Se han reemplazado las comas y la columna ahora contiene valores 'float'.
- Se imputaron los nulos con la mediana (3.0).

ㅤㅤ

---
---

### yearsatcompany

|    Tipo   |   Años en la empresa actual  |
|-----------|---------------|
| dtype: int64 |5ㅤㅤ12.75<br>1ㅤㅤ10.79<br>3 ㅤㅤ 8.88<br>2 ㅤㅤ 8.64<br>10ㅤㅤ8.28<br>4 ㅤㅤ 6.91<br>7 ㅤㅤ 6.85<br>8 ㅤㅤ 6.73<br>9 ㅤㅤ 5.84<br>6 ㅤㅤ 5.01<br>0 ㅤㅤ 2.8<br>11ㅤㅤ2.21<br>20ㅤㅤ1.79<br>13ㅤㅤ1.61<br>15ㅤㅤ1.31<br>14ㅤㅤ1.13<br>22ㅤㅤ1.07<br>18ㅤㅤ0.95<br>12ㅤㅤ0.89<br>(...)<br>30ㅤㅤ0.06<br>34ㅤㅤ0.06<br><br>Valores únicos: **37**<br>Número de registros: **1678**

---

ㅤㅤ
Sin anomalías. Mantener sin cambios.

Puede ser interesante comparar los años en la empresa actual con los valores nulos en la columna ``totalworkingyears`` para comprobar qué relato/perfil nos devuelve.

Ir a **[totalworkingyears](#numcompaniesworked)**.

---

### yearsincurrentrole

|   Tipo   |   yearsincurrentrole   |
|-----------|---------------|
| dtype: object |NaNㅤㅤ97.91<br>2,0ㅤㅤ0.72<br>7,0ㅤㅤ0.3<br>0,0ㅤㅤ0.24<br>4,0ㅤㅤ0.18<br>1,0ㅤㅤ0.18<br>11,0ㅤㅤ0.12<br>6,0ㅤㅤ0.12<br>3,0ㅤㅤ0.12<br>12,0ㅤㅤ0.06<br>13,0ㅤㅤ0.06<br><br>Valores únicos: **10**<br>Número de registros: **1678**

---

ㅤㅤ
Hay 1643 nulos en una columna con 1678 registros, casi el 98%

**Propuesta de mejora:**

       > Eliminar la columna, no es una muestra representativa para obtener información.
ㅤㅤ
**Propuestas ejecutadas:**

- La columna ha sido eliminada.

ㅤㅤ
---

---

### yearssincelastpromotion

|    Tipo   |   yearssincelastpromotion   |
|-----------|---------------|
| dtype: int64 |0ㅤㅤ39.03<br>1ㅤㅤ23.66<br>2ㅤㅤ10.91<br>7ㅤㅤ5.66<br>4ㅤㅤ4.11<br>3ㅤㅤ3.87<br>5ㅤㅤ3.16<br>6ㅤㅤ2.26<br>11ㅤㅤ1.61<br>8ㅤㅤ1.31<br>9ㅤㅤ1.13<br>15ㅤㅤ0.95<br>14ㅤㅤ0.66<br>12ㅤㅤ0.66<br>13ㅤㅤ0.6<br>10ㅤㅤ0.42<br><br>Valores únicos: **16**<br>Número de registros: **1678**

---

ㅤㅤ
Es una horquilla de años entre 0 a 15.

Sin anomalías. Mantener sin cambios.

---
---

### yearswithcurrmanager

|    Tipo   |   Años bajo el mismo manager   |
|-----------|---------------|
| dtype: int64 |2ㅤㅤ23.54<br>0ㅤㅤ16.98<br>7ㅤㅤ16.39<br>3 ㅤㅤ 9.06<br>8 ㅤㅤ 7.27<br>4 ㅤㅤ 6.44<br>1 ㅤㅤ 5.18<br>9 ㅤㅤ 4.23<br>5 ㅤㅤ 2.32<br>10ㅤㅤ1.97<br>6 ㅤㅤ 1.85<br>11ㅤㅤ1.31<br>12ㅤㅤ1.19<br>13ㅤㅤ1.01<br>17ㅤㅤ0.48<br>15ㅤㅤ0.3<br>14ㅤㅤ0.3<br>16ㅤㅤ0.18<br><br>Valores únicos: **18**<br>Número de registros: **1678**

---

ㅤㅤ
Es una horquilla de años entre 0 a 17.

Sin anomalías. Mantener sin cambios.

---
---

### sameasmonthlyincome

|    Tipo   |   *columna sin especificar*  |
|-----------|---------------|
| dtype: object |NaNㅤㅤ29.14<br>2342,59$ㅤㅤ13.59<br>4492,84$ㅤㅤ13.53<br>8339,32$ㅤㅤ6.26<br>12783,92$ㅤㅤ2.5<br>15943,72$ㅤㅤ1.49<br>4420,00$ㅤㅤ0.3<br>3612,50$ㅤㅤ0.18<br>2949,17$ㅤㅤ0.18<br>(...)<br>2241,67$ㅤㅤ0.06<br>15034,17$ㅤㅤ0.06<br><br>Valores únicos: **493**<br>Número de registros: **1678**

---

ㅤㅤ

Los registros presentan coma decimal e incluyen en el dato el simbolo ``$``.

ㅤ
**Propuesta de mejora:**

       > Cambiar ',' por '.'.

       > Eliminar también el símbolo '$'.

       > Modificar valor tipo 'objeto' a 'float'.

       > Comprobar si esta columna es una copia redundante de 'monthlyincome', si en efecto lo es, eliminar.

ㅤ
Ir a **[monthlyincome](#monthlyincome)**

**Propuestas ejecutadas:**

- La columna ha sido eliminada.

ㅤ

---
---

### datebirth

|    Tipo   |   Año de nacimiento  |
|-----------|---------------|
| dtype: int64 |1992ㅤㅤ5.3<br>1988ㅤㅤ5.24<br>1989ㅤㅤ5.13<br>1994ㅤㅤ4.89<br>1987ㅤㅤ4.77<br>1991ㅤㅤ3.99<br>1993ㅤㅤ3.93<br>1985ㅤㅤ3.81<br>1990ㅤㅤ3.75<br>1983ㅤㅤ3.58<br>1986ㅤㅤ3.34<br>1996ㅤㅤ3.22<br>1995ㅤㅤ3.22<br>1978ㅤㅤ2.98<br>1981ㅤㅤ2.98<br>(...)<br>1964ㅤㅤ0.66<br>2003ㅤㅤ0.66<br>2005ㅤㅤ0.54<br>2004ㅤㅤ0.54<br>1966ㅤㅤ0.36<br>1963ㅤㅤ0.3<br><br>Valores únicos: **43**<br>Número de registros: **1678**

---

ㅤ
Presenta el formato para un año de nacimiento.

Sin anomalías. Mantener sin modificaciones.

---

### salary

|    Tipo   |   Salario anual calculado para el empleado   |
|-----------|---------------|
| dtype: object |NaNㅤㅤㅤㅤㅤ16.98<br>53914,11$ ㅤㅤ 16.09<br>28111,13$ㅤ   ㅤ 15.2<br>100071,84$ ㅤㅤ 7.27<br>153407,07$ ㅤㅤ 2.68<br>191324,62$ ㅤㅤ 1.67<br>63470,00$ㅤㅤㅤ 0.18<br>20330,00$ㅤㅤㅤ 0.18<br>53040,00$ㅤㅤㅤ 0.18<br>(...)<br>134020,00$ ㅤㅤ 0.06<br>195370,00$ ㅤㅤ 0.06<br>199990,00$ ㅤㅤ 0.06<br>49600,00$ㅤㅤㅤ0.06<br>27410,00$ㅤㅤㅤ0.06<br>24390,00$ㅤㅤㅤ0.06<br>28040,00$ㅤㅤㅤ0.06<br>46480,00$ㅤㅤㅤ0.06<br>29560,00$ㅤㅤㅤ0.06<br><br>Valores únicos: **583**<br>Número de registros: **1678**

---

ㅤㅤ

Los registros presentan coma decimal e incluyen en el dato el simbolo ``$``.

ㅤ
**Propuesta de mejora:**

       > Cambiar ',' por '.'.

       > Eliminar también el símbolo '$'.
       
       > Modificar valor tipo ``objeto`` a ``float``.

       > Relleno de nulos calculando 'salary = monthlyincome * 12'

ㅤ
**Propuestas ejecutadas:**

- Todas las propuestas han sido ejecutadas.

ㅤ

---
---

### roledepartament

|    Tipo   |   Combinación de rol y departamento   |
|-----------|---------------|
| dtype: object |NaNㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ81.41<br>Sales exECutIVE  -  Salesㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ0.12<br> humAN resoURCEs  -  Human Resources ㅤㅤㅤㅤㅤ ㅤㅤ 0.12<br> labORAtoRy tEcHNICIAN  -  Research & Developmentㅤㅤ0.12<br> hEalthCaRe reprEseNTaTiVe  -  Research & Developmentㅤ0.12<br> LaBoratory TECHnICIAn  -  Research & Development ㅤ ㅤ 0.12<br> LaborAtorY Technician  -  Research & Developmentㅤㅤㅤ 0.12<br> LABOrATOrY TEchnIcIAn  -  Research & Development ㅤㅤ 0.12<br>(...)<br> SALEs REpRESentatIve  -  Sales ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ0.06<br> heaLtHcArE repResENtATiVe  -  Research & Developmentㅤ0.06<br><br>Valores únicos: **301**<br>Número de registros: **1678**

---

ㅤㅤ
Registros de escritura irregular que no pueden agruparse debidamente y 81.41% de valores nulos.

ㅤㅤ
**Propuesta de mejora:**

       > Estandarizar a formato letras minúsculas.

       > Comprobar si esta columna es sólo redundante o si contiene los datos que faltan en columnas 'department' y 'jobrole'.
       
Ir a **[department](#department)**
Ir a **[jobrole](#jobrole)**

       > Destinarla a eliminación una vez reubicados todos los valores.

ㅤㅤ
**Propuestas ejecutadas:**

- La columna ha sido eliminada.

ㅤㅤ

---
---

### numberchildren

|    Tipo   |   Número de hijos   |
|-----------|---------------|
| dtype: float64 |NaNㅤㅤ100.0<br><br>Valores únicos: **0**<br>Número de registros: **1678**

---

ㅤㅤ
No hay datos recogidos para este campo.

ㅤㅤ
**Propuesta de mejora:**

       > Posible columna a eliminar.
       > Incluir recomendaciones para la empresa.

ㅤㅤ
**Propuestas ejecutadas:**

- La columna se eliminó.

ㅤㅤ
---

---

### remotework

|    Tipo   |   El empleado trabaja de forma remota (Yes/No)   |
|-----------|---------------|
| dtype: object |1ㅤㅤㅤ 22.3<br>trueㅤㅤ21.38<br>0ㅤㅤㅤ 19.14<br>falseㅤㅤ18.9<br>yes ㅤㅤ 18.28<br><br>Valores únicos: **5**<br>Número de registros: **1614**

---

ㅤㅤ
Quizás el 0 signifique Sí/Yes y el 1 signifique No. También es posible que el True sea igual a Sí/Yes y el False sea No.

**Propuesta de mejora:**

       > Consultar con PO información respecto a las entradas de registro.
       > Estandarizar formato.

ㅤㅤ
**Propuestas ejecutadas**:

- Sin ejecutar.

## 4. Cambios ejecutados

       Hipervínculo + parte crucial del código que soluciona
       Y así sucesivamente

---

## 5. Nuestras cuestiones sobre los datos

*Presentación de preguntas de Patri + enfoque de Andrea*

---

## 6. Visualización como respuesta

**A continuación, la información que hemos obtenido en consecuencia:**

Aqui mostramos correlaciones positivas fuertes (con un valor mayor a 0.5) que he encontrado en tus datos. Parece que hay varias variables con una correlación perfecta o casi perfecta (1.0000 o 0.9701), lo que podría indicar que son dependientes entre sí o redundantes.

 Correlaciones positivas fuertes (> 0.5) encontradas:

- monthlyrate y dailyrate: 1.0000
- hourlyrate y monthlyrate: 1.0000  
- dailyrate y hourlyrate: 1.000
- hourlyrate y joblevel: 0.9701
- joblevel y dailyrate: 0.9701
- joblevel y monthlyrate: 0.9701
- salary y hourlyrate: 0.8528
- monthlyrate y salary: 0.8528  
- dailyrate y salary: 0.8528
- salary y joblevel: 0.8295
- performancerating y percentsalaryhike: 0.7751  
- joblevel y totalworkingyears: 0.7727
- totalworkingyears y hourlyrate: 0.7634
- totalworkingyears y monthlyrate: 0.7634
- dailyrate y totalworkingyears: 0.7634  
- yearsatcompany y yearswithcurrmanager: 0.7571  
- monthlyincome y salary: 0.7453
- totalworkingyears y age: 0.6687
- yearsatcompany y totalworkingyears: 0.6367  
- monthlyrate y monthlyincome: 0.6270
- hourlyrate y monthlyincome: 0.6270
- monthlyincome y dailyrate: 0.6270
- monthlyincome y joblevel: 0.6151  
- yearsatcompany y yearssincelastpromotion: 0.6118
- totalworkingyears y monthlyincome: 0.5979  
- salary y totalworkingyears: 0.5979
- joblevel y yearsatcompany: 0.5324
- yearsatcompany y dailyrate: 0.5221
- yearsatcompany y hourlyrate: 0.5221
- yearsatcompany y monthlyrate: 0.5221
- age y joblevel: 0.5074
- yearssincelastpromotion y yearswithcurrmanager: 0.5009
- hourlyrate y age: 0.5007
- age y monthlyrate: 0.5007
- dailyrate y age: 0.5007

Aquí mostramos un resumen de las variables que presentan un número considerable de valores atípicos, lo que indica una alta dispersión:

- trainingtimeslastyear: 268 outliers
- performancerating: 214 outliers
- yearssincelastpromotion: 116 outliers
- yearsatcompany: 114 outliers

Estas variables son las que tienen los datos más dispersos.
Análisis de outliers (valores atípicos) por variable:

- Variable 'dailyrate': Se encontraron 18 outliers.
- Variable 'distancefromhome': Se encontraron 40 outliers.
- Variable 'hourlyrate': Se encontraron 18 outliers.  
- Variable 'monthlyincome': Se encontraron 11 outliers.
- Variable 'monthlyrate': Se encontraron 18 outliers.
- Variable 'numcompaniesworked': Se encontraron 59 outliers.
- Variable 'performancerating': Se encontraron 214 outliers.
- Variable 'stockoptionlevel': Se encontraron 89 outliers.
- Variable 'totalworkingyears': Se encontraron 42 outliers.
- Variable 'trainingtimeslastyear': Se encontraron 268 outliers.
- Variable 'yearsatcompany': Se encontraron 114 outliers.
- Variable 'yearssincelastpromotion': Se encontraron 116 outliers.
- Variable 'yearswithcurrmanager': Se encontraron 16 outliers.
- Variable 'salary': Se encontraron 15 outliers.


## 7. Próximos Pasos (Next Steps)

1. Optimización Técnica

- Dinamización de Datos: Investigar la posibilidad de convertir una cifra estática clave en un valor dinámico, calculado automáticamente a partir de la fecha de nacimiento

2. Validación y Calidad de Datos

- Refuerzo del Back-end: Implementar validaciones estrictas para prevenir la entrada de datos erróneos o inconsistentes.

3. Normalización y Documentación

- Glosario de Valores: Crear un glosario que defina explícitamente el significado de cada valor en las escalas utilizadas (ej. ‘1: Insatisfecho’, ‘4: Muy satisfecho’).
- Convención de Escala: Documentar formalmente el uso de los valores 0 y 5 en las escalas, aunque no aparezcan en los registros actuales.

4. Inclusión y Diversidad

- Ampliación de Género: Incorporar opciones de género no binario y diversidad de género en los campos correspondientes para mejorar la representatividad e inclusividad del proyecto.

5. Comentarios de la Empresa

- Recopilar y analizar feedback directo de la empresa para alinear las mejoras con sus expectativas y necesidades.

6. Visualizaciones

- Mejorar la presentación de datos mediante gráficos y dashboards interactivos, facilitando la interpretación y toma de decisiones. (editado)
