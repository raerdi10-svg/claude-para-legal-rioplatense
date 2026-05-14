---
name: revision-tabular
description: >
  Revisión tabular de documentos de data room para due diligence corporativo.
  Produce una tabla con una fila por documento y columnas: Documento, Categoría,
  Observación, Riesgo (ALTO/MEDIO/BAJO), Cita normativa, Acción requerida.
  Categorías: societario, laboral, fiscal, contractual, PI, litigioso,
  ambiental, regulatorio. Optimizado para LGS (Ley 19.550) y LSC (Ley 16.060).
argument-hint: "[listar documentos del data room o adjuntar índice del VDR]"
user-invocable: true
---

# Skill: Revisión Tabular de Data Room

## Propósito

Producir una tabla de revisión estructurada del data room, donde cada documento recibe una fila con su categoría, observación principal, nivel de riesgo, cita normativa y acción requerida. Es el primer producto de un due diligence: permite al equipo M&A tener una visión panorámica del estado del target antes de profundizar el análisis en cada categoría.

---

## Paso 0 — Lectura del perfil

Leer `CLAUDE.md` del plugin para incorporar:
- Jurisdicción del deal (AR / UY / ambas)
- Categorías de due diligence que el estudio siempre cubre
- Umbrales de riesgo del estudio
- Estilo de outputs preferido

---

## Paso 1 — Recolección de datos

Solicitar al usuario:

1. **Índice del data room:** lista de documentos con su nombre (o adjuntar directamente los documentos).
2. **Jurisdicción del target:** Argentina (LGS) / Uruguay (LSC) / Ambas.
3. **Tipo de deal:** share deal / asset deal / fusión / otro.
4. **Rol del cliente:** comprador (buy-side) / vendedor (sell-side).
5. **Categorías a revisar:** confirmar cuáles de las ocho categorías estándar aplican al deal.
6. **Fecha de inicio del due diligence y plazo para el informe:** para priorizar la revisión.
7. **Documentos ya analizados previamente:** si el due diligence es parcial o continúa uno anterior.

---

## Paso 2 — Clasificación por categoría

Para cada documento recibido, asignarlo a una de las siguientes categorías:

| Categoría | Descripción | Norma de referencia |
|---|---|---|
| **SOCIETARIO** | Estatutos, actas, libros societarios, inscripciones registrales, estructura accionaria | LGS arts. 11, 63, 73, 234, 261 / LSC arts. 1, 13, 160, 337, 392 |
| **LABORAL** | Contratos de trabajo, convenios colectivos, liquidaciones, litigios laborales, situación ante AFIP/BPS | LCT / Ley 18.566 UY |
| **FISCAL** | Declaraciones juradas, deudas impositivas, dictámenes fiscales, situación DGI/AFIP | Ley 11.683 AR / TOCAF UY |
| **CONTRACTUAL** | Contratos materiales con clientes, proveedores, financiadores, distribuidores, licenciantes | CCyCN arts. 957 ss. / CC UY arts. 1247 ss. |
| **PI** | Marcas, patentes, software, derechos de autor, licencias de entrada y salida | Ley 22.362 (marcas AR) / Ley 9.739 (UY) / Ley 11.723 (PI AR) |
| **LITIGIOSO** | Demandas recibidas, medidas cautelares, laudos arbitrales, acuerdos de transacción | Código Procesal / Regulación arbitral |
| **AMBIENTAL** | Permisos ambientales, auditorías, pasivos, sanciones de autoridades ambientales | Ley 25.675 AR / Ley 16.112 UY y normativa MVOT |
| **REGULATORIO** | Habilitaciones sectoriales, licencias, autorizaciones de funcionamiento, cumplimiento CNV/BCU/ANMAT | Normas sectoriales por rubro |

Si un documento corresponde a más de una categoría, asignarlo a la categoría principal e indicar la secundaria en la observación.

---

## Paso 3 — Análisis de cada documento

Para cada documento, determinar:

### Nivel de riesgo:

- **ALTO:** El documento revela o genera una contingencia significativa, un defecto formal que invalida un acto societario relevante, o un incumplimiento legal con consecuencias para la operación.
- **MEDIO:** El documento tiene observaciones que pueden negociarse, corregirse o mitigarse con ajustes en la estructura del deal (retención de precio, escrow, declaraciones y garantías específicas, indemnidades).
- **BAJO:** El documento está en orden con observaciones menores de forma; no genera contingencia significativa.
- **PENDIENTE:** No se recibió el documento o está incompleto — incluir en lista de documentos pendientes.

### Acción requerida (valores posibles):

- **Ninguna** — Documento en orden.
- **Aclaración al vendedor** — Solicitar información adicional o aclaración.
- **Subsanar antes del cierre** — Defecto que el vendedor debe regularizar antes de firmar el SPA.
- **Representación y garantía** — Incluir en las declaraciones y garantías del SPA con indemnidad específica.
- **Retención de precio / escrow** — Retener parte del precio hasta resolución de la contingencia.
- **Consultar área especializada** — Derivar a laboral, fiscal, PI u otra área para análisis profundo.
- **Escalamiento a socio M&A** — El issue es de nivel ALTO y requiere decisión del socio a cargo.
- **Negociación del precio** — La contingencia cuantificada impacta en la valuación del target.

---

## Paso 4 — Construcción de la tabla

Producir la tabla en el siguiente formato:

| N° | Documento | Categoría | Observación | Riesgo | Cita | Acción requerida |
|---|---|---|---|---|---|---|
| 1 | [Nombre del documento] | [Categoría] | [Observación concisa: qué dice el documento, qué está bien o mal] | ALTO / MEDIO / BAJO / PENDIENTE | [Art. X LGS / LSC / CCyCN / norma aplicable] | [Acción] |
| 2 | | | | | | |
| ... | | | | | | |

**Reglas de formato de la tabla:**
- La observación debe ser de una a tres líneas máximo — concisa y directa.
- La cita normativa debe ser específica: "art. 234 LGS", no solo "LGS".
- Si el documento no fue recibido, la fila dice: `[PENDIENTE DE RECIBIR]` en la columna Documento y la cita indica qué norma exige ese documento.

---

## Paso 5 — Resumen estadístico

Al final de la tabla, incluir un bloque de resumen:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMEN DE LA REVISIÓN TABULAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total de documentos analizados:    [N]
Issues ALTO:                       [N] — [categorías afectadas]
Issues MEDIO:                      [N] — [categorías afectadas]
Issues BAJO:                       [N]
Documentos pendientes de recibir:  [N]

Categorías con mayor concentración de riesgo:
  1. [Categoría] — [N] issues ALTO/MEDIO
  2. [Categoría] — [N] issues ALTO/MEDIO

Acciones urgentes antes del cierre:
  - [Lista de acciones "Subsanar antes del cierre" de nivel ALTO]

Próximos pasos sugeridos:
  → Compartir tabla con el vendedor para que subsane los puntos indicados
  → Profundizar análisis en [categoría X] con el equipo especializado
  → Actualizar valuación si la contingencia fiscal/laboral se confirma
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 6 — Lista de documentos pendientes

Producir una lista separada de todos los documentos que no fueron recibidos o están incompletos, con:

| N° | Documento requerido | Categoría | Norma que lo exige | Urgencia | Destinatario del pedido |
|---|---|---|---|---|---|
| 1 | [Nombre] | [Categoría] | [Norma] | Alta / Media / Baja | [Vendedor / Asesores del vendedor / Autoridad] |

---

## Guardrails

- Nunca afirmar que el target "está en regla" o que "no hay contingencias" — usar "el análisis tabular preliminar no revela issues de nivel ALTO en las categorías revisadas".
- Si se recibe un índice de documentos sin los documentos mismos, indicar que el análisis es de índice y que las observaciones son provisorias hasta recibir los documentos.
- Para documentos en idioma extranjero, advertir que el análisis es preliminar y puede requerir validación por abogado en esa jurisdicción.
- Los issues de nivel ALTO deben siempre incluir la acción requerida y no pueden quedar en "ninguna".
- En deals con sociedad target argentina: verificar siempre si hay inscripción de modificaciones estatutarias en IGJ/DPPJ (arts. 5 y 7 LGS — la inscripción es constitutiva para las SA).
- En deals con sociedad target uruguaya: verificar vigencia en AIN y publicación en el Diario Oficial de los actos que lo requieren (art. 16 LSC).
- Si el deal involucra activos inmuebles: agregar fila de verificación de dominio y gravámenes en el Registro de la Propiedad.
