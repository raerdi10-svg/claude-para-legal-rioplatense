---
name: busqueda-marca
description: >
  Primera pasada de clearing marcario. Analiza el signo a registrar (descriptividad,
  genericidad, distintividad), identifica knock-outs probables en el DNPI (Uruguay) o
  el INPI (Argentina), aplica heurísticas de confusión fonética, gráfica y conceptual,
  y produce un dictamen de riesgo de oposición con recomendación sobre procedencia del registro.
argument-hint: "[signo marcario y clase(s) Nice a registrar]"
user-invocable: true
---

# Skill: Búsqueda y Clearing de Marca — Primera Pasada

## Propósito

Realizar una primera pasada de análisis de viabilidad de registro de un signo marcario,
identificando los principales riesgos de irregistrabilidad absoluta y los posibles
conflictos con marcas preexistentes (knock-outs). El resultado es un dictamen de riesgo
con recomendación sobre si proceder con el registro, ajustar el signo, o abstenerse de
registrar hasta realizar una búsqueda formal en la base oficial.

**Advertencia permanente:** Este análisis es una primera aproximación basada en heurísticas
y conocimiento general. Siempre debe complementarse con una búsqueda formal en las bases
de datos del DNPI (Uruguay) o del INPI (Argentina) antes de tomar una decisión de registro.

---

## Paso 0 — Recolección de datos

Solicitar al abogado:

1. **El signo marcario** que se pretende registrar:
   - Si es una marca denominativa (solo palabras): texto exacto.
   - Si es una marca figurativa (solo imagen): descripción detallada del diseño.
   - Si es una marca mixta (texto + imagen): texto y descripción de los elementos gráficos.
   - Si hay un color reivindicado: indicarlo.
   - Si es una marca tridimensional, sonora o de posición: descripción específica.

2. **Clase(s) de la Clasificación Internacional de Niza (11.ª edición)** en las que se
   pretende registrar. Si el cliente no las conoce, solicitar una descripción de los
   productos o servicios para clasificarlos.

3. **Jurisdicción(es):** ¿Uruguay (DNPI), Argentina (INPI), o ambas?

4. **Sector del cliente y mercado objetivo** (ayuda a identificar marcas competidoras
   relevantes).

5. **¿El signo ya está en uso?** ¿Desde cuándo? ¿El cliente lo usa actualmente en Uruguay
   o Argentina?

6. **¿Hay alguna marca conocida del sector que el cliente ya identificó como potencial
   conflicto?** (Esto no reemplaza el análisis, pero ayuda a dirigirlo.)

---

## Paso 1 — Análisis intrínseco del signo

Evaluar el signo en sí mismo, con independencia de las marcas de terceros:

### 1.1 Clasificación del tipo de signo

| Tipo | Descripción | Fuerza distintiva inherente |
|---|---|---|
| Arbitrario | Palabra existente sin relación con el producto (ej. "APPLE" para computadoras) | Muy alta |
| Fanciful / de fantasía | Palabra inventada sin significado previo (ej. "KODAK") | Muy alta |
| Sugestivo | Evoca una característica del producto sin describirla directamente (ej. "VISA") | Alta |
| Descriptivo | Describe directamente una característica del producto | Baja — requiere secondary meaning |
| Genérico | Nombre común del producto o servicio | No registrable |

Clasificar el signo propuesto en una de estas categorías y justificar.

### 1.2 Causales de irregistrabilidad absoluta

Verificar si el signo incurre en alguna causal de irregistrabilidad absoluta:

**Uruguay — art. 5 Ley 17.011:**
- (a) No ser distintivo
- (b) Consistir en la forma o color usual del producto
- (c) Ser contrario a la moral o las buenas costumbres
- (d) Inducir a error sobre la naturaleza, cualidades, procedencia geográfica o características del producto
- (e) Reproducir o imitar la bandera, escudo u otro símbolo nacional o extranjero
- (f) Consistir en denominaciones de organismos internacionales
- (g) Ser el nombre común o genérico del producto en el país

**Argentina — art. 2 Ley 22.362:**
- (a) Nombres técnicos o científicos que designan al producto
- (b) Expresiones de uso común para designar el producto
- (c) Formas que sean la resultante de la naturaleza del producto
- (d) Color solo (salvo que tenga formas que lo individualicen)
- (e) Designaciones contrarias a la moral, las buenas costumbres y el orden público
- (f) Siglas, emblemas y denominaciones de organismos estatales

Para cada causal relevante, indicar si el signo la cumple (INCURRE / NO INCURRE / DUDOSO).

### 1.3 Evaluación de la fuerza del signo

Asignar una valoración de fuerza:

| Fuerza | Criterio |
|---|---|
| FUERTE | Arbitrario o de fantasía; máxima protección; mínimo riesgo de rechazo por irregistrabilidad |
| MEDIA | Sugestivo; protegible pero con mayor superficie de ataque en oposiciones |
| DÉBIL | Descriptivo o con secondary meaning dudoso; difícil de registrar y difícil de defender |
| NO REGISTRABLE | Genérico o incurso en causal absoluta de irregistrabilidad |

---

## Paso 2 — Clasificación de productos / servicios en la Nomenclatura de Niza

Si el cliente no identificó las clases, clasificar los productos y servicios descriptos
conforme a la 11.ª edición de la Clasificación Internacional de Niza.

Indicar:
- Clase(s) principal(es) donde se concentra la actividad del cliente.
- Clase(s) relacionadas donde una marca de tercero podría generar riesgo de confusión
  aunque no sea la misma clase (ej. clases 30 y 43 para servicios de alimentación y
  restaurantes).

Recordar que el DNPI y el INPI aplican el principio de especialidad: la protección se
limita a las clases registradas, pero la confusión puede darse entre clases relacionadas.

---

## Paso 3 — Identificación de knock-outs probables

Identificar los tipos de marcas preexistentes que, de existir en la base oficial, serían
los obstáculos más probables para el registro:

### 3.1 Marcas idénticas en las mismas clases

El riesgo más grave. Una marca idéntica en las mismas clases es un knock-out casi
inevitable. Analizar:
- ¿El signo propuesto es idéntico (gráfica y fonéticamente) a una marca conocida del sector?
- ¿Hay marcas internacionales con ese mismo nombre activas en Uruguay o Argentina vía
  el Sistema de Madrid?

### 3.2 Marcas similares — heurísticas de confusión

Aplicar las tres perspectivas clásicas de análisis de confusión:

**a) Confusión fonética:**
- ¿El signo suena similar a una marca conocida del sector al pronunciarse en voz alta?
- Aplicar el test del consumidor medio con atención media: ¿podría confundirlos al escucharlos?
- Considerar variantes ortográficas que producen el mismo sonido (ej. "Qualix" / "Calix").

**b) Confusión gráfica (para marcas mixtas o figurativas):**
- ¿Los elementos visuales principales del signo (tipografía, diseño, disposición) se
  asemejan a marcas conocidas del sector?
- ¿Se reivindica algún color que sea característico de una marca competidora?

**c) Confusión conceptual:**
- ¿El significado del signo evoca el mismo concepto que el de una marca preexistente?
  (Ej. "SUNFLOW" y "GIRASOL" para el mismo producto pueden generar confusión conceptual.)

### 3.3 Marcas notorias y de alta reputación

Verificar si el signo podría colisionar con una marca notoriamente conocida:
- En Uruguay: la protección de la marca notoria se extiende más allá de la clase
  registrada (art. 13 inc. (b) Ley 17.011; art. 2 bis Convenio de París).
- En Argentina: ídem (art. 3 inc. (d) Ley 22.362; art. 6 bis Convenio de París).
- Listar las marcas notorias del sector que deberían verificarse en la búsqueda formal.

---

## Paso 4 — Tabla de knock-outs identificados

Producir una tabla con los conflictos potenciales identificados:

| N.° | Marca potencialmente conflictiva | Titular conocido | Clase(s) | Tipo de confusión | Riesgo | Observación |
|---|---|---|---|---|---|---|
| K1 | [Nombre de la marca conocida] | [Titular, si se conoce] | [Clase(s)] | Fonética / Gráfica / Conceptual / Idéntica | ALTO / MEDIO / BAJO | [Descripción del conflicto] |

Si no se identifican knock-outs conocidos, indicarlo explícitamente y aclarar que la
ausencia de conflictos conocidos no garantiza la disponibilidad del signo: la búsqueda
formal en la base oficial es imprescindible.

---

## Paso 5 — Evaluación del riesgo de oposición

Asignar un nivel de riesgo global de oposición:

| Nivel | Criterio |
|---|---|
| **ALTO** | Existen marcas idénticas o muy similares en las mismas clases · el signo es descriptivo o genérico · colisión probable con marca notoria |
| **MEDIO** | Existen marcas similares en clases relacionadas · el signo es sugestivo y puede generar confusión fonética o conceptual · mercado con alta densidad marcaria |
| **BAJO** | El signo es arbitrario o de fantasía · no se identifican marcas similares conocidas en las clases objetivo · mercado con baja densidad marcaria |

---

## Paso 6 — Recomendación

Emitir una de las siguientes recomendaciones con su fundamentación:

| Recomendación | Cuándo aplicar |
|---|---|
| **REGISTRAR** | Signo fuerte, riesgo BAJO, sin knock-outs identificados. Proceder con la solicitud una vez confirmada la disponibilidad en la búsqueda formal. |
| **REGISTRAR CON AJUSTES** | Signo registrable pero con elementos de riesgo mitigables. Indicar los ajustes sugeridos (ej. agregar elemento distintivo, cambiar tipografía, modificar la lista de productos para reducir solapamiento). |
| **NO REGISTRAR — BUSCAR ALTERNATIVA** | Signo débil o con knock-outs de alto riesgo. Recomendar un signo alternativo y describir las características que debería tener. |
| **BÚSQUEDA AMPLIADA NECESARIA** | El análisis preliminar no es suficiente para una recomendación fundada. Indicar por qué (alta densidad marcaria, sector especialmente litigioso, duda sobre marca notoria del sector). |

---

## Paso 7 — Dictamen de clearing

Producir el dictamen completo con la siguiente estructura:

```
DICTAMEN DE PRIMERA PASADA DE CLEARING MARCARIO

Signo: [Nombre / descripción]
Tipo de marca: [Denominativa / Figurativa / Mixta]
Clase(s) Nice solicitada(s): [X, Y, Z]
Jurisdicción: [Uruguay (DNPI) / Argentina (INPI) / Ambas]
Fecha: [día/mes/año]
Elaborado por: [Abogado / Estudio]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ANÁLISIS INTRÍNSECO DEL SIGNO
   Tipo de signo: [Arbitrario / Sugestivo / Descriptivo / Genérico]
   Fuerza distintiva: [FUERTE / MEDIA / DÉBIL / NO REGISTRABLE]
   Causales absolutas de irregistrabilidad: [NINGUNA / [descripción de la causal]]

2. ANÁLISIS DE CONFUSIÓN CON MARCAS PREEXISTENTES
   2.1 Confusión fonética: [análisis]
   2.2 Confusión gráfica: [análisis]
   2.3 Confusión conceptual: [análisis]
   2.4 Marcas notorias relevantes: [lista o NINGUNA IDENTIFICADA]

3. TABLA DE KNOCK-OUTS
   [Tabla del Paso 4]

4. EVALUACIÓN DE RIESGO
   Riesgo global de oposición: [ALTO / MEDIO / BAJO]
   Fundamento: [1-2 oraciones]

5. RECOMENDACIÓN
   [REGISTRAR / REGISTRAR CON AJUSTES / NO REGISTRAR / BÚSQUEDA AMPLIADA]
   Fundamento: [Párrafo con citas normativas]
   [Si aplica: Ajustes sugeridos / Alternativas]

6. PRÓXIMOS PASOS
   1. Realizar búsqueda formal en la base del DNPI (https://api.dnpi.gub.uy) o del
      INPI (https://markaronline.inpi.gob.ar) antes de presentar la solicitud.
   2. [Otros pasos según la recomendación]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ADVERTENCIA: Este dictamen es una primera pasada de análisis y no reemplaza la búsqueda
formal en la base de datos oficial del DNPI o del INPI. La disponibilidad definitiva
del signo solo puede confirmarse mediante esa búsqueda formal. La opinión emitida está
sujeta a los resultados de dicha búsqueda y puede variar.
```

---

## Guardrails

- **Nunca afirmar que el signo está disponible** ni que el registro será concedido:
  solo indicar el nivel de riesgo y la recomendación como primera pasada.
- **Incluir siempre la advertencia** de que el análisis no reemplaza la búsqueda formal
  en la base oficial del DNPI o del INPI.
- **No analizar marcas internacionales** (EUIPO, USPTO, WIPO) como parte de este
  análisis, salvo que el cliente lo solicite expresamente y el perfil del estudio lo contemple.
- **Si el signo es idéntico a una marca notoria de primera línea** (ej. coincide con el
  nombre de una multinacional conocida en el mismo sector), señalar el riesgo como ALTO
  y recomendar no proceder sin búsqueda formal y revisión del socio.
- **Si el signo puede ser engañoso** sobre la procedencia geográfica del producto
  (ej. nombres de ciudades, regiones o países), alertar sobre la causal de irregistrabilidad
  por deception (art. 5 inc. (d) Ley 17.011 / art. 2 inc. (d) Ley 22.362).
- **No opinar sobre el registro de marcas que reproduzcan símbolos nacionales** sin
  escalar al socio de práctica.
