---
name: revision-nda
description: >
  Clasificación VERDE/AMARILLO/ROJO de acuerdos de confidencialidad (NDA)
  entrantes. Verifica partes, definición de información confidencial,
  exclusiones, plazo, obligaciones post-vencimiento, jurisdicción, remedy
  y datos personales. Produce semáforo con lista de cambios requeridos
  y texto de cláusulas sugeridas.
argument-hint: "[pegar texto del NDA o indicar nombre del archivo adjunto]"
user-invocable: true
---

# Skill: Revisión de NDA — Semáforo VERDE/AMARILLO/ROJO

## Propósito

Clasificar rápidamente un acuerdo de confidencialidad (NDA) entrante como VERDE (aceptable para firma), AMARILLO (negociable con cambios identificados) o ROJO (no firmar sin modificaciones sustanciales). La skill está optimizada para NDAs unilaterales y bilaterales en el contexto rioplatense, con foco en las cláusulas que generan exposición legal real para el cliente receptor.

---

## Paso 0 — Lectura del perfil

Leer `CLAUDE.md` del plugin para incorporar umbrales de riesgo y preferencias de jurisdicción del estudio. Identificar si el estudio tiene templates propios de NDA en la sección "Documentos semilla".

---

## Paso 1 — Recolección de datos

Solicitar al usuario:

1. **Texto del NDA:** pegar el texto completo o adjuntar el archivo.
2. **Posición del cliente:** ¿El cliente es (a) la parte divulgadora, (b) la parte receptora, o (c) ambas (NDA bilateral)?
3. **Contexto de la transacción:** ¿Para qué se firma el NDA? (due diligence, exploración de negocio, contratación de proveedor, otra)
4. **Sector:** tecnología, farma, fintech, manufactura, servicios, otro — relevante para el plazo razonable de confidencialidad.
5. **¿Involucra datos personales?** Sí / No / No está claro.

---

## Paso 2 — Verificación de los ocho puntos críticos

Para cada punto, determinar si el NDA es: **Conforme** / **Observación menor** / **Cambio requerido** / **No aceptable**.

### Punto 1 — Identificación de las partes

- ¿Están correctamente identificadas con denominación legal completa (razón social, CUIT/RUT, domicilio)?
- ¿La persona firmante tiene facultades suficientes? (verificar si se trata de representante legal o apoderado)
- ¿El NDA es unilateral o bilateral? ¿La clasificación se corresponde con la asimetría real de la información que se intercambiará?

**Alerta:** NDA formalmente bilateral pero con obligaciones asimétricas de facto (solo una parte divulga información real) puede ser tratado como unilateral a los efectos de interpretación.

### Punto 2 — Definición de "información confidencial"

Verificar:
- (a) ¿La definición es precisa y acotada?
- (b) ¿Incluye una cláusula "catch-all" sin límites? → Cambio requerido.
- (c) ¿Requiere marcación formal (ej. sello "confidencial") para que la información quede protegida? ¿Es operativamente viable para el cliente?
- (d) ¿Excluye la información oral? Si sí, ¿se puede negociar la inclusión con un mecanismo de confirmación escrita en plazo razonable?

**Posición del estudio:** la definición debe ser suficientemente amplia para proteger al divulgador pero suficientemente acotada para que el receptor pueda identificar qué no puede divulgar sin ambigüedad.

### Punto 3 — Exclusiones de confidencialidad

Verificar que estén presentes las cinco exclusiones estándar:

| N° | Exclusión | Presente | Texto adecuado |
|---|---|---|---|
| 1 | Información en dominio público al momento de la divulgación o que pase a dominio público sin culpa del receptor | ☐ | |
| 2 | Información conocida previamente por el receptor, acreditada mediante documentos con fecha cierta | ☐ | |
| 3 | Información recibida lícitamente de un tercero sin obligación de confidencialidad | ☐ | |
| 4 | Información desarrollada independientemente por el receptor sin uso de la información confidencial | ☐ | |
| 5 | Divulgación exigida por ley, reglamentación o resolución judicial o administrativa | ☐ | |

Si falta alguna de las cinco exclusiones → **Cambio requerido** para la parte receptora.

Para la exclusión N° 5 (divulgación legal), verificar si se exige notificación previa al divulgador cuando sea razonablemente posible — es una cláusula favorable para el divulgador que el estudio generalmente acepta.

### Punto 4 — Plazo de confidencialidad

- ¿Se establece un plazo de vigencia del NDA?
- ¿Se establece un plazo de confidencialidad post-vencimiento del acuerdo?
- Criterios de razonabilidad por sector:

| Sector | Plazo post-vencimiento razonable |
|---|---|
| Tecnología de consumo / software | 2-3 años |
| Fintech / servicios financieros | 3 años |
| Farmacéutico / biotecnología | 5 años |
| Manufactura / procesos industriales | 3-5 años |
| Servicios profesionales generales | 2 años |

- Si el plazo es "indefinido" o "hasta que la información deje de ser confidencial" → **Cambio requerido** para la parte receptora (añadir plazo máximo determinado).
- Si el plazo es excesivamente corto (menos de 1 año post-vencimiento para información estratégica) → **Observación** para la parte divulgadora.

### Punto 5 — Obligaciones post-vencimiento

- ¿Se establece la obligación de devolver o destruir soportes con información confidencial al vencimiento?
- ¿Se fija un plazo máximo para ello? (El estudio exige máximo 30 días desde solicitud)
- ¿Se permite conservar copias de respaldo de archivo legal? ¿Con qué restricciones?
- ¿Se incluye certificación de destrucción?

**Alerta:** la ausencia de cláusula de destrucción o devolución es una observación menor para plazos cortos, pero se convierte en cambio requerido cuando el NDA tiene plazo indefinido o involucra información estratégica.

### Punto 6 — Jurisdicción y ley aplicable

- ¿La ley aplicable es Argentina (CCyCN) o Uruguay (Código Civil)? Si es derecho extranjero → **No aceptable** sin revisión adicional.
- ¿La jurisdicción corresponde a la sede del cliente o a la de la contraparte?
- Si hay arbitraje: ¿sede y reglamento son razonables? (CAM, CCI, CNUDMI con sede en Buenos Aires o Montevideo)
- ¿La cláusula de jurisdicción excluye medidas cautelares urgentes ante los tribunales ordinarios? Verificar que se preserve la posibilidad de medidas cautelares de urgencia.

### Punto 7 — Remedy (medidas ante incumplimiento)

- ¿Se reconoce expresamente que el incumplimiento puede causar daños irreparables que justifican medidas cautelares?
- ¿Se prevé una cláusula penal por incumplimiento? Si sí:
  - ¿El monto es razonable o desproporcionado?
  - ¿Supera el 30 % del valor estimado de la transacción? → ALTO.
  - ¿Se acumula con el resarcimiento de daños reales sin reducción? → **Cambio requerido** (art. 1744 CCyCN — reducibilidad judicial).
- ¿Se establece que la parte afectada podrá solicitar medidas cautelares sin necesidad de acreditar daño cuantificado? Esta cláusula es válida en AR y UY y generalmente favorable para el divulgador.

### Punto 8 — Datos personales

- ¿La información confidencial a intercambiar incluye o puede incluir datos personales de terceros?
- Si sí:
  - Argentina (Ley 25.326): verificar si el intercambio requiere consentimiento de los titulares o encuadra en excepción legal. Si se trata de un encargado de tratamiento, incluir cláusula de instrucción del responsable al encargado.
  - Uruguay (Ley 18.331): ídem; verificar registro de la base de datos en URCDP si corresponde.
- ¿Se incluye una cláusula de protección de datos personales o el NDA silencia el tema?
- Si el NDA silencia datos personales pero la transacción los involucra → **Cambio requerido**: agregar cláusula de protección de datos o un addendum específico.

---

## Paso 3 — Clasificación semáforo

Aplicar la siguiente lógica:

```
ROJO — No firmar sin modificaciones sustanciales:
  → Al menos un punto clasificado como "No aceptable"
  → Más de dos puntos con "Cambio requerido"
  → Ausencia total de exclusiones de confidencialidad
  → Jurisdicción extranjera sin justificación
  → Cláusula penal desproporcionada acumulable con daños

AMARILLO — Negociable (firmar solo con los cambios indicados):
  → Uno o dos puntos con "Cambio requerido"
  → Plazo post-vencimiento irrazonable pero negociable
  → Falta alguna exclusión estándar
  → Cláusula de remedy ausente pero el contexto es de bajo riesgo

VERDE — Aceptable para firma (sin cambios o con ajustes menores):
  → Todos los puntos en "Conforme" u "Observación menor"
  → Las observaciones menores no generan exposición significativa
  → La jurisdicción es razonable para el cliente
```

---

## Paso 4 — Producción del output

### Formato del output:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REVISIÓN DE NDA — SEMÁFORO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Partes:         [Divulgadora] → [Receptora]
Tipo:           [Unilateral / Bilateral]
Fecha análisis: [DD/MM/AAAA]
Rol cliente:    [Divulgadora / Receptora / Ambas]
Contexto:       [Due diligence / Exploración de negocio / otro]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CLASIFICACIÓN: 🔴 ROJO / 🟡 AMARILLO / 🟢 VERDE
[Una oración que explica la razón de la clasificación]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TABLA DE VERIFICACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Punto | Estado | Observación |
|---|---|---|
| 1. Partes | [Conforme / Observación / Cambio requerido / No aceptable] | |
| 2. Definición de confidencial | | |
| 3. Exclusiones (5/5 presentes) | | |
| 4. Plazo | | |
| 5. Obligaciones post-vencimiento | | |
| 6. Jurisdicción y ley aplicable | | |
| 7. Remedy | | |
| 8. Datos personales | | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMBIOS REQUERIDOS (si clasificación ROJO o AMARILLO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Para cada cambio requerido:]

CAMBIO N°[X] — [Nombre del punto]
Problema: [descripción del issue con cita normativa]
Texto actual: "[fragmento del NDA]"
Texto sugerido: "[cláusula de reemplazo completa, lista para usar]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLÁUSULAS SUGERIDAS COMPLETAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Texto de las cláusulas de reemplazo en formato listo para insertar en el contrato]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AVISO LEGAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Este análisis es preliminar y no reemplaza el consejo
legal del abogado actuante. La clasificación y las
cláusulas sugeridas deben ser revisadas por un
profesional habilitado antes de su uso.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Si el NDA está en idioma extranjero, advertir que el análisis puede ser incompleto y que se requiere validación por abogado en esa jurisdicción.
- No clasificar como VERDE un NDA que silencia completamente los datos personales si el contexto de la transacción involucra datos personales de forma evidente.
- La clasificación ROJO no implica que el NDA "no puede firmarse jamás" — implica que no puede firmarse en su estado actual sin modificaciones sustanciales que protejan al cliente.
- Siempre incluir las cinco exclusiones estándar en las cláusulas sugeridas, aunque el NDA original solo carezca de alguna de ellas.
- En NDAs bilaterales, verificar que las obligaciones sean simétricas cuando el intercambio de información es simétrico, y asimétricas cuando no lo es.
- Citar normas: art. 1744 CCyCN para reducibilidad de la cláusula penal; art. 987 CCyCN para interpretación contra el predisponente en adhesión; Ley 25.326 y Ley 18.331 para datos personales.
