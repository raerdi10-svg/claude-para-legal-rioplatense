---
name: clasificacion-trabajador
description: >
  Dado un engagement propuesto (persona física, tipo de servicio, forma de pago, exclusividad,
  duración), aplica el test de relación de dependencia (LCT art. 21 / jurisprudencia MTSS UY)
  y concluye: relación de dependencia vs. locación de servicios. En zona gris, lista factores
  de riesgo y medidas de mitigación para reducir la contingencia de registración laboral.
argument-hint: "[descripción del engagement: tipo de servicio, forma de pago, exclusividad, duración, modalidad]"
user-invocable: true
---

# Skill: Clasificación de Trabajador

## Propósito

Determinar si un engagement propuesto con una persona física configura una relación de
dependencia laboral o una locación de servicios / contrato de obra, a efectos de decidir
el régimen de registración (AFIP/ARCA / BPS) y las obligaciones previsionales del cliente.
El análisis aplica el test multifactorial de la jurisprudencia rioplatense.

---

## Paso 0 — Recolección de datos

Solicitar la siguiente información sobre el engagement propuesto:

1. **Jurisdicción:** Argentina / Uruguay / Ambas
2. **Tipo de servicio:** ¿Qué tarea realizará la persona? (ej. desarrollo de software, consultoría, servicios de limpieza, venta de productos, diseño gráfico, asesoramiento periódico)
3. **Duración:** ¿Es un proyecto puntual (con fecha de fin) o continuo / indefinido?
4. **Exclusividad:** ¿La persona puede prestar servicios similares a otras empresas mientras dure el engagement?
5. **Forma de pago:**
   - ¿Precio fijo por proyecto o por hora / jornada?
   - ¿Pago mensual fijo independientemente del resultado?
   - ¿Factura la persona (monotributo / responsable inscripto / empresa unipersonal)?
6. **Dirección del trabajo:**
   - ¿La empresa fija horarios, lugar de trabajo, metodología?
   - ¿Hay supervisor que controla día a día?
   - ¿La persona puede subcontratar o debe hacerlo personalmente?
7. **Medios de trabajo:** ¿Quién aporta las herramientas, equipos, software, insumos?
8. **Riesgo económico:** ¿La persona asume el riesgo del resultado (puede perder si el trabajo está mal)? ¿O simplemente cobra por su tiempo?
9. **Historial de la relación:** ¿Cuánto tiempo lleva esta modalidad? ¿Hubo alguna vez relación de dependencia con esta misma persona?

---

## Paso 1 — Test de relación de dependencia

Aplicar el test multifactorial. Cada factor se puntúa:
- **Apunta a dependencia** (D)
- **Apunta a independencia** (I)
- **Neutro / ambiguo** (N)

### Factores del test (LCT art. 21 / jurisprudencia CSJN y MTSS UY)

| # | Factor | Pregunta clave | Resultado |
|---|---|---|---|
| 1 | **Subordinación jurídica** | ¿La empresa tiene poder de dar instrucciones, sancionar o fijar horario? | D / I / N |
| 2 | **Subordinación técnica** | ¿La empresa controla el modo en que se ejecuta el trabajo (no solo el resultado)? | D / I / N |
| 3 | **Subordinación económica** | ¿La persona depende económicamente de este ingreso para subsistir? | D / I / N |
| 4 | **Exclusividad** | ¿No puede prestar servicios a otros? ¿En la práctica lo hace? | D / I / N |
| 5 | **Ajenidad del riesgo** | ¿La empresa asume el riesgo económico de la actividad; la persona solo pone trabajo? | D / I / N |
| 6 | **Continuidad** | ¿La relación es continua, no episódica ni por proyecto específico? | D / I / N |
| 7 | **Medios de trabajo** | ¿Los aporta la empresa (equipo, oficina, software)? | D / I / N |
| 8 | **Inserción en organización** | ¿La persona integra la estructura de la empresa (orgigrama, email, reuniones, uniforme)? | D / I / N |
| 9 | **Personalidad del servicio** | ¿Debe prestarlo personalmente, sin posibilidad de subcontratar? | D / I / N |
| 10 | **Forma de pago** | ¿Pago periódico fijo, independiente del resultado? | D / I / N |
| 11 | **Facturación** | ¿La persona no factura o factura pero como monotributista sin actividad real independiente? | D / I / N |
| 12 | **Denominación del acuerdo** | ¿El contrato dice "locación de servicios" o "monotributo" pero los hechos no lo confirman? | D / I / N |

**Nota sobre el factor 12 (denominación):** en Argentina, la jurisprudencia de la CSJN y la Cámara Nacional de Apelaciones del Trabajo aplica sistemáticamente el principio de primacía de la realidad (art. 14 LCT): el nombre del contrato no determina la relación; los hechos sí.

### Semáforo de resultado

```
Conteo de factores:

D (dependencia): ___
I (independencia): ___
N (neutro): ___

RESULTADO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Si D ≥ 8 de 12:
  → RELACIÓN DE DEPENDENCIA PROBABLE
  → Riesgo muy alto de registración obligatoria
  → Recomendación: registrar como empleado o rediseñar el engagement

Si D entre 5 y 7:
  → ZONA GRIS
  → Riesgo medio-alto; analizar mitigantes
  → Documentar independencia real; revisar forma de pago y autonomía

Si D ≤ 4 y I ≥ 6:
  → INDEPENDENCIA PROBABLE
  → Riesgo bajo; mantener factores de independencia documentados
  → No es inatacable: si la práctica cambia, el riesgo vuelve
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 2 — Consecuencias de una clasificación errónea

### Argentina

- **Registración retroactiva obligatoria** como empleado desde el primer día (art. 7 LCT: no puede pactarse un régimen diferente al legal).
- **Multas AFIP/ARCA** por trabajo no registrado (Ley 24.013 arts. 8, 9, 10 — indemnizaciones agravadas: 25% de la deuda previsional).
- **Indemnizaciones laborales** desde el inicio de la relación real, incluyendo preaviso, antigüedad, SAC, vacaciones.
- **Responsabilidad solidaria** de directores y gerentes (art. 59 LSC) en algunos precedentes.
- **Planilla de inspección de trabajo** de la AASTR o provincial: multa y exposición pública.

### Uruguay

- **Aportes al BPS** adeudados desde el inicio del vínculo, con recargos e intereses.
- **Multa del MTSS** por fraude laboral.
- **Indemnización por despido** calculada desde la fecha real de inicio de la relación.
- **Responsabilidad penal** del empleador en casos de reiteración o fraude doloso (art. 1 Ley 18.345 interpretado por el MTSS).

---

## Paso 3 — Mitigantes para zona gris

Si el resultado es zona gris, listar las medidas de mitigación disponibles:

| Mitigante | Descripción | Eficacia |
|---|---|---|
| Pluralidad de clientes | Documentar que la persona presta servicios a otros clientes simultáneamente | Alta |
| Autonomía en la ejecución | La empresa fija el resultado pero no el método; la persona decide cómo | Alta |
| Riesgo propio | La persona puede perder si entrega un trabajo deficiente (sin pago o con penalidad) | Alta |
| Facturación real | Emisión de facturas con detalle de servicios; no solo "honorarios mensuales" | Media |
| Medios propios | La persona trabaja con su propio equipo, conectividad, software | Media |
| Sin inserción en estructura | Sin email corporativo, sin inclusión en organigramas, sin uniformes | Media |
| Contrato de obra por resultado | Contrato con entregables específicos, no por tiempo de dedicación | Media |
| Posibilidad de subcontratación | Cláusula explícita de que puede delegar en terceros | Media-baja |
| Sin exclusividad | Cláusula contractual y práctica real de trabajo para múltiples clientes | Media |

**Mitigantes de bajo valor (no recomendados como única medida):**
- Solo el nombre del contrato ("locación de servicios") sin cambios reales
- Que la persona "acepte" ser independiente (la primacía de la realidad se impone)
- El monto de la factura (monotributista de categoría alta puede seguir siendo dependiente)

---

## Paso 4 — Output de clasificación

```
CLASIFICACIÓN DE TRABAJADOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Engagement evaluado: [descripción breve]
Jurisdicción: [AR / UY / Ambas]
Fecha de análisis: [DD/MM/AAAA]

RESULTADO: [RELACIÓN DE DEPENDENCIA PROBABLE / ZONA GRIS / INDEPENDENCIA PROBABLE]
Nivel de riesgo: [ALTO / MEDIO / BAJO]

FACTORES QUE APUNTAN A DEPENDENCIA:
- [listar]

FACTORES QUE APUNTAN A INDEPENDENCIA:
- [listar]

FACTORES NEUTROS O AMBIGUOS:
- [listar]

RECOMENDACIÓN:
[Una de las tres opciones:]
1. Registrar como empleado desde el inicio
2. Rediseñar el engagement con los mitigantes listados antes de iniciar
3. Proceder como locación de servicios con monitoreo periódico

MITIGANTES RECOMENDADOS (si aplica):
1. [mitigante 1]
2. [mitigante 2]
...

ADVERTENCIA FINAL
Este análisis es un insumo para el abogado actuante. La clasificación definitiva
depende de los hechos que se verifiquen durante la ejecución del contrato, no solo
de la documentación inicial. Una relación que comienza como locación de servicios puede
convertirse en relación de dependencia si los hechos cambian.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- El principio de primacía de la realidad (art. 14 LCT) prevalece sobre la denominación contractual — nunca afirmar que "como dice locación de servicios, está bien".
- En Argentina, la AFIP/ARCA puede verificar la relación en inspecciones de trabajo; los documentos internos del cliente (correos, chats, reportes) son prueba contra el empleador.
- En Uruguay, el MTSS tiene amplias facultades de inspección; la carga de la prueba de independencia recae en el empleador en caso de conflicto.
- Si el resultado es RELACIÓN DE DEPENDENCIA PROBABLE: no sugerir mitigantes cosméticos; recomendar registración inmediata y advertir sobre el pasivo retroactivo acumulado.
- Si el engagement ya está en curso por más de 3 meses con características de dependencia: calcular el pasivo estimado retroactivo y escalarlo según los umbrales del estudio (ver CLAUDE.md).
- No opinar sobre el diseño de estructuras que busquen evadir la registración laboral — solo asesorar en cumplimiento.
