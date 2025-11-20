# Memoria Proyecto ABC Corporation

### Conclusiones del Análisis Exploratorio de Datos (**EDA**)

El archivo *.csv* proporcionado para el proyecto presenta las siguientes columnas con datos:

    ['age',
    'attrition',
    'businesstravel',
    'dailyrate',
    'department',
    'distancefromhome',
    'education',
    'educationfield',
    'employeecount',
    'employeenumber',
    'environmentsatisfaction',
    'gender',
    'hourlyrate',
    'jobinvolvement',
    'joblevel',
    'jobrole',
    'jobsatisfaction',
    'maritalstatus',
    'monthlyincome',
    'monthlyrate',
    'numcompaniesworked',
    'over18',
    'overtime',
    'percentsalaryhike',
    'performancerating',
    'relationshipsatisfaction',
    'standardhours',
    'stockoptionlevel',
    'totalworkingyears',
    'trainingtimeslastyear',
    'worklifebalance',
    'yearsatcompany',
    'yearsincurrentrole',
    'yearssincelastpromotion',
    'yearswithcurrmanager',
    'sameasmonthlyincome',
    'datebirth',
    'salary',
    'roledepartament',
    'numberchildren',
    'remotework']

En las que se observan los siguientes patrones y características:

**age**     
Edad del empleado
> presenta números y ('51', '52'...) y palabras ('fifty-five').

propuesta de mejora:
> .

**attrition**   
Indica si el empleado dejó la empresa (Yes/No)
> .

propuesta de mejora:
> .

**businesstravel**  
Frecuencia de viajes
> .

propuesta de mejora:
> .

**dailyrate**   
Tarifa diaria estimada para clientes, calculada en base al salario

> .

propuesta de mejora:
> 

**department**
Departamento en el que trabaja el empleado
> .

propuesta de mejora:
> .

**distancefromhome**
Distancia en millas o kilómetros desde el hogar al trabajo
> .

propuesta de mejora:
> .

**education**   
Nivel educativo del empleado en escala numérica
> .

propuesta de mejora:
> .

**educationfield**  
Campo de estudio académico del empleado
> .

propuesta de mejora:
> .

**employeecount**   
Valor constante de "1", indicando un solo empleado por registro
> .

propuesta de mejora:
> .

**employeenumber**
Número de identificación del empleado
> .

propuesta de mejora:
> .

**environmentsatisfaction** 
Nivel de satisfacción con el ambiente laboral
> .

propuesta de mejora:
> .

**gender**  
Género del empleado
> .

propuesta de mejora:
> .

**hourlyrate**  
Tarifa por hora calculada
> .

propuesta de mejora:
> .

**jobinvolvement**
Nivel de compromiso del empleado en el trabajo
> .

propuesta de mejora:
> .

**joblevel**
Nivel jerárquico del puesto del empleado
> .

propuesta de mejora:
> .

**jobrole**
Función o rol específico del empleado
> .

propuesta de mejora:
> . 


**jobsatisfaction**
Satisfacción general en el puesto
> .

propuesta de mejora:
> . 

**maritalstatus**
Estado civil (e.g., Single, Married)
> .

propuesta de mejora:
> . 

**monthlyincome**
Ingreso mensual estimado en base al salario anual
> .

propuesta de mejora:
> . 

**monthlyrate**
Tarifa mensual estimada en función de la tarifa diaria
> .

propuesta de mejora:
> . 

**numcompaniesworked**
Número de empresas previas en las que ha trabajado
> .

propuesta de mejora:
> . 

  
**over18**  
Columna no definida
> .

propuesta de mejora: 
> .

**overtime**  
Indica si el empleado trabaja horas extras (Yes/No)
> . 

propuesta de mejora: 
> . 


**percentsalaryhike** 
Incremento porcentual en el salario
> . 

propuesta de mejora: 
> . 


**performancerating** 
Evaluación de desempeño en una escala numérica 
> . 

propuesta de mejora: 
> . 


**relationshipsatisfaction** 
Satisfacción con relaciones interpersonales en el trabajo
> . 

propuesta de mejora: 
> . 


**standardhours**  
Clasificación de jornada (Full Time/Part Time)
> . 

propuesta de mejora: 
> . 


**stockoptionlevel** 
Nivel de opciones sobre acciones asignadas 
> . 

propuesta de mejora: 
> . 


**totalworkingyears** 
Años totales de experiencia laboral 
> . 

propuesta de mejora: 
> . 


**trainingtimeslastyear** 
Número de sesiones de entrenamiento en el último año 
> . 

propuesta de mejora: 
> . 


**worklifebalance**  
Nivel de balance entre vida personal y laboral
> . 

propuesta de mejora: 
> . 


**yearsatcompany**  
Años en la empresa actual.
> .

propuesta de mejora:
> . 


**yearsincurrentrole**
> . Valores = array([nan, '13,0', '12,0', '11,0', '7,0', '6,0', '4,0', '3,0', '2,0',
       '1,0', '0,0'], dtype=object)

Tipo de dato = Object

propuesta de mejora:
> .  
# 1. Reemplazar la "," por "."
df["yearsincurrentrole"] = df["yearsincurrentrole"].str.replace(',', '.')
# 2. Convertir a numérico (los errores se vuelven NaN)
df["yearsincurrentrole"] = pd.to_numeric(df["yearsincurrentrole"], errors='coerce')
# 3. Rellenar los vacíos con 0
df["yearsincurrentrole"] = df["yearsincurrentrole"].fillna(0)
# 4. Ahora sí, pasar a entero sin miedo
df["yearsincurrentrole"] = df["yearsincurrentrole"].astype(int)
  

**yearssincelastpromotion**
> . Valores = [15, 11,  5,  2,  4,  7,  0,  1, 13, 14,  8, 12,  3,  6, 10,  9]

Tipo de dato = float

propuesta de mejora:
> . En principio nada


**yearswithcurrmanager**
> . Valores = [15,  9,  6,  8,  7, 11, 10, 12,  4,  0,  5, 17,  2, 14,  1, 13,  3, 16]

Tipo de dato = float

propuesta de mejora:
> . En principio nada


**sameasmonthlyincome**  
> . Valores = Datos tipo objeto, con simbolo en "Español" para los decimales y además incluido en el dato el simbolo $

propuesta de mejora:
> .  Cambiar la "," por ".", eliminar también el simbolo "$". Por último cambiar el dato str en float

df["sameasmonthlyincome"] = df["sameasmonthlyincome"].str.replace(',', '.')
df["sameasmonthlyincome"] = df["sameasmonthlyincome"].str.replace('$', '', regex=False)
df["sameasmonthlyincome"] = df["sameasmonthlyincome"].astype(float)



**datebirth**  
Año de nacimiento del empleado
> . Valores = [1972, 1971, 1981, 1976, 1977, 1975, 1964, 1982, 1967, 1985, 1968,
       1983, 1965, 1988, 1978, 1990, 1987, 1989, 1970, 1980, 1963, 1991,
       1986, 1974, 1984, 1973, 1979, 1993, 1994, 1992, 1969, 1966, 1996,
       1995, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005]

Tipo de dato = float

propuesta de mejora:
> . En principio nada


**salary**  
Salario anual calculado para el empleado
> . Valores = Datos tipo objeto, con simbolo en "Español" para los decimales y además incluido en el dato el simbolo $

propuesta de mejora:
> . Cambiar la "," por ".", eliminar también el simbolo "$". Por último cambiar el dato str en float

df["salary"] = df["salary"].str.replace(',', '.')
df["salary"] = df["salary"].str.replace('$', '', regex=False)
df["salary"] = df["salary"].astype(float)


**roledepartament**  
Combinación de rol y departamento.
> . df["roledepartament"].value_counts().sum() el resultado es 312 nombres distintos pero hay muchos que son lo mismo pero cambiando mayusculas y minusculas

propuesta de mejora:

> .df["roledepartament"].str.lower()
    
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


**numberchildren**  
Número de hijos del empleado
> . Valores = [nan]

propuesta de mejora:
> . Posible columna a eliminar


**remotework**  
Empleado trabaja de forma remota Si/No
> . Valores =[ 'Yes', '1', 'False', '0', 'True']

Todos son str aunque haya número de por medio. Quizás el 0 signifique Si/Yes y el 1 signifique No. También es posible que el True sea igual a Si/Yes y el False sea No
propuesta de mejora:
> . unificar datos