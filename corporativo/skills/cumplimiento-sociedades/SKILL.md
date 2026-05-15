---
name: cumplimiento-sociedades
description: >
  Tracker de obligaciones societarias anuales para sociedades en Argentina
  (LGS Ley 19.550, IGJ) y Uruguay (LSC Ley 16.060, AIN). Lista todas las
  obligaciones con fechas límite: presentación de balances, actualización
  de autoridades, declaraciones juradas, renovaciones y publicaciones.
  Alerta las obligaciones que vencen en los próximos 60 días.
argument-hint: "[tipo de sociedad] [jurisdicción AR/UY] [fecha de cierre de ejercicio]"
user-invocable: true
---

# Skill: Tracker de Cumplimiento Societario

## Propósito

Generar el calendario completo de obligaciones societarias de una sociedad determinada, con fechas límite calculadas a partir de la fecha de cierre de ejercicio y la fecha de constitución, e identificar las que vencen en los próximos 60 días para actuar antes del vencimiento. Es una herramienta de gestión preventiva que evita sanciones de IGJ/AIN, caducidad de inscripciones y responsabilidad personal de directores por incumplimientos formales.

---

## Paso 0 — Lectura del perfil

Leer `CLAUDE.md` del plugin para incorporar jurisdicción, tipo de sociedad habitual y estilo de outputs. Verificar la fecha actual del sistema para calcular correctamente los plazos.

---

## Paso 1 — Recolección de datos

Solicitar al usuario:

1. **Denominación social y tipo:** SA / SRL / SAS (AR) / SA / SRL (UY) / sucursal de extranjera.
2. **Jurisdicción de registro:** CABA (IGJ) / Provincia de Buenos Aires (DPPJ) / otra provincia / Uruguay (AIN).
3. **Fecha de cierre del ejercicio económico:** ej. 31/12, 30/06, 31/03.
4. **Año del ejercicio a considerar:** para calcular cuándo vencen las obligaciones del ejercicio en curso y del próximo.
5. **Fecha de vencimiento del mandato de las autoridades** (directores, síndicos): ¿cuándo vence el último nombramiento inscripto?
6. **¿La sociedad cotiza en bolsa?** (CNV / BCU) — hay obligaciones adicionales de disclosure.
7. **¿La sociedad opera en algún sector regulado?** (financiero, salud, energía, telecomunicaciones) — obligaciones adicionales ante el regulador.
8. **¿Hay filiales o sucursales en otras jurisdicciones?** — para incluir sus obligaciones también.

---

## Paso 2 — Generación del calendario

### ARGENTINA — SA (Ley 19.550 + Res. IGJ 7/2015 y modificatorias)

#### Obligaciones anuales post-cierre de ejercicio:

| Obligación | Plazo desde el cierre de ejercicio | Norma | Consecuencia del incumplimiento |
|---|---|---|---|
| Celebrar asamblea ordinaria de aprobación de estados contables | Dentro de los 4 meses del cierre (art. 234 inc. 1° LGS) | Art. 234 y 243 LGS | Incumplimiento de directorio; posible sanción IGJ |
| Presentar estados contables ante IGJ (CABA) | Dentro de los 15 días de aprobados por la asamblea | Res. IGJ 7/2015 art. 281 | Multa; mora del depósito |
| Publicar en el Boletín Oficial el acta de asamblea (si corresponde) | Dentro de los 15 días de la asamblea | Art. 10 LGS | Actos inoponibles a terceros |
| Integrar reserva legal (5 % de las ganancias hasta el 20 % del capital) | Resolverse en la asamblea de aprobación de estados contables | Art. 70 LGS | Distribución de dividendos inválida |
| Presentar informe del síndico (si la sociedad tiene sindicatura obligatoria) | Junto con los estados contables | Arts. 294-295 LGS | Incumplimiento del síndico |
| Presentar memoria del directorio | Junto con los estados contables | Art. 66 LGS | Incumplimiento del directorio |

#### Obligaciones por vencimiento de mandatos:

| Obligación | Plazo | Norma | Consecuencia |
|---|---|---|---|
| Renovar mandato de directores (plazo máximo 3 ejercicios, salvo estatuto) | Antes del vencimiento del mandato; resolver en asamblea ordinaria | Art. 257 LGS | Director actúa sin mandato vigente — actos ineficaces |
| Renovar mandato del síndico (plazo máximo 3 ejercicios) | Antes del vencimiento | Art. 284 LGS | Sindicatura irregular |
| Inscribir en IGJ los nuevos nombramientos | Dentro de los 15 días de la asamblea | Art. 12 LGS + Res. IGJ | Inoponibilidad a terceros del nombramiento |
| Publicar en Boletín Oficial el nombramiento | Al momento de la inscripción o simultáneamente | Art. 10 LGS | Inoponibilidad |

#### Obligaciones permanentes (no ligadas al ejercicio):

| Obligación | Periodicidad | Norma | Consecuencia |
|---|---|---|---|
| Mantener libros societarios rubricados y actualizados (actas de directorio y asamblea, registro de acciones) | Continua | Art. 61-63 LGS | Multa IGJ; valor probatorio comprometido |
| Declarar el beneficiario final (UBO) ante la UIF | Anualmente o ante cambios | Res. UIF 53/2019 y modificatorias | Sanciones Ley 25.246 |
| Presentar declaración jurada de accionistas ante IGJ (para SA con participación extranjera) | Según resolución IGJ vigente | Res. IGJ | Restricción para inscribir actos |
| Inscribir modificaciones estatutarias | Dentro de los 15 días del acto que las genera | Art. 12 LGS | Inoponibilidad del acto modificatorio |
| Renovar inscripciones de sucursales de extranjeras (art. 118 LGS) | Cada 5 años ante IGJ | Res. IGJ | Caducidad de la inscripción |
| Conservar documentación contable | 10 años desde el cierre del ejercicio (art. 328 CCyCN) | Art. 328 CCyCN | Responsabilidad en procedimientos de verificación |

---

### ARGENTINA — SRL (Ley 19.550)

Las SRL tienen obligaciones similares a las SA, con las siguientes particularidades:

| Diferencia | SRL | SA |
|---|---|---|
| Órgano de gobierno | Reunión de socios (art. 159 LGS) — puede ser escrita y sin reunión presencial | Asamblea (art. 233 LGS) — con formalidades de convocatoria |
| Sindicatura | Optativa, salvo capital > $ [umbral actualizable por IGJ] | Obligatoria en SA cerradas que superen el capital mínimo; siempre en SA cotizantes |
| Plazo para aprobación de estados contables | 4 meses del cierre de ejercicio | 4 meses del cierre de ejercicio |
| Inscripción de cambio de socios (cesión de cuotas) | Inscripción en IGJ dentro de los 15 días; publicación en BO | Registro de acciones (sin inscripción registral para acciones nominativas escriturales) |
| Designación de gerentes | En el estatuto o por reunión de socios | Directorio elegido por asamblea |

---

### URUGUAY — SA (Ley 16.060 + Decreto 335/990)

#### Obligaciones anuales post-cierre de ejercicio:

| Obligación | Plazo | Norma | Consecuencia |
|---|---|---|---|
| Celebrar asamblea ordinaria para aprobar estados contables | Dentro de los 4 meses del cierre (art. 337 LSC) | Art. 337 LSC | Incumplimiento del directorio |
| Presentar estados contables ante AIN | Dentro de los 30 días de la aprobación asamblearia | Decreto 335/990 art. 88 | Multa AIN; observación registral |
| Publicar extracto del balance en el Diario Oficial (si la sociedad está obligada) | Dentro de los 30 días de aprobados | Art. 91 Decreto 335/990 | Sanción y publicidad inoponible |
| Integrar reserva legal (5 % de las ganancias del ejercicio hasta el 20 % del capital) | En la distribución de dividendos | Art. 93 LSC | Distribución inválida |

#### Obligaciones por vencimiento de mandatos:

| Obligación | Plazo | Norma | Consecuencia |
|---|---|---|---|
| Renovar directores (plazo de 2 ejercicios salvo estatuto — art. 392 LSC) | Antes del vencimiento; asamblea ordinaria | Art. 392 LSC | Director sin mandato actúa irregularmente |
| Renovar síndico (art. 394 LSC) | Junto con la renovación del directorio | Art. 394 LSC | Sindicatura irregular |
| Inscribir nombramiento en AIN y Registro Nacional de Comercio | Dentro de los 30 días de la asamblea | Art. 16 LSC | Inoponibilidad a terceros |
| Publicar en el Diario Oficial | Simultáneamente con la inscripción | Art. 16 LSC | Inoponibilidad |

#### Obligaciones permanentes:

| Obligación | Periodicidad | Norma | Consecuencia |
|---|---|---|---|
| Declarar beneficiario final ante la Secretaría Antilavado / sujetos obligados | Anualmente o ante cambios | Ley 19.484 y Decreto 166/017 | Sanciones SENACLAFT |
| Mantener registro de accionistas actualizado | Continua | Art. 305 LSC | Litigios de titularidad |
| Conservar libros societarios y contables | 10 años | Art. 71 Código de Comercio UY | Responsabilidad en procedimientos |
| Renovar habilitación de funcionamiento municipal | Anualmente (varía por departamento) | Normativa municipal | Multa / clausura |

---

## Paso 3 — Alerta de vencimientos próximos (60 días)

Con la fecha actual del sistema y las fechas de cierre de ejercicio y mandatos indicadas por el usuario, calcular las obligaciones que vencen en los próximos 60 días:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  ALERTAS — VENCIMIENTOS EN LOS PRÓXIMOS 60 DÍAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fecha de hoy: [DD/MM/AAAA]
Ventana de alerta: hasta el [DD/MM/AAAA]

[Para cada obligación que vence en esa ventana:]

🔴 URGENTE — [N] días
  Obligación:   [Nombre de la obligación]
  Vencimiento:  [DD/MM/AAAA]
  Norma:        [Art. X LGS/LSC]
  Acción:       [Qué debe hacerse]
  Responsable:  [Directorio / Síndico / Abogado actuante / Contador]

🟡 PRÓXIMO — entre 30 y 60 días
  [Mismo formato]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 4 — Calendario anual completo

Producir el calendario en formato tabla para el año en curso y el siguiente:

| Mes | Obligación | Plazo exacto | Norma | Estado | Responsable |
|---|---|---|---|---|---|
| [MES] | [Obligación] | [DD/MM/AAAA] | [Norma] | Pendiente / Cumplida / Atrasada | [Directorio / Síndico / Externo] |
| ... | | | | | |

Ordenar cronológicamente. Marcar con "⚠️ VENCE EN 60 DÍAS" las que entran en la ventana de alerta.

---

## Paso 5 — Checklist de estado actual

Al cierre del informe, incluir un checklist de estado para que el abogado actuante lo revise con el cliente:

```
CHECKLIST DE ESTADO SOCIETARIO — [DENOMINACIÓN SOCIAL]
Fecha de revisión: [DD/MM/AAAA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GOBIERNO Y REGISTROS
□ Directores con mandato vigente (vence: [DD/MM/AAAA])
□ Síndico con mandato vigente (vence: [DD/MM/AAAA])
□ Estatuto actualizado e inscripto
□ Libros de actas al día (último acta asentada: [DD/MM/AAAA])
□ Libro de registro de acciones / socios actualizado

CONTABLE Y REGISTRAL
□ Ejercicio [AAAA] cerrado al [DD/MM/AAAA]
□ Estados contables aprobados por asamblea: [Sí / No / Pendiente]
□ Estados contables presentados ante IGJ/AIN: [Sí / No / Pendiente]
□ Reserva legal integrada correctamente: [Sí / No]
□ Publicaciones en BO/Diario Oficial al día: [Sí / No]

CUMPLIMIENTO REGULATORIO
□ Declaración de beneficiario final presentada: [Sí / No / Pendiente — vence DD/MM/AAAA]
□ Habilitaciones de funcionamiento vigentes: [Sí / No]
□ Obligaciones sectoriales al día (si aplica): [Sí / No / N/A]
□ Obligaciones ante AFIP/DGI al día: [Sí / No]
□ Obligaciones ante ANSES/BPS al día: [Sí / No]

OBSERVACIONES DEL ABOGADO ACTUANTE:
[Espacio para notas]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Los plazos calculados deben basarse en la fecha actual del sistema — si no se tiene acceso a ella, usar la fecha indicada en el encabezado de `CLAUDE.md` (`currentDate`).
- En Argentina, la Resolución IGJ vigente puede haber modificado plazos y procedimientos de presentación — advertir que el usuario verifique la resolución actualizada en el sitio oficial de IGJ antes de la presentación.
- En Uruguay, el Decreto 335/990 ha sido modificado varias veces — recomendar verificación ante AIN de los plazos vigentes para la presentación de estados contables.
- Si el mandato de los directores ya venció, marcar el item como "ATRASADO" y advertir que los actos que estos directores firmen pueden ser cuestionados hasta que el nombramiento sea renovado e inscripto.
- Para SA argentinas con capital mayor al umbral que exige sindicatura obligatoria (verificar monto actualizable por IGJ): alertar si no hay síndico designado.
- Nunca afirmar que la sociedad "está en regla" — usar "el análisis preliminar no detecta incumplimientos en las obligaciones relevadas"; aclarar que el estado definitivo requiere consulta directa con el registro (IGJ/AIN) y con el contador de la sociedad.
- Si el usuario indica que la sociedad tiene filiales o sucursales en otras jurisdicciones, recordar que cada jurisdicción tiene sus propios plazos y organismos de registro.
