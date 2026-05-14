---
name: diff-politica
description: >
  Análisis de brecha entre un cambio normativo nuevo y las políticas internas vigentes
  del cliente. Identifica políticas desactualizadas, nuevas obligaciones, plazos de
  adecuación y áreas del negocio impactadas, y produce tabla de brechas con prioridad.
argument-hint: "[texto o referencia del cambio normativo y descripción de las políticas del cliente]"
user-invocable: true
---

# Skill: Análisis de Brecha entre Cambio Normativo y Políticas Internas (diff-política)

## Propósito

Comparar un cambio normativo reciente (resolución, comunicación, decreto, circular, ley)
contra la biblioteca de políticas internas del cliente y producir un análisis de brechas
que permita al abogado asesorar sobre qué documentos internos deben actualizarse, en qué
plazo y con qué prioridad. El output es una tabla de brechas con columnas de prioridad,
plazo y área impactada.

---

## Paso 0 — Recolección de datos

Solicitar al abogado:

1. **Texto o referencia del cambio normativo:**
   - Nombre completo de la norma (ej. "Comunicación A 7724 del BCRA, 12/03/2024").
   - Texto completo o fragmentos relevantes (si está disponible).
   - Si no está disponible el texto, solicitar la referencia exacta para localizarlo.

2. **¿Cuándo entró en vigencia la norma?** ¿Hay un plazo de adecuación explícito?

3. **Biblioteca de políticas del cliente:**
   - Lista de políticas, procedimientos o manuales vigentes del cliente (con fecha de
     última actualización si está disponible).
   - Si el cliente tiene documentos cargados como semillas en CLAUDE.md, usarlos.
   - Si no hay documentos disponibles, solicitar al menos la descripción de las áreas
     de políticas existentes (AML, seguridad de la información, atención al cliente,
     RRHH, ventas, etc.).

4. **Sector del cliente y organismos reguladores relevantes** (referencia al CLAUDE.md).

5. **Áreas del negocio del cliente** que podrían estar impactadas (compliance, legal,
   operaciones, tecnología, comercial, RRHH, etc.).

---

## Paso 1 — Análisis del cambio normativo

Descomponer el cambio normativo en sus elementos constitutivos:

### 1.1 Identificación de la norma

| Campo | Contenido |
|---|---|
| Tipo de norma | Ley / Decreto / Resolución / Comunicación / Circular / Disposición |
| Organismo emisor | [BCU / BCRA / URSEC / CNV / AAIP / ANMAT / etc.] |
| Número y fecha | [Número y día/mes/año] |
| Vigencia | [Fecha de entrada en vigor] |
| Plazo de adecuación | [Si lo hay: día/mes/año] |
| Derogaciones | [Normas anteriores que deroga o modifica] |
| Publicación oficial | [Diario Oficial UY / Boletín Oficial AR — fecha] |

### 1.2 Resumen de las obligaciones nuevas

Para cada artículo o sección relevante de la norma, extraer:

| N.° | Artículo / Sección | Obligación nueva | Sujeto obligado | Plazo de cumplimiento |
|---|---|---|---|---|
| 1 | Art. X | [Descripción concisa de la obligación] | [Empresa / Persona física / Sector] | [Plazo] |

### 1.3 Clasificación del impacto

Para cada obligación nueva, clasificar:
- **Tipo:** Nueva obligación / Modificación de obligación existente / Derogación de obligación
- **Área de impacto:** Compliance / Legal / Operaciones / Tecnología / RRHH / Comercial / Atención al cliente / Otro
- **Nivel de cambio:** Estructural (requiere rediseño de proceso) / Documental (requiere actualización de política) / Formal (requiere actualización de formularios o comunicaciones)

---

## Paso 2 — Análisis de la biblioteca de políticas del cliente

Para cada política o procedimiento del cliente (o área temática si no hay documentos):

| N.° | Política / Procedimiento | Última actualización | Cobertura actual | ¿Cubre las nuevas obligaciones? |
|---|---|---|---|---|
| 1 | [Nombre del documento] | [Fecha] | [Descripción del alcance actual] | Sí completo / Parcial / No |

Si los documentos están disponibles, analizar sección a sección. Si solo se cuenta con
la descripción del cliente, hacer el análisis en base a la descripción.

---

## Paso 3 — Tabla de brechas

Producir la tabla central del análisis con el siguiente formato:

| N.° Brecha | Obligación nueva (norma + art.) | Política/área interna afectada | Tipo de brecha | Prioridad | Plazo de adecuación | Área responsable | Acción recomendada |
|---|---|---|---|---|---|---|---|
| B1 | [Art. X — Com. A XXXX BCRA] | [Política de Crédito v2.1] | Ausencia total | 🔴 CRÍTICA | [día/mes/año] | Compliance | Redactar nueva sección sobre [tema] |
| B2 | [Art. Y — Com. A XXXX BCRA] | [Manual de Atención al Cliente] | Actualización parcial | 🟡 ALTA | [día/mes/año] | Operaciones | Actualizar cláusula X para incluir [obligación] |
| B3 | [Art. Z — Com. A XXXX BCRA] | [Política de Seguridad de la Información] | Sin impacto | 🟢 OK | — | — | Sin acción requerida |

**Criterios de prioridad:**
- **CRÍTICA (🔴):** La brecha implica incumplimiento legal desde la fecha de vigencia.
  Puede generar sanciones inmediatas. Requiere adecuación antes del plazo legal.
- **ALTA (🟡):** La brecha requiere adecuación dentro del plazo de transición previsto
  por la norma o dentro de 30 días si no hay plazo explícito.
- **MEDIA (🟠):** La brecha es una mejora de cumplimiento recomendable pero no urgente.
  Plazo sugerido: 60-90 días.
- **BAJA (⚪):** La brecha es menor o la política vigente cubre sustancialmente la nueva
  obligación con ajustes de redacción. Puede incorporarse en la próxima revisión ordinaria.

---

## Paso 4 — Nuevas políticas o procedimientos requeridos

Si la norma crea obligaciones que no tienen correlato en ninguna política existente del
cliente, listar las nuevas políticas o procedimientos que deben crearse:

| N.° | Documento nuevo requerido | Contenido mínimo | Área responsable | Plazo |
|---|---|---|---|---|
| NP1 | [Nombre del documento] | [Descripción del contenido mínimo exigido por la norma] | [Área] | [día/mes/año] |

---

## Paso 5 — Impacto en áreas del negocio

Producir un resumen del impacto por área del negocio:

| Área | Impacto | Documentos afectados | Prioridad máxima |
|---|---|---|---|
| Compliance | Alto / Medio / Bajo / Sin impacto | [Lista] | [🔴/🟡/🟠/⚪] |
| Legal | | | |
| Operaciones | | | |
| Tecnología / IT | | | |
| Recursos Humanos | | | |
| Comercial / Ventas | | | |
| Atención al cliente | | | |
| Dirección / Gobierno | | | |

---

## Paso 6 — Resumen ejecutivo y plan de acción

Producir:

**Resumen ejecutivo (3 párrafos):**
1. Descripción del cambio normativo y su alcance general.
2. Número de brechas identificadas por prioridad y áreas más impactadas.
3. Recomendación principal y riesgos de no actuar.

**Plan de acción priorizado:**

| Prioridad | Acción | Responsable | Plazo | Estado inicial |
|---|---|---|---|---|
| 1 | [Acción crítica más urgente] | [Área / Abogado] | [Fecha] | Pendiente |
| 2 | ... | ... | ... | ... |

---

## Paso 7 — Alertas especiales

Señalar explícitamente si:

- Hay obligaciones con **plazo de adecuación ya vencido o próximo a vencer** (< 15 días).
- La norma requiere **notificación al organismo regulador** de las medidas adoptadas.
- La norma genera **nuevas obligaciones de registro, reporte o declaración** periódica.
- El incumplimiento puede generar **sanciones con efecto suspensivo o inhabilitación**
  de la operación.
- El análisis requiere **consulta adicional al organismo** por ambigüedad interpretativa.

---

## Guardrails

- **No sustituir la lectura directa de la norma** por el abogado. El skill produce un
  análisis basado en el texto aportado, pero siempre es el abogado quien valida la
  interpretación legal.
- **Si la norma tiene artículos de interpretación ambigua**, señalarlo explícitamente
  y no asumir la interpretación más restrictiva ni la más laxa: presentar ambas opciones
  al abogado.
- **Si el cliente opera en ambas jurisdicciones**, asegurarse de que el análisis cubra
  las obligaciones de ambas y no mezcle normas de una con plazos de la otra.
- **Si la norma afecta un área de alto riesgo** (AML, seguridad de la información,
  habilitaciones), escalar al socio de práctica antes de remitir el análisis al cliente.
- **No incluir en el análisis información confidencial de terceros clientes** que pueda
  haberse utilizado como referencia.
- **Verificar siempre** si la norma tiene normas complementarias, aclaraciones o
  preguntas frecuentes publicadas por el organismo emisor, ya que suelen afectar la
  interpretación.
