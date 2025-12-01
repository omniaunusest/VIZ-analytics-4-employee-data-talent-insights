## Guía de 'estilo'

**Formato para crear tablas en markdown:**

|    T   |   D   |
| ----------- | ----------- |
| dtype: | Linea <br><br> Linea |
---

**Recurso de espacio: **    
En caso de espaciado predeterminado, se usará éste por defecto.

    ㅤㅤ                                (ㅤㅤ) 
    
                        entre paréntesis hay un caracter en blanco

---
---

### Función para devolver conteo, registros únicos y duplicados en documento de Memoria

( ! ) Hay que tener en cuenta que no es lo mismo un duplicado que una entrada que se repite, no siempre la devolución es un dato **significativo** para nosotras:

    def dataconduplo(df, columna):
        valores_unicos = df[columna].nunique()
        num_registros = len(df[columna])
        duplicados = num_registros - valores_unicos``

        print(f"Valores únicos: **{valores_unicos}**<br>Número de registros: **{num_registros}**<br><br>Registros duplicados: **{duplicados}**")

        print('----------------')

        print("\nPorcentajes:")
        print(df[columna]
        .value_counts(normalize=True, dropna=False)
        .mul(100)
        .round(2)
        .sort_values(ascending=False))

USO: ``dataconduplo(df, "employeenumber")``</center>