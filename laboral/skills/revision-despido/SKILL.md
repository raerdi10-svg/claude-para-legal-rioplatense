---
name: revision-despido
description: >
  Ejecuta una propuesta de despido contra los flags de riesgo jurisdiccional. Verifica
  causal, antigüedad, cálculo de indemnización (LCT art. 245 / Ley 16.906 UY), fueros
  especiales y riesgo de despido discriminatorio. Produce semáforo de riesgo, cálculo
  de liquidación final y lista de pasos previos obligatorios antes de notificar el despido.
argument-hint: "[nombre/datos del empleado, causal propuesta, antigüedad, remuneración] [--jurisdiccion=AR|UY]"
user-invocable: true
---

# Skill: Revisión de Despido

## Propósito

Asistir al abogado en la evaluación previa a un despido, identificando los riesgos legales,
calculando el pasivo estimado y estableciendo los pasos previos que deben cumplirse antes
de notificar la desvinculación. El output es un insumo de análisis para el profesional
actuante — no reemplaza el consejo legal ni la decisión final del cliente.

---

## Paso 0 — Recolección de datos

Solicitar la siguiente información antes de emitir cualquier análisis:

1. **Jurisdicción:** Argentina (LCT / jurisdicción provincial) o Uruguay (Ley 16.906 y CGT)
2. **Datos del empleado:**
   - Nombre (puede ser anónimo: "Empleado A")
   - Fecha de ingreso y fecha prevista de desvinculación
   - Categoría / convenio colectivo aplicable (si conoce)
   - Remuneración mensual bruta (y composición: básico, variables, beneficios remuneratorios)
3. **Causal propuesta:** ¿despido con causa (indicar cuál) o sin causa?
4. **Situación protegida:** ¿El empleado está o estuvo recientemente en alguna de estas situaciones?
   - Licencia por maternidad / paternidad / adopción
   - Enfermedad o accidente (art. 208 LCT o equivalente UY)
   - Delegado gremial / candidato / período de tutela sindical (Ley 23.551 AR / Ley 17.940 UY)
   - Participó en conflicto gremial, huelga o denuncia ante organismo laboral en los últimos 12 meses
   - Pertenece a grupo protegido (Ley 23.592 AR / Ley 17.817 UY)
5. **Documentación disponible:** legajo de sanciones, apercibimientos, sumarios previos, partes médicos

---

## Paso 1 — Verificación de la causal

### Argentina (LCT)

El despido con causa requiere (art. 242 LCT):
- Injuria suficientemente grave que impida la prosecución del vínculo
- La causal debe ser real, demostrable y proporcional
- No puede invocarse una causal distinta a la notificada (art. 243 LCT — invariabilidad)

**Checklist de causal:**

| Verificación | Resultado |
|---|---|
| ¿La conducta está documentada en el legajo? | SÍ / NO / PARCIAL |
| ¿Hubo sanciones previas progresivas (apercibimiento, suspensión)? | SÍ / NO |
| ¿El trabajador fue oído / pudo ejercer descargo? | SÍ / NO |
| ¿La conducta es contemporánea (no prescripta)? | SÍ / NO |
| ¿La causal es proporcional a la gravedad? | SÍ / NO |
| ¿Hay testigos o prueba objetiva disponible? | SÍ / NO |

Si alguna verificación resulta NO: alerta de riesgo de conversión a despido sin causa.

### Uruguay (Ley 16.906 y Derecho del Trabajo)

Uruguay no exige causal tipificada para el despido (es un sistema de despido libre con
indemnización). Sin embargo:
- La Ley 17.940 prohíbe el despido antisindical (nulidad del despido + reintegro o multa).
- La Ley 18.561 prohíbe el despido por acoso sexual (sanción agravada).
- El Ley 17.817 protege contra discriminación (acción de amparo + reparación integral).
- La Ley 19.196 (acoso laboral) puede fundar impugnación si hay denuncia previa.

---

## Paso 2 — Identificación de fueros especiales

### Fueros que impiden o condicionan el despido (Argentina)

| Fuero | Normativa | Duración | Consecuencia del despido |
|---|---|---|---|
| Maternidad | Art. 177-178 LCT | 7 meses y 1/2 antes y después del parto (presunción) | Nulidad + indemnización agravada (art. 182 LCT = 1 año de remuneraciones) |
| Matrimonio | Art. 180-181 LCT | 3 meses antes y 6 meses después | Presunción + indemnización agravada (art. 182 LCT) |
| Enfermedad / accidente | Art. 208 LCT | Plazos de reserva: 3/6/12 meses según antigüedad | Si despido durante licencia médica: salarios de enfermedad + indemnización ordinaria |
| Delegado gremial | Arts. 48-52 Ley 23.551 | Tutela sindical: durante el mandato + 1 año | Exclusión de tutela sindical ante autoridad laboral — sin exclusión el despido es nulo |
| Candidato gremial | Art. 50 Ley 23.551 | 6 meses desde postulación | Igual que delegado |
| Licencia gremial | Art. 48 Ley 23.551 | Durante el período de licencia | Nulidad + reincorporación |

### Fueros Uruguay

| Protección | Normativa | Consecuencia |
|---|---|---|
| Maternidad / paternidad | Ley 16.045, Ley 19.120 | Despido nulo durante licencia + 6 meses post-licencia |
| Tutela sindical | Ley 17.940, art. 1 | Reintegro forzoso + daños |
| Acoso sexual | Ley 18.561 | Agravante + sanción administrativa MTSS |

---

## Paso 3 — Cálculo de indemnización

### Argentina (LCT)

**Fórmula art. 245 LCT:**
```
Indemnización por antigüedad = Mejor remuneración mensual normal y habitual × Años de antigüedad
(con tope: 3 veces el promedio de las remuneraciones del CCT aplicable; mínimo: 1 mes)
```

**Liquidación final completa:**
| Rubro | Base de cálculo | Monto estimado |
|---|---|---|
| Indemnización por antigüedad (art. 245 LCT) | Mejor remuneración × años | [calcular] |
| Preaviso (art. 231-232 LCT) | 1 mes (< 5 años) / 2 meses (≥ 5 años) | [calcular] |
| Integración mes de despido (art. 233 LCT) | Días restantes del mes en curso | [calcular] |
| Vacaciones no gozadas (art. 156 LCT) | Proporcional al período trabajado | [calcular] |
| SAC proporcional (art. 122-123 LCT) | Mitad de lo devengado en el semestre | [calcular] |
| **TOTAL ESTIMADO** | | **[suma]** |

Nota: si hay suspensiones del contrato, verificar arts. 208-212 LCT para ajuste del cálculo.

**Si hay fuero y el despido igual procede (con exclusión):**
Agregar indemnización especial art. 182 LCT (maternidad/matrimonio) = 1 año de remuneraciones adicionales.

### Uruguay (Ley 16.906 y modificaciones)

**Indemnización por despido:**
```
Hasta 6 años: 1 mes de sueldo por año trabajado (o fracción > 6 meses)
De 6 a 10 años: 2 meses por año trabajado
Más de 10 años: 3 meses por año trabajado
Tope: 6 meses de salario
```

**Liquidación final Uruguay:**
| Rubro | Base | Monto estimado |
|---|---|---|
| Indemnización por despido (Ley 16.906) | Según escala | [calcular] |
| Salario vacacional (proporcional) | 20% sobre licencia devengada | [calcular] |
| Licencia proporcional | Días trabajados en el año | [calcular] |
| Aguinaldo proporcional | Semestre en curso | [calcular] |
| **TOTAL ESTIMADO** | | **[suma]** |

---

## Paso 4 — Semáforo de riesgo

```
SEMÁFORO DE RIESGO — DESPIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 ALTO — No proceder sin revisión inmediata del socio si:
   □ Existe fuero especial activo (maternidad, gremial, enfermedad con plazo vigente)
   □ El empleado realizó denuncia ante AFIP / MTSS / organismo laboral en últimos 12 meses
   □ La causal no está documentada o es inconsistente
   □ El empleado pertenece a grupo protegido (Ley 23.592 / Ley 17.817 UY)
   □ Indemnización estimada supera el umbral de escalamiento del estudio

🟡 MEDIO — Proceder con precaución adicional si:
   □ La causal existe pero la documentación es incompleta
   □ No hubo sanciones previas progresivas (primer incumplimiento directo)
   □ El empleado conoce información sensible o comercialmente estratégica
   □ Existe CCT aplicable con cláusulas de estabilidad o procedimientos especiales

🟢 BAJO — Riesgo ordinario (con cumplimiento de todos los pasos) si:
   □ Sin fuero especial
   □ Causal documentada (en caso de despido con causa) o despido sin causa ordinario
   □ Liquidación calculada y fondos disponibles
   □ Sin conflicto gremial previo o activo
```

---

## Paso 5 — Lista de pasos previos al despido

### Obligatorios (Argentina)

1. Verificar que no haya tutela sindical vigente — si hay, iniciar exclusión ante el MTSS antes de notificar.
2. Si hay causal: preparar telegrama colacionado con descripción concisa y completa (no modificable luego — art. 243 LCT).
3. Preparar liquidación final y chequear fondos disponibles para el pago.
4. Si el empleado está en período de enfermedad: esperar vencimiento de plazos del art. 208 LCT.
5. Contar con backup documental de la causal si se invoca (legajo, correos, partes, testigos).
6. Registrar la desvinculación en el sistema AFIP/ARCA en los plazos correspondientes.

### Obligatorios (Uruguay)

1. Verificar inexistencia de tutela sindical (MTSS) antes de cualquier acción.
2. Preparar comunicación de despido (puede ser verbal con carta o telegrama).
3. Calcular y tener disponible el pago de la indemnización — el retraso genera intereses.
4. Notificar al BPS dentro de los 10 días hábiles del egreso.
5. Entregar al trabajador la "constancia de trabajo" con datos del período.

---

## Guardrails

- Nunca afirmar que "el despido es válido" en forma absoluta — solo que cumple los requisitos formales al momento del análisis.
- Si se detecta fuero especial activo: detener el análisis de viabilidad y escalar inmediatamente al socio.
- En Argentina, la invariabilidad de la causal (art. 243 LCT) es fatal: una vez notificada, no puede cambiarse. Advertir siempre antes de redactar la comunicación.
- Si el monto estimado supera el umbral de escalamiento del estudio (ver CLAUDE.md), marcar con alerta y derivar.
- No calcular indemnizaciones en moneda extranjera sin aclarar la base de conversión utilizada y su fecha.
- Los CCT pueden establecer indemnizaciones agravadas o procedimientos previos distintos a la LCT — verificar siempre el convenio aplicable.
