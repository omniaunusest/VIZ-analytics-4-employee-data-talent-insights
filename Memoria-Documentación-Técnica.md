# Memoria de Proyecto ABC Corporation: Gestión del Talento en Ecosistemas Empresariales

*ABC Corporation* invierte en tecnología de talento, la misión con esta simulación de proyecto completo no es solo optimizar costes sino **Auditar el Bienestar** de la empresa mediante un proyecto de I+D, para maximizar diferentes grados de beneficio: implementando guías para un crecimiento estable y responsable basadas en el gobierno del dato.


#### Nuestro objetivo: Calidad del dato = Calidad de vida


## Índice

- [1. Campos y categorías](#1-campos-y-categorías)

- [2. Patrones generales](#2-patrones)

- [3. Análisis Exploratorio de Datos (EDA)](#3-análisis-exploratorio-de-datos-eda)

- [4. Cambios ejecutados](#4-cambios-ejecutados)

- [5. Nuestras cuestiones sobre los datos](#5-nuestras-cuestiones-sobre-los-datos)

- [6. Visualización como respuesta](#6-visualización-como-respuesta:)

- [7. Próximos pasos: vistas a futuro](#7-próximos-pasos-next-steps)

- [8. Glosario de definiciones](#8-glosarios)

## 1. Campos y categorías

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

<details>
<summary> (Para expandir la exploración completa: click aquí)</summary>

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

|    dtype: float64  |   Salario/hora   |
|-----------|---------------|
||
||**Top 5:**
||nan  75.51%
||36.25443871706758  4.53%
||69.53208262471655  4.47%
||129.06091077207583  2.44%
||197.8464183087028  0.83%
||<br>
||**Bottom 5:**
||108.23015873015872  0.06%
||247.47718253968256  0.06%
||67.42460317460318  0.06%
||34.82142857142857  0.06%
||133.15972222222223  0.06%
||<br>
||**Media:** 83.14076792768908
||**Mediana:** 69.53208262471655
||**Moda:** 36.25443871706758
||<br>
||Valores únicos: **194**
||Número de registros: **1678**
||Valores nulos: **1267**
||Registros duplicados: **1484**|
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

|    dtype: int64  |   Nivel de compromiso del empleado en el trabajo   |
|-----------|---------------|
||
||3  59.3
||2  25.09
||4  10.13
||1  5.48
||<br>
||**Media:** 2.74
||**Mediana:** 3
||**Moda:** 3
||<br>
||Valores únicos: **4**
||Número de registros: **1678**
||Valores nulos: **0**|
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

|    dtype: int64  |   Rango de   |
|-----------|---------------|
||
||2  36.83
||1  36.47
||3  15.2
||4  6.79
||5  4.71
||<br>
||**Media:** 2.06
||**Mediana:** 2
||**Moda:** 2
||<br>
||Valores únicos: **5**
||Número de registros: **1678**
||Valores nulos: **0**|
---

ㅤㅤ
Escala de rangos.

Sin anomalías. Mantener sin cambios.

⚑ Incluir en un glosario el significado de los rangos.

ㅤㅤ

---
---

### jobrole

|    dtype: object  |   jobrole   |
|-----------|---------------|
||
||**Top 5:**
|| mANagerㅤㅤㅤㅤㅤㅤ0.3%
|| mAnageRㅤㅤㅤㅤㅤㅤ0.18%
|| ManagErㅤㅤㅤㅤㅤㅤ0.18%
|| mAnaGeRㅤㅤㅤㅤㅤㅤ0.18%
|| ManageRㅤㅤㅤㅤㅤㅤ0.18%
||<br>
||**Bottom 5:**
|| SaleS eXeCuTIVEㅤㅤㅤㅤㅤㅤ 0.06%
|| hEAltHCarE REpreSentaTiVe ㅤ  0.06%
|| mANUFacTURInG DIREctoR  ㅤ 0.06%
|| heALtHCArE RepRESENTATIVE 0.06%
|| maNUFacturing DiRectorㅤ ㅤ 0.06%
||<br>
||<br>
||Valores únicos: **1579**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **99**|
---
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

|    dtype: int64  |   Satisfacción con el empleo  |
|-----------|---------------|
||
||4ㅤㅤ32.06
||3ㅤㅤ29.62
||1ㅤㅤ19.43
||2ㅤㅤ18.89
||<br>
||**Media:** 2.74
||**Mediana:** 3
||**Moda:** 4
||<br>
||Valores únicos: **4**
||Número de registros: **1678**
||Valores nulos: **0**|
---
---

Mantener sin cambios.  

**Nota:**     
Poder definir y documentar explícitamente el significado de cada valor: 
       ej: 1: 'Insatisfecho',
       2: 'Poco satisfecho',
       3: 'Satisfecho',
       4: 'Muy satisfecho'

Incluimos 0 y 5 en la escala aunque no aparezcan en la recolección de puntuaciones.

⚑ Incluir en un glosario el significado de la escala.

---

### maritalstatus

|    dtype: object  |  Estado Civil   |
|-----------|---------------|
||
||NaNㅤㅤㅤ40.23
||Married ㅤ 24.97
||Singleㅤㅤ 20.44
||Divorcedㅤ11.56
||Marreidㅤㅤ2.15
||divorced ㅤ 0.66
||<br>
||<br>
||Valores únicos: **5**
||Número de registros: **1678**
||Valores nulos: **675**|
---

Propuesta de mejora:

       > Estandarizar a letras minúsculas y registros con entrada erronea.
       > Gestión de nulos.

Propuestas ejecutadas:

- Estandarización: formato letras minúsculas.
- Sustituidas incorrecciones ortográficas.
- Los nulos han sido sustituidos por ``insértese aquí lo propio``.

---

### monthlyincome

|    dtype: object  |   Ingreso mensual estimado por el salario anual   |
|-----------|---------------|
||
||**Top 5:**
||NaNㅤㅤㅤㅤ29.14%
||2342,59$ㅤㅤ13.59%
||4492,84$ㅤㅤ13.53%
||8339,32$ㅤㅤ 6.26%
||12783,92$ㅤㅤ2.5%
||
||**Bottom 5:**
||1980,00$ㅤㅤ0.06%
||2115,83$ㅤㅤ0.06%
||1923,33$ㅤㅤ0.06%
||2241,67$ㅤㅤ0.06%
||15034,17$ㅤ 0.06%
||<br>
||<br>
||Valores únicos: **493**
||Número de registros: **1678**
||Valores nulos: **489**|
---
---

**Propuesta de mejora:**

- Gestión de valores nulos: calcular el salario mensual dividiendo el valor existente de la columna ``salary`` /12.

**Propuestas ejecutadas:**

- Calculo de valores faltantes.

---

### monthlyrate

|    dtype: object  |   Tarifa mensual estimada en función de la tarifa diaria   |
|-----------|---------------|
||
||**Top 5:**
||11681,39$ㅤㅤ19.43%
||6090,75$ ㅤㅤ 18.36%
||21682,23$ ㅤㅤ 8.94%
||33238,20$ ㅤㅤ 3.28%
||41453,67$ㅤㅤ 2.26%
||<br>
||**Bottom 5:**
||11160,50$  0.06%
||6203,17$  0.06%
||6192,33$  0.06%
||2446,17$  0.06%
||23287,33$  0.06%
||<br>
||<br>
||Valores únicos: **673**
||Número de registros: **1678**
||Valores nulos: **0**|
---

ㅤ     
**Propuesta de mejora:**

        > Reemplazar ',' por '.'.

       > Convertir valores a tipo 'float'.

**Propuestas ejecutadas:**

- Se han reemplazado las comas y la columna ahora contiene valores 'float'.


---
---

### numcompaniesworked

|    dtype: int64  |   Número de empresas previas en las que ha trabajado   |
|-----------|---------------|
||
||1ㅤㅤ35.58
||0ㅤㅤ13.95
||3ㅤㅤ10.37
||4ㅤㅤ 9.89
||2ㅤㅤ 9.71
||7ㅤㅤ 5.24
||6ㅤㅤ 4.47
||5ㅤㅤ 3.99
||9ㅤㅤ 3.52
||8ㅤㅤ 3.28
||<br>
||**Media:** 2.67
||**Mediana:** 2
||**Moda:** 1
||<br>
||Valores únicos: **10**
||Número de registros: **1678**
||Valores nulos: **0**|
---

- Entendemos que son empleos en compañías anteriores.

De cara al volcado a SQL:

- Podemos llamarlo experiencia previa en empresas o score de empleos previos.

Sin anomalías. Mantener sin cambios.


---
---

### over18

|    dtype: object  |  *columna no definida*  |
|-----------|---------------|
||
||NaNㅤㅤㅤ55.9
||Yㅤㅤㅤㅤ44.1
||<br>
||<br>
||Valores únicos: **1**
||Número de registros: **1678**
||Valores nulos: **938**|
---

No existe valor N (No), solo Y (Yes) o NaN.

Es muy incompleto, con 55.9% de valores nulos, para darle peso en el analisis global.

Propuesta de mejora:

- Gestión de nulos.
- Inferir que los nulos, en ausencia de No, pueden tener ese valor.
- Consultar con nuestro enlace de proyecto, Product Owner: Pilar.

ㅤㅤ   

---
---

### overtime

|    dtype: object  |   Indica si el empleado trabaja horas extras (Yes/No)   |
|-----------|---------------|
||
||No  42.55
||NaN  41.48
||Yes  15.97
||<br>
||**Media:** nan
||**Mediana:** nan
||**Moda:** nan
||<br>
||Valores únicos: **2**
||Número de registros: **1678**
||Valores nulos: **696**
||Registros duplicados: **1676**|
---

**Propuesta de mejora:**

       > Gestión de nulos: atribuir 'NaN' como 'Desconocido' y darle valor a la información de quien tiene un claro 'Yes'.

       > Consultar con Product Owner.


**Propuestas ejecutadas:**

- Se ha sustituido ``NaN`` por ``unknown``

---
---

### percentsalaryhike

|    dtype: int64  |   Incremento porcentual en el salario   |
|-----------|---------------|
||
||11ㅤㅤ14.36
||13ㅤㅤ14.24
||12ㅤㅤ14.18
||14ㅤㅤ13.65
||15ㅤㅤ 6.67
||18ㅤㅤ 6.08
||17ㅤㅤ 5.48
||16ㅤㅤ 5.3
||19ㅤㅤ 5.13
||22ㅤㅤ 3.64
||20ㅤㅤ 3.58
||21ㅤㅤ 3.04
||23ㅤㅤ 1.97
||24ㅤㅤ 1.55
||25ㅤㅤ 1.13
||<br>
||**Media:** 15.15
||**Mediana:** 14
||**Moda:** 11
||<br>
||Valores únicos: **15**
||Número de registros: **1678**
||Valores nulos: **0**|

---
Propuesta de mejora:
Mantener sin cambios.

---
---

### performancerating

|    dtype: object  |   Evaluación de desempeño en una escala numérica   |
|-----------|---------------|
||
||3,0ㅤ 74.91
||4,0ㅤ 13.17
||NaN  11.92
||<br>
||<br>
||Valores únicos: **2**
||Número de registros: **1678**
||Valores nulos: **200**|
---

ㅤ     
**Propuesta de mejora:**

       > Reemplazar ',' por '.'

       > Convertir a float.

       > Para evitar que un valor baje la media del *performance rating*, sustituir por ``Desconocido``.


**Propuestas ejecutadas:**

- Se han reemplazado las comas y la columna ahora contiene valores 'float'.

---
---

### relationshipsatisfaction

|    dtype: int64  |   Satisfacción con relaciones interpersonales en el trabajo   |
|-----------|---------------|
||
||3ㅤ 31.41
||4ㅤ 28.78
||2ㅤ 20.86
||1ㅤ 18.95
||<br>
||**Media:** 2.7
||**Mediana:** 3
||**Moda:** 3
||<br>
||Valores únicos: **4**
||Número de registros: **1678**
||Valores nulos: **0**|
---

Sin anomalías. Mantener sin cambios.  

**Nota:**     
Definir y documentar explícitamente el significado de cada valor: 
       1: 'Insatisfecho',
       2: 'Poco satisfecho',
       3: 'Satisfecho',
       4: 'Muy satisfecho'

Incluimos 0 y 5 en la escala aunque no aparezcan en la recolección de puntuaciones.

⚑ Incluir en un glosario el significado de la escala.

---
---

### standardhours

|    dtype: object  |   Clasificación de jornada (Full Time/Part Time)   |
|-----------|---------------|
||
||Part Timeㅤ 55.24
||Full Timeㅤ 23.84
||NaNㅤ ㅤㅤ20.92
||<br>
||<br>
||Valores únicos: **2**
||Número de registros: **1678**
||Valores nulos: **351**|
---

Hay 927 valores atribuidos a *Part Time*, 400 *Full Time* y **351** nulos.


**Propuesta de mejora:**

       > Averiguar si hay categorías ausentes.

       > En base a la información que obtengamos podemos proceder a reemplazar nulos por otra catergoría o reasignarlos.

       > Explorar la relacion con otras columnas para asegurarnos si el valor nulo se da por falta de información o por otro tipo de clasificacion de jornada (ej: 'Freelance', 'Otro', 'No Especificado').
       
       > Convertir todo a minúsculas para normalizar todas las categorías.


**Propuestas ejecutadas:**

- Se han reemplazado valores ``NaN`` por ``full time``, información facilitada por Product Owner.

---
---

### stockoptionlevel

|    dtype: int64  |   Nivel de opciones sobre acciones asignadas.   |
|-----------|---------------|
||
||0ㅤㅤ42.85
||1ㅤㅤ41.06
||2ㅤㅤ10.55
||3ㅤㅤ 5.54
||<br>
||**Media:** 0.78
||**Mediana:** 1.0
||**Moda:** 0.0
||<br>
||Valores únicos: **4**
||Número de registros: **1678**
||Valores nulos: **0**|
---

Sin anomalías. Mantener sin cambios.


---
---

### totalworkingyears

|    dtype: object  |   Años totales de experiencia laboral   |
|-----------|---------------|
||
||**Top 5:**
||NaNㅤㅤ32.72%
||10,0 ㅤ ㅤ9.0%
||6,0ㅤㅤㅤ5.24%
||8,0ㅤㅤㅤ5.13%
||9,0ㅤㅤㅤ4.23%
||<br>
||**Bottom 5:**
||32,0ㅤㅤ0.18%
||30,0ㅤㅤ0.18%
||35,0ㅤㅤ0.18%
||34,0ㅤㅤ0.12%
||38,0ㅤㅤ0.06%
||<br>
||<br>
||Valores únicos: **40**
||Número de registros: **1678**
||Valores nulos: **549**|
---

**Propuesta de mejora:**

       > Reemplazar ',' por '.'

       > Convertir a valores tipo 'float'.

Comprobar si el nulo en años de experiencia laboral es dispar con la columna [numcompaniesworked](#numcompaniesworked), una vez comprobado se ha concluido dejar los valores nulos y convertir los datos a tipo ``float``.

**Propuestas ejecutadas:**

- Se ha reemplazado ``,`` por ``.``.
- Los valores ahora son ``float``.
- Se han mantenido los nulos.

---
---

### trainingtimeslastyear

|    dtype: int64  |   Número de sesiones de entrenamiento en el último año.   |
|-----------|---------------|
||
||2  37.25
||3  33.19
||4  8.52
||5  8.16
||1  4.83
||6  4.29
||0  3.75
||<br>
||**Media:** 2.79
||**Mediana:** 3
||**Moda:** 2
||<br>
||Valores únicos: **7**
||Número de registros: **1678**
||Valores nulos: **0**|
---

Sin anomalías. Mantener sin cambios.

---
---

### worklifebalance

|    dtype: object  |   worklifebalance   |
|-----------|---------------|
||
||3,0ㅤㅤ56.38
||2,0ㅤㅤ22.29
||4,0ㅤㅤ9.65
||NaNㅤㅤ6.79
||1,0ㅤㅤ4.89
||<br>
||<br>
||Valores únicos: **4**
||Número de registros: **1678**
||Valores nulos: **114**|
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

|    dtype: int64  |   Años en la empresa actual   |
|-----------|---------------|
||
||**Top 5:**
||5ㅤㅤ12.75%
||1ㅤㅤ10.79%
||3 ㅤㅤ 8.88%
||2 ㅤㅤ 8.64%
||10ㅤㅤ8.28%
||**Bottom 5:**
||<br>
||23ㅤㅤ0.12%
||29ㅤㅤ0.12%
||37ㅤㅤ0.06%
||30ㅤㅤ0.06%
||34ㅤㅤ0.06%
||<br>
||**Media:** 7.12
||**Mediana:** 5
||**Moda:** 5
||<br>
||Valores únicos: **37**
||Número de registros: **1678**
||Valores nulos: **0**|
---

ㅤ     
ㅤㅤ
Sin anomalías. Mantener sin cambios.

Puede ser interesante comparar los años en la empresa actual con los valores nulos en la columna ``totalworkingyears`` para comprobar qué relato/perfil nos devuelve.

Ir a **[totalworkingyears](#totalworkingyears)**.

---
---

### yearsincurrentrole

|    dtype: object  |   Años en el puesto actual   |
|-----------|---------------|
||
||NaNㅤㅤ97.91
||2,0ㅤㅤㅤ0.72
||7,0ㅤㅤㅤ0.3
||0,0ㅤㅤㅤ0.24
||4,0ㅤㅤㅤ0.18
||1,0ㅤㅤㅤ0.18
||11,0ㅤ ㅤ 0.12
||6,0ㅤㅤㅤ0.12
||3,0ㅤㅤㅤ0.12
||12,0ㅤㅤ 0.06
||13,0ㅤㅤ 0.06
||<br>
||<br>
||Valores únicos: **10**
||Número de registros: **1678**
||Valores nulos: **1643**|
---

ㅤ     

Hay 1643 nulos en una columna con 1678 registros, casi el 98%.

**Propuesta de mejora:**

       > Eliminar la columna, no es una muestra representativa para obtener información.
ㅤㅤ
**Propuestas ejecutadas:**

- La columna ha sido eliminada.

ㅤㅤ
---
---

### yearssincelastpromotion

|    dtype: int64  |   Años desde el último ascenso   |
|-----------|---------------|
||
||0ㅤㅤ39.03
||1ㅤㅤ23.66
||2ㅤㅤ10.91
||7ㅤㅤ 5.66
||4ㅤㅤ 4.11
||3ㅤㅤ 3.87
||5ㅤㅤ 3.16
||6 ㅤㅤ2.26
||11 ㅤ 1.61
||8ㅤㅤ 1.31
||9ㅤㅤ 1.13
||15ㅤㅤ0.95
||14ㅤㅤ0.66
||12ㅤㅤ0.66
||13ㅤㅤ0.6
||10ㅤㅤ0.42
||<br>
||**Media:** 2.24
||**Mediana:** 1
||**Moda:** 0
||<br>
||Valores únicos: **16**
||Número de registros: **1678**
||Valores nulos: **0**|
---
---

ㅤㅤ
Es una horquilla de años entre 0 a 15.

Sin anomalías. Mantener sin cambios.

---
---

### yearswithcurrmanager

|    dtype: int64  |   Años con el mismo jefe   |
|-----------|---------------|
||
||2ㅤㅤ23.54
||0ㅤㅤ16.98
||7ㅤㅤ16.39
||3ㅤㅤ9.06
||8ㅤㅤ7.27
||4ㅤㅤ6.44
||1ㅤㅤ5.18
||9ㅤㅤ4.23
||5ㅤㅤ2.32
||10 ㅤ 1.97
||6ㅤㅤ1.85
||11 ㅤ 1.31
||12 ㅤ 1.19
||13 ㅤ 1.01
||17 ㅤ 0.48
||15 ㅤ 0.3
||14 ㅤ 0.3
||16 ㅤ 0.18
||<br>
||**Media:** 4.2
||**Mediana:** 3
||**Moda:** 2
||<br>
||Valores únicos: **18**
||Número de registros: **1678**
||Valores nulos: **0**|
---

 ㅤ    
ㅤㅤ
Es una horquilla de años entre 0 a 17.

Sin anomalías. Mantener sin cambios.

---
---

### sameasmonthlyincome

|    dtype: object  |   *Columna sin especificar*  |
|-----------|---------------|
||
||**Top 5:**
||NaNㅤㅤㅤ29.14%
||2342,59$ㅤ13.59%
||4492,84$ㅤ13.53%
||8339,32$ㅤ 6.26%
||12783,92$ㅤ2.5%
||**Bottom 5:**
||<br>
||1980,00$ㅤ 0.06%
||2115,83$ㅤ 0.06%
||1923,33$ㅤ 0.06%
||2241,67$ㅤ 0.06%
||15034,17$ㅤ0.06%
||<br>
||<br>
||Valores únicos: **493**
||Número de registros: **1678**
||Valores nulos: **489**
||Registros duplicados: **1185**|
---

ㅤ     

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

|    dtype: int64  |   Año de nacimiento  |
|-----------|---------------|
||ㅤㅤ
||**Top 5:**
||1992ㅤㅤ5.3%
||1988ㅤㅤ5.24%
||1989ㅤㅤ5.13%
||1994ㅤㅤ4.89%
||1987ㅤㅤ4.77%
||<br>
||**Bottom 5:**
||2003ㅤㅤ0.66%
||2005ㅤㅤ0.54%
||2004ㅤㅤ0.54%
||1966ㅤㅤ0.36%
||1963ㅤㅤ0.3%
||<br>
||**Media:** 1986
||**Mediana:** 1987
||**Moda:** 1992
||<br>
||Valores únicos: **43**
||Número de registros: **1678**
||Valores nulos: **0**|
---

ㅤ     
Presenta el formato para un año de nacimiento.

Sin anomalías. Mantener sin modificaciones.

---
---

### salary

|    dtype: object  |   salary   |
|-----------|---------------|
||
||**Top 5:**
||NaN ㅤㅤㅤ 16.98%
||53914,11$ㅤ16.09%
||28111,13$ㅤ15.2%
||100071,84$ㅤ7.27%
||153407,07$ㅤ2.68%
||
||**Bottom 5:**
||27410,00$ㅤ 0.06%
||24390,00$ㅤ 0.06%
||28040,00$ㅤ 0.06%
||46480,00$ㅤ 0.06%
||29560,00$ㅤ 0.06%
||<br>
||<br>
||Valores únicos: **583**
||Número de registros: **1678**
||Valores nulos: **285**|
---

ㅤ     
Los registros presentan coma decimal e incluyen en el dato el simbolo ``$``.

ㅤ
**Propuesta de mejora:**

       > Cambiar ',' por '.'.

       > Eliminar también el símbolo '$'.
       
       > Modificar valor tipo 'objeto' a 'float'.

       > Inferior el valor de los nulos calculando el salario como ''monthlyincome' multiplicado por 12.

ㅤ
**Propuestas ejecutadas:**

- Todas las propuestas han sido ejecutadas.

ㅤ     

---
---

### roledepartament

|    dtype: object  |   Combinación de rol y departamento   |
|-----------|---------------|
||
||**Top 5:**
||NaNㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ 81.41%
|| Sales exECutIVE  -  Salesㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ ㅤ 0.12%
|| humAN resoURCEs  -  Human Resourcesㅤㅤㅤㅤ ㅤ 0.12%
|| labORAtoRy tEcHNICIAN  -  Research & Development 0.12%
|| hEalthCaRe reprEseNTaTiVe  -  Research & Development 0.12%
||<br>
||**Bottom 5:**
|| RESEArCH sCIenTIst  -  Research & Developmentㅤㅤ0.06%
|| hUMAn reSoUrCES  -  Human Resources ㅤ ㅤㅤㅤㅤ 0.06%
|| HUmAN rESOuRceS  -  Human Resources ㅤ ㅤㅤㅤㅤ 0.06%
|| SALEs REpRESentatIve  -  Sales ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ 0.06%
|| heaLtHcArE repResENtATiVe  -  Research & Development   0.06%
||<br>
||<br>
||Valores únicos: **301**
||Número de registros: **1678**
||Valores nulos: **1366**|
---

ㅤ     

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

ㅤ     

---
---

### numberchildren

|    dtype: float64  |   Número de hijos   |
|-----------|---------------|
||
||NaN  100.0
||<br>
||<br>
||Valores únicos: **0**
||Número de registros: **1678**
||Valores nulos: **1678**|
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

|    dtype: object  |   Indica si el empleado trabaja a distancia   |
|-----------|---------------|
||
||1ㅤㅤㅤㅤ22.35
||True ㅤㅤ 21.57
||Falseㅤㅤ 18.95
||0ㅤㅤㅤㅤ18.95
||Yesㅤㅤㅤ18.18
||<br>
||**Media:** 0.54
||**Mediana:** 1
||**Moda:** 1
||<br>
||Valores únicos: **5**
||Número de registros: **1678**
||Valores nulos: **0**
||Registros duplicados: **1673**|
---

No hay un formato concreto para el registro de la información de estas entradas. Presencia heterogénea de valores que no esclarecen, en una relación donde sólo necesita 2.

**Propuesta de mejora:**

       > Averiguar qué valor tiene 1 respecto a Yes/No, y 0 respectivamente.

       > Consultar con PO información respecto a las entradas de registro.

       > Estandarizar formato.

ㅤㅤ
**Propuestas ejecutadas**:

- Se han normalizado y estandarizado valores que no entraban en la norma. No obstante, ha subido la presencia de nulos.

ㅤ     
</details>


## 4. Cambios ejecutados

Propuestas ejecutadas generales y particulares a columnas concretas:

[Transformaciones]('ETL/Transformación.ipynb') | [Resultados, datos limpios]('files/raw_data_limpio.csv')

---

## 5. Nuestras cuestiones sobre los datos

Nuestras primeras preguntas para enfocar el análisis del proyecto: 

1. Rotación por Departamento y Rol:

       > ¿Hay roles críticos con alta rotación que requieran atención?

Identificar qué departamentos o roles tienen la mayor tasa de rotación.

2. Satisfacción Laboral y Rotación:


       > ¿Los empleados insatisfechos tienen mayor probabilidad de irse?
 
       > ¿Cómo afecta el equilibrio vida-trabajo en la rotación?

3. Compensación y Rotación:

       > ¿Los empleados con salarios más bajos tienen mayor rotación?

       > ¿Los empleados con menos opciones de acciones se van más?

4. Experiencia y Estabilidad Laboral:

       > ¿Los empleados con menos tiempo en la empresa tienen mayor rotación?

       > ¿Los empleados sin promociones recientes se van más?

5. Demografía y Rotación

       > ¿Los empleados más jóvenes tienen mayor rotación?

       > ¿Existen diferencias por género o estado civil?

6. Flexibilidad Laboral y Rotación:

       > ¿Los empleados que viajan con frecuencia tienen mayor rotación?

       > ¿El trabajo remoto reduce la rotación?

---

### 6. Pasos previos a la visualización de datos:


Hay evidencias de correlaciones positivas fuertes (con un valor mayor a 0.5) en varias variables. 

Muestran una correlación perfecta o casi perfecta (1.0000 o 0.9701), lo que podría indicar que son dependientes entre sí o, en su defecto, redundantes.

| Campo A                | Campo B                     | Coeficiente de correlación |
|---------------------------|--------------------------------|-------------|
| monthlyrate               | dailyrate                      | 1.0000      |
| hourlyrate                | monthlyrate                    | 1.0000      |
| dailyrate                 | hourlyrate                     | 1.0000      |
| hourlyrate                | joblevel                       | 0.9701      |
| joblevel                  | dailyrate                      | 0.9701      |
| joblevel                  | monthlyrate                    | 0.9701      |
| salary                    | hourlyrate                     | 0.8528      |
| monthlyrate               | salary                         | 0.8528      |
| dailyrate                 | salary                         | 0.8528      |
| salary                    | joblevel                       | 0.8295      |
| performancerating         | percentsalaryhike              | 0.7751      |
| joblevel                  | totalworkingyears             | 0.7727      |
| totalworkingyears         | hourlyrate                     | 0.7634      |
| totalworkingyears         | monthlyrate                    | 0.7634      |
| dailyrate                 | totalworkingyears             | 0.7634      |
| yearsatcompany            | yearswithcurrmanager           | 0.7571      |
| monthlyincome             | salary                         | 0.7453      |
| totalworkingyears         | age                            | 0.6687      |
| yearsatcompany            | totalworkingyears             | 0.6367      |
| monthlyrate               | monthlyincome                  | 0.6270      |
| hourlyrate                | monthlyincome                  | 0.6270      |
| monthlyincome             | dailyrate                      | 0.6270      |
| monthlyincome             | joblevel                       | 0.6151      |
| yearsatcompany            | yearssincelastpromotion        | 0.6118      |
| totalworkingyears         | monthlyincome                  | 0.5979      |
| salary                    | totalworkingyears             | 0.5979      |
| joblevel                  | yearsatcompany                 | 0.5324      |
| yearsatcompany            | dailyrate                      | 0.5221      |
| yearsatcompany            | hourlyrate                     | 0.5221      |
| yearsatcompany            | monthlyrate                    | 0.5221      |
| age                       | joblevel                       | 0.5074      |
| yearssincelastpromotion   | yearswithcurrmanager           | 0.5009      |
| hourlyrate                | age                            | 0.5007      |
| age                       | monthlyrate                    | 0.5007      |
| dailyrate                 | age                            | 0.5007      |
---
---

#### Resumen de valores atípicos (outliers)

Las siguientes variables presentan un número considerable de valores atípicos, indicando alta dispersión:
 | Variable                  | Nº de outliers |
 |---------------------------|----------------|
 | trainingtimeslastyear     | 268            |
 | performancerating         | 214            |
 | yearssincelastpromotion   | 116            |
 | yearsatcompany            | 114            |
 | numcompaniesworked        | 59             |
 | totalworkingyears         | 42             |
 | distancefromhome          | 40             |
 | dailyrate                 | 18             |
 | hourlyrate                | 18             |
 | monthlyrate               | 18             |
 | yearswithcurrmanager      | 16             |
 | salary                    | 15             |
 | monthlyincome             | 11             |

---
---
## 7. Visualización como respuesta

       .


---
---


## 8. NEXT STEPS: pasos a futuro

La **Auditoría de Bienestar** ha revelado que la baja calidad de los datos tiene un impacto **ético y económico** directo:

Nos impide ver la inestabilidad en los ecosistemas empresariales y las grietas en el rendimiento de los trabajadores. 

Una sucesión de errores tipográficos en una jornada o el dato nulo en escalas de satisfacción críticas, puede ser alguien de nuestro personal al que estamos dejando de prestar atención, puede que sea incluso recíproco.

Por todo esto, concluimos que **la precisión técnica es un imperativo ético**.

### Propuesta de valor: 

### La fiabilidad del Modelo (I+D):

Al limpiar y estandarizar la fuente, la estructura de código está preparada para una escalabilidad de procesos completos ETL, con fin a la carga de la información transformada en bases de datos.

Esto significa que si *ABC Corporation* utiliza este dataset saneado para entrenar un modelo de retención, ese modelo será más justo y preciso, reduciendo el riesgo de sesgo algorítmico.

Es una arquitectura de código escalable y replicable en otras localizaciones, lista para optimizar la gestión del talento.

Un ejemplo es nuestra visualización del campo ``worklifebalance``:

>Muestra que el 60% de los empleados se concentra en los niveles 1 y 2. 

Una IA solo puede optimizar el talento si sabe que el problema principal no es el salario, sino el desgaste. 

Esto es el insight humano que el dato limpio nos permite ver.
		
### Plan de Auditoría Continua: 

Enlaza la limpieza de datos con la fiabilidad de futuras implementaciones de IA. 

> “La IA es tan ética como los datos que la entrenan. 

    
Proponemos blindar validaciones estrictas en el sistema back-end en el formulario de recogida de datos para evitar las anomalías encontradas y así entrenar modelos de retención más justos.

### Refuerzo de la recolección de datos

Recomendamos implementar **validaciones estrictas en el back-end** del sistema de gestión de talento:

- Eliminando la posibilidad de ``input``erróneo. Por ejemplo, que la columna maritalstatus no pueda aceptar 'marreid' y el sistema fuerce el valor a 'Married' o que no permita dejar el valor nulo en categorías fundamentales”.

### Ampliación del marco ético:

Implementar la **propuesta ética** de gender (incluir la opción 'Other' o 'Non-Binary') como estándar.

Este paso y otros no es solo limpieza, es un abanico abierto para un análisis más exhaustivo de parámetros que pueden estar quedándose fuera en la gestión de talento.

### Plan de auditoría continua

La limpieza que hemos realizado en la Fase 2 es vital, pero es **solo el principio**. 

El riesgo de **data drift*** es constante porque **la cultura de una empresa es orgánica**. 

Por eso, proponemos la creación de un *Plan de Auditoría Continua*, para garantizar que los modelos de IA que se desarrollen tengan la garantía de la toma de decisiones basada en la realidad actual de los empleados, no en la historia almacenada. 

Esto transforma nuestra Fase 2 **de ser un "parche" a ser un "sistema de control de calidad" indispensable** para el futuro de la empresa”.

**data drift*: ocurre cuando las propiedades estadísticas de los datos cambian con el tiempo de forma inesperada (el mundo cambia, y los datos por ende. Es la principal razón por la que los modelos de Inteligencia Artificial (IA) y de Machine Learning pierden precisión después de un tiempo, incluso si fueron entrenados perfectamente).


### Normalización y Documentación

- Glosario de Valores: Sería necesario un glosario que defina explícitamente el significado de cada valor en las escalas utilizadas (ej. ‘1: Insatisfecho’, ‘4: Muy satisfecho’).

- Convención de Escala: Documentar formalmente el uso de los valores 0 y 5 en las escalas, aunque no aparezcan en los registros actuales.

### Futuras visualizaciones 

- Mejorar la presentación de datos mediante gráficos y dashboards interactivos, facilitando la interpretación y toma de decisiones. 

Usando tecnologías como *PowerBI* y *Tableau+*.


