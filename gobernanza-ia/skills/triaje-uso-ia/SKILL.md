---
name: triaje-uso-ia
description: >
  Dado un uso propuesto de IA, clasifica el caso de uso, evalúa si cae en categorías de
  alto riesgo según las regulaciones aplicables, identifica derechos afectados (privacidad,
  no discriminación, explicabilidad) y emite una recomendación con semáforo: proceder /
  proceder con medidas / consultar regulador / no proceder.
argument-hint: "[descripción del uso de IA propuesto] [--sector=financiero|salud|rrhh|publico|otro]"
user-invocable: true
---

# Skill: Triaje de Uso de IA

## Propósito

Clasificar un uso propuesto de IA y emitir una recomendación regulatoria inicial basada en los regímenes aplicables al cliente. El triaje no reemplaza la evaluación de impacto completa (ver `/gobernanza-ia:evaluacion-impacto-ia`), pero permite determinar con rapidez si el uso es viable, requiere medidas adicionales, necesita consulta regulatoria previa, o directamente no debe proceder.

---

## Paso 0 — Recolección de datos

Formular las siguientes preguntas si no están contenidas en el argumento inicial:

1. **Descripción del uso de IA:** ¿Qué hace el sistema? ¿Qué input recibe y qué output produce?
2. **Sector de aplicación:** financiero / salud / recursos humanos / sector público / comercio / educación / otro
3. **Jurisdicción:** Argentina / Uruguay / con alcance UE / multinacional
4. **Tipo de personas afectadas:** empleados / clientes / usuarios del sistema / beneficiarios de prestaciones / menores
5. **Naturaleza de los datos utilizados:** ¿El sistema procesa datos personales? ¿Datos sensibles (salud, biometría, origen étnico, situación financiera, afiliación sindical)?
6. **Impacto de la decisión:** ¿El output del sistema tiene efectos vinculantes o genera consecuencias económicas, laborales o de acceso a servicios para el afectado?
7. **Supervisión humana:** ¿Existe revisión humana antes de que el output tenga efecto? ¿Es siempre obligatoria o solo ocasional?

---

## Paso 1 — Clasificación del caso de uso

Clasificar el uso en una de las siguientes categorías:

| Categoría | Descripción | Ejemplos |
|---|---|---|
| Decisión automatizada | El sistema toma o determina una decisión que afecta a una persona | Scoring crediticio, evaluación de riesgo de fuga laboral, aprobación de prestaciones |
| Generación de contenido | El sistema produce texto, imágenes, audio o video | Redacción de contratos, generación de informes, chatbots, deepfakes |
| Análisis predictivo | El sistema estima probabilidades o tendencias futuras | Modelos de churn, predicción de demanda, análisis de riesgo de cartera |
| Clasificación | El sistema categoriza personas, objetos o situaciones | Reconocimiento facial, detección de fraude, análisis de sentimiento |
| Automatización de procesos | El sistema ejecuta tareas repetitivas sin decisión sobre personas | RPA, extracción de datos de documentos, OCR con validación humana |
| Otro | Indicar descripción libre | — |

---

## Paso 2 — Evaluación de riesgo regulatorio

### 2.1 — Verificación de prohibiciones absolutas (AI Act UE, art. 5)

Si aplica el AI Act (cliente con presencia o usuarios en UE), verificar si el uso cae en alguna de estas categorías prohibidas:

- [ ] Sistemas de puntuación social (social scoring) por autoridades públicas
- [ ] Manipulación subliminal de conducta humana explotando vulnerabilidades
- [ ] Inferencia de emociones en entornos laborales o educativos (salvo excepciones médicas o de seguridad)
- [ ] Categorización biométrica que infiera características protegidas (raza, orientación sexual, creencias)
- [ ] Identificación biométrica en tiempo real en espacios públicos por fuerzas del orden (salvo excepciones tasadas)
- [ ] Predicción de conducta delictiva basada en perfilado sin base objetiva

**Si alguna casilla queda marcada:** emitir resultado ROJO inmediato — NO PROCEDER — y alertar al usuario que requiere análisis legal urgente con el referente de práctica antes de cualquier paso adicional.

### 2.2 — Verificación de alto riesgo (AI Act Anexo III)

Verificar si el uso corresponde a alguno de los dominios de alto riesgo:

- [ ] Infraestructuras críticas (energía, agua, transporte)
- [ ] Educación y formación profesional (acceso, evaluación)
- [ ] Empleo, gestión de trabajadores y acceso al empleo por cuenta propia
- [ ] Acceso a servicios privados esenciales y prestaciones públicas (crédito, seguros, salud, beneficios sociales)
- [ ] Aplicación de la ley (evaluación de riesgos sobre personas)
- [ ] Gestión de migración, asilo y control de fronteras
- [ ] Administración de justicia y procesos democráticos

**Si alguna casilla queda marcada:** clasificar como ALTO RIESGO bajo AI Act — aplicar Paso 3 completo.

### 2.3 — Verificación de obligaciones de transparencia (AI Act, art. 50)

- [ ] El sistema interactúa con personas humanas de forma que puedan creer que hablan con una persona
- [ ] El sistema genera contenido sintético (texto, audio, imagen, video) que podría confundirse con contenido humano

**Si alguna casilla queda marcada:** obligación de informar al usuario que interactúa con IA.

### 2.4 — Verificación bajo derecho local (AR/UY)

**Argentina — Ley 25.326, art. 20:**
- [ ] La decisión produce efectos jurídicos o afecta significativamente al titular de los datos
- [ ] La decisión se adopta exclusivamente mediante tratamiento automatizado de datos personales
- [ ] El titular puede oponerse (derecho de oposición) y exigir revisión humana

**Uruguay — Ley 18.331, art. 16:**
- [ ] El titular tiene derecho a no ser sometido a decisión con efectos significativos basada exclusiva­mente en tratamiento automatizado
- [ ] El responsable debe informar los criterios de valoración utilizados cuando el titular lo solicite

**Datos sensibles (AR: art. 2 y 7 Ley 25.326 / UY: art. 18 Ley 18.331):**
- [ ] El sistema procesa datos de salud, biométricos, origen racial o étnico, opiniones políticas, creencias religiosas, vida sexual o afiliación sindical
- Si es así: verificar base jurídica específica (consentimiento expreso o excepción legal) y medidas de seguridad reforzadas

**Sector financiero:**
- [ ] AR: cumplimiento con Com. BCRA A 7724 (gestión de riesgos tecnológicos) verificado
- [ ] UY: cumplimiento con normativa BCU sobre riesgos tecnológicos verificado

---

## Paso 3 — Identificación de derechos afectados

Para cada derecho, indicar si está afectado (Sí / No / Potencialmente):

| Derecho | Fundamento | Afectado |
|---|---|---|
| Privacidad y protección de datos personales | Ley 25.326 (AR); Ley 18.331 (UY); RGPD si aplica | |
| No discriminación | Art. 16 CN (AR); art. 8 Constitución UY; art. 21 Carta DFU | |
| Explicabilidad / derecho a información sobre decisión automatizada | Art. 20 Ley 25.326 (AR); art. 16 Ley 18.331 (UY); art. 86 AI Act | |
| Derecho a impugnar / revisión humana | Art. 20 Ley 25.326 (AR); art. 16 Ley 18.331 (UY) | |
| Protección del consumidor / usuario | Ley 24.240 (AR); Ley 17.250 (UY) | |
| Derechos laborales (si el sistema afecta a empleados) | Ley 20.744 LCT (AR); Código del Trabajo (UY) | |

---

## Paso 4 — Emisión del resultado (ficha de triaje)

Producir la siguiente ficha:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FICHA DE TRIAJE — USO DE IA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fecha de análisis:      [DD/MM/AAAA]
Descripción del uso:    [síntesis del sistema analizado]
Categoría de uso:       [decisión automatizada / generación / predictivo / clasificación / otro]
Sector:                 [sector identificado]
Jurisdicción:           [AR / UY / UE / combinación]

RESULTADO: [color del semáforo]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 NO PROCEDER         — Uso prohibido o de riesgo inaceptable
🟠 CONSULTAR REGULADOR — Requiere clarificación con autoridad competente antes de desplegar
🟡 PROCEDER CON MEDIDAS — Viable con implementación de las medidas indicadas abajo
🟢 PROCEDER            — Sin restricciones regulatorias identificadas en este triaje
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FUNDAMENTO REGULATORIO:
[Citar las normas aplicadas y el razonamiento]

DERECHOS AFECTADOS:
[Listar los derechos identificados en el Paso 3]

MEDIDAS REQUERIDAS (si aplica):
[ ] [Medida 1 con referencia normativa]
[ ] [Medida 2 con referencia normativa]
[ ] [...]

PRÓXIMOS PASOS:
1. [Acción concreta]
2. [Acción concreta]
3. Si el resultado es ALTO RIESGO: iniciar EIA-IA con /gobernanza-ia:evaluacion-impacto-ia

ADVERTENCIA:
Esta ficha es de análisis preliminar y no reemplaza la opinión legal
del abogado actuante ni la consulta a la autoridad regulatoria competente.
El marco regulatorio de IA está en evolución — verificar actualizaciones normativas.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Si el uso cae en las prohibiciones absolutas del art. 5 del AI Act o sus equivalentes locales, emitir resultado ROJO inmediatamente y escalar al referente de práctica configurado en CLAUDE.md.
- No emitir resultado VERDE si hay datos sensibles involucrados sin verificar la base jurídica del tratamiento.
- No emitir resultado VERDE si hay decisiones automatizadas sin supervisión humana sobre personas físicas sin verificar el cumplimiento del art. 20 Ley 25.326 o art. 16 Ley 18.331.
- Nunca afirmar que el sistema "cumple" la normativa — solo que no se identificaron restricciones regulatorias en el triaje; la EIA-IA completa es necesaria para los sistemas de alto riesgo.
- Si el AI Act no aplica pero el uso involucra datos personales, aplicar igualmente los arts. de decisiones automatizadas de la Ley 25.326 o Ley 18.331 según corresponda.
