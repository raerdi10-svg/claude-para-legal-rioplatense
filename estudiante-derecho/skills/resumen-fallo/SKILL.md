---
name: resumen-fallo
description: >
  Resume un fallo judicial en el formato preferido del estudiante: esquema doctrinal,
  IRAC o ficha de jurisprudencia. Incluye preguntas de comprensión al final.
argument-hint: "[texto del fallo o identificación: tribunal, fecha, partes, número]"
user-invocable: true
---

# Skill: Resumidor de Fallos

## Propósito

Producir resúmenes de fallos judiciales adaptados al nivel y formato preferido del estudiante,
registrados en el perfil de práctica (`CLAUDE.md`). El resumen no reemplaza la lectura del fallo
completo — es una herramienta de estudio y fichero de jurisprudencia.

---

## Paso 0 — Identificación del fallo y formato

1. **Fallo**: texto completo o identificación (tribunal, fecha, número, partes, país).
2. **Formato preferido** (leer del `CLAUDE.md` del estudiante; si no está configurado, preguntar):
   - **A — Esquema doctrinal**: estructura analítica completa
   - **B — IRAC**: Issue / Rule / Application / Conclusion
   - **C — Ficha**: tarjeta mínima para fichero de jurisprudencia
3. **Propósito del resumen**: ¿para qué materia / parcial / concurso?

---

## Paso 1 — Resumen en formato A: Esquema Doctrinal

```
TRIBUNAL:         [nombre completo del tribunal]
FECHA:            [DD/MM/AAAA]
PARTES:           [Actor c/ Demandado] o [Fiscal c/ Imputado]
JURISDICCIÓN:     [UY / AR / Provincia / CSJN / SCJ / etc.]
MATERIA:          [Civil / Comercial / Laboral / Penal / CA / etc.]

HECHOS RELEVANTES (máx. 8 líneas):
[Narración cronológica y objetiva de los hechos que motivaron el litigio]

CUESTIÓN JURÍDICA CENTRAL:
[Formulada como pregunta: ¿Tiene derecho X a Y en las circunstancias Z?]

NORMA APLICADA:
[Cita exacta: art. X Ley Y / art. X CCyCN / art. X CGP / etc.]

HOLDING:
[Qué decidió el tribunal — una o dos oraciones]

RATIO DECIDENDI:
[Por qué lo decidió — el razonamiento jurídico central, no los obiter]

OBITER DICTA:
[Afirmaciones del tribunal que no son necesarias para la decisión, pero son relevantes]

RELEVANCIA PARA LA MATERIA:
[Por qué este fallo importa — qué principio, regla o excepción establece o confirma]

FALLOS RELACIONADOS:
[Si el tribunal citó precedentes relevantes, listarlos aquí]
```

---

## Paso 2 — Resumen en formato B: IRAC

```
ISSUE (Cuestión):
[Pregunta jurídica precisa que el tribunal debía resolver]

RULE (Norma):
[Norma o principio aplicable con cita exacta]

APPLICATION (Aplicación):
[Cómo aplicó el tribunal la norma a los hechos concretos]

CONCLUSION:
[Resultado al que llegó el tribunal]
```

---

## Paso 3 — Resumen en formato C: Ficha de Jurisprudencia

```
┌─────────────────────────────────────────────────────────────┐
│ TRIBUNAL: [nombre]          FECHA: [DD/MM/AAAA]             │
│ PARTES: [Actor c/ Demandado]                                 │
│ PROBLEMA JURÍDICO: [una línea]                              │
│ SOLUCIÓN: [una línea]                                        │
│ NORMA: [cita exacta]                                         │
│ RELEVANCIA: [una línea — por qué se cita este fallo]        │
└─────────────────────────────────────────────────────────────┘
```

---

## Paso 4 — Preguntas de comprensión

Al final de cualquier formato, incluir 3 preguntas:

1. **Comprensión directa**: sobre los hechos o la norma aplicada
   Ej.: "¿Cuál fue el argumento central del demandante que el tribunal rechazó?"

2. **Análisis**: sobre el razonamiento del tribunal
   Ej.: "¿Por qué el tribunal consideró que no había relación de causalidad?"

3. **Extensión**: sobre aplicación del precedente a un caso variante
   Ej.: "¿Cambiaría la solución si el contrato hubiera sido celebrado en Argentina? ¿Por qué?"

---

## Guardrails

- Si el fallo involucra normativa posterior a agosto 2025, advertir: "Puede haber jurisprudencia posterior o modificaciones normativas no conocidas por el modelo. Verificar en base de datos actualizada (La Ley, Microjuris, DataLegal) antes de usar en un trabajo."
- No opinar sobre si el tribunal resolvió correctamente — el resumen es objetivo. Las preguntas de comprensión pueden explorar si el estudiante acuerda con el razonamiento, pero el resumen en sí no toma postura.
- Si el fallo no se puede identificar con los datos provistos, decirlo claramente en lugar de construir un fallo hipotético.
- Para fallos en materia penal: respetar la presunción de inocencia en la formulación de los hechos (usar "el imputado" y "según la acusación" donde corresponda).
