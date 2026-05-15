---
name: revision-contratacion
description: >
  Revisa cartas oferta y contratos de trabajo e identifica cláusulas problemáticas: período
  de prueba, no competencia, confidencialidad, propiedad intelectual de creaciones del
  empleado, beneficios con posible carácter remuneratorio y jurisdicción aplicable. Produce
  tabla de cláusulas con nivel de riesgo, observación y texto sugerido de reemplazo.
argument-hint: "[pegar texto de la carta oferta o contrato] [--jurisdiccion=AR|UY]"
user-invocable: true
---

# Skill: Revisión de Contratación

## Propósito

Identificar en cartas oferta y contratos de trabajo las cláusulas que pueden generar
contingencias laborales, previsionales o de propiedad intelectual, antes de que el
documento sea firmado. El análisis sigue el playbook del estudio (CLAUDE.md) y la
normativa laboral de Argentina y Uruguay.

---

## Paso 0 — Recolección de datos

1. **Documento:** pegar el texto completo de la carta oferta o contrato (o adjuntar el archivo).
2. **Jurisdicción:** Argentina / Uruguay / Ambas (para empleados con base en los dos países).
3. **Posición del cliente:** ¿El estudio representa al empleador o al empleado?
4. **Categoría del trabajador:** ¿Jerárquico / ejecutivo (Directors, VP, C-suite) o posición general?
5. **Industria / CCT aplicable:** si se conoce.
6. **¿Hay template propio del estudio para comparar?** (si hay documento semilla en CLAUDE.md, tomarlo como referencia).

---

## Paso 1 — Mapa de cláusulas

Identificar y listar todas las cláusulas presentes en el documento, agrupadas por categoría:

| Categoría | Cláusula identificada | Presente (SÍ/NO) |
|---|---|---|
| Período de prueba | | |
| Remuneración y beneficios | | |
| Jornada y horario | | |
| No competencia post-contractual | | |
| Confidencialidad | | |
| Propiedad intelectual de creaciones | | |
| Resolución de conflictos / jurisdicción | | |
| Rescisión anticipada / penalidad | | |
| Capacitación con devolución | | |
| Cláusula de retorno de beneficios ("clawback") | | |
| Ley aplicable | | |

---

## Paso 2 — Análisis cláusula a cláusula

### 2.1 Período de prueba

**Argentina (art. 92 bis LCT):**
- Duración máxima: 3 meses (prorrogable a 6 por CCT).
- El empleador puede rescindir sin indemnización de antigüedad, pero debe pagar preaviso de 15 días.
- El trabajador DEBE estar registrado en AFIP/ARCA desde el primer día.
- Alerta ALTO: cláusulas que fijan períodos de prueba superiores a 3 meses (o 6 con CCT) son nulas — se aplica la LCT.

**Uruguay:**
- No existe período de prueba legal; cualquier plazo convenido es opcional y debe ser explícito.
- Si se establece, verificar que no se use como mecanismo para eludir el pago de indemnización.

### 2.2 Remuneración y beneficios

Identificar todos los rubros de pago y clasificarlos:

| Rubro | ¿Remuneratorio? | Observación |
|---|---|---|
| Sueldo básico | SÍ | Base para cálculo de SAC, vacaciones e indemnización |
| Comisiones / variables | SÍ (en general) | Art. 103 LCT — todo pago por causa del trabajo es remuneratorio |
| Viáticos sin rendición | SÍ | Art. 106 LCT — sin rendición de cuentas = remuneración |
| Viáticos con rendición documentada | NO | Art. 106 LCT — con comprobantes = no remuneratorio |
| Cobertura médica | NO | Beneficio en especie sin carácter remuneratorio |
| Celular / laptop corporativa | NO | Herramientas de trabajo |
| Vehículo de uso exclusivo personal | Puede ser | Verificar si hay beneficio adicional al uso laboral |
| Préstamos o adelantos | NO | Crédito — no salario |
| Bonos discrecionales | GRIS | Si son habituales y regulares: riesgo de incorporación (art. 58 LCT) |

**Alerta:** bonos que se pagan en forma habitual y periódica pueden convertirse en parte del salario
habitual aunque el contrato los llame "discrecionales" (art. 58 LCT — renuncia tácita por conducta).

**Uruguay:** mismos principios con base en el Código General del Proceso y jurisprudencia del MTSS.

### 2.3 No competencia post-contractual

**Argentina:**
- La LCT no regula expresamente el pacto de no competencia post-contractual.
- Jurisprudencia mayoritaria: válido si tiene: (a) plazo razonable (máx. 2 años), (b) área geográfica limitada, (c) compensación económica adecuada.
- Sin compensación económica: alta probabilidad de invalidez judicial.
- Alerta ALTO: cláusula de no competencia sin plazo, sin límite geográfico, o sin contraprestación.

**Uruguay:**
- Mismo criterio jurisprudencial: requiere causa justa (protección de interés legítimo), plazo limitado y compensación.
- Verificar si el CCT aplicable incluye disposiciones sobre no competencia.

**Texto sugerido AR (con compensación):**
```
"El/la trabajador/a se compromete a no ejercer actividades competitivas directas con
[EMPRESA] en [TERRITORIO] durante [PLAZO, máx. 24 meses] contados desde la fecha
de egreso, por cualquier causa. En compensación, [EMPRESA] abonará una suma equivalente
a [PORCENTAJE]% del salario mensual bruto del trabajador por cada mes de vigencia
de la restricción. Esta obligación queda sin efecto si el contrato es rescindido por
voluntad unilateral del empleador sin causa justificada."
```

### 2.4 Confidencialidad

Verificar:
- ¿La definición de "información confidencial" es razonable o abarca "todo" sin exclusiones?
- ¿Incluye exclusiones estándar (dominio público, conocimiento previo, fuente independiente, exigencia legal)?
- ¿El plazo de vigencia es razonable (máximo 3-5 años post-egreso según industria)?
- ¿La cláusula cubre datos personales de terceros? → Verificar cumplimiento Ley 25.326 AR / Ley 18.331 UY.
- ¿Incluye obligación de devolución / destrucción de soportes?

### 2.5 Propiedad intelectual de creaciones del empleado

**Argentina (Ley 11.723):**
- Art. 4 y 55: las obras creadas por el empleado en el marco de la relación laboral y en cumplimiento de sus funciones pertenecen al empleador.
- Si el empleado crea algo fuera de su función habitual, la titularidad puede ser disputada.
- Verificar: ¿la cláusula extiende la cesión de PI a creaciones fuera del horario y función laboral? → Alerta ALTO.

**Uruguay (Ley 9.739 y Ley 17.164):**
- Régimen similar al argentino para obras en relación de dependencia.
- En programas de computación: Ley 17.164 regula patentes; la PI del software se trata como obra literaria.

**Texto sugerido:**
```
"Todas las obras, invenciones, desarrollos, mejoras, software y demás creaciones intelectuales
que el/la trabajador/a realice en el marco de sus funciones laborales, utilizando recursos de
la empresa o en relación directa con su actividad, serán de titularidad exclusiva de [EMPRESA].
Esta cesión no alcanza las creaciones realizadas fuera del horario laboral, con recursos propios
y sin relación con las funciones asignadas, salvo expreso acuerdo por escrito."
```

### 2.6 Jurisdicción y ley aplicable

- Verificar que la jurisdicción pactada no desplace el fuero laboral de orden público.
- Argentina: los jueces laborales tienen competencia de orden público — no puede renunciarse al fuero laboral del domicilio del trabajador.
- Uruguay: ídem; la Ley 18.566 establece normas imperativas de orden público.
- Alerta ALTO: cláusulas que someten el contrato a jurisdicción extranjera para conflictos laborales.

### 2.7 Cláusula de retorno de beneficios y capacitación

- Las cláusulas de devolución proporcional de costos de capacitación son válidas si: (a) el costo fue real y documentado, (b) el plazo de restitución es proporcional, (c) no excede el costo real.
- Argentina: no pueden deducirse del salario (art. 131 LCT — prohibición de descuentos unilaterales); deben canalizarse por separado.
- Alerta MEDIO: cláusulas de clawback sobre bonos sin definición precisa del hecho que activa la restitución.

---

## Paso 3 — Output: tabla consolidada de hallazgos

```
REVISIÓN DE CONTRATACIÓN — [POSICIÓN / EMPLEADO] — [FECHA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESUMEN EJECUTIVO
[Máximo 3 líneas: si el documento es apto para firmar, qué cambios son críticos antes de firmar,
y cuál es el nivel de riesgo global.]

TABLA DE CLÁUSULAS
┌─────────────────────┬────────┬──────────────────────────┬────────────────────────────┐
│ Cláusula            │ Nivel  │ Observación              │ Recomendación              │
├─────────────────────┼────────┼──────────────────────────┼────────────────────────────┤
│ No competencia      │ ALTO   │ Sin plazo ni compensación│ Incorporar plazo y pago     │
│ PI de creaciones    │ MEDIO  │ Alcance excesivo fuera   │ Acotar a funciones laborales│
│                     │        │ de horario laboral       │                            │
│ Período de prueba   │ BAJO   │ 3 meses — conforme LCT  │ Sin cambios                 │
└─────────────────────┴────────┴──────────────────────────┴────────────────────────────┘

CLÁUSULAS SUGERIDAS DE REEMPLAZO
[Texto completo de cada cláusula propuesta, listo para copiar y pegar]

COMPUERTA DE APROBACIÓN
□ Abogado matriculado revisó el análisis y las cláusulas sugeridas
□ El cliente (empleador o empleado) fue informado de los riesgos identificados
□ Las cláusulas sugeridas fueron aceptadas o modificadas por el cliente
□ Si hay CCT aplicable: verificar que las cláusulas del contrato no estén por debajo del piso convencional
□ Versión final del contrato revisada antes de la firma
```

---

## Guardrails

- Nunca afirmar que una cláusula "es válida" o "es inválida" en forma absoluta; indicar el riesgo y la posición jurisprudencial mayoritaria.
- Los pisos mínimos de la LCT y de la Ley 18.566 UY son irrenunciables: una cláusula contractual que esté por debajo de esos mínimos es nula de pleno derecho aunque el trabajador la haya firmado (art. 12 LCT / art. 1 Ley 18.566).
- Si el cliente es el empleado y el análisis detecta cláusulas abusivas de alto impacto, alertar que puede no tener poder de negociación real pero que la cláusula puede ser inaplicable igualmente.
- Si se mencionan datos de remuneración, tratar esa información como confidencial y no incluirla en outputs destinados a terceros.
- Los CCT establecen pisos que el contrato individual no puede reducir (art. 8 LCT / Ley 14.250); verificar el convenio antes de concluir que una cláusula está "en orden".
