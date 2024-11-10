## Ejercicio: Juegos Olímpicos

### Esquema de BD

`JUEGO<año_olimpiada, pais_olimpiada, nombre_deportista, pais_deportista, nombre_disciplina, asistente>`

### Restricciones

a. `pais_olimpiada` es el país donde se realizó el juego olímpico del año correspondiente.
b. `pais_deportista` es el país que representa el deportista.
c. Un deportista representa en todos los juegos olímpicos siempre al mismo país. Por un país, participan varios deportistas cada juego olímpico.
d. En un año determinado se hacen los juegos olímpicos en un solo país, pero en un país pueden haberse jugados varios juegos olímpicos en diferentes años.
e. Cada deportista puede participar en varios juegos olímpicos y en varias disciplinas en diferentes juegos olímpicos. Pero en un juego olímpico solamente participa en una disciplina.
f. Un deportista tiene un asistente en cada juego olímpico, pero puede variar en diferentes juegos.

### Paso 1: Determinar las Dependencias Funcionales (DFs)

A partir del esquema y las restricciones dadas, se pueden determinar las siguientes dependencias funcionales:

1. **año_olimpiada -> pais_olimpiada**: Cada año los juegos olímpicos se llevan a cabo en un único país anfitrión, por lo que `pais_olimpiada` depende funcionalmente de `año_olimpiada`.
   
2. **nombre_deportista -> pais_deportista**: Dado que un deportista representa siempre al mismo país en todos los juegos, `pais_deportista` depende funcionalmente de `nombre_deportista`.

3. **año_olimpiada, nombre_deportista -> asistente**: Cada deportista puede tener un asistente distinto en cada juego olímpico, por lo que el `asistente` depende de la combinación de `año_olimpiada` y `nombre_deportista`.

4. **año_olimpiada, nombre_deportista -> nombre_disciplina**: Un deportista participa en solo una disciplina en cada juego olímpico, por lo que `nombre_disciplina` depende funcionalmente de la combinación `año_olimpiada` y `nombre_deportista`.

### Paso 2: Determinar las Claves Candidatas

Para determinar las **claves candidatas**, buscamos el conjunto mínimo de atributos que identifique de forma única cada registro en la tabla `JUEGO`.

- La combinación **`año_olimpiada`, `nombre_deportista`** es suficiente para identificar de manera única cada registro, ya que:
  - `año_olimpiada` especifica el año de la olimpiada.
  - `nombre_deportista` identifica de forma única al participante en esa olimpiada.

Por lo tanto, la **clave candidata** es:

- (`año_olimpiada`, `nombre_deportista`)

### Paso 3: Diseño en Tercera Forma Normal (3FN)

Para alcanzar la **Tercera Forma Normal (3FN)**, eliminamos dependencias transitivas y nos aseguramos de que cada atributo no clave dependa únicamente de la clave primaria completa.

El diseño en 3FN se logra dividiendo la tabla original en cuatro tablas (`Olimpiada`, `Deportista`, `Disciplina`, y `Participacion`) para eliminar dependencias transitivas y asegurar la integridad de los datos.

El diseño en 3FN sería el siguiente:

1. **Tabla `Juegos`**
   - `año_olimpiada` (Clave primaria)
   - `pais_olimpiada`

2. **Tabla `Deportistas`**
   - `nombre_deportista` (Clave primaria)
   - `pais_deportista`

3. **Tabla `Disciplina`**
   - `nombre_disciplina` (Clave primaria)

4. **Tabla `Participacion`**
   - `año_olimpiada` (Clave foránea que referencia `Olimpiada`)
   - `nombre_deportista` (Clave foránea que referencia `Deportista`)
   - `nombre_disciplina` (Clave foránea que referencia `Disciplina`)
   - `asistente`
   - Clave primaria compuesta: (`año_olimpiada`, `nombre_deportista`)
