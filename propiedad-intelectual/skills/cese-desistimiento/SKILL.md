---
name: cese-desistimiento
description: >
  Redacta una carta de cese y desistimiento por infracción de derechos de propiedad
  intelectual (marcas, derechos de autor, patentes, secreto empresarial) en Uruguay y Argentina,
  con fundamento legal exacto, plazo razonable y advertencia de consecuencias.
argument-hint: "[descripción del infractor y la conducta infractora] [--jurisdiccion=UY|AR|ambas]"
user-invocable: true
---

# Skill: Redactor de Carta de Cese y Desistimiento

## Propósito

Redactar cartas de cese y desistimiento por infracción de derechos de propiedad intelectual,
con identificación precisa de la conducta, fundamento jurídico exacto, plazo razonable para
cumplir y advertencia de las consecuencias del incumplimiento. La carta es un borrador para
revisión del abogado titular del derecho.

---

## Paso 0 — Recolección de datos

1. **Jurisdicción**: Uruguay / Argentina / Ambas
2. **Titular del derecho**: nombre, domicilio, CUIT/CI/RUT
3. **Infractor**: nombre o razón social, domicilio, si es conocido
4. **Tipo de derecho infringido**:
   - Marca registrada (indicar número de registro y clases)
   - Derecho de autor (indicar obra y número de registro si existe)
   - Patente (indicar número de patente)
   - Secreto empresarial / know-how
   - Nombre de dominio / cybersquatting
5. **Conducta infractora**: descripción precisa (uso de signo confundible, reproducción de obra, fabricación sin licencia, etc.)
6. **Evidencia disponible**: capturas de pantalla, productos, publicaciones, fechas de primera detección
7. **¿Se desea proponer regularización** (licencia, coexistencia) o solo se exige el cese?

---

## Paso 1 — Clasificación de la infracción y norma aplicable

### Uruguay

| Tipo | Norma | Acción disponible |
|---|---|---|
| Uso de marca confundible | Art. 5 y 13 Ley 17.011 | Cese + daños (arts. 68-71 Ley 17.011); medida cautelar (art. 70) |
| Reproducción de obra sin autorización | Ley 9.739 arts. 44-46 | Acción civil + denuncia penal (art. 46 bis Ley 9.739) |
| Infracción de patente | Ley 17.164 arts. 79-82 | Cese + daños + embargo cautelar |
| Apropiación de secreto empresarial | Ley 17.616 + CC art. 1319 | Acción de daños y perjuicios |
| Cybersquatting | Ley 17.011 + reglamento SECOM | Procedimiento ante SECOM + acción civil |

### Argentina

| Tipo | Norma | Acción disponible |
|---|---|---|
| Uso de marca confundible | Arts. 2, 3 y 31 Ley 22.362 | Acción civil (art. 37) + denuncia penal (art. 31, pena hasta 3 años) |
| Reproducción de obra sin autorización | Ley 11.723 arts. 71-72 | Querella penal (art. 72) + acción civil |
| Infracción de patente | Ley 24.481 arts. 80-83 | Cese + daños + embargo cautelar (art. 87) |
| Apropiación de secreto empresarial | Ley 24.766 | Acción civil + posible penal si hay sustracción |
| Cybersquatting | Ley 22.362 + resoluciones NIC Argentina | Procedimiento ante NIC AR + acción civil |

---

## Paso 2 — Evaluación de si la carta interrumpe la prescripción

- **Uruguay**: la carta fehaciente interrumpe la prescripción (CC art. 1233) si constituye reconocimiento o acto jurídico que haga valer el derecho. Anotar la fecha de envío.
- **Argentina**: la carta documento interrumpe la prescripción si constituye intimación fehaciente (CCyCN art. 2546). Verificar que sea enviada por medio fehaciente (carta documento Correo Argentino / telegrama colacionado).

---

## Paso 3 — Redacción de la carta

```
[Ciudad], [DD] de [mes] de [AAAA]

A: [Nombre del infractor]
   [Domicilio del infractor]

De nuestra consideración:

Nos dirigimos a usted en nombre y representación de [TITULAR DEL DERECHO], titular de
[descripción del derecho: marca Nº X / obra registrada bajo Nº X / patente Nº X / know-how
relacionado con X], conforme [cita normativa exacta: art. X Ley Y].

I. TITULARIDAD DEL DERECHO
[Nombre del titular] es [titular registral / titular originario / licenciatario exclusivo]
del [tipo de derecho] individualizado como [descripción completa, número de registro si existe,
clases si es marca].

II. CONDUCTA INFRACTORA
Ha llegado a nuestro conocimiento que [nombre del infractor] [descripción precisa de la conducta:
utiliza el signo X en productos/servicios Y / reproduce la obra Z en el sitio web / fabrica y
comercializa el producto X sin autorización / utiliza el know-how confidencial de X]. Dicha
conducta fue detectada el día [fecha] mediante [descripción de la evidencia].

La conducta descripta constituye infracción a [norma exacta], al [descripción del acto infractor
en términos normativos].

III. EXIGENCIA DE CESE
Por las razones expuestas, intimamos a usted a CESAR EN FORMA INMEDIATA E ÍNTEGRA en la
conducta descripta en el punto II, dentro del plazo de [5 / 10] días hábiles contados desde
la recepción de la presente.

[Si se propone regularización:] Sin perjuicio de lo anterior, nuestro representado está
dispuesto a evaluar la posibilidad de regularizar la situación mediante [licencia / acuerdo de
coexistencia]. En ese caso, rogamos ponerse en contacto antes del vencimiento del plazo indicado.

IV. CONSECUENCIAS DEL INCUMPLIMIENTO
El incumplimiento de la presente intimación facultará a [nombre del titular] a:
- Iniciar las acciones civiles por daños y perjuicios previstas en [norma];
- Solicitar medidas cautelares de urgencia [embargo de stock / prohibición de comercializar /
  secuestro] ante los tribunales competentes, las cuales pueden decretarse sin previo
  conocimiento del afectado;
[Si aplica:] - Formular denuncia penal ante [Fiscalía / Juzgado Criminal competente] por
infracción a [art. X Ley Y], cuya pena es de [descripción de la pena].

Sin otro particular, quedamos a vuestra disposición.

Atentamente,

[FIRMA DEL ABOGADO]
[MATRÍCULA / TOMO Y FOLIO]
[DIRECCIÓN DEL ESTUDIO]
[DATOS DE CONTACTO]
```

---

## Paso 4 — Instrucciones de envío

- **Argentina**: enviar como **carta documento** a través del Correo Argentino (fehaciente, genera constancia con acuse de recibo). Conservar el duplicado sellado.
- **Uruguay**: enviar como **carta certificada con aviso de retorno** (Correo Uruguayo) o **telegrama colacionado** (Antel). Para mayor fuerza probatoria: carta con firma certificada notarialmente.
- Si se conoce el domicilio real del infractor pero no el legal: enviar a ambos.
- Guardar constancia de envío con fecha — es el dies a quo para el cómputo del plazo.

---

## Guardrails

- No enviar la carta sin revisión del abogado titular del derecho.
- Verificar que el cliente tenga título válido y vigente sobre el derecho invocado antes de enviar (registro vigente, no caducado, sin nulidad pendiente).
- Si el infractor ya fue notificado previamente y continuó infringiendo, mencionar esa circunstancia en la carta (agrava la situación del infractor).
- No exigir sumas de dinero ni proponer acuerdos económicos en la misma carta de cese sin instrucción expresa del cliente.
- En marcas argentinas: si la marca no ha sido usada en los últimos 5 años, el infractor puede reconvenir por caducidad (art. 26 Ley 22.362) — verificar uso antes de enviar.
- En derechos de autor: si la obra es de dominio público o si el uso cae bajo excepción legal (cita, parodia, uso educativo), la carta puede ser improcedente — verificar antes de enviar.
