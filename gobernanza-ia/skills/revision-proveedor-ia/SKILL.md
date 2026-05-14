---
name: revision-proveedor-ia
description: >
  Revisa los términos de un proveedor de IA (API, SaaS, plataforma). Verifica uso de datos
  para entrenamiento, responsabilidad por outputs, jurisdicción y ley aplicable, nivel de
  servicio, portabilidad de datos, auditoría y cumplimiento con normativas de privacidad.
  Produce tabla con semáforo y cláusulas sugeridas de reemplazo o adición.
argument-hint: "[nombre del proveedor o pegá los términos de servicio a revisar]"
user-invocable: true
---

# Skill: Revisión de Términos de Proveedor de IA

## Propósito

Analizar los términos de servicio, política de privacidad y cláusulas contractuales de un proveedor de IA con el fin de identificar riesgos regulatorios, de privacidad y de responsabilidad para el cliente que contrata el servicio. La revisión produce una tabla de semáforo con issues y cláusulas sugeridas de reemplazo o adición para la negociación con el proveedor.

---

## Paso 0 — Recolección de material

Solicitar al usuario que provea:

1. **Términos de servicio o acuerdo de uso** del proveedor (texto completo o secciones relevantes)
2. **Política de privacidad** del proveedor
3. **Data Processing Agreement (DPA)** o Acuerdo de Encargado de Tratamiento, si existe
4. **SLA (Service Level Agreement)**, si existe por separado
5. **Nombre del proveedor** y tipo de producto (API / SaaS / plataforma on-premise / modelo open-source con soporte comercial)
6. **Tipo de datos que el cliente enviará al proveedor** (datos anonimizados / datos personales / datos sensibles / datos de negocio sin PII)
7. **Jurisdicción del cliente** (Argentina / Uruguay / ambas / con presencia en UE)

Si el usuario no puede proveer el texto completo, trabajar con las secciones disponibles y consignar las brechas de información.

---

## Paso 1 — Estructura de la revisión

Analizar el material provisto en las siguientes dimensiones:

### Dimensión 1: Uso de datos para entrenamiento del modelo

**Preguntas clave:**
- ¿Los términos permiten al proveedor usar los datos enviados por el cliente (inputs) para entrenar o mejorar sus modelos?
- ¿Existe un mecanismo de opt-out del entrenamiento? ¿Está activo por defecto o debe activarse expresamente?
- ¿Los outputs generados por el modelo son utilizados para entrenamiento?
- ¿Los datos se comparten con terceros para entrenamiento o con filiales del proveedor?
- ¿Los datos se retienen después de la terminación del contrato?

**Normas aplicables:**
- AR: Ley 25.326 — el tratamiento para finalidades distintas de las originales requiere nueva base jurídica (art. 4 inc. 3)
- UY: Ley 18.331 — principio de finalidad (art. 8); datos solo pueden usarse para el fin que motivó su recolección
- UE: RGPD — art. 5(1)(b) principio de limitación de la finalidad; art. 28 — los encargados no pueden subcontratar sin autorización del responsable

### Dimensión 2: Responsabilidad por outputs incorrectos

**Preguntas clave:**
- ¿Los términos excluyen toda responsabilidad del proveedor por la exactitud, completitud o idoneidad de los outputs?
- ¿Existe un tope (cap) de responsabilidad? ¿A qué monto equivale en relación al valor del contrato?
- ¿El proveedor excluye responsabilidad por daños indirectos, lucro cesante o daño emergente?
- ¿El proveedor excluye responsabilidad cuando el cliente modifica, combina o usa los outputs fuera de las condiciones de uso?
- ¿Qué mecanismo de reclamo tiene el cliente frente a outputs incorrectos que causen daño a sus propios usuarios?

**Normas aplicables:**
- AR: CCyCN art. 1743 — límites a las cláusulas de exoneración; art. 1744 — reducibilidad de la pena; art. 1728 — previsibilidad de consecuencias en contratos profesionales
- UY: CC art. 1341 — no se puede excluir responsabilidad por dolo; Ley 17.250 art. 31 si hay relación de consumo

### Dimensión 3: Jurisdicción, ley aplicable y resolución de conflictos

**Preguntas clave:**
- ¿Qué ley rige el contrato? ¿Es la ley de un Estado de EE.UU. (ej. Delaware, California), de Irlanda (para proveedores UE), u otra?
- ¿Cuál es el fuero o el mecanismo de resolución de conflictos (tribunales del Estado del proveedor / arbitraje / mediación)?
- ¿El proveedor ha renunciado al fuero del domicilio del cliente?
- Si el contrato somete a arbitraje: ¿en qué institución, bajo qué reglamento y en qué sede?

**Normas aplicables:**
- AR: CCyCN arts. 2651-2654 (autonomía de la voluntad en contratos internacionales; límites de orden público)
- UY: DIPr — Protocolo de Buenos Aires; arts. 2401-2403 Ley General de DIPr
- Alerta ALTO: jurisdicción extranjera fuera del hemisferio sin conexión sustancial con el cliente o sus datos

### Dimensión 4: Nivel de servicio y continuidad

**Preguntas clave:**
- ¿El SLA establece un uptime mínimo garantizado? ¿Con qué consecuencias ante incumplimiento (créditos / terminación)?
- ¿El proveedor puede suspender el servicio unilateralmente? ¿Bajo qué condiciones y con qué preaviso?
- ¿Existe una política de descontinuación del producto (end of life)? ¿Con cuánto preaviso?
- ¿Hay mecanismos de disaster recovery y backup claramente definidos?

### Dimensión 5: Portabilidad y exportación de datos

**Preguntas clave:**
- ¿El cliente puede exportar todos sus datos (inputs históricos, outputs, modelos fine-tuned) antes de terminar el contrato?
- ¿En qué formato se proveen los datos exportados?
- ¿Cuánto tiempo tiene el proveedor para entregar la exportación tras la solicitud?
- ¿El proveedor elimina los datos del cliente dentro de un plazo razonable tras la terminación?

**Normas aplicables:**
- AR: Ley 25.326 art. 6 — derecho de acceso (por analogía, el responsable debe poder acceder a los datos tratados por el encargado)
- UY: Ley 18.331 art. 13 — derecho de acceso
- AI Act art. 13 y Considerando 78: transparencia sobre capacidades y limitaciones del sistema

### Dimensión 6: Auditoría y transparencia del modelo

**Preguntas clave:**
- ¿El proveedor provee documentación técnica del modelo (model card, ficha técnica, ficha de sistema)?
- ¿El cliente puede auditar el sistema o solicitar informes de auditoría de terceros (SOC 2, ISO 27001)?
- ¿El proveedor notifica al cliente de cambios materiales en el modelo que puedan afectar el rendimiento o los outputs?
- ¿El proveedor informa sobre incidentes de seguridad o brechas de datos en los plazos requeridos por la normativa?

**Normas aplicables:**
- AI Act arts. 9, 12 y 17 — obligaciones de transparencia y documentación para sistemas de alto riesgo
- AR: Ley 25.326 art. 9 — deber de notificación de brechas (interpretación amplia)
- UY: Ley 18.331 art. 10 — deber de seguridad y notificación de vulneraciones

### Dimensión 7: Cumplimiento con normativas de privacidad

**Preguntas clave:**
- ¿El proveedor ha suscrito un DPA o equivalente que lo constituya como encargado de tratamiento (y no responsable)?
- ¿Los términos identifican correctamente al cliente como responsable del tratamiento y al proveedor como encargado?
- ¿El proveedor acepta instrucciones del responsable sobre el tratamiento de los datos?
- ¿El proveedor informa sobre transferencias a subencargados (subprocesadores)?
- ¿El proveedor certifica cumplimiento con la ley de privacidad aplicable al cliente (Ley 25.326, Ley 18.331, RGPD)?
- ¿Los servidores donde se procesan los datos del cliente están en jurisdicciones con nivel adecuado de protección?

---

## Paso 2 — Tabla de semáforo

Producir la siguiente tabla con una fila por dimensión analizada:

| # | Dimensión | Cláusula/sección | Semáforo | Riesgo identificado | Recomendación |
|---|---|---|---|---|---|
| 1 | Uso de datos para entrenamiento | [§ X.X] | 🔴/🟡/🟢 | [descripción] | [acción: negociar / aceptar / exigir opt-out / rechazar] |
| 2 | Responsabilidad por outputs | [§ X.X] | 🔴/🟡/🟢 | [descripción] | [acción] |
| 3 | Jurisdicción y ley aplicable | [§ X.X] | 🔴/🟡/🟢 | [descripción] | [acción] |
| 4 | Nivel de servicio y continuidad | [§ X.X] | 🔴/🟡/🟢 | [descripción] | [acción] |
| 5 | Portabilidad y exportación | [§ X.X] | 🔴/🟡/🟢 | [descripción] | [acción] |
| 6 | Auditoría y transparencia | [§ X.X] | 🔴/🟡/🟢 | [descripción] | [acción] |
| 7 | Cumplimiento normativas privacidad | [§ X.X] | 🔴/🟡/🟢 | [descripción] | [acción] |

Criterios de semáforo:
- **ROJO**: cláusula inaceptable — riesgo legal o regulatorio directo — exige negociación antes de firmar
- **AMARILLO**: cláusula preocupante — riesgo identificado — evaluar negociación o mitigación alternativa
- **VERDE**: cláusula aceptable — sin issues materiales identificados

---

## Paso 3 — Cláusulas sugeridas

Para cada ítem con semáforo ROJO o AMARILLO, proponer texto de cláusula alternativa o addendum:

### Cláusula sugerida: Uso de datos para entrenamiento (opt-out)

```
"El Proveedor no utilizará los Datos del Cliente —incluyendo los inputs, outputs,
conversaciones, documentos ni ningún otro material enviado o generado en el marco
del uso del Servicio— para entrenar, ajustar, mejorar ni evaluar sus modelos de
inteligencia artificial, sin el consentimiento previo, expreso y por escrito del Cliente.
El Proveedor adoptará las medidas técnicas y organizativas necesarias para aislar
los datos del Cliente de cualquier proceso de entrenamiento. Esta restricción se
mantiene durante la vigencia del contrato y por un período de dos (2) años adicionales
tras su terminación, o hasta la acreditación de la eliminación completa de los datos,
lo que ocurra primero."
```

### Cláusula sugerida: Responsabilidad por outputs

```
"Sin perjuicio de las exclusiones de responsabilidad previstas en el presente acuerdo,
el Proveedor responderá por los daños directos y probados causados al Cliente como
consecuencia de un output manifiestamente erróneo, inexacto o contrario a las instrucciones
del Cliente, cuando dicho error sea atribuible a un fallo del sistema de IA del Proveedor
y no a un uso indebido del servicio por parte del Cliente. La responsabilidad total del
Proveedor en virtud de esta cláusula no excederá el monto equivalente a doce (12) meses
de facturación del servicio al Cliente."
```

### Cláusula sugerida: Portabilidad y eliminación de datos

```
"Al vencimiento o terminación del contrato, el Proveedor pondrá a disposición del Cliente,
dentro de los treinta (30) días corridos siguientes a la solicitud, una exportación completa
de todos los Datos del Cliente en formato estándar interoperable (JSON, CSV o equivalente
abierto). Transcurridos noventa (90) días desde la terminación, el Proveedor eliminará de
manera segura todos los Datos del Cliente de sus sistemas y subencargados, certificando
dicha eliminación por escrito dentro de los diez (10) días corridos posteriores."
```

### Cláusula sugerida: Notificación de incidentes

```
"El Proveedor notificará al Cliente dentro de las veinticuatro (24) horas de tomar
conocimiento de cualquier acceso no autorizado, pérdida, alteración o divulgación
de los Datos del Cliente (incidente de seguridad). La notificación inicial incluirá:
(i) descripción del incidente; (ii) categorías de datos afectados; (iii) número
estimado de registros afectados; (iv) medidas adoptadas. El Proveedor cooperará con
el Cliente en la notificación a la autoridad de control competente (AAIP en Argentina;
URCDP en Uruguay) en los plazos previstos por la normativa aplicable."
```

---

## Paso 4 — Output: informe de revisión

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORME DE REVISIÓN — TÉRMINOS DE PROVEEDOR DE IA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fecha del análisis:     [DD/MM/AAAA]
Proveedor:              [nombre]
Tipo de producto:       [API / SaaS / plataforma]
Documentos revisados:   [lista de documentos provistos]
Cliente / jurisdicción: [nombre del cliente y jurisdicción aplicable]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESUMEN EJECUTIVO
[3 líneas: evaluación global, número de ítems rojos, amarillos y verdes, y recomendación principal]

TABLA DE SEMÁFORO
[Tabla del Paso 2]

ISSUES CRÍTICOS (ítems ROJOS)
[Descripción desarrollada de cada ítem rojo con referencia normativa]

CLÁUSULAS SUGERIDAS
[Texto de las cláusulas del Paso 3 relevantes para este proveedor]

RECOMENDACIÓN FINAL
[  ] Contratar con las cláusulas sugeridas incorporadas como adendum
[  ] Continuar negociación sobre los puntos señalados antes de firmar
[  ] No contratar hasta resolver los issues críticos indicados
[  ] Escalar al referente de práctica para decisión

COMPUERTA DE APROBACIÓN
□ Abogado actuante revisó el informe y las cláusulas sugeridas
□ El cliente fue informado de los riesgos identificados
□ Si hay datos personales: el DPA fue revisado y considerado adecuado
□ Si hay transferencias internacionales: se verificaron las garantías aplicables
□ El cliente tomó la decisión de contratar / negociar / no contratar

ADVERTENCIA
Este informe es de análisis preliminar. La revisión se basó en el material provisto
por el usuario; pueden existir términos adicionales, políticas específicas de producto
o adendos que modifiquen el análisis. Verificar siempre la versión vigente de los
términos al momento de firmar. El marco regulatorio de IA y privacidad está en
evolución — consultar actualizaciones antes de implementar las recomendaciones.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- No emitir el informe sin la compuerta de aprobación del abogado actuante.
- Si los términos del proveedor no cuentan con ningún DPA y el cliente enviará datos personales: emitir alerta inmediata de ROJO — el tratamiento sin DPA expone al cliente a incumplimiento de la Ley 25.326 (AR) o Ley 18.331 (UY).
- Si el proveedor es exclusivamente responsable del tratamiento de los datos según sus términos (y no encargado): alertar que eso implica que el proveedor puede usar los datos libremente y que el cliente pierde el control sobre ellos — riesgo ROJO.
- Si los términos están redactados íntegramente en inglés y el cliente es consumidor o pequeña empresa sin capacidad de negociación, alertar que en Argentina las cláusulas abusivas en contratos de adhesión son inválidas (art. 1117 CCyCN).
- No recomendar "aceptar" un ítem con semáforo ROJO sin explicar el riesgo concreto que asume el cliente al hacerlo.
- Las cláusulas sugeridas son puntos de partida para la negociación; el abogado actuante debe adaptarlas a las circunstancias concretas del contrato y del cliente.
