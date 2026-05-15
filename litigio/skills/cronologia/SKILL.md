---
name: cronologia
description: >
  Dado un expediente o relato de hechos, construye: tabla cronológica con fecha, hecho,
  fuente/prueba y relevancia jurídica; identificación de hechos controvertidos vs. no
  controvertidos; línea de tiempo visual en texto; y hitos procesales clave con fechas
  límite. Para causas de responsabilidad civil o PI: cuadro elemento a elemento de la
  norma vs. los hechos del caso.
argument-hint: "[relato de hechos o descripción del expediente] [--jurisdiccion=AR|UY] [--fuero=civil|comercial|laboral|admin]"
user-invocable: true
---

# Skill: Cronología de Hechos

## Propósito

Construir el mapa temporal y probatorio de una causa, como insumo para la estrategia
litigiosa, la redacción de demanda o contestación, y la identificación de hechos que
necesitan ser acreditados. Una cronología precisa es el cimiento de cualquier escrito
procesal eficaz.

---

## Paso 0 — Recolección de datos

1. **Jurisdicción:** Argentina / Uruguay
2. **Fuero:** Civil / Comercial / Laboral / Contencioso-administrativo
3. **Rol del cliente:** Actor (demandante) / Demandado / Tercero
4. **Tipo de causa:** (ej. incumplimiento contractual, daños y perjuicios, cobro de pesos, responsabilidad civil extracontractual, propiedad intelectual, despido, nulidad de acto, etc.)
5. **Relato de hechos:** pegar el texto del expediente, la demanda, el contrato, los correos o el relato del cliente.
6. **Documentos disponibles:** lista de prueba con la que cuenta el cliente (contratos, correos, facturas, partes médicos, testigos identificados, informes periciales, etc.)
7. **¿Hay plazos procesales próximos?** (contestación de demanda, contestación de excepción, producción de prueba, alegato)

---

## Paso 1 — Tabla cronológica de hechos

Construir la tabla organizando todos los hechos identificados en orden cronológico:

```
CRONOLOGÍA DE HECHOS — [CARÁTULA / DESCRIPCIÓN DE LA CAUSA]
Jurisdicción: [AR / UY] | Fuero: [Fuero] | Cliente: [Actor / Demandado]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────────┬──────────────────────────────┬──────────────────────┬────────────────────────────┐
│ Fecha      │ Hecho                        │ Fuente / Prueba      │ Relevancia jurídica        │
├────────────┼──────────────────────────────┼──────────────────────┼────────────────────────────┤
│ DD/MM/AAAA │ [Descripción objetiva]       │ [Contrato / correo / │ [Elemento de la norma que  │
│            │                              │ testigo / factura]   │ acredita o contradice]     │
├────────────┼──────────────────────────────┼──────────────────────┼────────────────────────────┤
│ ...        │ ...                          │ ...                  │ ...                        │
└────────────┴──────────────────────────────┴──────────────────────┴────────────────────────────┘
```

**Instrucciones para completar la tabla:**
- Fecha: usar formato DD/MM/AAAA. Si la fecha es aproximada, indicarlo (ej. "aprox. 03/2024").
- Hecho: descripción objetiva y neutral — no calificar jurídicamente en esta columna.
- Fuente / Prueba: indicar el documento o testigo que acredita el hecho; si no hay prueba disponible, marcar "SIN PRUEBA".
- Relevancia jurídica: conectar el hecho con el elemento jurídico que acredita (ej. "acredita el incumplimiento — art. 1078 CCyCN", "determina el inicio del plazo de prescripción — art. 2554 CCyCN").

---

## Paso 2 — Clasificación de hechos

### 2.1 Hechos no controvertidos

Hechos que ambas partes admiten o que surgen de documentos indubitados:

| Hecho | Fuente de la admisión / documento |
|---|---|
| [Hecho] | [Por qué no se discute] |

### 2.2 Hechos controvertidos

Hechos sobre los cuales las versiones de las partes difieren, o que el cliente afirma pero carece de prueba directa:

| Hecho | Versión del cliente | Versión de la contraparte (si conocida) | Prueba disponible | Prueba faltante |
|---|---|---|---|---|
| [Hecho] | [Versión] | [Versión] | [Prueba] | [Necesidad probatoria] |

### 2.3 Hechos nuevos o de difícil prueba

Hechos que el cliente desconoce o que requieren producción de prueba compleja (pericial, informativa a terceros, testimonial de parte contraria):

| Hecho a probar | Medio de prueba propuesto | Complejidad |
|---|---|---|
| [Hecho] | [Medio] | ALTA / MEDIA / BAJA |

---

## Paso 3 — Línea de tiempo visual (texto)

Representar la secuencia de hechos principales en formato visual de texto:

```
LÍNEA DE TIEMPO — [DESCRIPCIÓN DE LA CAUSA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[DD/MM/AAAA] ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●
INICIO        Firma del contrato / hecho generador                FIN / DEMANDA

Eventos clave:
│
├─ [DD/MM/AAAA] → [Hecho clave 1]
│                  Prueba: [documento]
│
├─ [DD/MM/AAAA] → [Hecho clave 2]
│                  Prueba: [documento]
│
├─ [DD/MM/AAAA] → [HITO CRÍTICO: incumplimiento / daño / intimación]
│                  ⚠️ Inicio del plazo de prescripción
│
├─ [DD/MM/AAAA] → [Hecho clave 3]
│
└─ [DD/MM/AAAA] → [Presentación de la demanda / inicio del proceso]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 4 — Hitos procesales y fechas límite

### Argentina (CPCCN / CPCC provincial)

Identificar los hitos procesales relevantes con sus plazos:

| Hito procesal | Normativa | Plazo | Fecha límite | Días restantes |
|---|---|---|---|---|
| Contestación de demanda | Art. 338 CPCCN | 15 días hábiles desde notificación | [DD/MM/AAAA] | [N] |
| Oposición de excepciones previas | Art. 346 CPCCN | Junto con o en lugar de contestación | [DD/MM/AAAA] | [N] |
| Ofrecimiento de prueba | Arts. 333-334 CPCCN | Con demanda / contestación | [DD/MM/AAAA] | [N] |
| Período de prueba | Art. 358 CPCCN | 40 días hábiles (ordinario) | [DD/MM/AAAA] | [N] |
| Alegato | Art. 482 CPCCN | 6 días desde clausura de prueba | [DD/MM/AAAA] | [N] |
| Apelación de sentencia | Art. 244 CPCCN | 5 días hábiles desde notificación | [DD/MM/AAAA] | [N] |
| Prescripción de la acción | Art. 2560 CCyCN (general) | 5 años desde el hecho | [DD/MM/AAAA] | [N] |

**Plazos de prescripción especiales (Argentina):**
- Responsabilidad civil extracontractual: 3 años (art. 2561 CCyCN)
- Daños por mala praxis: 3 años (art. 2561 CCyCN)
- Acción ejecutiva (pagaré, cheque): 3 años (art. 61 Decreto-Ley 5965/63)
- Acción laboral: 2 años (art. 256 LCT)
- Acciones por nulidad relativa: 2 años (art. 2562 CCyCN)
- Acciones reales: 10 años (art. 2560 CCyCN)

### Uruguay (CGP — Código General del Proceso)

| Hito procesal | Normativa | Plazo | Fecha límite | Días restantes |
|---|---|---|---|---|
| Contestación de demanda | Art. 340 CGP | 30 días corridos desde traslado | [DD/MM/AAAA] | [N] |
| Reconvención | Art. 340 CGP | Con la contestación | [DD/MM/AAAA] | [N] |
| Audiencia preliminar | Art. 341 CGP | Fijada por el tribunal | [DD/MM/AAAA] | [N] |
| Audiencia de prueba | Arts. 343-344 CGP | En el plazo fijado en audiencia preliminar | [DD/MM/AAAA] | [N] |
| Apelación de sentencia definitiva | Art. 254 CGP | 15 días desde notificación | [DD/MM/AAAA] | [N] |
| Prescripción ordinaria | Art. 1216 CC UY | 20 años | [DD/MM/AAAA] | [N] |
| Prescripción corta (responsabilidad extracontractual) | Art. 1332 CC UY | 4 años | [DD/MM/AAAA] | [N] |

---

## Paso 5 — Cuadro elemento a elemento (para causas de responsabilidad o PI)

### Responsabilidad civil (Argentina — CCyCN)

Para acreditar la responsabilidad civil, verificar cada elemento:

| Elemento | Norma | Hecho del caso que lo acredita | Prueba disponible | Estado |
|---|---|---|---|---|
| Factor de atribución (dolo / culpa / riesgo creado) | Arts. 1721-1724 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |
| Antijuridicidad (daño sin justificación) | Art. 1717 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |
| Daño (patrimonial / moral / punitivo) | Arts. 1737-1746 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |
| Nexo causal (adecuación causal) | Arts. 1726-1736 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |

### Incumplimiento contractual (Argentina — CCyCN)

| Elemento | Norma | Hecho del caso | Prueba disponible | Estado |
|---|---|---|---|---|
| Existencia y validez del contrato | Arts. 957-1010 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |
| Incumplimiento (total / parcial / tardío) | Arts. 1077-1079 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |
| Mora (interpelación o mora automática) | Arts. 886-888 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |
| Daño derivado del incumplimiento | Arts. 1082-1083 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |
| Relación causal entre incumplimiento y daño | Art. 1726 CCyCN | [Hecho] | [Prueba] | ACREDITADO / PENDIENTE / AUSENTE |

---

## Guardrails

- La cronología debe ser objetiva: describir hechos, no calificarlos. La calificación jurídica va en la columna "Relevancia jurídica" con cita normativa.
- Si hay hechos sin fecha precisa: no inventar una fecha; indicar "aprox. [mes/año]" o "fecha a confirmar".
- Los plazos procesales son fatales — si un plazo vence en menos de 5 días hábiles, mostrar banner de alerta urgente y recomendar acción inmediata.
- La prescripción debe calcularse desde el hito correcto: en AR, generalmente desde que el daño es conocido o cognoscible (art. 2554 CCyCN); en UY, desde el hecho generador (art. 1332 CC UY). Indicar siempre qué hito se tomó como punto de partida.
- No afirmar que un hecho "está probado" si la prueba no fue aún incorporada al expediente; usar "disponible" o "pendiente de producción".
- Si el relato del cliente presenta inconsistencias internas, señalarlas y pedir aclaración antes de construir la cronología final.
