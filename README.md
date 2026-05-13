# Claude para Legal Rioplatense

Agentes de referencia, skills y conectores de datos para los flujos de trabajo jurídicos más frecuentes en **Uruguay y Argentina** — derecho civil y comercial, laboral, corporativo, litigio, regulatorio, privacidad, propiedad intelectual, administrativo, gobernanza de IA, y el lado formativo de la práctica (clínicas jurídicas y estudiantes de derecho).

> **¿Empezás acá?** Comenzá por [QUICKSTART.md](./QUICKSTART.md) — instalación en 60 segundos. Este README es la referencia completa.

Todo está disponible **de dos formas desde una sola fuente**: instalalo como plugin de [Claude Cowork](https://claude.com/product/cowork) o [Claude Code](https://claude.com/product/claude-code), o deployalo vía la [API de Claude Managed Agents](https://docs.claude.com/en/api/managed-agents) detrás de tu propio motor de workflow. Mismo system prompt, mismas skills — vos elegís dónde corre.

---

> **IMPORTANTE — No es asesoramiento jurídico.**
> Todo output de estos plugins es un **borrador para revisión por abogado matriculado** — no es asesoramiento legal, no es una conclusión jurídica, no reemplaza a un profesional. Están construidos con salvaguardas que lo reflejan: atribución de fuente en cada cita, defaults conservadores en privilegio y decisiones subjetivas, jurisdicción siempre declarada (Uruguay / Argentina / ambas), y compuertas explícitas antes de que cualquier escrito se presente, se envíe o se use como fundamento. El abogado revisa, verifica y asume responsabilidad profesional por todo lo que sale del estudio. Estos plugins hacen esa revisión más rápida; no la reemplazan.
>
> **Estos plugins no representan posiciones jurídicas de Anthropic.** Son herramientas que ayudan a los abogados a analizar situaciones. El profesional que usa el plugin — no el plugin, ni Anthropic — es responsable de las posiciones jurídicas adoptadas en el trabajo.

---

## Base legal cubierta

### Uruguay
- Código Civil (CC)
- Código General del Proceso (CGP — Ley 15.982)
- Código del Proceso Penal (CPP — Ley 19.293)
- Código Penal (CP)
- Ley de Sociedades Comerciales (LSC — Ley 16.060)
- Ley de Relaciones Laborales (Ley 18.566) y normativa MTSS
- Ley de Protección de Datos Personales (LPDP — Ley 18.331) y Decreto 414/009
- Ley de Defensa de la Competencia (Ley 18.159)
- Marco regulatorio BCU (SIIF, SAFI, intermediación financiera)
- Marco regulatorio URSEA, URSEC, URSEC, TCA (Tribunal de lo Contencioso Administrativo)
- Ley de Acceso a la Información Pública (Ley 18.381)
- Ley de Propiedad Industrial (Ley 17.011) y Ley de Derecho de Autor (Ley 9.739)
- Normativa MGAP, MSP, MIEM, MEF, MEVIR, MIDES

### Argentina
- Código Civil y Comercial de la Nación (CCyCN — Ley 26.994, vigente 2015)
- Código Procesal Civil y Comercial de la Nación (CPCCN)
- Código Penal de la Nación (CPN)
- Ley General de Sociedades (LGS — Ley 19.550 y mod.)
- Ley de Contrato de Trabajo (LCT — Ley 20.744 y mod.)
- Ley de Protección de Datos Personales (PDPA — Ley 25.326) y normativa AAIP
- Ley de Defensa de la Competencia (LDC — Ley 27.442) y CNDC
- Marco regulatorio BCRA (Com. A, Circulares CAMEX)
- Marco regulatorio CNV, AFIP/ARCA, CONICET, ANMAT, ENTE
- Ley de Marca (Ley 22.362) y Ley de Propiedad Intelectual (Ley 11.723)
- Ley de Procedimientos Administrativos (LPA — Ley 19.549)
- Códigos procesales provinciales: CABA (CPCCBA), Buenos Aires, Córdoba, Santa Fe, Mendoza

---

## Agentes

Cada agente tiene nombre por el flujo que ejecuta. Son la superficie más usada — empezá por los que coincidan con tu práctica y después ajustá la skill subyacente, el perfil de práctica y los conectores a cómo trabaja tu equipo.

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de Contratos Comerciales** | Revisa un contrato contra tu playbook y produce un memo con observaciones y cláusulas sugeridas | `civil-comercial` | `/civil-comercial:revision-contratos` |
| **Clasificador NDA** | VERDE/AMARILLO/ROJO de NDAs entrantes | `civil-comercial` | `/civil-comercial:revision-nda` |
| **Trazador de Cesiones** | Traza cómo cambió un contrato a lo largo de sus adendas y cesiones | `civil-comercial` | `/civil-comercial:historial-cesiones` |
| **Vigía de Vencimientos** | Escanea el registro contractual para fechas de renovación y rescisión | `civil-comercial` | agente programado |
| **Router de Escalamiento** | Deriva issues contractuales al aprobador correcto y redacta la consulta | `civil-comercial` | `/civil-comercial:escala-escalamiento` |
| **Revisión Tabular de Diligencia** | Revisión tabular sobre un data room — una fila por documento, cada celda citada | `corporativo` | `/corporativo:revision-tabular` |
| **Extractor de Issues** | Lee documentos de VDR y extrae issues por categorías de umbral | `corporativo` | `/corporativo:extraccion-issues` |
| **Redactor de Actas de Directorio** | Redacta actas de directorio en formato casa con búsqueda de precedentes | `corporativo` | `/corporativo:consentimiento-directorio` |
| **Tracker de Cumplimiento Societario** | Plazos de presentación entre jurisdicciones y tipos societarios | `corporativo` | `/corporativo:cumplimiento-sociedades` |
| **Revisor de Despidos** | Ejecuta una propuesta de despido contra las banderas de riesgo jurisdiccional (LCT / CGP) | `laboral` | `/laboral:revision-despido` |
| **Revisor de Contratación** | Revisa cartas oferta y cláusulas restrictivas con control de jurisdicción | `laboral` | `/laboral:revision-contratacion` |
| **Clasificador de Trabajadores** | Testea un engagement propuesto contra la normativa aplicable (MTSS / AFIP) | `laboral` | `/laboral:clasificacion-trabajador` |
| **Conductor de Investigación Interna** | Abre, rastrea, agrega y resume asuntos de investigación interna | `laboral` | `/laboral:investigacion-interna` |
| **Redactor de Políticas Laborales** | Redacta políticas de empleo con suplementos jurisdiccionales | `laboral` | `/laboral:politica-laboral` |
| **Q&A Laboral** | Q&A laboral consciente de jurisdicción para el canal de "consulta rápida" | `laboral` | `/laboral:qa-laboral` |
| **Respondedor ARCO** | Redacta acuses y respuestas sustantivas a solicitudes ARCO/HABEAS DATA | `privacidad` | `/privacidad:respuesta-arco` |
| **Revisor DPA** | Revisa un DPA contra tu playbook como responsable o encargado | `privacidad` | `/privacidad:revision-dpa` |
| **Generador EIA** | Genera una Evaluación de Impacto en la Privacidad en formato casa | `privacidad` | `/privacidad:generacion-eia` |
| **Revisor de Lanzamiento** | Revisa un lanzamiento de producto contra tu calibración de riesgo | `regulatorio` | `/regulatorio:revision-lanzamiento` |
| **Monitor de Normas** | Monitorea el DOF/BO/BCU/BCRA/AFIP para cambios normativos | `regulatorio` | agente programado |
| **Rastreador de Diferencias Políticas** | Diffa un cambio regulatorio contra la biblioteca de políticas indexada | `regulatorio` | `/regulatorio:diff-politica` |
| **Buscador de Marca** | Primera pasada de clearing con control de knockout y heurísticas de confusión (DNPI/INPI) | `propiedad-intelectual` | `/propiedad-intelectual:busqueda-marca` |
| **Redactor de Carta de Cese** | Redacta o clasifica una carta documento / cese y desistimiento | `propiedad-intelectual` | `/propiedad-intelectual:cese-desistimiento` |
| **Gráfica de Reclamación** | Cuadro elemento a elemento, patente o causa civil | `litigio` | `/litigio:cronologia` |
| **Vigía de Expedientes** | Monitorea expedientes judiciales para presentaciones y plazos | `litigio` | agente programado |
| **Redactor de Carta Documento** | Redacta carta documento o intimación previa | `litigio` | `/litigio:carta-documento` |
| **Triaje de Demanda Recibida** | Analiza demanda entrante — opciones, cross-check cartera, traspaso | `litigio` | `/litigio:demanda-recibida` |
| **Triaje de Uso de IA** | Clasifica usos propuestos de IA contra el registro | `gobernanza-ia` | `/gobernanza-ia:triaje-uso-ia` |
| **Evaluador de Impacto IA** | Ejecuta una EIA-IA a través de los regímenes en scope | `gobernanza-ia` | `/gobernanza-ia:evaluacion-impacto-ia` |
| **Revisor de IA de Proveedor** | Revisa términos de IA de proveedor | `gobernanza-ia` | `/gobernanza-ia:revision-proveedor-ia` |
| **Ingreso de Clínica** | Ingreso estructurado de cliente con identificación de issues y conflictos | `clinica-juridica` | `/clinica-juridica:ingreso-cliente` |
| **Armazón de Memo de Caso** | Memo de análisis de caso armado en IRAC con brechas marcadas | `clinica-juridica` | `/clinica-juridica:memo-caso` |
| **Coach de Prep para Concurso** | Práctica de escritos y oral orientada a materias débiles | `estudiante-derecho` | `/estudiante-derecho:drill-socratico` |
| **Resumidor de Fallos** | Resume un fallo en el formato preferido del estudiante | `estudiante-derecho` | `/estudiante-derecho:resumen-fallo` |

---

## Estructura del Repositorio

```
civil-comercial/          # contratos comerciales — revisión, NDAs, SaaS, renovaciones, escalamiento
corporativo/              # M&A, diligencia, cronograma de clausura, actas, cumplimiento societario
laboral/                  # contratación/despido, clasificación laboral, investigaciones, políticas
privacidad/               # DPA, ARCO, EIA, triaje de privacidad, monitor de políticas
regulatorio/              # monitor de normas, diff de política, brechas, consultas públicas
gobernanza-ia/            # triaje de casos IA, EIA-IA, revisión de proveedor IA, brechas
propiedad-intelectual/    # clearing de marca, FTO, cese-desistimiento, cláusulas IP, portfolio
litigio/                  # cartera, expedientes, holds, cartas documento, depo prep, cronologías
administrativo/           # actos admin, recursos, acción de nulidad, amparo, habeas corpus, licitaciones
clinica-juridica/         # setup de clínica, rampa del estudiante, ingreso, plazos, memos, handoffs
estudiante-derecho/       # drill socrático, resumen de fallos, esquemas, práctica IRAC, estudio
hub-constructor/          # descubrimiento e instalación de skills de la comunidad con trust gate
managed-agent-cookbooks/  # cookbooks de Managed Agents — un dir por agente programado
  diligencia-grilla/
  seguimiento-expedientes/
  radar-lanzamiento/
  monitor-normas/
  vencimiento-contratos/
scripts/                  # deploy-managed-agent.sh · validate.py · orchestrate.py
.claude-plugin/
  marketplace.json
references/               # legislación de referencia, tablas de jurisdicción, guías de estilo
```

Cada directorio de plugin tiene la misma forma:

```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # perfil de práctica — completado por /<plugin>:cold-start-interview
  README.md
  skills/                 # skills — cada una es un comando slash /<plugin>:<skill>
  agents/                 # agentes programados (si aplica)
  hooks/                  # hooks pre y post herramienta (si aplica)
```

---

## Cómo Empezar

### Claude Cowork

En Cowork:
1. Abrí la pestaña **Cowork**.
2. Hacé clic en **Personalizar** en el panel izquierdo.
3. Hacé clic en **Explorar plugins** e instalá los que quieras, **o** subí un archivo de plugin personalizado (cualquier directorio de plugin comprimido en zip).

Tras la instalación, las skills se activan automáticamente cuando son relevantes, los comandos slash están disponibles via `/`, y los agentes programados corren en la cadencia definida en su frontmatter.

### Claude Code

```bash
# Agregá el marketplace (usá la ruta absoluta a este repo o una URL de GitHub)
/plugin marketplace add <ruta-a-este-repo>

# Instalá un plugin — elegí los que coincidan con tu práctica
/plugin install civil-comercial@claude-para-legal-rioplatense
/plugin install laboral@claude-para-legal-rioplatense
/plugin install litigio@claude-para-legal-rioplatense

# Reiniciá Claude Code y ejecutá el setup de cada plugin instalado
/civil-comercial:cold-start-interview
/laboral:cold-start-interview
/litigio:cold-start-interview
```

**Ejecutá la entrevista de cold-start primero.** Cada otra skill de un plugin lee desde el perfil de práctica que esta entrevista escribe. Saltear el setup es la razón más común por la que una skill produce output genérico. La entrevista toma 10–20 minutos por plugin.

### Claude Managed Agents

```bash
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh monitor-normas
scripts/deploy-managed-agent.sh vencimiento-contratos
scripts/deploy-managed-agent.sh seguimiento-expedientes
scripts/deploy-managed-agent.sh diligencia-grilla
scripts/deploy-managed-agent.sh radar-lanzamiento
```

---

## Plugins Verticales

### Transaccional y asesoría

| Plugin | Qué agrega |
|---|---|
| **[civil-comercial](./civil-comercial)** | Revisión de contratos consciente de playbook (UR/AR). NDAs, SaaS, servicios profesionales. Trazado de adendas y cesiones. Registro de renovaciones con alertas. Routing de escalamiento. Resúmenes para contraparte o negocio. |
| **[corporativo](./corporativo)** | Diligencia M&A con revisión tabular y cita por celda. Cronogramas de cierre, actas de directorio, consentimientos. Tracker de cumplimiento societario (S.A., S.R.L., S.A.S., S.A.P.I.). Integración post-cierre. |
| **[privacidad](./privacidad)** | Triaje de privacidad (EIA vs PIA vs DPIA vs proceder), generación de EIA, revisión de DPA como responsable o encargado, respuesta ARCO/HABEAS DATA con plazos legales UR/AR. Monitor de políticas. |
| **[regulatorio](./regulatorio)** | Monitor de cambios normativos (BCU, BCRA, AFIP/ARCA, CNV, URSEA, URSEC, ANMAT). Diff de políticas. Tracker de brechas. Consultas públicas. Digest semanal. |
| **[laboral](./laboral)** | Revisión de contratación y despido con flags jurisdiccionales (LCT / MTSS). Clasificación laboral. Investigaciones internas. Redacción de políticas con suplementos por jurisdicción. Q&A laboral. |
| **[gobernanza-ia](./gobernanza-ia)** | Triaje de casos de uso IA contra tu registro. Evaluaciones de impacto. Revisión de IA de proveedor. Análisis de brechas regulatorio-a-política. |
| **[propiedad-intelectual](./propiedad-intelectual)** | Clearing de marca (DNPI / INPI), FTO, redacción y triaje de cartas documento, revisión de cláusulas IP, cumplimiento OSS, portfolio. |
| **[administrativo](./administrativo)** | Triaje de actos administrativos, recursos en vía administrativa, acción de nulidad ante TCA (UY) / Cámara Contencioso-Administrativa (AR), amparo, habeas corpus, licitaciones. |

### Litigio

| Plugin | Qué agrega |
|---|---|
| **[litigio](./litigio)** | Trabaja dos superficies. **Cartera / in-house:** ingreso de expediente, estado de cartera, holds judiciales, cartas documento, estado de estudio externo. **Estudio / solo:** cronologías, cartas de elemento-a-elemento (patente y civil), prep de testigo, revisión de prueba, redacción de escrito. |

### Formación y práctica

| Plugin | Qué agrega |
|---|---|
| **[estudiante-derecho](./estudiante-derecho)** | Drill socrático, resumen de fallos, construcción de esquemas, práctica IRAC, prep de oral, flashcards, prep para concurso de oposición, estudio. **Modo aprendizaje, no modo respuesta** — nunca te da la respuesta. |
| **[clinica-juridica](./clinica-juridica)** | Setup del profesor y rampa semestral del estudiante. Guía por área de práctica con postura pedagógica (asistir / guiar / enseñar). Ingreso estructurado con identificación de issues. Seguimiento de plazos. Memos, cartas de cliente (rutina + lenguaje llano), handoffs de fin de semestre. |

### Ecosistema

| Plugin | Qué agrega |
|---|---|
| **[hub-constructor](./hub-constructor)** | Descubrimiento e instalación de skills de la comunidad con trust gate real — registros vigilados, framework de QA, actualizaciones con hash fijado, y comprobación de confianza obligatoria antes de que nada aterrice en tu entorno. |

---

## Cómo Encaja Todo

| | Qué es | Dónde vive |
|---|---|---|
| **Plugins** | Bundles de área de práctica autocontenidos — skills, agentes, hooks y perfil de práctica. Instalás los que necesitás. | `<plugin>/` |
| **Skills** | Expertise de dominio, convenciones y métodos paso a paso que Claude usa automáticamente cuando son relevantes — y acciones slash que disparás explícitamente. | `<plugin>/skills/<skill>/SKILL.md` |
| **Agentes** | Flujos programados o event-driven (vigía de vencimientos, seguimiento de expedientes, monitor de cambios normativos). Corre en background. | `<plugin>/agents/` |
| **Perfil de práctica** | `CLAUDE.md` en lenguaje llano describiendo tu playbook, reglas de escalamiento y estilo casa. Cada skill lo lee. | `~/.claude/plugins/config/claude-para-legal-rioplatense/<plugin>/CLAUDE.md` |
| **Conectores** | Servidores MCP que conectan Claude a tus datos — CLM, DMS, plataformas de investigación, productividad. | `.mcp.json` (por plugin) |
| **Cookbooks de Managed Agent** | `agent.yaml` + subagentes depth-1 + ejemplos de steering para despliegue headless. | `managed-agent-cookbooks/<slug>/` |

---

## Conectores MCP

> **Conectá una herramienta de investigación primero.** Todo es mejor con una, y las citas no están verificadas sin una. Las citas que vienen de un conector de investigación están etiquetadas con la fuente. Las citas solo del conocimiento del modelo están marcadas `[verificar]`.

| Conector | Qué le da a Claude | Plugins | Notas |
|---|---|---|---|
| **Slack** | Leer canales, buscar, enviar mensajes | todos | Tu workspace |
| **Google Drive** | Leer docs, sheets, slides; fetch por enlace | todos | Tu cuenta |
| **Poder Judicial UY** | Consulta de expedientes públicos en línea | `litigio`, `clinica-juridica` | Público |
| **PJN Argentina** | Consulta de expedientes (MEV, SEER) | `litigio` | Público; requiere CUIT |
| **BCU (Uruguay)** | Normativa COPOM, circulares, resoluciones | `regulatorio`, `civil-comercial` | Público |
| **BCRA (Argentina)** | Comunicaciones "A", circulares CAMEX | `regulatorio`, `civil-comercial` | Público |
| **DNPI Uruguay** | Base de marcas y patentes | `propiedad-intelectual` | Público |
| **INPI Argentina** | Base de marcas, patentes, modelos | `propiedad-intelectual` | Público |
| **AFIP/ARCA** | Consulta de situación fiscal, RUT, padrón | `corporativo`, `laboral` | API pública |
| **BPS Uruguay** | Consulta de historia laboral, aportes | `laboral` | Con credenciales |
| **La Ley Online** | Jurisprudencia y doctrina AR/UY | `litigio`, `clinica-juridica`, `estudiante-derecho` | Suscripción cliente |
| **Thomson Reuters Checkpoint** | Base normativa integrada AR/UY | `regulatorio`, `laboral` | Suscripción cliente |
| **DataLegal UY** | Jurisprudencia uruguaya | `litigio`, `clinica-juridica` | Suscripción cliente |
| **Microjuris** | Jurisprudencia regional integrada | `litigio`, `estudiante-derecho` | Suscripción cliente |
| **UDELAR / UCES (repositorios)** | Tesis y doctrina académica | `estudiante-derecho`, `clinica-juridica` | Público |
| **Box** | Archivos y carpetas en VDRs y salas de asunto | `corporativo` | Tu tenant |
| **DocuSign** | Estado de envelopes, contratos ejecutados | `civil-comercial` | Suscripción cliente |
| **Linear** | Tracker de lanzamientos | `regulatorio` | Tu workspace |
| **Asana** | Tracker de proyectos | `regulatorio`, `corporativo` | Tu workspace |

> Conectores marcados "suscripción cliente" necesitan la cuenta y API key propias del cliente.
> **¿Construís un conector?** Ver [CONNECTORS.md](./CONNECTORS.md) para qué hace un buen servidor MCP legal y cómo enviarlo para inclusión.

---

## Tabla de Jurisdicción Rápida

Cada skill declara su jurisdicción por defecto y pregunta en el cold-start. Las skills son conscientes de que Uruguay y Argentina divergen en áreas clave:

| Área | Uruguay | Argentina |
|---|---|---|
| Proceso civil | CGP (Ley 15.982) | CPCCN + codes provinciales |
| Sociedades | LSC (Ley 16.060) | LGS (Ley 19.550) |
| Contrato de trabajo | Ley 18.566 + MTSS | LCT (Ley 20.744) |
| Protección de datos | LPDP (Ley 18.331) / Decreto 414 | PDPA (Ley 25.326) / AAIP |
| Defensa del consumidor | Ley 17.250 + UCU | LDC (Ley 24.240) + DNCI |
| Contencioso-administrativo | TCA (Ley 15.524) | Cámaras CAF / Ley 19.549 |
| Prescripción ordinaria | 20 años (CC art. 1216) | 5 años (CCyCN art. 2560) |
| Moneda de condena | Pesos UY / UI / USD | Pesos AR / UVA / USD (pacto) |

---

## Personalizarlo

Estas son plantillas de referencia. Mejoran cuando las ajustás a cómo trabaja tu equipo.

- **Ejecutá la entrevista de cold-start.** Es el mecanismo de personalización. Pregunta cómo funciona tu práctica, lee tus documentos semilla y escribe tu perfil de práctica.
- **Editá el perfil de práctica.** Tu perfil vive en `~/.claude/plugins/config/claude-para-legal-rioplatense/<plugin>/CLAUDE.md`. Editalo directamente para correcciones pequeñas.
- **Re-ejecutá el setup.** `/<plugin>:cold-start-interview` de nuevo para una re-entrevista completa cuando tu práctica cambia materialmente.
- **Swapeá conectores.** Apuntá `.mcp.json` a tu CLM, DMS, plataforma de investigación.
- **Traé tu playbook y plantillas.** Tirá tu terminología, estilo casa y plantillas de formato en el `CLAUDE.md` y `references/` del plugin.
- **Forkeá skills para estilo casa.** Cada skill es un archivo markdown bajo `skills/`. Editá los pasos, las compuertas, el formato de output.

Sin build step. Todo es markdown y JSON.

---

## Contribuir

Todo acá es markdown y JSON. Fork, editar, PR.

- **Nueva skill** → agregala bajo `<plugin>/skills/<nombre-skill>/SKILL.md` con el frontmatter que usan las skills existentes. Mantenés la descripción bajo 1024 caracteres.
- **Nuevo agente** → agregá `<plugin>/agents/<nombre>.md` con frontmatter de scheduling.
- **Skills de la comunidad** → usá `/hub-constructor:instalador-skill` para probar una skill de la comunidad en tu entorno.

---

## Licencia

Licenciado bajo la [Licencia Apache, Versión 2.0](./LICENSE).

Copyright 2026 Anthropic PBC.
