---
name: demanda-recibida
description: >
  Analiza una demanda entrante para el cliente demandado: pretensión y monto exacto,
  fundamentos jurídicos del actor con evaluación crítica, cronología del actor vs.
  versión del cliente, prueba ofrecida por el actor con valoración de su fortaleza,
  plazos procesales para contestar y oponer excepciones, opciones estratégicas con
  pros y contras, e identificación de issues de cross-cartera con la misma contraparte.
argument-hint: "[pegue el texto de la demanda recibida o una descripción detallada de la misma]"
user-invocable: true
---

# Skill: Triaje de Demanda Recibida

## Propósito

Analizar en forma rápida y estructurada una demanda entrante para que el abogado
pueda tomar decisiones estratégicas informadas antes de la primera reunión con el
cliente. El output incluye un resumen ejecutivo para el socio, el análisis técnico
de la demanda y una tabla de opciones estratégicas con pros, contras y costo estimado.

---

## Paso 0 — Recolección de datos

Si el usuario adjuntó el texto de la demanda, comenzar el análisis directamente.
Si solo hay una descripción verbal, preguntar:

1. **Jurisdicción y fuero:** ¿Argentina o Uruguay? ¿Civil / comercial / laboral /
   contencioso-administrativo?
2. **Fecha de notificación de la demanda:** día/mes/año. Si se desconoce, advertir que
   los plazos no pueden calcularse hasta obtenerla.
3. **¿El estudio tiene información sobre el historial de la contraparte?** ¿Hay otras
   causas en cartera con este mismo actor o empresa vinculada?
4. **¿El cliente tiene documentación relevante** (contratos, correos, facturas, recibos,
   cartas documento previas) que permita contrastar la versión del actor?

No avanzar al Paso 1 sin conocer al menos la jurisdicción y la fecha de notificación.

---

## Paso 1 — Pretensión exacta y monto reclamado

Identificar con precisión:

- **Objeto principal:** ¿Qué pide el actor? (pago de suma / resolución de contrato /
  indemnización por daños / reintegro de inmueble / cumplimiento de obligación de hacer /
  nulidad de acto jurídico / otro)
- **Monto reclamado:** indicar el capital reclamado, los intereses (tasa, desde cuándo),
  la actualización si aplica, las costas y el total estimado al día de la notificación.
  Si no hay monto determinado (ej. daños a liquidar), indicarlo y estimar la cuantía
  probable si el relato lo permite.
- **¿Es la pretensión principal la única?** Identificar si hay pretensiones subsidiarias
  o alternativas.
- **¿Se solicitan medidas cautelares?** Indicar cuáles (embargo / inhibición general de
  bienes / prohibición de innovar / intervención judicial) y si ya fueron otorgadas.

---

## Paso 2 — Fundamentos jurídicos del actor

Listar las normas invocadas por el actor y evaluarlas:

| N.° | Norma invocada | Propósito en la demanda | ¿Correctamente aplicada? | Observación |
|---|---|---|---|---|
| 1 | [Art. X CCyCN / CGP / etc.] | [Para qué la invoca el actor] | Sí / No / Parcialmente | [Comentario técnico] |
| 2 | [Art. Y] | [Propósito] | Sí / No / Parcialmente | [Comentario] |

Para cada norma incorrectamente aplicada, explicar:
- Por qué la aplicación es errónea (elemento faltante, mal interpretado o norma
  inaplicable al caso).
- Qué norma debería aplicarse en su lugar, si hay alguna.
- Si el error es relevante para la defensa (puede generar excepción de falta de acción
  o defensa de fondo que debilite la demanda).

**Evaluación global de los fundamentos:**
- ¿La teoría jurídica del actor es sólida, débil o francamente errónea?
- ¿Hay omisiones relevantes de normas que podrían jugar a favor del demandado?

---

## Paso 3 — Cronología del actor vs. versión del cliente

Construir una tabla comparativa de las versiones sobre los hechos:

| Fecha | Hecho según el actor | Hecho según el cliente | ¿Controvertido? | Prueba disponible |
|---|---|---|---|---|
| [DD/MM/AAAA] | [Versión del actor] | [Versión del cliente] | Sí / No | [Documento / testigo] |

**Diferencias clave entre versiones:** listar los puntos de mayor divergencia y evaluar
cuáles son los que más impactan en la responsabilidad invocada.

Si el usuario no tiene aún la versión del cliente, dejar la columna "Hecho según el
cliente" con `[a relevar con el cliente]` e indicar que esos hechos deben ser
verificados antes de redactar la contestación.

---

## Paso 4 — Prueba ofrecida por el actor

Listar la prueba ofrecida por el actor en la demanda y evaluar la fortaleza de cada medio:

| Medio de prueba | Descripción | Fortaleza | Posibilidad de impugnación | Observación |
|---|---|---|---|---|
| Documental | [Lista de documentos acompañados] | ALTA / MEDIA / BAJA | Sí / No | [Obs.] |
| Testimonial | [Lista de testigos o "en su oportunidad"] | ALTA / MEDIA / BAJA | Sí / No | [Obs.] |
| Pericial | [Perito propuesto y materia] | ALTA / MEDIA / BAJA | Sí / No | [Obs.] |
| Informativa | [Organismos o empresas a informar] | ALTA / MEDIA / BAJA | Sí / No | [Obs.] |

**Evaluación global de la prueba del actor:**
- ¿Tiene prueba suficiente para probar los hechos constitutivos de su pretensión?
- ¿Hay brechas probatorias relevantes que el demandado pueda explotar?
- ¿Hay prueba del actor que pueda ser impugnada (documentos cuestionables,
  testigos con interés, peritos con conflicto de interés)?

---

## Paso 5 — Plazos procesales

Calcular todos los plazos a partir de la fecha de notificación indicada.

### Argentina — CPCCN

| Hito procesal | Norma | Plazo | Fecha límite | Días hábiles restantes | Urgencia |
|---|---|---|---|---|---|
| Contestación de demanda | Art. 338 CPCCN | 15 días hábiles | [DD/MM/AAAA] | [N] | [URGENTE / NORMAL] |
| Oposición de excepciones previas | Art. 346 CPCCN | Dentro del plazo de contestación | [DD/MM/AAAA] | [N] | [URGENTE / NORMAL] |
| Reconvención (si aplica) | Art. 357 CPCCN | Con la contestación de demanda | [DD/MM/AAAA] | [N] | — |
| Impugnación de documentos | Art. 356 inc. 1 CPCCN | Con la contestación | [DD/MM/AAAA] | [N] | — |
| Respuesta a medida cautelar (si ya otorgada) | Arts. 198-199 CPCCN | 5 días hábiles | [DD/MM/AAAA] | [N] | [URGENTE] |

**Excepciones previas aplicables (art. 347 CPCCN):** evaluar si corresponde oponer:
- Incompetencia
- Falta de personería
- Falta de legitimación manifiesta
- Litispendencia
- Defecto legal en el modo de proponer la demanda
- Cosa juzgada
- Transacción, conciliación y desistimiento del derecho
- Prescripción (cuando es manifiesta)

### Uruguay — CGP (Código General del Proceso)

| Hito procesal | Norma | Plazo | Fecha límite | Días corridos restantes | Urgencia |
|---|---|---|---|---|---|
| Contestación de demanda | Art. 339 CGP | 30 días corridos | [DD/MM/AAAA] | [N] | [URGENTE / NORMAL] |
| Reconvención (si aplica) | Art. 340 CGP | Con la contestación | [DD/MM/AAAA] | [N] | — |
| Excepciones previas | Arts. 133-135 CGP | Dentro del plazo de contestación | [DD/MM/AAAA] | [N] | — |
| Impugnación de documentos | Art. 173 CGP | Al contestar demanda | [DD/MM/AAAA] | [N] | — |
| Respuesta a medida cautelar | Arts. 311-318 CGP | Sin plazo fijo; inaudita parte | [DD/MM/AAAA] | Urgente | [URGENTE] |

**Excepciones previas aplicables (art. 133 CGP):** evaluar si corresponde oponer:
- Incompetencia
- Incapacidad del actor
- Falta de personería del actor o del demandado
- Litispendencia
- Falta de legitimación del actor
- Prescripción manifiesta
- Cosa juzgada
- Compromiso arbitral

---

## Paso 6 — Opciones estratégicas

Presentar una tabla con las opciones disponibles para el cliente demandado:

| Opción | Descripción | Pros | Contras | Costo estimado | Recomendación inicial |
|---|---|---|---|---|---|
| **Allanamiento total** | Reconocer la pretensión en su totalidad | Evita costas judiciales completas · cierra el conflicto con rapidez · puede reducir monto si el juez aplica art. 70 CPCCN (sin costas al allanado) | Implica pago total o cumplimiento de la obligación · reconoce la versión del actor · puede afectar relaciones comerciales futuras | [Monto a pagar] | Considerar si la deuda es líquida, cierta y no hay defensa viable |
| **Allanamiento parcial + negociación** | Reconocer la parte indiscutida y negociar la diferencia | Reduce litigiosidad · puede generar quita en el excedente · demuestra buena fe | Requiere que la contraparte acepte negociar · puede verse como debilidad si no hay oferta clara | [Monto discutido] | Considerar si hay componente claramente procedente y otro cuestionable |
| **Contestación con excepciones previas** | Contestar la demanda oponiendo defensas de forma y de fondo | Abre el debate sobre presupuestos procesales · puede dilatar el proceso · excepciones procedentes pueden terminar la causa | Agrega costos y tiempo · el juez puede rechazar las excepciones en limine | [Honorarios contestación + excepciones] | Considerar si hay excepción viable de fondo (prescripción, incompetencia, falta de legitimación) |
| **Contestación simple** | Negar los hechos y el derecho invocado sin oponer excepciones | Eficiente si la defensa es de fondo · evita el incidente de excepciones | El caso sigue su curso ordinario · no dilata el proceso | [Honorarios contestación] | Opción base cuando no hay excepciones previas claras |
| **Reconvención** | Contrademandar al actor por créditos o perjuicios propios | Permite acumular un crédito del demandado · puede generar compensación o presión para acordar | Requiere mérito propio · agrega complejidad y costo · prolonga el proceso | [Honorarios contestación + reconvención] | Evaluar si el estudio tiene crédito líquido contra el actor |

**Análisis de la mejor opción inicial:** sobre la base de los pasos anteriores, indicar
cuál parece la opción más favorable según la información disponible, aclarando que la
recomendación definitiva requiere conocer la versión completa del cliente y revisar
toda la documentación.

---

## Paso 7 — Issues de cross-cartera

Verificar si existen situaciones de cross-cartera que deban coordinarse:

- **¿Hay otras causas activas con este mismo actor o empresa vinculada?** Si el perfil
  del estudio lo registra, indicar las causas relacionadas y la estrategia de coordinación.
- **¿La presente demanda puede afectar acuerdos o contratos en curso con el actor?**
  (ej. si hay un contrato de distribución vigente entre las partes)
- **¿El actor es también parte en otras causas donde el estudio lo representa?**
  Evaluar conflicto de interés potencial y escalar al socio si lo hay.
- **¿Hay medidas cautelares en otras causas que puedan verse afectadas?**

---

## Output — Resumen ejecutivo para el socio

Al cierre del análisis, producir un resumen en el siguiente formato:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIAJE DE DEMANDA — RESUMEN EJECUTIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cliente demandado:     [Nombre]
Actor (demandante):    [Nombre]
Jurisdicción / fuero:  [AR o UY — civil / comercial / laboral]
Fecha de notificación: [DD/MM/AAAA]
Plazo para contestar:  [DD/MM/AAAA] ([N] días hábiles / corridos restantes)
URGENCIA:              [ALTA / MEDIA / NORMAL]

PRETENSIÓN PRINCIPAL:
[Una oración con el objeto y el monto.]

EVALUACIÓN INICIAL:
[Dos o tres oraciones sobre la solidez de la demanda, los puntos fuertes
del actor y los puntos débiles que favorecen al demandado.]

OPCIÓN ESTRATÉGICA SUGERIDA (preliminar):
[Una oración con la opción más favorable según el análisis, sujeta a
confirmación con el cliente.]

PRÓXIMAS ACCIONES:
1. Reunión urgente con el cliente antes del [fecha, 5 días antes del vencimiento].
2. Obtener documentación: [lista de documentos clave].
3. Verificar cross-cartera: [indicar si hay o no hay issues identificados].
4. [Otras acciones necesarias según el análisis.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Si el plazo para contestar la demanda está a **menos de 5 días hábiles**, abrir el
  output con una alerta en mayúsculas antes de cualquier otro contenido:
  **ALERTA URGENTE — PLAZO CRÍTICO: quedan [N] días hábiles para contestar la demanda.
  Actuar de inmediato.**
- No opinar sobre la probabilidad de éxito del cliente sin conocer su versión completa
  y haber revisado la documentación de respaldo. El análisis es preliminar.
- No recomendar el allanamiento total sin verificar primero con el cliente si acepta
  la pretensión como legítima y si tiene capacidad de pago o cumplimiento.
- No asumir que la versión del actor es verdadera: identificar los hechos controvertidos
  y dejar espacio para la versión del cliente.
- Si la demanda contiene pretensiones de naturaleza penal (denuncia penal o querella
  accesoria), alertar y derivar al área de litigio penal del estudio.
- Si se detecta un posible conflicto de interés (el estudio ya representa al actor en
  otro asunto), no continuar el análisis y escalar al socio a cargo inmediatamente.
- Citar siempre el artículo exacto de la norma procesal. No usar fórmulas genéricas
  como "según el código".
