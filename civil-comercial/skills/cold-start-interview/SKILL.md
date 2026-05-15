---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil del estudio civil y comercial.
  Recopila jurisdicción principal, tipos de contrato, umbrales de escalamiento,
  socio de referencia, moneda habitual y preferencias de estilo, luego escribe
  el perfil resultante en CLAUDE.md para que lo usen todas las skills del plugin.
argument-hint: "[opcional: nombre del estudio o socio a cargo]"
user-invocable: true
---

# Skill: Cold-Start Interview — Civil y Comercial

## Propósito

Configurar el perfil de práctica civil y comercial del estudio antes de usar cualquier otra skill del plugin. Sin este perfil, las skills de revisión de contratos, escalamiento y trazado de cesiones operan con valores por defecto genéricos. Con el perfil completo, los memos y análisis reflejan los estándares, umbrales y personas de referencia reales del estudio.

---

## Paso 0 — Presentación

Al invocar la skill, mostrar el siguiente bloque introductorio:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIGURACIÓN DE PERFIL — PRÁCTICA CIVIL Y COMERCIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Esta entrevista toma entre 5 y 10 minutos.
Las respuestas quedan guardadas en CLAUDE.md y pueden
editarse manualmente en cualquier momento.
Responda con la información actual del estudio; puede
dejar en blanco las preguntas que no apliquen.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 1 — Recolección de datos (una pregunta por turno)

Formular cada pregunta en un turno separado. Esperar respuesta antes de continuar.

### Bloque A — Jurisdicción

**Pregunta A1:**
> ¿En qué jurisdicción(es) opera principalmente el estudio?
> (a) Solo Argentina — CCyCN (Ley 26.994)
> (b) Solo Uruguay — Código Civil / LSC (Ley 16.060)
> (c) Ambas jurisdicciones con igual peso
> (d) Otra combinación — por favor detallar

**Pregunta A2 (si eligió Argentina o ambas):**
> ¿Cuál es el fuero habitual para contratos domésticos argentinos?
> (a) Justicia Nacional Comercial — CABA
> (b) Justicia provincial — ¿cuál provincia?
> (c) Arbitraje institucional — ¿qué institución? (CAM, CIAM, CCI, CNUDMI)

**Pregunta A3 (si eligió Uruguay o ambas):**
> ¿Cuál es el fuero habitual para contratos domésticos uruguayos?
> (a) Juzgados Letrados de Primera Instancia en lo Civil — Montevideo
> (b) Juzgados del interior — ¿departamento?
> (c) Arbitraje — ¿reglamento? (CAU, CCI, CNUDMI)

---

### Bloque B — Tipos de contrato

**Pregunta B1:**
> ¿Cuáles son los tres tipos de contrato más frecuentes en el estudio?
> Ejemplos: compraventa de mercaderías, distribución, prestación de servicios TI,
> NDA, licencia de software, joint venture contractual, franquicia, suministro,
> cesión de créditos, obra civil, contrato de agencia.

**Pregunta B2:**
> ¿El estudio trabaja principalmente como:
> (a) Parte cedente / contratante fuerte (redacta contratos propios)
> (b) Parte receptora / revisora (recibe contratos de contraparte para revisar)
> (c) Ambos roles con igual frecuencia

**Pregunta B3:**
> ¿Cuál es la moneda de denominación habitual en los contratos del estudio?
> (a) Pesos argentinos (ARS)
> (b) Dólares estadounidenses (USD)
> (c) Pesos uruguayos (UYU)
> (d) Mixto — por favor indicar combinación típica

---

### Bloque C — Umbrales de escalamiento

**Pregunta C1:**
> ¿A partir de qué monto de contrato se debe consultar al socio a cargo antes
> de firmar o enviar comentarios al contrato?
> (Ejemplos: USD 100.000 / USD 500.000 / ARS 50.000.000)

**Pregunta C2:**
> ¿Qué porcentaje de cláusula penal sobre el valor del contrato activa
> una revisión de escalamiento?
> (Por defecto del plugin: 20 % para nivel MEDIO, 30 % para nivel ALTO)

**Pregunta C3:**
> ¿Cuántos días de vigencia sin cláusula de salida generan alerta?
> (Por defecto del plugin: más de 5 años)

---

### Bloque D — Personas de referencia

**Pregunta D1:**
> ¿Cuál es el nombre del socio o área de referencia para contratos que
> superan el umbral de monto definido en C1?

**Pregunta D2:**
> ¿Existe un área o referente específico para:
> (a) Arbitraje internacional → nombre/área:
> (b) Propiedad intelectual → nombre/área:
> (c) Datos personales / privacidad → nombre/área:
> (d) Área financiera para garantías bancarias → nombre/área:
> (Dejar en blanco las que no apliquen)

---

### Bloque E — Estilo y documentos semilla

**Pregunta E1:**
> ¿El estudio tiene contratos modelo o templates propios que deban usarse
> como referencia al sugerir cláusulas? Si es así, ¿cómo se llaman o
> dónde están almacenados?

**Pregunta E2:**
> ¿Alguna preferencia de estilo para los memos de revisión?
> (a) Estilo formal clásico (tratamiento de usted, sin abreviaturas)
> (b) Estilo técnico conciso (tablas, bullets, mínimo texto narrativo)
> (c) Mixto — ejecutivo primero, técnico después
> (Por defecto: mixto)

**Pregunta E3:**
> ¿Alguna norma interna del estudio que deba reflejarse en los análisis?
> (Ej.: no recomendar arbitraje en CIADI salvo instrucción expresa del socio;
> siempre proponer cláusula de mediación previa; usar legislación de tal provincia, etc.)

---

## Paso 2 — Confirmación de perfil

Antes de escribir, mostrar un resumen de las respuestas en formato tabla para que el usuario confirme:

```
RESUMEN DEL PERFIL A GUARDAR
═══════════════════════════════════════════════════════
Jurisdicción principal:          [respuesta A1]
Fuero Argentina:                 [respuesta A2 o N/A]
Fuero Uruguay:                   [respuesta A3 o N/A]
Contratos más frecuentes:        [respuesta B1]
Rol habitual del estudio:        [respuesta B2]
Moneda habitual:                 [respuesta B3]
Umbral de escalamiento (monto):  [respuesta C1]
Umbral cláusula penal MEDIO:     [respuesta C2 — parte 1]
Umbral cláusula penal ALTO:      [respuesta C2 — parte 2]
Vigencia sin salida (alerta):    [respuesta C3]
Socio a cargo:                   [respuesta D1]
Árbitros / PI / Privacidad:      [respuesta D2]
Documentos semilla:              [respuesta E1]
Estilo de memo:                  [respuesta E2]
Notas internas:                  [respuesta E3]
═══════════════════════════════════════════════════════
¿Confirmamos y guardamos este perfil en CLAUDE.md? (sí / no / corregir [campo])
```

---

## Paso 3 — Escritura en CLAUDE.md

Una vez confirmado, reescribir las secciones correspondientes del archivo
`CLAUDE.md` del plugin civil-comercial con los valores recopilados.
Mantener intactas las secciones que no fueron respondidas.

Secciones a actualizar:
- `## Jurisdicción principal`
- `## Tipos de contrato más frecuentes`
- `## Umbrales de riesgo` (ajustar valores en la tabla)
- `## Reglas de escalamiento` (completar montos, nombres y áreas)
- `## Estilo de outputs` (ajustar si el usuario eligió variante)
- `## Documentos semilla` (listar los documentos indicados)
- `## Notas adicionales` (agregar normas internas del estudio)

---

## Paso 4 — Mensaje de cierre

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERFIL GUARDADO EXITOSAMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El perfil de práctica civil y comercial fue actualizado
en CLAUDE.md. Todas las skills del plugin leerán este
perfil en cada análisis.

Para ajustes menores, edite CLAUDE.md directamente.
Para reconfigurar el perfil completo, vuelva a invocar
esta skill: /civil-comercial:cold-start-interview

Skills disponibles:
  /civil-comercial:revision-contratos
  /civil-comercial:revision-nda
  /civil-comercial:historial-cesiones
  /civil-comercial:escala-escalamiento
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- No inferir valores no proporcionados; si el usuario deja una pregunta en blanco, dejar el campo como `[a completar]` en CLAUDE.md.
- No sobrescribir el `## Playbook de cláusulas críticas` existente en CLAUDE.md — ese contenido lo mantiene el equipo del plugin, no la entrevista.
- Si el umbral de monto indicado en C1 parece inusualmente bajo (ej. USD 1.000), advertir antes de guardar y pedir confirmación.
- Si el usuario indica una jurisdicción fuera de Argentina y Uruguay, advertir que el plugin está optimizado para derecho rioplatense y el análisis para otras jurisdicciones requiere revisión adicional.
- Nunca omitir el paso de confirmación (Paso 2) antes de escribir en CLAUDE.md.
