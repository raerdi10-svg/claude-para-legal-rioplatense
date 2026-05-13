# Cómo Contribuir

Todo acá es markdown y JSON. Fork, editar, PR.

## Skills nuevas

Agregá la skill bajo `<plugin>/skills/<nombre-skill>/SKILL.md` con el frontmatter que usan las existentes:

```yaml
---
name: nombre-skill
description: >
  Descripción de la skill — qué hace, cuándo se activa. Máximo 1024 caracteres.
  Este es el trigger signal: cuanto más preciso, mejor activa.
argument-hint: "[argumentos opcionales]"
user-invocable: true
---
```

La skill queda disponible como `/<plugin>:<nombre-skill>`.

Para skills solo invocadas por otras skills (no por el usuario), usar `user-invocable: false`.

## Agentes nuevos

Agregá `<plugin>/agents/<nombre>.md` con frontmatter de scheduling:

```yaml
---
name: nombre-agente
schedule: "0 8 * * 1"  # cron UTC
timezone: "America/Montevideo"
description: "Qué hace este agente"
---
```

Si querés deployment headless: agregá también `managed-agent-cookbooks/<nombre>/agent.yaml`.

## Skills de la comunidad

Usá `/hub-constructor:instalador-skill` para probar una skill de la comunidad en tu entorno.
El hub ejecuta `/hub-constructor:qa-skill` contra cada skill antes de instalar.

## Criterios de calidad para skills legales

Antes de hacer PR, verificar:

- [ ] La skill **declara** su jurisdicción (UY / AR / MIXTA / AMBAS)
- [ ] La skill **lee el perfil de práctica** (`CLAUDE.md`) antes de producir output
- [ ] La skill incluye **compuerta de revisión** obligatoria en el output
- [ ] La skill **nunca afirma** que el output es asesoramiento jurídico definitivo
- [ ] La skill **cita normativa** con número de artículo y ley, no solo referencias genéricas
- [ ] La skill **maneja el caso de falta de información**: pide los datos que necesita antes de proceder
- [ ] La skill **no inventa citas** — si no hay conector de investigación, marca `[verificar]`
- [ ] La descripción tiene **menos de 1024 caracteres**
- [ ] El output tiene **formato consistente** con las demás skills del plugin

## Actualización de referencias normativas

Las tablas en `references/jurisdiccion-UY-AR.md` deben actualizarse cuando cambie:
- Montos de prescripción
- Organismos regulatorios
- Caps de indemnización (actualizar referencia a RIPTE / SMVM)
- Plazos procesales

Marcar la actualización con fecha en el PR.

## Conectores

¿Construís un conector para un sistema legal local (Poder Judicial UY, PJN, La Ley, etc.)?
Seguí el estándar MCP y abrí un issue con el tag `conector` antes de hacer PR.

## Código de conducta

Este proyecto adopta el Contributor Covenant v2.1.

## Licencia

Al contribuir, aceptás que tu contribución se licencia bajo Apache 2.0, igual que el resto del repo.
