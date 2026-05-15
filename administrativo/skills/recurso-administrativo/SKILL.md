---
name: recurso-administrativo
description: >
  Identifica y estructura el recurso administrativo correcto ante actos de la Administración
  en Uruguay (Decreto 500/991, recurso de revocación / jerárquico / anulación ante TCA) y
  Argentina (Ley 19.549, recurso de reconsideración / jerárquico / alzada). Calcula plazos
  y genera el escrito base para revisión del abogado.
argument-hint: "[descripción del acto / resolución impugnada] [--jurisdiccion=UY|AR]"
user-invocable: true
---

# Skill: Recurso Administrativo

## Propósito

Identificación del recurso correcto, cálculo de plazos fatales y generación del escrito base
para impugnar actos administrativos en Uruguay y Argentina. Los plazos en materia administrativa
son generalmente de días hábiles y son fatales — una presentación tardía cierra la vía administrativa
y puede impedir el posterior acceso a la vía jurisdiccional.

---

## Paso 0 — Recolección de datos

1. **Jurisdicción:** Uruguay / Argentina / Ambas (ente bi-jurisdiccional)
2. **Descripción del acto impugnado:** (resolución, disposición, acto de trámite)
3. **Organismo emisor:** nombre del ente u organismo
4. **Fecha de notificación al administrado:** (día/mes/año)
5. **Contenido del acto:** ¿Qué decidió?
6. **Agravios del recurrente:** ¿En qué se apoya la impugnación?
   - Vicio de procedimiento / falta de motivación
   - Exceso de poder / desviación de poder
   - Violación de norma superior
   - Error en los hechos
   - Lesión a derechos adquiridos
7. **¿El recurrente tiene legitimación activa?** ¿Es titular de un derecho o interés legítimo afectado?

---

## Paso 1 — Identificación del recurso correcto

### Uruguay (Decreto 500/991 — Procedimiento Administrativo)

```
Árbol de decisión:

¿El acto es de un Ministerio u organismo centralizado?
→ SÍ: Recurso de Revocación (ante el mismo órgano) — plazo: 10 días hábiles desde notificación
       Agotada revocación → Recurso Jerárquico (ante jerarca máximo / Presidencia) — plazo: 10 días
       Agotada vía → Acción de Nulidad ante TCA — plazo: 60 días corridos desde agotamiento
       
¿El acto es de un Ente Autónomo o Servicio Descentralizado (BCU, URSEA, ANP, ANTEL, etc.)?
→ Recurso de Revocación ante el propio ente — 10 días hábiles
  Agotada vía → Acción de Nulidad ante TCA — 60 días corridos

¿El acto es omisión / silencio administrativo?
→ Denuncia de mora — exigir respuesta en 150 días hábiles (art. 8 Ley 15.869)
  Silencio transcurrido → denegatoria ficta → habilita vía ante TCA

Plazos fatales Uruguay:
- Recurso de revocación: 10 días hábiles desde notificación
- Recurso jerárquico: 10 días hábiles desde resolución o silencio de revocación
- Acción de nulidad TCA: 60 días corridos desde agotamiento de vía administrativa
```

### Argentina (Ley 19.549 — LPA + RLPA Decreto 1759/72)

```
Árbol de decisión:

¿El acto es definitivo o asimilable a definitivo (causa estado)?
→ SÍ: Recurso de Reconsideración (ante el mismo órgano) — plazo: 10 días hábiles
       O Recurso Jerárquico (ante jerarca del organismo) — plazo: 15 días hábiles
       O Recurso de Alzada (si es ente descentralizado, ante Ministerio) — plazo: 15 días

¿El acto es de trámite pero causa indefensión o retarda?
→ Recurso de Queja — sin plazo fijo, aconsejable dentro de 5 días

¿Agotada la vía administrativa?
→ Acción judicial:
   - Acción contencioso-administrativa federal: ante Cámara CAF, plazo 90 días hábiles judiciales
   - Acción de amparo (si hay urgencia y violación manifiesta): plazo: dentro de la lesión

Silencio administrativo Argentina:
- Vencido el plazo de 30 días sin resolución → denegatoria ficta → habilita impugnación

Plazos fatales Argentina:
- Reconsideración: 10 días hábiles (RLPA art. 84)
- Jerárquico: 15 días hábiles (RLPA art. 90)
- Alzada: 15 días hábiles (RLPA art. 94)
- Acción judicial post-agotamiento: 90 días hábiles judiciales (Ley 26.854 cautelares)
```

---

## Paso 2 — Cálculo de plazos

Con la fecha de notificación provista, calcular:

| Hito | Fecha límite | Días restantes |
|---|---|---|
| Vencimiento recurso [tipo] | [DD/MM/AAAA] | [N] días hábiles |
| Vencimiento jerárquico (si aplica) | [DD/MM/AAAA] | [N] días hábiles |
| Vencimiento acción judicial | [DD/MM/AAAA] | [N] días |

⚠️ Si quedan menos de 5 días hábiles para cualquier plazo: mostrar banner de alerta urgente.

---

## Paso 3 — Generación del escrito base

### Uruguay — Recurso de Revocación (modelo)

```
[Ciudad], [DD] de [mes] de [AAAA]

Señor/a Ministro/a de [MINISTERIO] / Presidente/a de [ENTE]
Presente

[NOMBRE RECURRENTE], C.I. / RUT [XXXXXXXXX], con domicilio en [DIRECCIÓN], constituyendo
domicilio procesal en [DIRECCIÓN MONTEVIDEO O CIUDAD SEDE], a Ud. me dirijo a fin de
interponer RECURSO DE REVOCACIÓN conforme al artículo 317 de la Constitución de la República
y el Decreto 500/991, contra [IDENTIFICACIÓN DEL ACTO: número, fecha, objeto].

I. LEGITIMACIÓN ACTIVA
[El recurrente es titular de un derecho subjetivo / interés legítimo afectado por el acto porque...]

II. ACTO IMPUGNADO
[Descripción precisa del acto, fecha, contenido dispositivo]

III. AGRAVIOS
[Desarrollar cada agravio: primero los de nulidad, luego los de mérito]
A. [Primer agravio — vicio de procedimiento / falta de motivación / violación normativa]
B. [Segundo agravio — ...]

IV. DERECHO
[Artículos de la Constitución, Decreto 500/991, ley sectorial aplicable]

V. PETITORIO
Por lo expuesto, solicito:
1. Se tenga por interpuesto en tiempo y forma el presente recurso de revocación.
2. Se revoque / modifique / anule el acto impugnado por las razones expuestas.
3. [Otras peticiones accesorias]

Provea de conformidad.

[FIRMA]
[ACLARACIÓN Y NÚMERO DE CÉDULA]
[DATOS DEL ABOGADO PATROCINANTE si corresponde]
```

### Argentina — Recurso de Reconsideración (modelo)

```
[Ciudad], [DD] de [mes] de [AAAA]

Señor/a [CARGO Y NOMBRE DEL FUNCIONARIO]
[Organismo]
Expediente N°: [si existe]

[NOMBRE RECURRENTE], CUIT/CUIL [XXXXXXXX], con domicilio real en [DIRECCIÓN] y
constituyendo domicilio especial administrativo en [DIRECCIÓN], me presento y digo:

I. OBJETO
Que en legal tiempo y forma vengo a interponer Recurso de Reconsideración (art. 84 RLPA)
contra [ACTO: número / fecha / contenido], notificado con fecha [DD/MM/AAAA].

II. LEGITIMACIÓN
[El recurrente es titular de un derecho subjetivo / interés legítimo afectado...]

III. HECHOS
[Narración cronológica de los hechos relevantes]

IV. DERECHO
[Fundamentos: LPA arts. X, CCyCN si aplica, normativa sectorial]

V. AGRAVIOS
A. [Vicio de procedimiento / ausencia de motivación / art. 7 LPA]
B. [Exceso de poder / desviación de poder]
C. [Error en la apreciación de los hechos]

VI. OFRECE PRUEBA (si aplica)
[Documental / testimonial / pericial]

VII. PETITORIO
1. Se tenga por interpuesto en tiempo y forma el presente recurso.
2. Se revoque / modifique el acto atacado.
3. [Subsidiariamente: se eleve en jerárquico si no hay resolución en plazo]

Provea V.S. de conformidad.

[FIRMA DEL RECURRENTE Y LETRADO]
[TOMO Y FOLIO del letrado si aplica]
```

---

## Paso 4 — Output y compuerta

```
COMPUERTA ANTES DE PRESENTAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Abogado matriculado revisó y completó el escrito
□ Plazo verificado contra fecha exacta de notificación
□ Legitimación activa del recurrente confirmada
□ Agravios priorizados: primero los de nulidad (forma), luego mérito
□ Domicilio procesal / especial constituido en sede del organismo
□ Presentación: formato papel y/o electrónico según el organismo
□ Copia sellada para el expediente del recurrente

DESPUÉS DE PRESENTAR:
→ Archivar constancia de presentación (sello / número de ingreso)
→ Anotar fecha de inicio del plazo de resolución
→ Calendarizar el vencimiento del silencio administrativo
→ Si sin respuesta en plazo: coordinar si se agota vía o se interpone el siguiente recurso
```

---

## Guardrails

- Los plazos en materia administrativa son fatales — nunca subestimar su importancia.
- En Uruguay, el plazo de 60 días ante el TCA corre desde la notificación del último acto o desde que el silencio habilita la acción — verificar siempre cuál es el hito correcto.
- En Argentina, el Decreto 1759/72 sufrió reformas — verificar la versión vigente con el conector de investigación.
- Nunca afirmar que el recurso "prosperará" — solo que está correctamente formulado para la revisión profesional.
- Si el agravio involucra derechos constitucionales de urgente tutela: alertar sobre la posibilidad de medida cautelar o amparo paralelo.
