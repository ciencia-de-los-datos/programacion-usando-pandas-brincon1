"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    numFilas = len(tbl0)
    return numFilas

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    numCol = tbl0.columns
    x = len(numCol)

    return x

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    x = tbl0["_c1"].value_counts().sort_index() 

    return x

def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    x=tbl0.groupby("_c1")["_c2"].mean()

    return x

def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    x = tbl0.groupby("_c1")["_c2"].max()
    return x

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    x = tbl1["_c4"].sort_values().unique()
    y = list(map(lambda x: x.upper(), x))
    return y


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    x = tbl0.groupby("_c1")["_c2"].sum()
    return x


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    tbl0["suma"] = tbl0["_c0"] + tbl0["_c2"]
    return tbl0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    tbl0["year"] = tbl0["_c3"].map(lambda x: x.split("-")[0])
    return tbl0

def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
#Forma número 1
    #convierto a cadena 
    #tbl0["x"] = tbl0["_c2"].apply(str)
    # def listaUnida(df):
    #     lis = list(df["x"])
    #     lis.sort()
    #     lis = ":".join(lis)
    #     return lis

    # x = tbl0.groupby("_c1").apply(listaUnida)
    # x = pd.DataFrame(x)
    # #x = x.rename_axis("_c1")
    # x = x.rename(columns={0: "_c2"})
    # x = pd.DataFrame(x)

# Forma número 2
    #convierto a cadena 
    tbl0["x"] = tbl0["_c2"].apply(str)
    #sumo la cadena de los números de tal forma que se peguen los números
    x = tbl0.groupby("_c1")["x"].sum() # mas cerca
    #hago un for para dividir eso números con una lista, luego los ordeno y los uno con :.
    s = []
    for y in x:
        y = list(y)
        y.sort()
        y = ":".join(y)
        s.append(y)

    #creo la lista de las letras ordenada, se que va a asociarse bien con la columna c2 porque 
    #cuando se aplico el groupby y el sum, quedo ordenado por lo que resta unirlas
    letras = tbl0["_c1"].sort_values().unique()
    #uno las letras ordenadas y la columna ordenada y unida con el join, que se hizo en el for
    #renombro las columnas y luego le digo que el indice es la columna _c1
    x = pd.DataFrame(zip(letras, s))
    x = x.rename(columns={1: "_c2", 0:"_c1"})
    x = x.set_index("_c1")

    return x

# Forma número tres, en lugar de de hacer el sum en el groupby creo directamente el diccionario, 
# esto ayuda a que en el for no se tenga que dividir sino que se haga la unión de una vez.
# además se ordenan de una vez los valores del diccionario y se trabaja con las claves.

# tbl0["x"] = tbl0["_c2"].apply(str)
# dicc = (tbl0.sort_values(["x"], ascending=True).groupby("_c1")["x"].apply(list).to_dict())
# print(dicc)

# listaNumeros = list(dicc.keys())
# x = list(dicc.values())

# s = []
# for y in x:
#     y = ":".join(y)
#     s.append(y)

# print(s)

# x = pd.DataFrame(zip(listaNumeros, s))
# x = x.rename(columns={1: "_c2", 0:"_c1"})
# x = x.set_index("_c1")

# print(x)


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    dicc = (tbl1.sort_values(["_c4"], ascending=True).groupby("_c0")["_c4"].apply(list).to_dict())

    listaNumeros = list(dicc.keys())
    x = list(dicc.values())

    s = []
    for y in x:
        y = ",".join(y)
        s.append(y)

    num = tbl1["_c0"].sort_values()

    x = pd.DataFrame(zip(listaNumeros, s))
    x = x.rename(columns={1: "_c4", 0:"_c0"})
    #x = x.set_index("_c1")

    return x

def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    #uno las dos columnas con : y aplico cadena para que deje hacerlo
    tbl2["uniCol"] = tbl2["_c5a"] + ":" + tbl2["_c5b"].apply(str)
    #creo un diccionario
    dicc = (tbl2.sort_values(["uniCol"], ascending=True).groupby("_c0")["uniCol"].apply(list).to_dict())

    #Saco las claves y valores
    listaNumeros = list(dicc.keys())
    x = list(dicc.values())

    #hago un for para quitar las listas de cada valor de tal forma que queden unidos en una sola lista
    # entonces itero en esas sublistas, y las uno mediante coma y las agrego a una lista para que queden en una sola lista.
    s = []
    for y in x:
        y = ",".join(y)
        s.append(y)

    #creo un dataframe con las dos lista, de claves que estan en una sola lista y de los valores que se aco de convertir
    x = pd.DataFrame(zip(listaNumeros, s))
    x = x.rename(columns={1: "_c5", 0:"_c0"})
   
    return x

def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    union = tbl0.set_index("_c0", inplace=True)
    union = tbl2.set_index("_c0", inplace=True)

    union = pd.concat(objs=[tbl0, tbl2,], axis=1)

    x = union.groupby("_c1")["_c5b"].sum()

    return x

# union = tbl0.set_index("_c0", inplace=True)
# union = tbl2.set_index("_c0", inplace=True)

# union = pd.concat(objs=[tbl0, tbl2,], axis=1)

# x = union.groupby("_c1")["_c5b"].sum()
# print(x)



