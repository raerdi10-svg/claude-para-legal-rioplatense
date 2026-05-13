# Inicio Rápido — Claude para Legal Rioplatense

Instalación en 60 segundos.

## Opción A — Claude Cowork

1. Instalá [Claude Desktop](https://claude.com/download).
2. Accedé a Claude Cowork.
3. **Cowork → Personalizar → Explorar plugins** → buscá `claude-para-legal-rioplatense`.
4. Instalá los plugins que coincidan con tu práctica.
5. Ejecutá `/<plugin>:cold-start-interview` en cualquier conversación.

Eso es todo. Las skills se activan solas; los comandos slash están disponibles via `/`.

---

## Opción B — Claude Code (línea de comandos)

### Requisitos

- Claude Code instalado (`npm install -g @anthropic-ai/claude-code`)
- `ANTHROPIC_API_KEY` seteada

### Pasos

```bash
# 1. Cloná el repo
git clone https://github.com/TU_ORG/claude-para-legal-rioplatense
cd claude-para-legal-rioplatense

# 2. Registrá el marketplace
/plugin marketplace add .

# 3. Instalá los plugins que necesitás
/plugin install civil-comercial@claude-para-legal-rioplatense
/plugin install laboral@claude-para-legal-rioplatense
/plugin install litigio@claude-para-legal-rioplatense

# 4. Reiniciá Claude Code

# 5. Ejecutá la entrevista de cold-start para cada plugin
/civil-comercial:cold-start-interview
/laboral:cold-start-interview
/litigio:cold-start-interview
```

### Primera vez — recomendación rápida

| Si tu práctica es... | Instalá primero... |
|---|---|
| Estudio comercial / in-house | `civil-comercial`, `corporativo` |
| Estudio laboral | `laboral` |
| Litigio civil | `litigio` |
| Privacidad / datos | `privacidad` |
| Regulatorio / financiero | `regulatorio` |
| Propiedad intelectual | `propiedad-intelectual` |
| Derecho público / administrativo | `administrativo` |
| Estudiante | `estudiante-derecho` |
| Clínica jurídica | `clinica-juridica` |

---

## Opción C — Managed Agents API (headless)

```bash
export ANTHROPIC_API_KEY=sk-ant-...

# Deployá los agentes programados que necesitás
bash scripts/deploy-managed-agent.sh monitor-normas
bash scripts/deploy-managed-agent.sh vencimiento-contratos
bash scripts/deploy-managed-agent.sh seguimiento-expedientes
```

Ver los cookbooks en [`managed-agent-cookbooks/`](./managed-agent-cookbooks) para configuración completa.

---

## Primeros pasos después de instalar

### 1. Ejecutá la entrevista de cold-start

```
/civil-comercial:cold-start-interview
```

Pregunta sobre tu práctica, jurisdicción principal (Uruguay, Argentina o ambas), umbral de riesgo, y documentos semilla. Escribe el perfil en `~/.claude/plugins/config/claude-para-legal-rioplatense/<plugin>/CLAUDE.md`.

### 2. Conectá una herramienta de investigación

Sin una, las citas del modelo van marcadas `[verificar]`. Con una (La Ley Online, Microjuris, DataLegal, etc.) las citas se verifican contra fuentes autoritativas.

### 3. Ejecutá tu primer workflow

```
/civil-comercial:revision-contratos
```

Subí el contrato cuando te lo pida. La skill identifica jurisdicción, aplica tu playbook y produce el memo.

---

## Estructura del perfil de práctica

El cold-start escribe tu `CLAUDE.md`. Podés editarlo directamente:

```markdown
# Perfil de Práctica — Civil y Comercial

## Jurisdicción principal
Uruguay (CGP, CC, LSC) — también cubro operaciones Argentina (CCyCN, LGS)

## Umbrales de riesgo
ALTO: cláusulas de responsabilidad ilimitada, arbitraje en jurisdicción extranjera, renuncia a fuero
MEDIO: plazos de prescripción modificados, garantías amplias, cláusulas penales > 20%
BAJO: modificaciones menores de forma, ajustes de protocolo de notificación

## Estilo casa
- Memos en español rioplatense formal
- Sin gerundio en inicio de oración
- Citas al Código General del Proceso art. X antes que a doctrina
- Formato de fecha: día/mes/año

## Escalamiento
Contrato > USD 500.000 → socio Fulana de Tal
Arbitraje internacional → área de litigio y socio de IP
```

---

## Soporte

- Issues: [github.com/TU_ORG/claude-para-legal-rioplatense/issues](https://github.com/TU_ORG/claude-para-legal-rioplatense/issues)
- Discusiones: [github.com/TU_ORG/claude-para-legal-rioplatense/discussions](https://github.com/TU_ORG/claude-para-legal-rioplatense/discussions)
