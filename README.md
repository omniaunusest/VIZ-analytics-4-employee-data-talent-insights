# proyecto-DA-promo-60-modulo-3-team-2

# Análisis de Datos de Recursos Humanos para ABC Corporation

Este repositorio contiene el análisis de datos realizado para la empresa **ABC Corporation** como parte de un proyecto académico para Adalab. El objetivo principal es identificar los factores clave que influyen en la satisfacción laboral y la retención de empleados.

## Resumen del Proyecto

En el competitivo entorno empresarial actual, la retención de talento es crucial. **ABC Corporation**, una consultora tecnológica especializada en IA y *machine learning*, nos ha contratado para analizar sus datos de recursos humanos. Nuestra misión es descubrir qué factores afectan la satisfacción de los empleados y provocan la rotación de personal, para así poder ofrecer recomendaciones que ayuden a la empresa a mejorar su ambiente laboral y retener a sus mejores talentos.

Este proyecto no solo tiene una finalidad técnica, sino también ética: asegurar que los datos que alimentan los sistemas de inteligencia artificial de gestión de talento sean justos y no contengan sesgos que puedan perjudicar la equidad en el entorno laboral.

## Objetivos

Los objetivos de este proyecto se dividen en dos enfoques principales:

1.  **Saneamiento y Solidez del Dato (El Cimiento Técnico):**
    *   Realizar una auditoría y limpieza exhaustiva del conjunto de datos de recursos humanos.
    *   Estandarizar y transformar los datos para garantizar su calidad e integridad.
    *   Diseñar una base de datos relacional para centralizar la información de forma estructurada.
    *   (Bonus) Desarrollar un proceso ETL (Extracción, Transformación y Carga) para automatizar la actualización de los datos.

2.  **Auditoría de Bienestar y Retención (El Valor Estratégico):**
    *   Analizar los datos limpios para identificar los factores de riesgo que impulsan la rotación de personal.
    *   Generar visualizaciones que permitan a la empresa comprender de forma clara las tendencias y áreas de mejora.
    *   Proporcionar un informe con conclusiones y recomendaciones para la toma de decisiones estratégicas.

## Fases del Proyecto

El proyecto se ha desarrollado siguiendo una metodología ágil, dividida en las siguientes fases:

1.  **Análisis Exploratorio de Datos (EDA):** Comprensión inicial del conjunto de datos y sus características.
2.  **Transformación de Datos:** Limpieza, normalización y corrección de inconsistencias en los datos.
3.  **Visualización de Datos:** Creación de gráficos para representar los hallazgos de manera clara y efectiva.

## El Conjunto de Datos

El conjunto de datos contiene información anonimizada sobre los empleados de ABC Corporation, incluyendo variables como:

*   Datos demográficos (edad, género).
*   Rol en la empresa (departamento, puesto, nivel).
*   Satisfacción y bienestar (satisfacción laboral, equilibrio vida-trabajo).
*   Salario y compensaciones.
*   Antigüedad y rotación (`Attrition`).

Para un análisis detallado de cada columna y las transformaciones realizadas, puedes consultar el documento [Memoria.md](Memoria.md).

## Hallazgos y Visualizaciones Clave

A continuación, se presentan algunas de las visualizaciones más relevantes generadas durante el análisis.

### Tasa de Rotación por Departamento

![Tasa de Rotación por Departamento](Imagenes/attrition_percentage_by_department.png)

El departamento de **Ventas (Sales)** presenta la tasa de rotación más alta, seguido de cerca por **Recursos Humanos (Human Resources)**. Aunque **Investigación y Desarrollo (Research & Development)** tiene el mayor número de renuncias en términos absolutos, su tasa de rotación es menor en proporción.

### Ingreso Mensual por Departamento y Rotación

![Ingreso Mensual por Departamento y Rotación](Imagenes/income_department_attrition_violin.png)

Este gráfico de violín muestra que en departamentos como **Ventas** y **Recursos Humanos**, los empleados que renuncian (`attrition = yes`) tienden a tener ingresos mensuales más bajos en comparación con los que se quedan.

### Rotación por Rol de Trabajo

![Rotación por Rol de Trabajo](Imagenes/Rotación%20Vs%20JobRole.png)

Los roles con mayor tasa de rotación son los **Representantes de Ventas (Sales Representative)** y los **Técnicos de Laboratorio (Laboratory Technician)**.

## Cómo Utilizar este Repositorio

Para explorar el análisis, puedes seguir estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-del-repositorio>
    ```

2.  **Instala las dependencias:**
    Asegúrate de tener instaladas las siguientes librerías de Python:
    ```
    pip install pandas numpy matplotlib seaborn scipy
    ```

3.  **Explora los notebooks:**
    Los análisis se encuentran en los siguientes cuadernos de Jupyter:
    *   `EDA-primera-ronda.ipynb`, `EDA-segunda-ronda.ipynb`, `EDA-tercera-y-última.ipynb`: Contienen el análisis exploratorio de datos.
    *   `Transformación.ipynb`: Detalla el proceso de limpieza y transformación de los datos.
    *   `visualizaciones.ipynb`: Contiene el código para generar las visualizaciones.

## Equipo

Este proyecto fue realizado por el **Equipo 2** de la promoción 60 del bootcamp de Data Analytics de Adalab, que está formado por Andrea R. Virgós, Claudia Cervantes, Mayka Durán, Ona Zaragoza y Patricia Merchán
