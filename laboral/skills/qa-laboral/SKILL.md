---
name: qa-laboral
description: >
  Responde consultas laborales rápidas de abogados. Para cada consulta identifica
  jurisdicción, cita la norma aplicable (LCT, CCT, Ley 18.566, etc.), da la respuesta,
  señala zonas grises y jurisprudencia contradictoria. Siempre con disclaimer de que
  es material de referencia, no asesoramiento legal.
argument-hint: "[consulta laboral] [--jurisdiccion=AR|UY]"
user-invocable: true
---

# Skill: Q&A Laboral

## Propósito

Responder consultas laborales rápidas de abogados con citas normativas precisas,
estado de la jurisprudencia y alerta de zonas grises. Este skill es una herramienta
de referencia rápida — no reemplaza el análisis de cada caso concreto ni el consejo
legal del abogado actuante.

---

## Paso 0 — Procesamiento de la consulta

Al recibir una consulta, identificar automáticamente:

1. **Jurisdicción:** ¿La consulta indica Argentina, Uruguay, o es binacional? Si no lo indica, preguntar.
2. **Tema principal:** categorizar en uno de los siguientes:
   - Extinción del contrato (despido, renuncia, abandono, mutuo acuerdo)
   - Remuneración y liquidación (salario, SAC, horas extra, comisiones)
   - Fueros especiales y protecciones particulares
   - Período de prueba
   - Licencias (enfermedad, maternidad, paternidad, estudio, otras)
   - Jornada laboral y descansos
   - Clasificación del trabajador (dependencia vs. independencia)
   - Convenios colectivos (aplicabilidad, jerarquía normativa, interpretación)
   - Prescripción laboral
   - Sanciones disciplinarias
   - Accidentes de trabajo y enfermedades profesionales
   - Negociación colectiva y derecho sindical
   - Otro: [especificar]
3. **Urgencia:** ¿Hay un plazo inminente mencionado en la consulta?

---

## Paso 1 — Formato de respuesta estándar

Cada respuesta sigue esta estructura fija:

```
CONSULTA LABORAL — [TEMA] — [JURISDICCIÓN]
Fecha: [DD/MM/AAAA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NORMA APLICABLE
[Artículo(s) de la LCT / Ley 18.566 / CCT / etc. con texto relevante o cita exacta]

RESPUESTA
[Respuesta directa a la pregunta formulada]

ESTADO DE LA JURISPRUDENCIA
[Posición mayoritaria de la CNAT (AR) / tribunales laborales UY; si hay divergencia, indicarla]

ZONAS GRISES / PUNTOS DE ATENCIÓN
[Aspectos donde la norma no es clara, hay jurisprudencia contradictoria o la situación
concreta puede dar resultados distintos]

DISCLAIMER
Esta respuesta es material de referencia normativa y jurisprudencial. No constituye
asesoramiento legal sobre el caso concreto. El abogado actuante debe evaluar los
hechos específicos antes de aconsejar al cliente.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 2 — Base de referencia por tema frecuente

### Extinción del contrato — Argentina

| Modalidad | Normativa | Puntos clave |
|---|---|---|
| Despido sin causa | Art. 245 LCT | Indemnización = mejor remuneración mensual normal y habitual × años de antigüedad (mínimo 1 mes; tope CCT) |
| Despido con causa | Arts. 242-243 LCT | Injuria grave; invariabilidad de la causal notificada |
| Renuncia | Art. 240 LCT | Telegrama colacionado o ante escribano; sin indemnización de antigüedad |
| Mutuo acuerdo | Art. 241 LCT | Escritura pública o ante autoridad judicial o administrativa laboral; libre negociación del monto |
| Abandono | Art. 244 LCT | Previa intimación fehaciente a reincorporarse con plazo mínimo de 2 días hábiles |
| Por jubilación | Arts. 252-253 LCT | El empleador puede intimar al trabajador en condiciones de jubilarse; plazo de 1 año para la gestión |
| Despido discriminatorio | Ley 23.592 | Nulidad del despido + reincorporación o indemnización agravada (plenario CNAT "Pellicori"); carga probatoria dinámica |

**Prescripción (Argentina):** 2 años desde el hecho (art. 256 LCT); se suspende por intimación fehaciente (art. 257).

### Extinción del contrato — Uruguay

| Modalidad | Normativa | Puntos clave |
|---|---|---|
| Despido (sistema libre) | Ley 16.906 | El despido no requiere causa; la indemnización es obligatoria salvo renuncia, mutuo acuerdo o causa grave |
| Causa grave | Decreto 277/011 | Lista taxativa de causales graves (robo, violencia, etc.); sin indemnización |
| Renuncia | Código Civil + práctica laboral | Por escrito; sin indemnización; se liquidan salarios devengados, licencia y aguinaldo proporcional |
| Despido antisindical | Ley 17.940 | Nulidad + reintegro obligatorio o multa; tutela especial de 6 meses a 2 años |

**Prescripción (Uruguay):** 2 años para créditos laborales (art. 30 Ley 14.188); algunos rubros tienen plazos especiales.

### Remuneración y liquidación

**Argentina:**
- SAC (art. 121-123 LCT): 50% de la mayor remuneración del semestre. Se paga el 30/06 y el 18/12 (o al egreso, proporcional).
- Vacaciones (arts. 150-156 LCT): proporcional a la antigüedad (14 a 35 días hábiles); si el egreso es antes del 1° de enero, compensar en dinero.
- Horas extra (art. 201 LCT): 50% de recargo días hábiles; 100% sábados después de las 13hs, domingos y feriados.
- Tope salarial del art. 245: tres veces el promedio mensual de las remuneraciones del CCT aplicable al trabajador al momento del despido.

**Uruguay:**
- Licencia anual: 20 días hábiles (Ley 12.590 + tiempo de servicio).
- Salario vacacional: 20% del salario sobre los días de licencia (Ley 12.590 art. 11 y Ley 16.101).
- Aguinaldo: 50% del salario mensual, pagadero en junio y diciembre (Ley 12.840 y Ley 14.774).
- Horas extra: 100% de recargo en días ordinarios; 150% en días de descanso.

### Licencias especiales — Argentina

| Licencia | Duración | Normativa |
|---|---|---|
| Maternidad | 90 días (45 antes + 45 después; opcional 30+60 o 60+30) | Art. 177 LCT |
| Paternidad | 2 días hábiles (art. 158 LCT) — pueden ampliarse por CCT | Art. 158 LCT; muchos CCT amplían a 15 días |
| Matrimonio | 10 días corridos | Art. 158 LCT |
| Fallecimiento de familiar | 3 días hábiles (cónyuge / conviviente / hijo) · 1 día (hermano) | Art. 158 LCT |
| Examen de estudio | 2 días corridos por examen, máx. 10 al año | Art. 158 LCT |
| Enfermedad inculpable | Plazos art. 208: 3/6/12 meses según antigüedad y cargas de familia | Art. 208 LCT |

### Licencias especiales — Uruguay

| Licencia | Duración | Normativa |
|---|---|---|
| Maternidad | 14 semanas (6 antes + 8 después) | Ley 18.345 |
| Paternidad | 13 días corridos (en expansión por reforma 2023) | Ley 18.345 + Ley 19.752 |
| Matrimonio | 3 días hábiles | Ley 16.101 |
| Enfermedad | Cobertura por BPS desde el 4° día (primeros 3 a cargo del empleador) | Ley 14.407 |

### Jornada laboral

**Argentina:**
- Jornada máxima: 8 horas diarias / 48 semanales (Ley 11.544).
- Jornada nocturna (21hs a 6hs): 7 horas equivalen a 8 diurnas.
- Jornada insalubre: 6 horas diarias / 36 semanales.
- Descanso diario: mínimo 12 horas entre jornadas (art. 197 LCT).
- Descanso semanal: desde las 13hs del sábado hasta las 24hs del domingo (art. 204 LCT).

**Uruguay:**
- Jornada máxima: 8 horas diarias / 48 semanales (Ley 5.350).
- Comercio e industria: en algunos sectores, el CCT establece jornadas menores.
- Descanso semanal: mínimo 36 horas continuas.

### Prescripción laboral

| Jurisdicción | Plazo general | Normativa | Suspensión / interrupción |
|---|---|---|---|
| Argentina | 2 años | Art. 256 LCT | Art. 257 LCT: intimación fehaciente suspende por 6 meses; el plazo se reinicia |
| Uruguay | 2 años | Art. 30 Ley 14.188 | Por intimación o demanda judicial |

### Régimen disciplinario (Argentina)

- Sanciones: apercibimiento, suspensión (máx. 30 días por año, art. 220 LCT).
- El trabajador puede impugnar la sanción dentro de los 30 días (art. 67 LCT).
- Las sanciones deben ser proporcionales y progresivas — no puede despedirse directamente sin sanciones previas salvo injuria grave.
- El empleador no puede compensar suspensiones con salarios (art. 131 LCT).

---

## Paso 3 — Zonas grises frecuentes y jurisprudencia contradictoria

### Beneficios habituales y carácter remuneratorio (Argentina)

- **Posición mayoritaria CNAT:** los beneficios abonados en forma habitual y periódica (bonos, vales, tickets) se incorporan al salario aunque el contrato los llame "no remuneratorios" (arts. 103 y 58 LCT; fallo plenario CNAT "Aiello").
- **Zona gris:** el límite entre "habitual y periódico" y "ocasional" es fáctico y debe analizarse caso a caso.

### Tope indemnizatorio art. 245 LCT (Argentina)

- El tope se aplica al promedio de remuneraciones del CCT; si no hay CCT, la CNAT aplica el convenio más cercano por actividad o por analogía.
- **Conflicto histórico:** si el tope supera el salario real del trabajador, la jurisprudencia es dividida; algunos tribunales aplican el tope de todas formas; otros lo inaplican por inconstitucionalidad.

### Indemnización agravada por despido discriminatorio (Argentina)

- La Ley 23.592 no fija monto; la jurisprudencia oscila entre 1 año (fallo "Pellejero" CSJN) y hasta 3-6 meses adicionales más daño moral.
- El plenario CNAT "Pellicori" fijó carga probatoria dinámica: basta con que el trabajador acredite que pertenece a un grupo protegido y que el despido ocurrió en contexto discriminatorio; el empleador debe probar el motivo real.

### Reversibilidad del teletrabajo (Argentina)

- Art. 8 Ley 27.555: el trabajador que pasó de presencial a remoto puede pedir volver; el empleador no puede negarse salvo causa objetiva.
- **Zona gris:** si el trabajador fue contratado originalmente como teletrabajador (nunca fue presencial), algunos intérpretes discuten si puede exigir presencialidad; la mayoría considera que el derecho de reversibilidad aplica igualmente.

---

## Guardrails

- Nunca afirmar que una acción laboral "tiene éxito garantizado" ni que un argumento "va a prosperar" — la jurisprudencia laboral es dinámica y depende del tribunal.
- Si la consulta involucra un plazo de prescripción próximo a vencer: alertar con banner de urgencia y recomendar acción inmediata (intimación o presentación judicial).
- Si la consulta describe una situación donde el trabajador podría tener fuero especial: alertar antes de dar cualquier respuesta sobre viabilidad de despido.
- Las respuestas citan la norma general; el CCT aplicable puede modificar el resultado — siempre advertir esta posibilidad.
- Si la consulta no especifica jurisdicción y el tema tiene respuesta distinta en AR y UY: dar ambas respuestas claramente separadas.
- Este skill no es un buscador de jurisprudencia en tiempo real — las citas son a precedentes conocidos y doctrina consolidada. Para casos donde el precedente exacto sea crítico, recomendar verificación en bases de datos (El Dial, Microjuris, Sentencias del TCAT UY).
