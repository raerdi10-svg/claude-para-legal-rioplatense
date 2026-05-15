---
name: extraccion-issues
description: >
  Lectura de todos los documentos de un VDR y extracción de issues agrupados
  por categoría con nivel de riesgo. Produce resumen ejecutivo más lista de
  issues con descripción, documento fuente, riesgo, acción recomendada y
  responsable sugerido. Complementa revision-tabular con análisis de fondo
  por categoría para deals M&A en Argentina y Uruguay.
argument-hint: "[adjuntar documentos del VDR o indicar categorías y documentos a analizar]"
user-invocable: true
---

# Skill: Extracción de Issues de VDR

## Propósito

Leer el contenido de los documentos de un data room (VDR) y extraer todos los issues legales relevantes agrupados por categoría, con su nivel de riesgo, el documento fuente, la acción recomendada y el responsable sugerido. Esta skill va un paso más allá de la revisión tabular: en lugar de catalogar documentos, analiza su contenido en profundidad y sintetiza los issues que impactan en la decisión de compra, la valuación o la estructura del deal.

---

## Paso 0 — Lectura del perfil

Leer `CLAUDE.md` del plugin para incorporar jurisdicción, categorías de due diligence, umbrales de riesgo y estilo de outputs. Identificar si existe una revisión tabular previa (`/corporativo:revision-tabular`) para integrar sus hallazgos.

---

## Paso 1 — Recolección de datos

Solicitar al usuario:

1. **Documentos del VDR:** adjuntar o listar todos los documentos a analizar.
2. **Resultado de la revisión tabular previa** (si existe): para no duplicar el análisis sino profundizarlo.
3. **Jurisdicción del target:** Argentina / Uruguay / Ambas.
4. **Tipo de deal y rol del cliente:** comprador / vendedor.
5. **Categorías de foco:** si el cliente solicita un análisis más profundo de alguna categoría específica.
6. **Contingencias ya conocidas:** issues que el vendedor ya declaró en el disclosure schedule o en la data room cover letter, para contextualizarlos (no ignorarlos).
7. **Monto del deal y umbrales de materialidad:** definir qué monto de contingencia es "material" para el deal (ej. contingencias > USD 50.000 son materiales en un deal de USD 5.000.000).

---

## Paso 2 — Análisis por categoría

Para cada categoría, aplicar el siguiente análisis de fondo:

### SOCIETARIO (arts. 59, 63, 94, 205, 234, 261 LGS / arts. 189, 337-340, 392-394 LSC)

**Verificaciones clave:**

- **Titularidad y cadena de accionistas:** ¿Existe un libro de registro de acciones actualizado? ¿Las transferencias pasadas fueron inscritas correctamente? ¿Hay acciones prendadas o con restricciones de transferencia?
- **Estatutos vigentes:** ¿El objeto social cubre todas las actividades que el target desarrolla? ¿Hay cláusulas de preferencia o restricción de transferencia que afecten el deal?
- **Actas de asamblea (AR: art. 234 LGS; UY: art. 337 LSC):** ¿Todas las asambleas de los últimos 5 años fueron regularmente convocadas y celebradas con quórum suficiente? ¿Hay actos aprobados por asamblea ordinaria que debieron aprobarse por extraordinaria?
- **Actas de directorio (AR: art. 261 LGS; UY: art. 379 LSC):** ¿Los directores actuaron dentro de sus facultades? ¿Hay actos ultra vires? ¿Los directores con interés contrario se abstuvieron (art. 272 LGS; art. 191 LSC)?
- **Representación legal:** ¿El representante legal con poder para firmar el SPA tiene facultades suficientes según el estatuto y las actas de asamblea?
- **Situación registral:** ¿Las últimas modificaciones estatutarias están inscriptas en IGJ/AIN? ¿Los nombramientos de autoridades están inscriptos y vigentes?
- **Capital social:** ¿El capital está integrado en los porcentajes que exige la ley? (art. 187 LGS para SA: 25 % al suscribir, resto en 2 años; art. 282 LSC UY).

**Issues frecuentes en categoría societaria:**

| Issue | Nivel | Norma | Impacto en el deal |
|---|---|---|---|
| Asamblea celebrada sin quórum o con convocatoria defectuosa | ALTO | Art. 237-243 LGS / Art. 337-340 LSC | Los actos aprobados pueden ser nulos |
| Director con mandato vencido firmando actos vinculantes | ALTO | Art. 257 LGS / Art. 392 LSC | Posible ineficacia del acto |
| Actos ultra vires fuera del objeto social | ALTO | Art. 58 LGS / Art. 189 LSC | Sociedad puede no estar obligada |
| Actas no refrendadas en el libro oficial | MEDIO | Art. 73 LGS / Art. 91 LSC | Prueba del acto incierta |
| Capital no integrado en plazo legal | MEDIO | Art. 187 LGS | Responsabilidad de accionistas morosos |
| Autoridades no inscriptas en IGJ/AIN | MEDIO | Art. 12 LGS / Art. 16 LSC | Inoponibilidad a terceros |

---

### LABORAL

**Verificaciones clave:**

- **Nómina y convenios colectivos:** ¿Los empleados están correctamente encuadrados en el CCT aplicable? ¿Hay trabajadores no declarados o en relación de dependencia encubierta?
- **Situación ante AFIP/ANSES (AR) / BPS (UY):** deudas, planes de facilidades vigentes, juicios de ejecución.
- **Contratos de ejecutivos clave:** ¿Hay cláusulas de change of control que activen indemnizaciones especiales o derecho de rescisión?
- **Litigios laborales:** contingencias cuantificadas; ¿hay procedimientos conciliatorios en el SECLO (AR) o MTSS (UY)?
- **Tercerización:** ¿El target tercerizó personal? En Argentina, verificar solidaridad del art. 30 LCT y art. 29 LCT (intermediación). En Uruguay, verificar responsabilidad del art. 1 Ley 18.099.
- **No competencia post-contractual de ejecutivos:** ¿Están correctamente instrumentadas? ¿Son razonables en tiempo y geografía?

---

### FISCAL

**Verificaciones clave:**

- **Situación impositiva general:** ¿Existen deudas con AFIP (AR) / DGI (UY) no declaradas? ¿El target tiene planes de facilidades vigentes?
- **Impuesto a las ganancias / IRAE:** ¿El target tiene ajustes por inflación pendientes (AR)? ¿Hay diferencias temporarias significativas?
- **IVA:** ¿Hay saldos técnicos o deudas de IVA?
- **Precios de transferencia:** ¿El target tiene operaciones con partes relacionadas? ¿Están documentadas con informes de precios de transferencia?
- **Asset deal:** verificar responsabilidad solidaria del adquirente por deudas del enajenante (art. 8 Ley 11.683 AR; art. 1 Ley 17.453 UY para fondo de comercio).
- **Impuesto a la transferencia:** ITBI en UY; impuesto de sellos en AR por jurisdicción.
- **Deudas ante municipios / intendencias:** impuestos municipales, tasas de habilitación.

---

### CONTRACTUAL

**Verificaciones clave:**

- **Contratos materiales:** ¿Los contratos con los 5-10 principales clientes y proveedores tienen cláusulas de change of control? ¿La operación activa rescisión o renegociación?
- **Contratos de crédito:** ¿Hay covenants de cambio de control? ¿El cierre del deal activa un evento de incumplimiento (cross-default)?
- **Garantías otorgadas:** ¿El target garantizó obligaciones de terceros (fianzas, avales)? ¿Están cuantificadas?
- **Contratos de distribución y agencia:** si hay contratos de larga duración con distribuidores, verificar indemnizaciones por rescisión.
- **Contratos con el Estado:** ¿Tienen restricciones de cesión o change of control?

---

### PI

**Verificaciones clave:**

- **Marcas:** ¿Están registradas a nombre del target? ¿Están vigentes? ¿Hay oposiciones o cancelaciones pendientes en INPI (AR) / MIEM (UY)?
- **Software:** ¿El código fuente es propio? ¿Hay desarrollos de terceros (open source o comercial) embebidos sin licencia adecuada?
- **Patentes y diseños:** vigencia, titularidad, litigios de validez.
- **Dominio y redes:** ¿Los dominios y perfiles en redes sociales son del target o de personas físicas?
- **Titularidad de obras:** ¿Los desarrollos de empleados y contratistas tienen cesión expresa al target?

---

### LITIGIOSO

**Verificaciones clave:**

- **Litigios civiles y comerciales:** cuantificar contingencias máximas y probabilidad de resultado adverso.
- **Litigios laborales:** ídem; en Argentina verificar si hay causas con fuero especial (sindical, maternidad).
- **Medidas cautelares:** ¿Hay embargos sobre activos del target que afecten el deal?
- **Laudos arbitrales:** ¿Hay laudos contra el target no satisfechos?
- **Contingencias regulatorias:** sanciones de la CNV, BCU, ANMAT u otros organismos.

---

### AMBIENTAL

**Verificaciones clave:**

- **Permisos ambientales:** ¿El target tiene todos los permisos de funcionamiento vigentes?
- **Pasivos ambientales:** ¿Hay suelo contaminado, residuos peligrosos sin tratamiento, vertidos no autorizados?
- **Sanciones:** ¿Hay expedientes sancionatorios en curso ante autoridades ambientales?
- **Sector de actividad:** en manufactura, minería, agro y energía, el análisis ambiental es siempre de nivel ALTO de prioridad.

---

### REGULATORIO

**Verificaciones clave:**

- **Habilitaciones de funcionamiento:** ¿están vigentes y a nombre del target?
- **Sector financiero:** ¿requiere autorización del BCRA / BCU para el cambio de control?
- **Sector salud:** ¿ANMAT (AR) / MSP (UY) debe autorizar la operación?
- **Telecomunicaciones:** ¿ENACOM (AR) / URSEC (UY) debe autorizar?
- **Defensa de la competencia:** ¿la fusión supera los umbrales de notificación obligatoria (CNDC - Ley 27.442 AR / URSEC UY)?

---

## Paso 3 — Consolidación y priorización de issues

Una vez analizadas todas las categorías, consolidar todos los issues en una lista única ordenada por nivel de riesgo:

```
LISTA DE ISSUES — [Nombre del Target] — [Fecha DD/MM/AAAA]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ISSUES DE NIVEL ALTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ISSUE A-[N] — [Categoría]
Descripción:        [Qué es el issue, qué norma infringe o qué riesgo genera]
Documento fuente:   [Nombre del documento del VDR]
Cuantificación:     [Monto de contingencia estimada, si es cuantificable]
Norma aplicable:    [Art. X LGS / LSC / ley aplicable]
Acción recomendada: [Subsanar / Representación y garantía / Escrow / Escalamiento]
Responsable:        [Área del estudio / Área del cliente]
Impacto en el deal: [Descripción del impacto en el precio o en la estructura]

[Repetir para cada issue ALTO]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ISSUES DE NIVEL MEDIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Mismo formato — descripción, documento fuente, norma, acción, responsable]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ISSUES DE NIVEL BAJO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Tabla condensada: Issue | Documento | Acción]
```

---

## Paso 4 — Output final: informe de due diligence

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORME DE DUE DILIGENCE LEGAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Target:             [Denominación social + CUIT/RUT]
Jurisdicción:       [AR / UY / Ambas]
Tipo de deal:       [Share deal / Asset deal / Otro]
Documentos analizados: [N]
Período analizado:  [Ejercicios o fechas cubiertas]
Fecha del informe:  [DD/MM/AAAA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I. RESUMEN EJECUTIVO
[Tres líneas: estado general del target, categorías con mayor riesgo y
recomendación de si el deal puede avanzar, requiere subsanaciones previas
o tiene issues que afectan materialmente la valuación.]

II. ISSUES CRÍTICOS (nivel ALTO)
[Lista del Paso 3 — solo los ALTO]

III. ANÁLISIS POR CATEGORÍA
[Para cada categoría con issues: descripción de los issues, norma aplicable,
acción recomendada. Omitir categorías sin observaciones.]

IV. DOCUMENTOS PENDIENTES DE RECIBIR
[Lista de documentos no recibidos que son necesarios para completar el análisis]

V. CONSIDERACIONES PARA LA NEGOCIACIÓN DEL SPA
[Issues que deben reflejarse en representaciones y garantías, escrow, precio
ajustado, o condiciones previas al cierre (conditions precedent)]

VI. CONCLUSIÓN
[Dictamen de cierre: el due diligence preliminar revela / no revela issues
de nivel ALTO que requieran acción inmediata. Aclarar que es análisis
preliminar sujeto a revisión por abogado matriculado.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Nunca emitir un dictamen de "due diligence limpio" — siempre indicar el alcance exacto del análisis y los documentos revisados.
- Si una categoría no pudo analizarse por falta de documentos, declararlo explícitamente en el informe — no silenciarlo.
- Los issues de nivel ALTO nunca pueden quedar sin acción recomendada y sin responsable asignado.
- Si la contingencia acumulada de issues MEDIO y ALTO supera el 10 % del precio de compra, recomendar explícitamente su consideración en la valuación.
- En deals de asset deal (compraventa de activos), verificar siempre la responsabilidad solidaria del adquirente por deudas laborales (art. 228 LCT AR) y fiscales (art. 8 Ley 11.683 AR), que no aplican en share deals.
- Citar siempre la norma específica: "art. 234 inc. 2° LGS", no solo "LGS".
