---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil del estudiante de derecho.
  Recopila universidad, año de la carrera, materias prioritarias, formato
  preferido de estudio y áreas de fortaleza y debilidad, y actualiza
  CLAUDE.md con el perfil resultante.
argument-hint: "[ninguno — la skill guía la conversación]"
user-invocable: true
---

# Skill: Cold-Start Interview — Estudiante de Derecho

## Propósito

Configurar el perfil de estudio personalizado antes de usar el drill socrático o el resumen de fallos. Sin este perfil, las skills operan con parámetros genéricos. Con el perfil completo, el drill ajusta la intensidad y los temas al año de la carrera y a las áreas débiles, y el resumen de fallos usa el formato preferido por el estudiante.

---

## Paso 0 — Presentación

Al invocar, mostrar:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIGURACIÓN DE PERFIL — ESTUDIANTE DE DERECHO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Esta entrevista toma entre 5 y 8 minutos.
Las respuestas quedan guardadas en CLAUDE.md y se
usan para personalizar el drill socrático y los
resúmenes de fallos.
Podés actualizar tu perfil en cualquier momento
volviendo a invocar esta skill.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 1 — Recolección de datos (una pregunta por turno)

### Bloque A — Datos académicos

**Pregunta A1:**
> ¿En qué universidad estudiás Derecho?
> ¿Estás en Argentina o Uruguay?

**Pregunta A2:**
> ¿En qué año de la carrera estás? ¿Cuántas materias tenés en curso este semestre/año?

**Pregunta A3:**
> ¿Cuáles son las tres materias en las que más querés mejorar o en las que tenés examen próximo?
> (Estas se priorizan en el drill socrático y en los ejemplos)

**Pregunta A4:**
> ¿Hay materias que ya tenés aprobadas y dominás bien?
> (Esto ayuda a saber qué base de conocimiento puedo asumir que tenés)

---

### Bloque B — Fortalezas y debilidades

**Pregunta B1:**
> ¿Hay algún área del derecho en la que te sentís fuerte o que te resulta fácil?
> (Ej.: derecho constitucional · teoría general del contrato · procesal penal · derecho internacional)

**Pregunta B2:**
> ¿Hay algún área en la que te cuesta más o en la que tenés lagunas?
> (El drill arranca con mayor exigencia en estas áreas para ayudarte a reforzarlas)

**Pregunta B3:**
> ¿Cuál es tu mayor dificultad al estudiar derecho?
> (a) Memorizar normas y artículos
> (b) Entender la lógica detrás de las normas
> (c) Aplicar las normas a casos concretos
> (d) Conectar temas entre materias distintas
> (e) Otro — indicar cuál

---

### Bloque C — Formato de estudio preferido

**Pregunta C1:**
> ¿Cómo preferís que te resuma un fallo?
> (a) **IRAC** — Issue / Rule / Application / Conclusion (útil para exámenes de casos prácticos)
> (b) **Esquema doctrinal** — hechos / norma aplicada / holding / ratio decidendi / obiter dicta (útil para materias de jurisprudencia)
> (c) **Ficha de jurisprudencia** — tribunal · fecha · partes · problema jurídico · solución · relevancia (útil para armarte tu propio fichero)
> (d) **Narrativo** — texto corrido con citas integradas (útil para leer de corrido y entender el hilo)
> (e) Mixto — indicar combinación

**Pregunta C2:**
> ¿Cómo preferís estudiar en general?
> (a) Leer textos y subrayar
> (b) Escuchar explicaciones y hacer preguntas
> (c) Resolver casos prácticos
> (d) Hacer mapas conceptuales o esquemas
> (e) Todo junto, dependiendo del tema

---

### Bloque D — Intensidad del drill

**Pregunta D1:**
> ¿Con qué nivel de intensidad querés que te haga el drill socrático?
> (a) **BÁSICO** — preguntas de comprensión directa ("¿qué dice el art. X?")
> (b) **INTERMEDIO** — preguntas de aplicación ("¿cómo aplica esta norma al caso?") — **recomendado**
> (c) **AVANZADO** — preguntas de análisis crítico, hechos complicadores y casos límite ("¿y si cambiamos este hecho, cambia la solución?")

**Pregunta D2:**
> ¿Tenés algún examen próximo? ¿En qué materia y qué temas entrán?
> (Si la hay: las skills priorizan esos temas en las próximas sesiones)

---

## Paso 2 — Confirmación de perfil

Presentar resumen:

```
RESUMEN DEL PERFIL A GUARDAR — ESTUDIANTE DE DERECHO
═══════════════════════════════════════════════════════
Universidad / país:             [respuesta A1]
Año de la carrera:              [respuesta A2]
Materias prioritarias:          [respuesta A3]
Materias aprobadas / base:      [respuesta A4]
Áreas de fortaleza:             [respuesta B1]
Áreas de debilidad:             [respuesta B2]
Mayor dificultad:               [respuesta B3]
Formato preferido de fallo:     [respuesta C1]
Estilo de estudio:              [respuesta C2]
Intensidad drill socrático:     [respuesta D1]
Examen próximo:                 [respuesta D2 o N/A]
═══════════════════════════════════════════════════════
¿Confirmamos y guardamos este perfil en CLAUDE.md? (sí / no / corregir [campo])
```

---

## Paso 3 — Escritura en CLAUDE.md

Una vez confirmado, reescribir las secciones correspondientes del archivo `CLAUDE.md` del plugin estudiante-derecho.

Secciones a actualizar:
- `## Universidad y sede`
- `## Año de la carrera y materias en curso`
- `## Materias prioritarias (foco de estudio actual)`
- `## Materias aprobadas (base de conocimiento disponible)`
- `## Áreas de fortaleza`
- `## Áreas de debilidad o dificultad`
- `## Formato preferido de estudio`
- `## Jurisdicción principal de estudio`
- `## Intensidad del drill socrático`
- `## Examen próximo`

---

## Paso 4 — Mensaje de cierre

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERFIL GUARDADO EXITOSAMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tu perfil de estudio fue guardado en CLAUDE.md.
El drill socrático y los resúmenes de fallos van a
usar este perfil de ahora en adelante.

Para actualizar el perfil (ej. nuevo examen próximo),
volvé a invocar esta skill o editá CLAUDE.md directamente.

Skills disponibles:
  /estudiante-derecho:drill-socratico
  /estudiante-derecho:resumen-fallo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- No inferir el año de la carrera a partir del nombre de las materias — preguntar siempre.
- No registrar información personal sensible del estudiante (ej. situación económica, familiar, de salud) en CLAUDE.md — ese perfil es solo de estudio.
- Si el estudiante indica un examen en menos de 7 días, priorizarlo en el mensaje de cierre y sugerir arrancar con el drill socrático en esa materia de inmediato.
- Si el estudiante indica que está en primer año o que tiene pocas materias aprobadas, ajustar el nivel de intensidad por defecto a BÁSICO, independientemente de lo que haya elegido en D1.
