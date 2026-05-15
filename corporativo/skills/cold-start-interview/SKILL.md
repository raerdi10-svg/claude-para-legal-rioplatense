---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil corporativo y M&A del estudio.
  Recopila tipos de operación habituales, tamaño típico de deal, jurisdicciones,
  organismos de registro principales, referentes de práctica y preferencias de
  estilo, y escribe el perfil resultante en CLAUDE.md del plugin corporativo.
argument-hint: "[opcional: nombre del estudio o socio M&A a cargo]"
user-invocable: true
---

# Skill: Cold-Start Interview — Corporativo y M&A

## Propósito

Configurar el perfil de práctica corporativa y M&A del estudio antes de usar cualquier otra skill del plugin. Con el perfil configurado, las skills de revisión tabular, extracción de issues, redacción de actas y tracker de cumplimiento reflejan los estándares, umbrales, personas de referencia y tipos de operación reales del estudio.

---

## Paso 0 — Presentación

Al invocar la skill, mostrar el siguiente bloque introductorio:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIGURACIÓN DE PERFIL — PRÁCTICA CORPORATIVA Y M&A
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

### Bloque A — Jurisdicción y tipos de sociedad

**Pregunta A1:**
> ¿En qué jurisdicción(es) opera principalmente la práctica corporativa del estudio?
> (a) Solo Argentina — LGS Ley 19.550; IGJ / DPPJ
> (b) Solo Uruguay — LSC Ley 16.060; AIN
> (c) Ambas jurisdicciones con igual peso
> (d) Otra combinación — detallar

**Pregunta A2:**
> ¿Cuáles son los tipos de sociedad más frecuentes en los asuntos del estudio?
> Seleccionar todos los que apliquen:
> (a) SA (sociedad anónima) — Argentina
> (b) SRL — Argentina
> (c) SAS (sociedad por acciones simplificada) — Argentina
> (d) SA — Uruguay
> (e) SRL — Uruguay
> (f) Sucursales de sociedades extranjeras (art. 118 LGS / art. 192 LSC)
> (g) Holdigns offshore con operaciones en AR/UY

**Pregunta A3:**
> ¿El estudio trabaja con sociedades cotizantes en bolsa (CNV / BCU)?
> (a) Sí, regularmente
> (b) Ocasionalmente
> (c) No

---

### Bloque B — Tipos de operación

**Pregunta B1:**
> ¿Cuáles son los tipos de operación M&A más frecuentes?
> (a) Share deal (compraventa de acciones / cuotas)
> (b) Asset deal (compraventa de activos / fondo de comercio)
> (c) Fusión o escisión societaria
> (d) Constitución de joint ventures societarios
> (e) Reestructuración de grupo económico
> (f) Private equity / venture capital (suscripción de acciones, notas convertibles)
> (g) Otra — detallar

**Pregunta B2:**
> ¿Cuál es el tamaño típico de deal que maneja el estudio?
> (a) Small cap — hasta USD 5.000.000
> (b) Mid cap — entre USD 5.000.001 y USD 50.000.000
> (c) Large cap — más de USD 50.000.000
> (d) Mixto — indicar el rango más frecuente

**Pregunta B3:**
> ¿Cuál es el umbral de monto a partir del cual un deal requiere coordinación
> con el socio M&A principal desde el inicio?
> (Ejemplo: desde el primer email de NDA / desde la firma del LOI / desde el inicio del due diligence)

---

### Bloque C — Due diligence

**Pregunta C1:**
> En los due diligences del estudio, ¿cuáles son las categorías que siempre
> se revisan y cuáles son opcionales según el deal?
> Categorías disponibles: societario, laboral, fiscal, contractual, PI,
> litigioso, ambiental, regulatorio

**Pregunta C2:**
> ¿El estudio suele estar del lado comprador (buy-side) o vendedor (sell-side),
> o ambos con igual frecuencia?

**Pregunta C3:**
> ¿Existe un formato de VDR (virtual data room) habitual que el estudio usa?
> (Intralinks, Datasite, iDeals, SharePoint, otro)
> Esto permite adaptar la nomenclatura de la revisión tabular.

---

### Bloque D — Gobierno corporativo y cumplimiento

**Pregunta D1:**
> ¿El estudio tiene clientes con sociedades que deben presentar balances regularmente
> ante IGJ (Argentina) o AIN (Uruguay)?
> (a) Sí, gestionamos el cumplimiento societario de varios clientes
> (b) Solo ocasionalmente
> (c) No

**Pregunta D2:**
> ¿El estudio redacta actas de directorio y de asamblea de forma habitual?
> Si es así, ¿tienen templates propios que deban respetarse?

**Pregunta D3:**
> ¿Hay sectores regulados entre los clientes del estudio?
> (Ej.: financiero — BCU / BCRA; energético — MIEM / Secretaría de Energía;
> salud — ANMAT / MSP; telecomunicaciones — URSEC / ENACOM)

---

### Bloque E — Personas de referencia

**Pregunta E1:**
> ¿Cuál es el nombre del socio o área de referencia para deals M&A que superan
> el umbral de monto definido en B3?

**Pregunta E2:**
> ¿Existe un área o referente específico para:
> (a) Defensa de la competencia / notificación CNDC/URSEC → nombre/área:
> (b) Cumplimiento regulatorio (CNV, BCU) → nombre/área:
> (c) Fiscalidad de la transacción → nombre/área:
> (d) PI en due diligence → nombre/área:
> (e) Laboral en due diligence → nombre/área:
> (Dejar en blanco las que no apliquen)

---

### Bloque F — Estilo y documentos semilla

**Pregunta F1:**
> ¿El estudio tiene modelos de:
> (a) SPA (Share Purchase Agreement)
> (b) Acuerdo de accionistas
> (c) Actas de directorio / resoluciones de socios
> (d) Acuerdos de LOI / carta de intención
> Si es así, ¿cómo se llaman o dónde están almacenados?

**Pregunta F2:**
> ¿Alguna preferencia específica de estilo para los memos y tablas de due diligence?
> (a) Tablas concisas — una fila por documento, observación en bullet points
> (b) Análisis narrativo por categoría con tabla de resumen
> (c) Mixto — tabla primero, narrativo donde hay issues ALTO
> (Por defecto: mixto)

**Pregunta F3:**
> ¿Alguna norma interna del estudio que deba reflejarse en los análisis?
> (Ej.: siempre incluir reserva de precio en SPAs que superen X monto;
> nunca recomendar fusión por absorción sin aprobación de asamblea extraordinaria;
> siempre verificar Ley 19.484 UY de beneficiario final en deals con offshore)

---

## Paso 2 — Confirmación de perfil

Antes de escribir, mostrar un resumen en formato tabla para que el usuario confirme:

```
RESUMEN DEL PERFIL CORPORATIVO A GUARDAR
═══════════════════════════════════════════════════════
Jurisdicción principal:           [respuesta A1]
Tipos de sociedad habituales:     [respuesta A2]
Cotizantes:                       [respuesta A3]
Operaciones más frecuentes:       [respuesta B1]
Tamaño típico de deal:            [respuesta B2]
Umbral de coordinación con socio: [respuesta B3]
Categorías de DD siempre cubiertas:[respuesta C1]
Rol habitual (buy/sell):          [respuesta C2]
Plataforma VDR habitual:          [respuesta C3]
Cumplimiento societario:          [respuesta D1]
Actas y templates propios:        [respuesta D2]
Sectores regulados:               [respuesta D3]
Socio M&A de referencia:          [respuesta E1]
Referentes especializados:        [respuesta E2]
Documentos semilla:               [respuesta F1]
Estilo de memo DD:                [respuesta F2]
Normas internas:                  [respuesta F3]
═══════════════════════════════════════════════════════
¿Confirmamos y guardamos este perfil en CLAUDE.md? (sí / no / corregir [campo])
```

---

## Paso 3 — Escritura en CLAUDE.md

Una vez confirmado, actualizar las secciones correspondientes del archivo `CLAUDE.md` del plugin corporativo con los valores recopilados.

Secciones a actualizar:
- `## Jurisdicción principal`
- `## Tipos de operación más frecuentes`
- `## Tamaño típico de deal` (ajustar rangos con los del estudio)
- `## Jurisdicciones y organismos de registro` (ajustar si hay jurisdicciones adicionales)
- `## Reglas de escalamiento` (completar montos, nombres y áreas)
- `## Estilo de outputs` (ajustar si el usuario eligió variante)
- `## Documentos semilla` (listar los documentos indicados)
- `## Notas adicionales` (agregar normas internas del estudio)

---

## Paso 4 — Mensaje de cierre

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERFIL CORPORATIVO GUARDADO EXITOSAMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El perfil de práctica corporativa y M&A fue actualizado
en CLAUDE.md. Todas las skills del plugin lo leerán
en cada análisis.

Skills disponibles:
  /corporativo:revision-tabular
  /corporativo:extraccion-issues
  /corporativo:consentimiento-directorio
  /corporativo:cumplimiento-sociedades
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- No inferir valores no proporcionados; dejar los campos sin respuesta como `[a completar]` en CLAUDE.md.
- Si el usuario indica que trabaja con cotizantes, añadir una nota en CLAUDE.md recordando que el análisis de operaciones con sociedades abiertas requiere verificación adicional de normativa CNV/BCU y puede tener obligaciones de disclosure.
- Si el usuario indica sectores regulados, agregar en "Notas adicionales" la referencia al organismo regulador correspondiente y la necesidad de verificar aprobaciones de change of control.
- Nunca omitir el paso de confirmación (Paso 2) antes de escribir en CLAUDE.md.
