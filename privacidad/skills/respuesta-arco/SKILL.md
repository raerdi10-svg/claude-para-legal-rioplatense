---
name: respuesta-arco
description: >
  Clasifica, calcula plazos y redacta el acuse de recibo y la respuesta sustantiva
  a solicitudes ARCO (Acceso, Rectificación, Cancelación, Oposición) y habeas data
  bajo la Ley 18.331 (Uruguay) y la Ley 25.326 (Argentina).
argument-hint: "[texto o descripción de la solicitud ARCO recibida]"
user-invocable: true
---

# Skill: Respuesta a Solicitudes ARCO / Habeas Data

## Propósito

Asistir al abogado en el análisis, clasificación y respuesta de solicitudes de derechos
de acceso, rectificación, cancelación, oposición y habeas data presentadas por titulares
de datos personales. El skill produce dos documentos listos para revisión: el acuse de
recibo formal y la respuesta sustantiva, con citas normativas precisas según la jurisdicción.

---

## Paso 0 — Recolección de datos

Antes de clasificar o redactar, recopilar la siguiente información del abogado:

1. **Texto o resumen de la solicitud recibida.** Si está disponible, solicitar el documento
   completo (carta, formulario, correo electrónico).
2. **Jurisdicción aplicable:** ¿El responsable del tratamiento está domiciliado en Uruguay,
   en Argentina, o tiene presencia en ambos países?
3. **Fecha de recepción de la solicitud** (día/mes/año). Este dato es crítico para el cálculo
   de plazos.
4. **Rol del cliente:** ¿Es responsable del tratamiento o encargado? Si es encargado, ¿tiene
   instrucciones del responsable sobre cómo gestionar solicitudes?
5. **¿Se ha verificado la identidad del solicitante?** ¿Con qué documento?
6. **¿El responsable ya posee los datos del titular?** ¿Los puede identificar en sus bases?
7. **¿Existe alguna restricción legal que pueda impedir la respuesta positiva?**
   (Ejemplo: secreto bancario, investigación penal en curso, datos de terceros.)

Si falta alguno de estos datos, solicitarlos antes de continuar.

---

## Paso 1 — Clasificación del tipo de solicitud

Analizar el texto de la solicitud y clasificarla en una de las siguientes categorías:

| Tipo | Descripción | Norma UY | Norma AR |
|---|---|---|---|
| **Acceso** | El titular pide conocer qué datos tiene el responsable y con qué finalidad | art. 13-15 Ley 18.331 | art. 14 Ley 25.326 |
| **Rectificación / Actualización** | El titular pide corregir datos inexactos o incompletos | art. 16 Ley 18.331 | art. 16 inc. 1 Ley 25.326 |
| **Cancelación / Supresión** | El titular pide eliminar datos que no deberían ser tratados | art. 16 Ley 18.331 | art. 16 inc. 2 Ley 25.326 |
| **Oposición** | El titular pide que cese un tratamiento para una finalidad específica (ej. marketing) | art. 16 Ley 18.331 | art. 27 inc. 3 Ley 25.326 |
| **Habeas Data** | Acción judicial o cuasi-judicial de tutela (solo en Uruguay: Ley 18.331 art. 37 ss.) | art. 37-47 Ley 18.331 | art. 43 CN; art. 33-40 Ley 25.326 |

Si la solicitud combina varios tipos (ej. acceso + cancelación), tratarlos individualmente
y emitir una respuesta unificada que aborde cada pedido.

---

## Paso 2 — Verificación de la legitimación del solicitante

Antes de confirmar o negar la existencia de datos, verificar:

1. **Identidad:** ¿El solicitante acreditó su identidad con cédula de identidad / DNI /
   documento equivalente? (art. 15 Ley 18.331; art. 14 inc. 2 Ley 25.326.)
2. **Representación:** Si actúa por representante, ¿adjuntó poder suficiente?
3. **Titularidad:** ¿Los datos sobre los que ejerce el derecho corresponden al propio
   solicitante? ¿O solicita datos de un tercero sin legitimación?

**Si la legitimación no está acreditada**, el acuse de recibo debe solicitar la subsanación
sin pronunciarse sobre la existencia ni el contenido de los datos.

---

## Paso 3 — Cálculo de plazos de respuesta

### Uruguay — Ley 18.331

| Derecho ejercido | Plazo para responder | Norma |
|---|---|---|
| Acceso | 5 días hábiles desde la recepción | art. 15 Ley 18.331 |
| Rectificación, Cancelación u Oposición | 5 días hábiles desde la recepción | art. 16 Ley 18.331 |
| Ampliación del plazo de acceso (datos complejos) | El responsable puede solicitar prórroga fundada | art. 15 in fine Ley 18.331 |

Los días hábiles se computan excluyendo sábados, domingos y feriados nacionales.

### Argentina — Ley 25.326

| Derecho ejercido | Plazo para responder | Norma |
|---|---|---|
| Acceso | 30 días corridos desde la recepción | art. 14 inc. 3 Ley 25.326 |
| Rectificación, Supresión u Oposición | 5 días hábiles desde la recepción | art. 16 inc. 3 Ley 25.326 |
| Bloqueo preventivo durante investigación | Inmediato (al recibir la solicitud) | art. 16 inc. 3 Ley 25.326 |

Calcular la fecha exacta de vencimiento a partir de la fecha de recepción indicada en
el Paso 0. Incluir la fecha de vencimiento en el acuse de recibo.

---

## Paso 4 — Evaluación de causas de denegación legítima

Analizar si existe alguna causa que justifique una respuesta negativa o parcialmente
negativa:

### Uruguay — causales de limitación (art. 14 Ley 18.331)
- Seguridad pública o defensa nacional
- Investigación de delitos (información suministrada a la Justicia)
- Derechos e intereses de terceros que no deben ser divulgados
- Secreto profesional o comercial legalmente protegido

### Argentina — causales de limitación (art. 17 Ley 25.326)
- Datos recopilados con fines de defensa nacional o seguridad pública
- Datos de inteligencia o investigación de delitos
- Datos cuya publicación afecte derechos de terceros
- Tratamientos para los que la ley prevé régimen específico (ej. secreto bancario, Ley 21.526)

Si existe una causal, documentarla con cita específica. La respuesta no puede ser una
negativa genérica: debe indicar la norma habilitante.

---

## Paso 5 — Redacción del acuse de recibo

Producir un acuse de recibo formal con la siguiente estructura:

```
[Lugar], [día/mes/año]

[Nombre del responsable del tratamiento]
[Domicilio legal]

Ref.: Acuse de recibo — Solicitud de ejercicio de derechos / Art. [15 Ley 18.331 | 14 Ley 25.326]

Señor/a [Nombre del solicitante]:
[Si actúa por representante: En representación de [nombre del titular]:]

Por medio de la presente, [razón social del responsable] acusa recibo de su solicitud de
ejercicio de derecho de [Acceso / Rectificación / Cancelación / Oposición], recibida el
[fecha de recepción].

En cumplimiento de lo dispuesto por [art. 15 Ley 18.331 / art. 14 Ley 25.326], la
respuesta será emitida dentro de los [5 días hábiles / 30 días corridos] computados
desde la fecha de recepción, es decir, a más tardar el [fecha de vencimiento].

[Si la legitimación está pendiente de verificación:]
A efectos de dar curso a su solicitud, le informamos que es necesario acreditar su
identidad mediante [documento requerido]. Sin dicha acreditación no es posible
procesar la solicitud.

[Si la legitimación está acreditada:]
Su identidad ha sido verificada. La solicitud se encuentra en trámite.

Sin otro particular, saluda atentamente,

[Nombre y cargo del firmante]
[Razón social del responsable]
[Datos de contacto del área de privacidad]
```

---

## Paso 6 — Redacción de la respuesta sustantiva

### Caso A — Respuesta positiva (con la información o con la acción realizada)

```
[Lugar], [día/mes/año]

[Nombre del responsable del tratamiento]
[Domicilio legal]

Ref.: Respuesta a solicitud de [Acceso / Rectificación / Cancelación / Oposición]
      — Art. [15-16 Ley 18.331 / 14-16 Ley 25.326]

Señor/a [Nombre del solicitante]:

En respuesta a su solicitud de fecha [fecha], y habiendo verificado su identidad
y los datos obrantes en nuestros registros, le informamos lo siguiente:

[DERECHO DE ACCESO]
Los datos personales que [razón social] trata en relación a su persona son los
siguientes:
- [Categoría de dato]: [descripción o campo]
- Finalidad del tratamiento: [finalidad]
- Base legal: [consentimiento / contrato / interés legítimo / obligación legal — art. XX]
- Destinatarios: [si los hay]
- Plazo de conservación: [plazo]
- Posibilidad de ejercer otros derechos: [rectificación, cancelación, oposición]

[DERECHO DE RECTIFICACIÓN / ACTUALIZACIÓN]
Los datos indicados en su solicitud han sido rectificados/actualizados en nuestros
registros con fecha [fecha]. Los datos corregidos son: [descripción].

[DERECHO DE CANCELACIÓN / SUPRESIÓN]
Los datos indicados en su solicitud han sido suprimidos/bloqueados de nuestros
registros con fecha [fecha]. [Si aplica: Se han comunicado la supresión a los
destinatarios a quienes los datos fueron cedidos, conforme art. 16 Ley 18.331 /
art. 16 inc. 4 Ley 25.326.]

[DERECHO DE OPOSICIÓN]
Hemos registrado su oposición al tratamiento de sus datos para [finalidad específica].
El tratamiento con esa finalidad ha cesado con fecha [fecha].

Sin otro particular, saluda atentamente,

[Nombre y cargo del firmante]
[Razón social del responsable]
```

### Caso B — Respuesta negativa (con fundamento legal)

```
[Lugar], [día/mes/año]

Ref.: Respuesta denegatoria a solicitud de [tipo]
      — Art. [14 Ley 18.331 / 17 Ley 25.326]

Señor/a [Nombre del solicitante]:

En respuesta a su solicitud de fecha [fecha], lamentamos informarle que no es
posible acceder a la misma por las siguientes razones:

[Describir la causal con cita normativa específica: art. 14 inc. [X] Ley 18.331 /
art. 17 inc. [X] Ley 25.326.]

Le informamos que, de no compartir este criterio, tiene derecho a:

[URUGUAY] Interponer acción de habeas data ante el Tribunal de Apelaciones en lo
Civil (art. 37 ss. Ley 18.331) o formular denuncia ante la URCDP (art. 36 Ley 18.331).

[ARGENTINA] Interponer acción de habeas data ante la justicia federal o provincial
competente (art. 33 Ley 25.326) o formular denuncia ante la AAIP (art. 29 inc. 2
Ley 25.326).

Sin otro particular, saluda atentamente,

[Nombre y cargo del firmante]
```

---

## Paso 7 — Entregable final

Producir:
1. Acuse de recibo (listo para firmar y enviar).
2. Respuesta sustantiva (listo para revisión y firma del abogado responsable).
3. Nota interna para el expediente con: tipo de solicitud, fecha de recepción, fecha de
   vencimiento, causal de denegación si aplica, y acción tomada.

---

## Guardrails

- **No confirmar ni negar la existencia de datos** sin antes verificar la legitimación
  del solicitante (identidad y titularidad). Si hay dudas, emitir únicamente el acuse
  de recibo solicitando subsanación.
- **No redactar la respuesta sustantiva** hasta que el abogado confirme que la
  legitimación fue verificada.
- **No omitir la información sobre vías de recurso** en respuestas negativas: su ausencia
  puede agravar la situación regulatoria del responsable.
- **No recomendar denegaciones genéricas**: toda negativa debe apoyarse en una causal
  legal específica con cita normativa.
- **Alertar** si la fecha de vencimiento está a 48 horas o menos de la fecha actual.
- **Alertar** si la solicitud podría constituir una acción judicial de habeas data
  (patrocinio letrado, sello judicial, notificación formal): en ese caso derivar al
  área de litigio del estudio.
