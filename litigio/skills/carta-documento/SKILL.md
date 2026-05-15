---
name: carta-documento
description: >
  Redacta una carta documento (Correo Argentino) o telegrama colacionado (Uruguay) con
  todos los datos formales requeridos. Recopila remitente, destinatario, domicilio, hechos,
  pretensión (pago / cese / cumplimiento / resolución), plazo y advertencia de acción
  judicial. Incluye cálculo del plazo de prescripción, urgencia y checklist de envío.
argument-hint: "[descripción de la situación: partes, hechos, pretensión] [--jurisdiccion=AR|UY]"
user-invocable: true
---

# Skill: Carta Documento

## Propósito

Redactar el texto de una carta documento (Argentina) o telegrama colacionado (Uruguay)
en formato listo para envío. La carta documento es el medio fehaciente más común para
constituir en mora, intimar al cumplimiento, resolver contratos, interrumpir prescripciones
y documentar reclamos extrajudiciales. Un error formal o de contenido puede invalidarla
o reducir su eficacia probatoria.

---

## Paso 0 — Recolección de datos

1. **Jurisdicción:** Argentina / Uruguay
2. **Remitente:**
   - Nombre completo (persona física) o razón social (persona jurídica)
   - DNI / CUIT / CUIL (AR) o Cédula de Identidad / RUT (UY)
   - Domicilio real o sede social completo (calle, número, piso, localidad, provincia / departamento)
3. **Destinatario:**
   - Nombre completo o razón social
   - DNI / CUIT / CUIL (AR) o Cédula / RUT (UY) — si se conoce
   - Domicilio al que se enviará (calle, número, piso, localidad)
   - Si hay domicilio especial pactado en el contrato: indicarlo
4. **Hechos que motivan la carta:** descripción cronológica y objetiva (incumplimiento, daño, deuda, conducta)
5. **Pretensión exacta:** ¿Qué se reclama o exige?
   - Pago de suma de dinero (indicar monto, moneda y concepto)
   - Cese de una conducta o actividad
   - Cumplimiento de una obligación de hacer
   - Resolución / rescisión del contrato
   - Restitución de bienes
   - Otro: [especificar]
6. **Plazo para cumplir:** ¿Cuántos días hábiles / corridos se otorgan para cumplir? (si la ley fija plazo mínimo, indicarlo)
7. **Advertencia:** ¿Se advierte con iniciar acciones judiciales? ¿Con qué tipo? (ordinarias, ejecutivas, cautelares)
8. **¿El remitente actúa en representación?** Si es apoderado, adjuntar datos del mandante.
9. **¿Hay contratos o documentos que respalden el reclamo?** (para citar en la carta)
10. **Urgencia:** ¿La prescripción está próxima a vencer? ¿Hay urgencia por otro motivo?

---

## Paso 1 — Verificación del plazo de prescripción

Antes de redactar, calcular si el crédito o acción está próxima a prescribir:

### Argentina (CCyCN)

| Tipo de acción | Plazo | Normativa | Hito de inicio |
|---|---|---|---|
| Ordinaria (general) | 5 años | Art. 2560 CCyCN | Desde que el crédito es exigible |
| Responsabilidad civil extracontractual | 3 años | Art. 2561 CCyCN | Desde el daño o su conocimiento |
| Mala praxis profesional | 3 años | Art. 2561 CCyCN | Desde el hecho dañoso |
| Acciones posesorias | 1 año | Art. 2564 CCyCN | Desde el acto turbatorio |
| Acciones ejecutivas (pagaré, cheque) | 3 años | Dec.-Ley 5965/63 y Ley 24.452 | Desde el vencimiento |
| Locaciones (cobro de alquileres) | 3 años | Art. 2561 CCyCN | Desde el vencimiento de cada período |
| Laboral | 2 años | Art. 256 LCT | Desde el crédito exigible |
| Nulidad relativa | 2 años | Art. 2562 CCyCN | Desde que el vicio fue conocible |

**Efectos de la carta documento (AR):**
- La intimación fehaciente suspende el plazo de prescripción por 6 meses (art. 2541 CCyCN).
- La presentación en mediación obligatoria suspende el plazo hasta 60 días después de que concluya (art. 18 Ley 26.589).

### Uruguay (Código Civil)

| Tipo de acción | Plazo | Normativa | Hito de inicio |
|---|---|---|---|
| Ordinaria (general) | 20 años | Art. 1216 CC UY | Desde el nacimiento del crédito |
| Responsabilidad extracontractual | 4 años | Art. 1332 CC UY | Desde el acto ilícito o su conocimiento |
| Laboral | 2 años | Art. 30 Ley 14.188 | Desde el crédito exigible |
| Acción de cobro de honorarios profesionales | 4 años | Art. 1217 CC UY | Desde la prestación del servicio |
| Acciones ejecutivas (letra de cambio) | 3 años | Ley 14.701 | Desde el vencimiento |

**Efectos del telegrama colacionado (UY):**
- Interrumpe la prescripción si constituye una reclamación extrajudicial fehaciente (art. 1234 CC UY).
- La interrupción hace correr el plazo de nuevo desde cero.

**Alerta:** si quedan menos de 60 días para la prescripción, marcar con banner de urgencia y recomendar presentación judicial en paralelo.

---

## Paso 2 — Redacción de la carta documento

### Argentina — Carta Documento (Correo Argentino)

```
CARTA DOCUMENTO
[Ciudad], [DD] de [mes] de [AAAA]

Señor/a [NOMBRE COMPLETO DEL DESTINATARIO]
DNI / CUIT [XXXXXXXXXX]
[Domicilio completo del destinatario]

El/La que suscribe, [NOMBRE COMPLETO DEL REMITENTE], DNI / CUIT [XXXXXXXXXX],
con domicilio en [DOMICILIO COMPLETO DEL REMITENTE], por medio de la presente
me dirijo a Ud. a fin de:

I. HECHOS

[Descripción objetiva y cronológica de los hechos que dan origen al reclamo.
Incluir fechas, documentos de respaldo, obligaciones incumplidas. Ser preciso
pero no prolijo — la carta documento no es un escrito judicial.]

Ejemplo:
"Con fecha [DD/MM/AAAA], las partes suscribieron el contrato de [tipo] identificado
como [N° o denominación], por el cual Ud. se comprometió a [obligación]. A la fecha
de la presente, Ud. ha incumplido dicha obligación, dado que [descripción del
incumplimiento]."

II. PRETENSIÓN E INTIMACIÓN

Por las razones expuestas, y en virtud de lo dispuesto por [norma aplicable:
arts. 1078-1079 CCyCN para resolución / art. 886 CCyCN para constitución en mora /
etc.], por medio de la presente lo/la intimo a Ud. a [describir exactamente
lo que se reclama: pagar la suma de $ [MONTO] / USD [MONTO] en concepto de [concepto];
cesar en [conducta]; cumplir con [obligación específica]; etc.], dentro del plazo
de [N] días hábiles / corridos contados desde la recepción de la presente.

III. APERCIBIMIENTO

Vencido dicho plazo sin que Ud. haya dado cumplimiento a lo solicitado, me reservo
el derecho de iniciar las acciones judiciales que correspondan, incluyendo [acciones
ordinarias / ejecutivas / cautelares], con más los intereses, costas y costos que
correspondan, siendo Ud. el único responsable de las consecuencias que de ello deriven.

IV. CONSTITUCIÓN EN MORA / INTERRUPCIÓN DE PRESCRIPCIÓN

La presente carta documento tiene además por objeto constituir a Ud. en mora de pleno
derecho y suspender el curso de la prescripción de la acción, conforme los arts. 886
y 2541 del Código Civil y Comercial de la Nación.

Sin otro particular, saludo a Ud. atentamente.

[FIRMA DEL REMITENTE]
[Nombre completo]
[DNI / CUIT]
[Domicilio]
```

### Uruguay — Telegrama Colacionado

```
TELEGRAMA COLACIONADO
[Ciudad], [DD] de [mes] de [AAAA]

A: [NOMBRE COMPLETO DEL DESTINATARIO]
C.I. / RUT: [XXXXXXXXXX]
Domicilio: [Domicilio completo del destinatario]

De: [NOMBRE COMPLETO DEL REMITENTE]
C.I. / RUT: [XXXXXXXXXX]
Domicilio: [Domicilio completo del remitente]

Por el presente telegrama colacionado me dirijo a Ud. a fin de:

PRIMERO — HECHOS. [Descripción concisa de los hechos que originan el reclamo,
con fechas y referencias a documentos si corresponde.]

SEGUNDO — INTIMACIÓN. En virtud de lo expuesto y conforme [norma aplicable:
art. 1431 CC UY / art. 1549 CC UY / etc.], lo/la intimo a Ud. a [pretensión
exacta] dentro del plazo de [N] días hábiles desde la recepción del presente.

TERCERO — APERCIBIMIENTO. Transcurrido dicho plazo sin cumplimiento, iniciaré
las acciones judiciales pertinentes ante los Juzgados Letrados de [Montevideo /
ciudad], con más intereses, daños y costas, siendo Ud. responsable de todas
las consecuencias.

CUARTO — INTERRUPCIÓN DE PRESCRIPCIÓN. El presente telegrama interrumpe el
curso de la prescripción conforme el art. 1234 del Código Civil.

[FIRMA DEL REMITENTE]
[Nombre completo]
[C.I. / RUT]
```

---

## Paso 3 — Checklist de envío y archivo

### Argentina — Correo Argentino

- [ ] Verificar que el domicilio del destinatario esté completo y correcto (incluyendo piso, depto, localidad y código postal)
- [ ] Si hay domicilio especial pactado en contrato: enviar al domicilio especial Y al domicilio real
- [ ] Solicitar "aviso de retorno" (acuse de recibo) al enviar
- [ ] Guardar el comprobante de envío con número de pieza postal
- [ ] Guardar el acuse de recibo cuando regrese
- [ ] Si el destinatario no retira: verificar el régimen de notificación ficta (generalmente 48hs después del primer aviso)
- [ ] Archivar copia sellada del texto enviado

### Uruguay — Telegrama Colacionado (Antel)

- [ ] Verificar dirección completa del destinatario
- [ ] Solicitar "acuse de recibo colacionado" para tener constancia de entrega
- [ ] Guardar el comprobante de envío y el talón de colación
- [ ] Si el destinatario no retira en 48hs: la notificación se tiene por cumplida según jurisprudencia del TCAT y SCJ
- [ ] Archivar copia del texto transmitido

---

## Guardrails

- La carta documento NO puede invocar una causal o pretensión distinta a la que luego se plantee en juicio si sirve de base para la acción (principio de congruencia). Verificar que la pretensión sea exactamente la que se intentará en sede judicial.
- En Argentina, el art. 243 LCT (invariabilidad de la causal en despidos) también aplica a telegramas laborales: lo que no se dice en el telegrama no puede invocarse después.
- En causas de consumo (Argentina), verificar si es obligatoria la conciliación previa ante COPREC o la instancia de mediación obligatoria (Ley 26.589) — la carta documento no la reemplaza.
- En Uruguay, para créditos laborales, verificar si el MTSS exige conciliación administrativa previa (Ley 18.566).
- Nunca incluir en la carta documento afirmaciones calificadas jurídicamente como "delito" o "estafa" sin que haya una condena — puede generar responsabilidad por daño al honor (art. 1770 CCyCN / arts. 1321-1322 CC UY).
- Si la prescripción está próxima a vencer: enviar la carta documento y simultáneamente preparar la demanda judicial como medida de resguardo.
- El abogado actuante debe revisar y aprobar el texto antes del envío — este borrador es un insumo, no el texto final.
