---
name: revision-dpa
description: >
  Revisión de un Acuerdo de Procesamiento de Datos (DPA) desde la perspectiva del cliente,
  ya sea responsable o encargado del tratamiento. Produce tabla semáforo de cláusulas y
  texto sugerido de mejora bajo la Ley 18.331 (Uruguay) y la Ley 25.326 (Argentina).
argument-hint: "[texto del DPA o descripción del acuerdo a revisar]"
user-invocable: true
---

# Skill: Revisión de DPA (Data Processing Agreement)

## Propósito

Analizar un Acuerdo de Procesamiento de Datos (DPA) con la mirada del abogado del cliente,
ya sea que este actúe como responsable del tratamiento (quien contrata al proveedor) o como
encargado (quien presta el servicio de procesamiento). El skill produce una tabla semáforo
cláusula a cláusula, identifica brechas de cumplimiento normativo y sugiere texto alternativo
o adicional para las cláusulas observadas.

---

## Paso 0 — Recolección de datos

Solicitar al abogado:

1. **Texto del DPA** a revisar (completo, en el idioma original).
2. **Rol del cliente** en el acuerdo:
   - Responsable del tratamiento (controller): quien determina fines y medios del tratamiento.
   - Encargado del tratamiento (processor): quien trata datos por cuenta del responsable.
   - Ambos en distintas secciones (acuerdo recíproco o mixed DPA).
3. **Jurisdicción(es) aplicable(s):** ¿Uruguay, Argentina, o ambas? ¿El DPA también
   invoca el RGPD u otra normativa extranjera?
4. **Sector del cliente y tipo de datos involucrados** (referencia al perfil del CLAUDE.md).
5. **Contexto del acuerdo:** ¿Es un DPA estándar del proveedor (take-it-or-leave-it) o
   hay margen de negociación?
6. **¿Hay sub-encargados ya identificados?** (Nombres o referencias en el DPA o en anexos.)

---

## Paso 1 — Verificación del objeto y finalidad del procesamiento

Revisar si el DPA establece con claridad:

- **Objeto del tratamiento:** qué operaciones se realizarán sobre los datos (recopilación,
  almacenamiento, análisis, transmisión, etc.).
- **Finalidad:** para qué fin se tratan los datos (prestación del servicio, facturación,
  soporte, analítica, etc.).
- **Prohibición de uso propio:** ¿El encargado tiene prohibido tratar los datos para fines
  propios o distintos de los instrucciones del responsable? (art. 10 inc. 4 Ley 18.331;
  art. 25 inc. 1 Ley 25.326.)
- **Instrucciones documentadas:** ¿El encargado actúa solo conforme a instrucciones
  documentadas del responsable? (art. 10 Ley 18.331; art. 25 Ley 25.326.)

Señal de alerta si el DPA usa fórmulas vagas como "tratamiento necesario para el servicio"
sin especificar operaciones concretas.

---

## Paso 2 — Base legal del tratamiento

Verificar:

- **¿Se identifica la base legal** del responsable para el tratamiento? (Consentimiento /
  contrato / interés legítimo / obligación legal — art. 9 Ley 18.331; art. 5 Ley 25.326.)
- **¿El encargado declara que no tratará los datos** sin base legal habilitante propia o
  que el tratamiento quedará limitado a las instrucciones del responsable?
- **Categorías especiales:** ¿Si hay datos sensibles (salud, biometría, origen étnico,
  orientación sexual), se identifica la base legal reforzada aplicable?
  (art. 18 Ley 18.331; art. 7 Ley 25.326.)

---

## Paso 3 — Tipos de datos y categorías especiales

Revisar:

- ¿El DPA lista las **categorías de datos personales** objeto del tratamiento?
  (Datos de identificación, financieros, laborales, de salud, biométricos, etc.)
- ¿Se identifican **categorías especiales** y se estipulan medidas adicionales?
- ¿Se define el **colectivo de titulares** (empleados, clientes, usuarios, menores)?
- ¿El DPA prohíbe expresamente el tratamiento de **datos de menores** si no está
  contemplado en el objeto? (art. 17 Ley 18.331; art. 8 Ley 25.326.)

---

## Paso 4 — Medidas de seguridad

Verificar conforme a los estándares normativos aplicables:

| Requisito | Norma UY | Norma AR |
|---|---|---|
| Obligación de implementar medidas técnicas y organizativas | art. 10 Ley 18.331 | art. 9 Ley 25.326 |
| Estándar de seguridad (riesgo del tratamiento) | Decreto 414/009, art. 8 | Disposición AAIP 47/2018 |
| Deber de confidencialidad del encargado y su personal | art. 10 Ley 18.331 | art. 10 Ley 25.326 |

Verificar que el DPA incluya:
- Descripción (aunque sea referenciada a un anexo) de las **medidas técnicas** (cifrado,
  seudonimización, control de acceso, backups, etc.).
- Descripción de las **medidas organizativas** (capacitación, políticas internas, control
  de accesos por roles).
- Obligación del encargado de garantizar que su **personal que accede a los datos** ha
  asumido un deber de confidencialidad.
- Referencia a estándares reconocidos (ISO 27001, SOC 2 Tipo II, PCI-DSS) si corresponde
  al sector.

Señal de alerta si las medidas de seguridad son meramente declarativas ("implementaremos
medidas adecuadas") sin especificación alguna o sin remisión a un anexo técnico.

---

## Paso 5 — Sub-encargados

Verificar:

- ¿El DPA **lista los sub-encargados autorizados** o establece un mecanismo de notificación
  previa al responsable? (art. 10 inc. 3 Ley 18.331; art. 25 inc. 2 Ley 25.326.)
- ¿El responsable tiene derecho a **objetar la incorporación de nuevos sub-encargados**?
- ¿El encargado asume responsabilidad ante el responsable por los **actos de los
  sub-encargados** como si fueran propios?
- ¿Se exige que los sub-encargados asuman las **mismas obligaciones** de protección de
  datos que el encargado principal?

Señal de alerta: autorización genérica e irrestricta de sub-encargados sin mecanismo de
control o notificación.

---

## Paso 6 — Transferencias internacionales de datos

Verificar:

- ¿El DPA **prohíbe transferencias internacionales** sin autorización del responsable?
- Si hay transferencias, ¿se identifican los **países de destino**?
- ¿Uruguay o Argentina han declarado adecuado el nivel de protección del país destino?
  - Uruguay: la URCDP mantiene lista de países con nivel adecuado. La UE reconoce a
    Uruguay como país adecuado (Decisión de la Comisión, 2012).
  - Argentina: la AAIP mantiene el Registro de Países con Nivel de Protección de
    Datos Adecuado.
- Si el destino no tiene nivel adecuado, ¿se establecen garantías contractuales equivalentes
  (cláusulas contractuales tipo, binding corporate rules, consentimiento explícito)?
  (art. 23-25 Ley 18.331; art. 12 Ley 25.326 y normas reglamentarias.)

---

## Paso 7 — Auditorías e inspecciones

Verificar:

- ¿El responsable tiene derecho a **auditar o inspeccionar** las instalaciones y sistemas
  del encargado para verificar el cumplimiento del DPA?
- ¿Se prevé una alternativa de **auditoría por tercero independiente** (certificaciones,
  reportes de auditoría como SOC 2)?
- ¿El encargado tiene obligación de **cooperar con autoridades regulatorias**
  (URCDP / AAIP) en caso de inspección?

---

## Paso 8 — Notificación de brechas de seguridad

Verificar los plazos y procedimientos:

| Aspecto | Uruguay | Argentina |
|---|---|---|
| Plazo de notificación del encargado al responsable | Sin plazo legal expreso: "sin demora indebida" (best practice: 24-48 hs) | Sin plazo legal expreso para encargado→responsable; best practice: 72 hs |
| Plazo de notificación del responsable a la URCDP/AAIP | Decreto 64/020: "en el menor tiempo posible" (en la práctica, 72 hs) | Disposición AAIP 3/2021: 72 hs desde conocimiento |
| Contenido de la notificación | Naturaleza de la brecha, datos afectados, medidas adoptadas | Naturaleza de la brecha, datos afectados, medidas adoptadas |
| Notificación a titulares afectados | Cuando la brecha genera riesgo alto | Cuando la brecha genera riesgo alto |

Verificar que el DPA incluya:
- Obligación del encargado de **notificar al responsable** sin demora injustificada.
- Obligación de proveer **información suficiente** para que el responsable pueda cumplir
  con sus propias obligaciones de notificación regulatoria.
- Obligación de **cooperar** en la investigación y mitigación.

Señal de alerta: DPA que no menciona brechas, o que fija plazos de notificación internos
superiores a 72 horas.

---

## Paso 9 — Plazo del tratamiento y devolución / destrucción de datos

Verificar:

- ¿El DPA fija el **plazo del tratamiento** (duración del contrato de servicio subyacente)?
- A la terminación, ¿el encargado se obliga a **devolver o destruir** todos los datos
  personales? (art. 10 inc. 5 Ley 18.331; art. 25 inc. 4 Ley 25.326.)
- ¿Se establece un **plazo razonable** para la devolución/destrucción (ej. 30 días desde
  la terminación)?
- ¿Hay excepciones a la destrucción por obligaciones legales de conservación del encargado?
  Si las hay, ¿están acotadas y documentadas?
- ¿El encargado debe emitir una **certificación** de destrucción?

---

## Paso 10 — Tabla semáforo de cláusulas

Producir la siguiente tabla con una fila por cláusula o sección revisada:

| N.° | Cláusula / Sección | Estado | Observación | Acción recomendada |
|---|---|---|---|---|
| 1 | Objeto y finalidad | 🔴 ALTO / 🟡 MEDIO / 🟢 OK | [descripción del hallazgo] | [acción concreta] |
| 2 | Base legal | ... | ... | ... |
| 3 | Categorías de datos | ... | ... | ... |
| 4 | Medidas de seguridad | ... | ... | ... |
| 5 | Sub-encargados | ... | ... | ... |
| 6 | Transferencias internacionales | ... | ... | ... |
| 7 | Auditorías | ... | ... | ... |
| 8 | Notificación de brechas | ... | ... | ... |
| 9 | Plazo y destrucción | ... | ... | ... |
| 10 | Ley aplicable y jurisdicción | ... | ... | ... |

Criterios del semáforo:
- **ROJO (ALTO):** Ausencia total de la cláusula o cláusula que viola una obligación legal
  imperativa. Impide la firma sin corrección.
- **AMARILLO (MEDIO):** Cláusula presente pero insuficiente, vaga o que puede mejorar
  a favor del cliente. Negociar antes de firmar.
- **VERDE (OK):** Cláusula completa y conforme con la normativa aplicable.

---

## Paso 11 — Cláusulas sugeridas

Para cada ítem con estado ROJO o AMARILLO, redactar la cláusula sugerida o el texto
de reemplazo / adición. Indicar en cada caso si es una cláusula de mínima legal (no
negociable) o una mejora de posición (negociable según contraparte).

---

## Paso 12 — Resumen ejecutivo

Producir un resumen de tres líneas con:
1. Cantidad de ítems ROJO, AMARILLO y VERDE.
2. Riesgo global del DPA (ALTO / MEDIO / BAJO) y fundamento en una frase.
3. Recomendación: firmar / firmar con las correcciones mínimas / no firmar sin renegociación.

---

## Guardrails

- **No emitir una opinión de "aprobado para firmar"** sin que el abogado revise la tabla
  semáforo y las cláusulas sugeridas. El skill produce un borrador de análisis, no una
  opinión legal definitiva.
- **Si el DPA aplica el RGPD** (por ser una contraparte europea), señalarlo y alertar
  que el análisis del skill está orientado a la normativa rioplatense: puede requerirse
  análisis complementario de cumplimiento RGPD.
- **Si el DPA contiene cláusula arbitral** en jurisdicción extranjera, señalar el riesgo
  como ALTO y derivar al área de litigio.
- **No compartir el contenido del DPA** más allá del análisis solicitado. La información
  es confidencial.
- **Si el DPA involucra datos de menores** y no tiene protecciones específicas, clasificar
  ese ítem como ROJO automáticamente.
