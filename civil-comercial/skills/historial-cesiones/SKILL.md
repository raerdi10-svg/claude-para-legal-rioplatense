---
name: historial-cesiones
description: >
  Trazado cronológico de cómo evolucionó un contrato a lo largo de adendas,
  modificaciones y cesiones. Produce tabla cronológica con fecha, tipo de
  modificación, cláusulas afectadas, partes intervinientes y observaciones.
  Identifica si cada cesión requirió consentimiento del cedido y si fue
  otorgado, con referencias a los arts. 1614-1623 CCyCN y equivalentes UY.
argument-hint: "[pegar o adjuntar contrato original + adendas/cesiones en orden cronológico]"
user-invocable: true
---

# Skill: Historial de Cesiones y Modificaciones Contractuales

## Propósito

Reconstruir la historia completa de un contrato desde su versión original hasta el estado vigente, identificando cada modificación, adenda y cesión, verificando la validez formal de cada hito y determinando si las partes que intervienen actualmente tienen efectivamente los derechos y obligaciones que invocan. Es una herramienta esencial en due diligence, litigios contractuales y renegociaciones donde la cadena de modificaciones es compleja.

---

## Paso 0 — Lectura del perfil

Leer `CLAUDE.md` del plugin para incorporar jurisdicción principal, umbrales de riesgo y estilo de outputs. En contratos transfronterizos, aplicar el marco de la ley elegida por las partes.

---

## Paso 1 — Recolección de documentos

Solicitar al usuario todos los documentos de la cadena contractual:

1. **Contrato original:** con fecha, partes originales y número/código de identificación.
2. **Adendas y modificaciones:** en orden cronológico; si no están numeradas, el usuario debe indicar el orden.
3. **Cesiones de posición contractual o de créditos:** con fecha, cedente, cesionario y, si existe, notificación al cedido.
4. **Notificaciones entre partes:** relevantes para la cadena de consentimientos.
5. **Cualquier otro documento que modifique, suspenda o extinga obligaciones:** cartas, correos, actas de reunión que tengan valor contractual.

Si los documentos llegan en desorden, pedir al usuario que los organice antes de proceder, o procesar indicando la incertidumbre sobre el orden.

---

## Paso 2 — Verificación de cada hito

Para cada documento de la cadena, verificar:

### Para adendas y modificaciones:

| Verificación | Resultado |
|---|---|
| ¿Tienen fecha cierta? | Sí / No / Dudoso |
| ¿Están firmadas por las mismas partes del contrato original o por sus apoderados con facultades suficientes? | |
| ¿Identifican explícitamente qué cláusulas modifican? | |
| ¿Preservan la vigencia del resto del contrato original? | |
| ¿Hay contradicción entre la adenda y el contrato original no resuelta? | |

### Para cesiones de posición contractual (arts. 1636-1640 CCyCN / arts. 1291 ss. CC UY):

| Verificación | Resultado |
|---|---|
| ¿Se cedió la "posición contractual" completa (derechos y obligaciones) o solo créditos? | |
| ¿Existe consentimiento expreso del cedido (contraparte del contrato base)? | |
| Si el consentimiento fue anticipado (en el contrato original): ¿la cláusula es suficientemente específica? | |
| ¿La cesión fue notificada fehacientemente al cedido? Fecha de notificación: | |
| ¿El cedente quedó liberado de sus obligaciones o permanece como garante? (art. 1637 CCyCN) | |
| ¿El cesionario aceptó expresamente las obligaciones del contrato cedido? | |

### Para cesiones de créditos (arts. 1614-1635 CCyCN / arts. 1756 ss. CC UY):

| Verificación | Resultado |
|---|---|
| ¿Se individualizaron los créditos cedidos con precisión? | |
| ¿Existe notificación al deudor cedido? (art. 1620 CCyCN: sin notificación, la cesión no es oponible al deudor) | |
| ¿Hay riesgo de doble cesión del mismo crédito? (art. 1622 CCyCN: prevalece la primera notificación) | |
| ¿Se cedieron garantías accesorias junto con el crédito? (art. 1615 CCyCN) | |
| ¿El cedente garantizó la existencia y legitimidad del crédito? ¿Garantizó la solvencia del deudor? | |

---

## Paso 3 — Construcción de la tabla cronológica

Producir la tabla en el siguiente formato:

| N° | Fecha | Tipo de documento | Partes intervinientes | Cláusulas afectadas | Consentimiento requerido | Consentimiento otorgado | Observaciones |
|---|---|---|---|---|---|---|---|
| 1 | [DD/MM/AAAA] | Contrato original | [Parte A] / [Parte B] | Todas | N/A | N/A | Ley aplicable: [X]; jurisdicción: [Y] |
| 2 | [DD/MM/AAAA] | Adenda N°1 | [Partes] | [Cláusulas X, Y] | No (solo modificación) | N/A | [Observación] |
| 3 | [DD/MM/AAAA] | Cesión de posición contractual | Cedente: [A]; Cesionario: [C]; Cedido: [B] | Todas | Sí — art. 1636 CCyCN | [Sí / No / Anticipado en cláusula X] | [Observación] |
| ... | | | | | | | |

Bajo la tabla, incluir una fila de **Estado actual** que sintetice:
- Partes vigentes
- Cláusulas en vigor (identificando las modificadas)
- Vigencia del contrato

---

## Paso 4 — Identificación de issues en la cadena

Analizar la cadena completa y producir una lista de issues con nivel de riesgo:

### Issues típicos a verificar:

**A — Cesiones sin consentimiento del cedido**
- Una cesión de posición contractual sin consentimiento del cedido es ineficaz respecto de él (art. 1636 CCyCN). Si el cedido no consintió, las obligaciones del cedente no se transmitieron y el cesionario no puede exigirle cumplimiento.
- Nivel de riesgo: ALTO si el contrato está siendo ejecutado por el cesionario sin consentimiento verificable.

**B — Consentimiento anticipado insuficiente**
- El art. 1636 CCyCN permite que el consentimiento del cedido sea anticipado (cláusula en el contrato original). Verificar si la cláusula es lo suficientemente específica para cubrir la cesión concreta que se realizó.
- Nivel: MEDIO si la cláusula es genérica; ALTO si la cesión excede claramente los términos del consentimiento anticipado.

**C — Notificación de cesión de créditos**
- Sin notificación fehaciente al deudor cedido, la cesión no es oponible a él (art. 1620 CCyCN). El deudor puede pagar válidamente al cedente original.
- Nivel: ALTO si hay pagos en curso y no hubo notificación.

**D — Modificaciones contradictorias entre sí**
- Si dos adendas modificaron la misma cláusula en sentido contradictorio, identificar cuál prevalece (criterio: la posterior prevalece, salvo disposición expresa en contrario).
- Nivel: MEDIO si la contradicción es sobre obligaciones económicas; BAJO si es sobre plazos o formas.

**E — Adendas firmadas solo por representantes sin acreditar facultades**
- Si una adenda fue firmada por un apoderado cuyo poder no consta en la cadena documental, la validez es incierta.
- Nivel: ALTO si la adenda modifica obligaciones económicas sustanciales.

**F — Ausencia de fecha cierta en documentos privados**
- Un documento privado sin fecha cierta no es oponible a terceros (arts. 317 y 1003 CCyCN). En una cadena de cesiones, esto puede afectar la prioridad entre cesionarios concurrentes.
- Nivel: MEDIO.

---

## Paso 5 — Diagrama de partes

Cuando la cadena tenga tres o más cesiones o partes, producir un diagrama textual de la evolución de las partes:

```
[Fecha original]
Parte A (comitente) ←→ Parte B (prestador)

[Fecha adenda N°1]
Parte A ←→ Parte B [modificación: cláusula 5 — nuevo plazo]

[Fecha cesión]
Parte A ←→ Parte C (cesionario de B)
             ↑
        Consentimiento de A: [Sí, escrito DD/MM/AAAA / Anticipado en cláusula X / No consta]
        Liberación de B: [Sí art. 1637 / No — B permanece como garante]

[Estado actual: DD/MM/AAAA]
Partes vigentes: Parte A / Parte C
```

---

## Paso 6 — Output final

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HISTORIAL DE MODIFICACIONES Y CESIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contrato base:    [Tipo — Partes originales — Fecha]
Ley aplicable:    [CCyCN / CC UY]
Documentos analizados: [N] documentos
Período cubierto: [DD/MM/AAAA] → [DD/MM/AAAA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I. TABLA CRONOLÓGICA
[Tabla del Paso 3]

II. DIAGRAMA DE PARTES
[Diagrama del Paso 5]

III. ISSUES IDENTIFICADOS EN LA CADENA
[Lista del Paso 4 con nivel de riesgo]

IV. ESTADO ACTUAL DEL CONTRATO
Partes vigentes:        [A] — [C]
Cláusulas en vigor:     [listado de las modificadas con referencia a la adenda que las modificó]
Vencimiento estimado:   [DD/MM/AAAA]
Obligaciones pendientes más relevantes:
  - [Parte A]: [obligación]
  - [Parte C]: [obligación]

V. RECOMENDACIONES
[Lista de acciones a tomar en función de los issues identificados]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Este análisis es de carácter preliminar. Los efectos jurídicos
de las cesiones y modificaciones deben ser confirmados por un
abogado matriculado en la jurisdicción aplicable.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Si la cadena de documentos está incompleta (faltan eslabones), advertir expresamente que el análisis es parcial y que las conclusiones sobre validez de cesiones pueden ser incorrectas.
- No concluir que una cesión "es válida" o "es inválida" en forma absoluta — concluir que "presenta los requisitos formales" o "no consta el consentimiento del cedido, lo que la haría ineficaz respecto de él bajo el art. 1636 CCyCN".
- En Uruguay, verificar el régimen del Código Civil uruguayo (arts. 1757-1778 CC UY para cesión de créditos), que difiere en algunos aspectos del CCyCN, especialmente en el mecanismo de notificación y sus efectos.
- Si un documento está en idioma extranjero, advertir que el análisis de ese hito específico es incierto.
- Ante documentos con fecha dudosa o documentos privados sin fecha cierta, incluir siempre la advertencia de inoponibilidad a terceros.
