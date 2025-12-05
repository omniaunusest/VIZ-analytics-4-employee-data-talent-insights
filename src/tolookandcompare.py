import pandas as pd

def transform_info(df: pd.DataFrame, columna: str) -> None:
    """
    Imprime estadísticas básicas y descriptivas de una columna de un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame de pandas.
        columna (str): Nombre de la columna a analizar.

    Example:
        >>> transform_info(df, "monthlyrate")
        Valores únicos: 10
        Número de registros: 100
        Valores nulos: 2
        Registros duplicados: 5
        dtype: int64
        ----------------
        Porcentajes:
        ...
        Media: 50.00
        Mediana: 45.00
        Moda: 30
    """
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    stats = df[columna].agg({
        'Mean': 'mean',
        'Median': 'median',
        'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
    })

    print(f"Valores únicos: {valores_unicos}\nNúmero de registros: {num_registros}\nValores nulos: {valores_nulos}\nRegistros duplicados: {duplicados}\ndtype: {dtype}")
    print('----------------')
    print("\nPorcentajes:")
    print(df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2).sort_values(ascending=False))
    print("\nEstadísticas descriptivas")
    print("---------------------------------")
    print(f"Media: {stats['Mean']:.2f}")
    print(f"Mediana: {stats['Median']:.2f}")
    print(f"Moda: {stats['Mode']}")

def to_doc_info(df: pd.DataFrame, columna: str) -> str:
    """
    Genera un reporte formateado con estadísticas descriptivas y frecuencias de una columna de un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame de pandas.
        columna (str): Nombre de la columna a analizar.

    Returns:
        str: Reporte formateado con estadísticas y frecuencias.

    Example:
        >>> reporte = to_doc_info(df, "monthlyrate")
        >>> print(reporte)
    """
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2).sort_values(ascending=False)
    tabla_frecuencias = "\n".join([f"||{idx}  {val}" for idx, val in frecuencias.items()])

    stats = df[columna].agg({
        'Mean': 'mean',
        'Median': 'median',
        'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
    })

    reporte = f"""
|    dtype: {dtype}  |   {columna}   |
|-----------|---------------|
{tabla_frecuencias}

||Media: {stats['Mean']:.2f}
||Mediana: {stats['Median']:.2f}
||Moda: {stats['Mode']}
||<br><br>Valores únicos: **{valores_unicos}**<br>Número de registros: **{num_registros}**<br>Valores nulos: **{valores_nulos}**<br>Registros duplicados: **{duplicados}**|
---
"""
    return reporte

def transform_headtail(df: pd.DataFrame, columna: str) -> None:
    """
    Imprime estadísticas básicas, descriptivas y los 5 valores más/menos frecuentes de una columna.

    Args:
        df (pd.DataFrame): DataFrame de pandas.
        columna (str): Nombre de la columna a analizar.

    Example:
        >>> transform_headtail(df, "monthlyrate")
        Valores únicos: 10
        Número de registros: 100
        Valores nulos: 2
        Registros duplicados: 5
        dtype: int64
        ----------------
        ...
        Media: 50.00
        Mediana: 45.00
        Moda: 30
    """
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    stats = df[columna].agg({
        'Mean': 'mean',
        'Median': 'median',
        'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
    })

    print(f"Valores únicos: {valores_unicos}\nNúmero de registros: {num_registros}\nValores nulos: {valores_nulos}\nRegistros duplicados: {duplicados}\ndtype: {dtype}")
    print('---------------------------------')
    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    print(frecuencias.head(5))
    print(frecuencias.tail(5))
    print("---------------------------------")
    print(f"Media: {stats['Mean']:.2f}")
    print(f"Mediana: {stats['Median']:.2f}")
    print(f"Moda: {stats['Mode']}")

def to_doc_headtail(df: pd.DataFrame, columna: str) -> str:
    """
    Genera un reporte formateado con estadísticas descriptivas y los 5 valores más/menos frecuentes de una columna.

    Args:
        df (pd.DataFrame): DataFrame de pandas.
        columna (str): Nombre de la columna a analizar.

    Returns:
        str: Reporte formateado con estadísticas y top/bottom 5.

    Example:
        >>> reporte = to_doc_headtail(df, "monthlyrate")
        >>> print(reporte)
    """
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    top5 = "\n".join([f"||{idx}  {val}%" for idx, val in frecuencias.head(5).items()])
    bottom5 = "\n".join([f"||{idx}  {val}%" for idx, val in frecuencias.tail(5).items()])

    stats = df[columna].agg({
        'Mean': 'mean',
        'Median': 'median',
        'Mode': lambda x: x.mode().iloc[0] if not x.mode().empty else None
    })

    reporte = f"""
|    dtype: {dtype}  |   {columna}   |
|-----------|---------------|
||Top 5:
{top5}
||Bottom 5:
{bottom5}
||<br>
||Media: {stats['Mean']:.2f}
||Mediana: {stats['Median']:.2f}
||Moda: {stats['Mode']}
<br><br>Valores únicos: **{valores_unicos}**<br>Número de registros: **{num_registros}**<br>Valores nulos: **{valores_nulos}**<br>Registros duplicados: **{duplicados}**|
---
"""
    return reporte
