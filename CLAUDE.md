# Claude para Legal Rioplatense — Documentación del Repositorio

> Guía técnica para asistentes de IA que trabajen sobre este repositorio.
> Para instrucciones de uso del sistema, ver `README.md` y `QUICKSTART.md`.

---

## Qué es este repositorio

Sistema de plugins y agentes para flujos de trabajo jurídicos en **Uruguay y Argentina**. Cada plugin cubre un área de práctica (civil-comercial, laboral, corporativo, litigio, privacidad, etc.) y expone skills que Claude ejecuta automáticamente o bajo comando slash.

El mismo sistema corre en tres superficies:
- **Claude Cowork** — plugins instalados desde el marketplace
- **Claude Code** — plugins instalados con `/plugin install`
- **Claude Managed Agents API** — agentes programados deployados con `scripts/deploy-managed-agent.sh`

---

## Estructura del repositorio

```
claude-para-legal-rioplatense/
│
├── CLAUDE.md                          ← este archivo (doc técnica del repo)
├── README.md                          ← referencia de usuario completa
├── QUICKSTART.md                      ← instalación en 60 segundos
├── CONTRIBUTING.md                    ← cómo contribuir
├── jurisdiccion-UY-AR.md              ← tabla de diferencias UY/AR por área
│
├── civil-comercial/                   ← plugin: contratos comerciales
├── corporativo/                       ← plugin: M&A y gobierno societario
├── laboral/                           ← plugin: derecho del trabajo
├── privacidad/                        ← plugin: datos personales y DPA
├── regulatorio/                       ← plugin: cambios normativos
├── propiedad-intelectual/             ← plugin: marcas, patentes, PI
├── litigio/                           ← plugin: litigio civil y cartera
├── administrativo/                    ← plugin: derecho público
├── gobernanza-ia/                     ← plugin: IA Act y regulación IA
├── clinica-juridica/                  ← plugin: setup de clínica
├── estudiante-derecho/                ← plugin: formación jurídica
├── hub-constructor/                   ← plugin: instalador de skills comunidad
│
├── managed-agent-cookbooks/           ← agentes programados (headless)
│   ├── vencimiento-contratos/
│   ├── seguimiento-expedientes/
│   ├── monitor-normas/
│   ├── diligencia-grilla/
│   └── radar-lanzamiento/
│
└── scripts/
    ├── deploy-managed-agent.sh        ← deploy de managed agents
    ├── validate.py                    ← validación de estructura
    └── orchestrate.py                 ← orquestación de agentes
```

---

## Arquitectura de un plugin

Cada directorio de plugin tiene estructura fija:

```
<plugin>/
  .claude-plugin/
    plugin.json          ← manifiesto del plugin
  CLAUDE.md              ← perfil de práctica (completado por cold-start-interview)
  skills/
    <nombre-skill>/
      SKILL.md           ← definición de la skill
  agents/                ← agentes programados (si aplica)
  hooks/                 ← hooks pre/post herramienta (si aplica)
```

### plugin.json

Manifiesto que declara el plugin y sus skills. Campos obligatorios:

```json
{
  "name": "nombre-plugin",
  "display_name": "Nombre Legible",
  "description": "Descripción en ≤ 1024 caracteres",
  "version": "1.0.0",
  "license": "Apache-2.0",
  "skills": [
    {
      "name": "nombre-skill",
      "description": "Qué hace esta skill (≤ 1024 caracteres)",
      "user-invocable": true
    }
  ]
}
```

- `user-invocable: true` → la skill aparece como comando slash `/<plugin>:<skill>`
- `user-invocable: false` → la skill se activa automáticamente cuando el contexto es relevante

### CLAUDE.md de cada plugin

Es el **perfil de práctica** del plugin: jurisdicción, umbrales de riesgo, playbook de cláusulas, reglas de escalamiento y estilo de outputs. Lo genera `/<plugin>:cold-start-interview` y cada skill lo lee en el Paso 0 antes de actuar.

Si el CLAUDE.md de un plugin está vacío o sin configurar, las skills advierten al usuario que ejecute la entrevista de cold-start y continúan con defaults del plugin.

---

## Estructura de una SKILL.md

Cada skill es un archivo markdown con frontmatter YAML:

```markdown
---
name: nombre-skill
description: >
  Descripción de la skill (≤ 1024 caracteres). Debe explicar
  qué produce, qué input toma y cuándo es relevante.
argument-hint: "[indicación de input para el usuario]"
user-invocable: true
---

# Skill: Nombre de la Skill

## Propósito
[Una o dos oraciones sobre qué hace y qué no hace.]

## Paso 0 — Lectura del perfil de práctica
[Siempre el primer paso: leer CLAUDE.md del plugin.]

## Paso 1 — Recolección de datos
## Paso 2 — Análisis
## Paso N — Output estructurado
## Paso final — Compuerta de aprobación profesional

## Guardrails
[Lista de restricciones: qué nunca afirmar, cuándo escalar,
qué disclaimers incluir siempre.]
```

**Convenciones de skills:**

- El Paso 0 siempre lee el `CLAUDE.md` del plugin para incorporar el perfil de práctica.
- El output final siempre incluye una compuerta de revisión profesional (checklist para que el abogado confirme antes de entregar al cliente).
- Los guardrails incluyen siempre: no afirmar validez absoluta, citar norma antes que doctrina, aclarar que es análisis preliminar.
- Clasificación de riesgo estándar: **ALTO / MEDIO / BAJO** según el perfil del estudio.
- Las citas normativas van en formato `art. [N] [CÓDIGO]` — ejemplo: `art. 1078 CCyCN`, `art. 245 LCT`, `art. 1 LSC`.

---

## Estructura de un managed agent cookbook

Los agentes programados viven en `managed-agent-cookbooks/<slug>/agent.yaml`:

```yaml
---
name: nombre-agente
display_name: "Nombre legible del agente"
description: >
  Qué hace el agente.
schedule: "0 8 * * 1"   # cron expression
timezone: "America/Montevideo"
# campos de configuración específicos del agente
---

# System Prompt — [Nombre del agente]

[Prompt completo del agente: objetivo, workflow paso a paso,
formato de output, protocolo de notificaciones, guardrails.]
```

Cada cookbook es autónomo: contiene todo lo necesario para deployar el agente. Se deploya con:

```bash
scripts/deploy-managed-agent.sh <slug>
```

---

## Jurisdicción y referencias normativas

El archivo `jurisdiccion-UY-AR.md` es la referencia rápida de divergencias entre Uruguay y Argentina por área. Toda skill consciente de jurisdicción lo usa como fuente de verdad secundaria (la primaria es el CLAUDE.md del plugin configurado por el estudio).

Las jurisdicciones son siempre **UY** (Uruguay) y **AR** (Argentina). No se incluyen otras jurisdicciones latinoamericanas — el scope del proyecto es explícitamente el Río de la Plata.

---

## Convenciones de desarrollo

### Idioma y estilo

- Todo el contenido (skills, prompts, docs) en **español rioplatense formal**.
- Citas normativas: código antes que doctrina — `art. 1291 CC`, `art. 19.550 LGS`, `art. 18.331 LPDP`.
- Fechas: `día/mes/año` (ej. `14/05/2026`).
- Sin gerundio al inicio de oración.

### Agregar una nueva skill

1. Crear directorio: `<plugin>/skills/<nombre-skill>/SKILL.md`
2. Incluir frontmatter con `name`, `description` (≤ 1024 caracteres), `argument-hint`, `user-invocable`.
3. Declarar la skill en `<plugin>/.claude-plugin/plugin.json` bajo el array `"skills"`.
4. Estructura mínima: Paso 0 (lectura de CLAUDE.md) → pasos de análisis → output estructurado → compuerta de aprobación → guardrails.
5. Validar: `python scripts/validate.py <plugin>`.

### Agregar un nuevo plugin

1. Crear directorio `<plugin>/` con la estructura estándar.
2. Crear `.claude-plugin/plugin.json` con el manifiesto.
3. Crear `CLAUDE.md` con las secciones del perfil de práctica (vacías — se completan con cold-start-interview).
4. Crear al menos una skill: `skills/cold-start-interview/SKILL.md`.
5. No hay build step — todo es markdown y JSON.

### Guardrails globales (aplican a todas las skills)

- Ninguna skill puede afirmar que un contrato "es válido", que una posición "va a ganar" o que un trámite "está en regla" en forma absoluta.
- Todo output es un **borrador para revisión por abogado matriculado**.
- Las skills deben declarar siempre la jurisdicción analizada (UY / AR / ambas).
- Las citas de fuentes no verificadas contra un conector MCP se marcan `[verificar]`.
- Antes de cualquier output que pueda usarse frente a un tercero, mostrar la compuerta de aprobación profesional.

---

## Plugins instalados y sus comandos

| Plugin | Comando cold-start | Skills principales |
|---|---|---|
| `civil-comercial` | `/civil-comercial:cold-start-interview` | `revision-contratos`, `revision-nda`, `historial-cesiones`, `escala-escalamiento` |
| `corporativo` | `/corporativo:cold-start-interview` | `revision-tabular`, `extraccion-issues`, `consentimiento-directorio`, `cumplimiento-sociedades` |
| `laboral` | `/laboral:cold-start-interview` | `revision-despido`, `revision-contratacion`, `clasificacion-trabajador`, `investigacion-interna`, `politica-laboral`, `qa-laboral` |
| `privacidad` | `/privacidad:cold-start-interview` | `respuesta-arco`, `revision-dpa`, `generacion-eia` |
| `regulatorio` | `/regulatorio:cold-start-interview` | `revision-lanzamiento`, `diff-politica` |
| `propiedad-intelectual` | `/propiedad-intelectual:cold-start-interview` | `busqueda-marca`, `cese-desistimiento` |
| `litigio` | `/litigio:cold-start-interview` | `cronologia`, `carta-documento`, `demanda-recibida` |
| `administrativo` | `/administrativo:cold-start-interview` | `recurso-administrativo` |
| `gobernanza-ia` | `/gobernanza-ia:cold-start-interview` | `triaje-uso-ia`, `evaluacion-impacto-ia`, `revision-proveedor-ia` |
| `clinica-juridica` | `/clinica-juridica:cold-start-interview` | `ingreso-cliente`, `memo-caso` |
| `estudiante-derecho` | `/estudiante-derecho:cold-start-interview` | `drill-socratico`, `resumen-fallo` |
| `hub-constructor` | — | `instalador-skill` |

---

## Managed agents deployados

| Slug | Schedule | Qué hace |
|---|---|---|
| `vencimiento-contratos` | Lunes 8 AM (Montevideo) | Escanea el CLM, clasifica vencimientos por horizonte y notifica en Slack |
| `seguimiento-expedientes` | Diario | Monitorea expedientes en Poder Judicial UY y PJN AR |
| `monitor-normas` | Diario | Monitorea BCU, BCRA, AFIP/ARCA, CNV, URSEA para cambios normativos |
| `diligencia-grilla` | On demand | Revisión tabular de data room para due diligence M&A |
| `radar-lanzamiento` | On demand | Revisión de lanzamiento de producto contra calibración regulatoria |

---

## Disclaimer obligatorio

Todo output de este sistema es un **borrador para revisión por abogado matriculado**. No es asesoramiento legal, no es una conclusión jurídica, no reemplaza a un profesional. Estos plugins no representan posiciones jurídicas de Anthropic.
