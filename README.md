# C2_Problem_based_learning

Programa que recibe un archivo .txt y un largo máximo de línea, justifica el texto y lo guarda en un archivo.

## Uso

El programa se ejecuta con los siguientes argumentos:
```
python main.py path max_width --sobreescribir
```

Donde cada argumento significa:
```
path: str           -> Path al archivo .txt a justificar
max_width: int      -> Máximo largo de cada línea
sobreescribir: bool -> Si se activa, el archivo se sobreescribe, si no, se crea uno nuevo
```

## Ejemplo

Consideremos el siguiente texto en el archivo `lorem_ipsum.txt`:
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non felis vitae tortor tempor elementum. Mauris sed finibus neque, quis consectetur ligula. In vel lectus ultricies, semper tellus ullamcorper, pretium arcu. Duis ac sodales libero, id facilisis arcu. Quisque a tortor nec lacus lobortis tempus. Sed dapibus posuere eleifend. Aenean finibus vel nunc a finibus. Etiam a elit congue, aliquet nisl eu, consectetur justo. Phasellus ut hendrerit mi, sit amet vehicula nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse potenti. Donec pharetra iaculis nibh, ut pharetra ante viverra et. Suspendisse convallis eu urna a pulvinar. Nullam.
```

Al ejecutar el comando
```
python main.py lorem_ipsum.py 75
```

se genera el archivo `lorem_ipsum_formateado.txt` con el texto:
```
Lorem  ipsum  dolor  sit  amet,  consectetur  adipiscing  elit. Quisque non
felis  vitae  tortor  tempor  elementum.  Mauris  sed  finibus  neque, quis
consectetur  ligula.  In  vel  lectus ultricies, semper tellus ullamcorper,
pretium   arcu.   Duis  ac  sodales  libero,  id  facilisis  arcu.  Quisque
a   tortor  nec  lacus  lobortis  tempus.  Sed  dapibus  posuere  eleifend.
Aenean  finibus  vel  nunc  a  finibus.  Etiam  a elit congue, aliquet nisl
eu,  consectetur  justo.  Phasellus  ut  hendrerit  mi,  sit  amet vehicula
nunc.  Interdum  et  malesuada  fames  ac  ante  ipsum  primis in faucibus.
Suspendisse   potenti.   Donec   pharetra   iaculis   nibh,   ut   pharetra
ante  viverra  et.  Suspendisse  convallis  eu  urna  a  pulvinar.  Nullam.
```