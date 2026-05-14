---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil de la clínica jurídica universitaria.
  Recopila universidad, área(s) de práctica, postura pedagógica, nivel de los estudiantes
  y preferencias de supervisión, y actualiza CLAUDE.md con el perfil resultante.
argument-hint: "[ninguno — la skill guía la conversación]"
user-invocable: true
---

# Skill: Cold-Start Interview — Clínica Jurídica

## Propósito

Configurar el perfil pedagógico e institucional de la clínica jurídica universitaria antes de usar cualquier otra skill del plugin. Sin este perfil, las skills de ingreso de cliente y elaboración de memos operan con valores genéricos. Con el perfil completo, el asistente adapta su postura socrática, el nivel de detalle y las referencias normativas al contexto real de la clínica.

---

## Paso 0 — Presentación

Al invocar la skill, mostrar el siguiente bloque introductorio:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIGURACIÓN DE PERFIL — CLÍNICA JURÍDICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Esta entrevista toma entre 10 y 15 minutos.
Las respuestas quedan guardadas en CLAUDE.md y las usan
todas las skills de este plugin.
Puede ser completada por el supervisor o coordinador
de la clínica. Responda con la información actual.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 1 — Recolección de datos (una pregunta por turno)

### Bloque A — Institución y contexto

**Pregunta A1:**
> ¿En qué universidad funciona la clínica jurídica?
> ¿Tiene nombre propio? (Ej.: Clínica de Interés Público · Clínica de Derechos Humanos · Consultorio Jurídico)

**Pregunta A2:**
> ¿En qué ciudad o departamento está ubicada la clínica?
> ¿Bajo qué fuero o jurisdicción trabajan principalmente los casos?

**Pregunta A3:**
> ¿Quién es el supervisor o coordinador docente de la clínica?
> ¿Hay más de un supervisor? ¿Cómo se asignan los casos entre ellos?

---

### Bloque B — Área(s) de práctica

**Pregunta B1:**
> ¿En qué área(s) de derecho trabaja la clínica?
> Seleccionar todos los que apliquen:
> - Derecho del consumidor
> - Derecho de familia y niñez
> - Derechos humanos e interés público
> - Derecho laboral
> - Derecho ambiental
> - Derecho de la vivienda y arrendamientos
> - Privacidad y datos personales
> - Derecho migratorio
> - Derecho penal (¿en qué rol: defensa, víctimas, ambos?)
> - Otro — indicar cuál

**Pregunta B2:**
> ¿Hay áreas que la clínica explícitamente no acepta?
> (Ej.: causas penales con imputados / causas empresariales / causas con honorarios pactados)

---

### Bloque C — Nivel y postura pedagógica

**Pregunta C1:**
> ¿En qué año de la carrera están los estudiantes que participan en la clínica?
> ¿Tienen materias básicas ya aprobadas (contratos, procesal, constitucional)?

**Pregunta C2:**
> ¿Cuál es la postura pedagógica que el supervisor prefiere para el asistente?
> (a) ASISTIR — el asistente puede dar orientación directa cuando el estudiante está bloqueado
> (b) GUIAR — el asistente formula preguntas y da pistas, pero no resuelve el problema
> (c) ENSEÑAR — el asistente explica el principio general pero nunca aplica por el estudiante
> (d) Mixto — indicar cuándo usar cada modalidad

**Pregunta C3:**
> ¿Qué formato prefiere el supervisor para los memos de análisis de caso?
> (a) IRAC (Issue / Rule / Application / Conclusion) — un bloque por issue
> (b) Esquema doctrinal (hechos / norma aplicada / holding / ratio decidendi)
> (c) Narrativo con citas al pie
> (d) Mixto — indicar combinación

---

### Bloque D — Supervisión y escalamiento

**Pregunta D1:**
> ¿Cuáles son las condiciones bajo las cuales el estudiante debe escalar el caso al supervisor de forma inmediata (sin asesorar primero)?

**Pregunta D2:**
> ¿Existe un protocolo de verificación de conflictos de interés con casos anteriores o actuales de la clínica?
> ¿Cómo se registran los casos para poder verificar?

**Pregunta D3:**
> ¿La clínica tiene áreas o profesionales de derivación para casos fuera de su alcance (ej.: causas penales complejas, amparos urgentes, casos con impacto colectivo)?
> Si es así: ¿a quién se deriva y bajo qué condiciones?

---

### Bloque E — Infraestructura y normativa

**Pregunta E1:**
> ¿La clínica opera bajo alguna normativa institucional específica sobre confidencialidad, consentimiento del cliente, o registro de casos?

**Pregunta E2:**
> ¿Los estudiantes cuentan con alguna herramienta de gestión de expedientes o calendario de vencimientos?

**Pregunta E3:**
> ¿Hay algún formato de ficha de ingreso o memo que el supervisor quiera mantener aunque el asistente lo ayude a completar?

---

## Paso 2 — Confirmación de perfil

Presentar resumen antes de guardar:

```
RESUMEN DEL PERFIL A GUARDAR — CLÍNICA JURÍDICA
═══════════════════════════════════════════════════════
Universidad:                    [respuesta A1]
Ciudad / jurisdicción:          [respuesta A2]
Supervisor/a:                   [respuesta A3]
Áreas de práctica:              [respuesta B1]
Áreas excluidas:                [respuesta B2 o N/A]
Nivel de los estudiantes:       [respuesta C1]
Postura pedagógica:             [respuesta C2]
Formato de memo:                [respuesta C3]
Condiciones de escalamiento:    [respuesta D1]
Protocolo de conflictos:        [respuesta D2]
Áreas de derivación:            [respuesta D3 o N/A]
Normativa institucional:        [respuesta E1 o N/A]
Gestor de expedientes:          [respuesta E2 o N/A]
Formato de ficha propio:        [respuesta E3 o N/A]
═══════════════════════════════════════════════════════
¿Confirmamos y guardamos este perfil en CLAUDE.md? (sí / no / corregir [campo])
```

---

## Paso 3 — Escritura en CLAUDE.md

Una vez confirmado, reescribir las secciones correspondientes del archivo `CLAUDE.md` del plugin clinica-juridica. Mantener intactas las secciones que no fueron respondidas.

Secciones a actualizar:
- `## Universidad y sede de la clínica`
- `## Área(s) de práctica de la clínica`
- `## Postura pedagógica`
- `## Nivel de los estudiantes`
- `## Supervisor(a) de la clínica`
- `## Áreas de derivación` (completar referentes y condiciones)
- `## Umbrales de supervisión directa` (ajustar si el supervisor agregó condiciones)
- `## Jurisdicción principal de la clínica`
- `## Fueros habituales`
- `## Notas adicionales` (agregar normativa institucional particular)

---

## Paso 4 — Mensaje de cierre

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERFIL GUARDADO EXITOSAMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El perfil de la clínica jurídica fue actualizado en
CLAUDE.md. Todas las skills del plugin leerán este
perfil en cada sesión de trabajo.

Para ajustes menores, edite CLAUDE.md directamente.
Para reconfigurar el perfil completo, vuelva a invocar
esta skill: /clinica-juridica:cold-start-interview

Skills disponibles:
  /clinica-juridica:ingreso-cliente
  /clinica-juridica:memo-caso
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- No inferir valores no proporcionados; si el supervisor deja una pregunta en blanco, dejar el campo como `[a completar]` en CLAUDE.md.
- No registrar datos de clientes ni de casos en CLAUDE.md — ese archivo es de configuración institucional, no de expedientes.
- Si el supervisor indica que la clínica acepta causas penales, registrar con precisión si es en rol de defensa, de asistencia a víctimas, o ambos — el rol define la postura y los límites del asesoramiento.
- Nunca omitir el paso de confirmación (Paso 2) antes de escribir en CLAUDE.md.
- Si el supervisor menciona que los estudiantes son de primeros años sin materias procesales aprobadas, consignar en la postura pedagógica que el asistente debe explicar conceptos procesales básicos antes de formular preguntas socráticas avanzadas.
