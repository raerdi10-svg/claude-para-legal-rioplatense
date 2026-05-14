---
name: escala-escalamiento
description: >
  Routing de issues contractuales al aprobador correcto según las reglas de
  escalamiento del estudio. Clasifica el issue, identifica al aprobador
  correspondiente y redacta el email o memo de consulta con contexto del
  contrato, naturaleza del issue, opciones recomendadas y plazo para decidir.
argument-hint: "[descripción del issue contractual o indicar contrato y cláusula específica]"
user-invocable: true
---

# Skill: Escalamiento de Issues Contractuales

## Propósito

Determinar si un issue contractual detectado durante la revisión de un contrato debe escalar a un aprobador (socio, área especializada o cliente), identificar a quién debe escalar y producir el email o memo de consulta con la información necesaria para que el aprobador tome una decisión informada en el menor tiempo posible.

---

## Paso 0 — Lectura del perfil

Leer `CLAUDE.md` del plugin. Las reglas de escalamiento son las definidas por el estudio en la tabla "Reglas de escalamiento" de ese archivo. Si CLAUDE.md no está configurado, usar las reglas por defecto del plugin (detalladas en el Paso 2).

---

## Paso 1 — Recolección de datos del issue

Solicitar al usuario:

1. **Descripción del issue:** ¿Qué cláusula o situación genera la necesidad de escalar?
2. **Contrato involucrado:** tipo, partes, valor estimado, jurisdicción, fecha de firma prevista.
3. **Urgencia:** ¿Cuándo vence el plazo para responder a la contraparte o firmar el contrato?
4. **Contexto adicional:** ¿El issue surgió en la revisión inicial, en la negociación, o ya durante la ejecución del contrato?
5. **Posición del cliente:** ¿Qué postura tiene el cliente sobre el issue? ¿Tiene instrucciones específicas?
6. **¿Ya se consultó informalmente con alguien?** ¿Qué se dijo?

---

## Paso 2 — Clasificación del issue según reglas de escalamiento

Aplicar las reglas de escalamiento de CLAUDE.md. Si el perfil no está configurado, usar las siguientes reglas por defecto:

| Condición | Aprobador | Nivel |
|---|---|---|
| Valor del contrato > USD 500.000 | Socio a cargo | ALTO |
| Arbitraje internacional fuera de AR/UY | Área de litigio / arbitraje internacional | ALTO |
| Cambio de ley aplicable a derecho extranjero | Socio senior + dictamen de otra jurisdicción | ALTO |
| Cesión de PI sin límite o por precio simbólico | Área de PI | ALTO |
| Datos personales sensibles en el contrato | Área de privacidad / DPO del cliente | ALTO |
| Cláusula penal > 30 % del valor del contrato | Socio a cargo | ALTO |
| Cláusula de responsabilidad ilimitada o exclusión total | Socio a cargo | ALTO |
| Renuncia a fuero ordinario sin contraprestación | Socio a cargo | ALTO |
| Garantías bancarias o seguros de caución requeridos | Área financiera del cliente | MEDIO |
| Vigencia > 5 años sin cláusula de salida | Socio a cargo | MEDIO |
| Cláusula penal entre 20 % y 30 % del valor | Socio a cargo | MEDIO |
| Exclusividad sin plazo definido | Área de competencia o socio a cargo | MEDIO |
| Prescripción modificada fuera del rango CCyCN | Socio a cargo | MEDIO |

Para cada issue relevado, determinar:
- ¿Activa alguna regla de escalamiento?
- ¿A qué aprobador corresponde?
- ¿Con qué nivel de urgencia?
- ¿Puede resolverse en el nivel actual (abogado revisor) con instrucciones del cliente, o requiere necesariamente una decisión de un nivel superior?

Si el issue activa múltiples reglas de escalamiento, identificar el aprobador de mayor jerarquía y notificar a todos los que correspondan.

---

## Paso 3 — Determinación de opciones recomendadas

Para el issue identificado, elaborar entre dos y cuatro opciones de acción para que el aprobador decida:

**Estructura de cada opción:**

```
OPCIÓN [N] — [Nombre corto]
Descripción: [Qué implica esta opción para el cliente]
Pros:
  - [Beneficio 1]
  - [Beneficio 2]
Contras:
  - [Riesgo o costo 1]
  - [Riesgo o costo 2]
Norma aplicable: [art. X CCyCN / art. Y CC UY]
Recomendación del equipo revisor: [Preferimos esta opción / No recomendamos / Neutral]
```

Ejemplos de opciones típicas:
- **Aceptar la cláusula tal como está:** con descripción del riesgo que se asume.
- **Proponer modificación puntual:** con el texto sugerido de la cláusula modificada.
- **Rechazar la cláusula y proponer eliminación:** con argumentos para la negociación.
- **Aceptar con contraprestación compensatoria:** ej. aceptar responsabilidad ilimitada a cambio de seguro de responsabilidad civil exigido al cliente.
- **Suspender la firma hasta nueva instrucción:** cuando el riesgo es tan elevado que no puede resolverse sin información adicional del cliente.

---

## Paso 4 — Redacción del email de consulta

Producir el email o memo de consulta al aprobador en el siguiente formato:

```
PARA:   [Nombre del aprobador / área]
DE:     [Nombre del abogado revisor]
ASUNTO: [ESCALAMIENTO] [Tipo de contrato] — [Partes] — Issue: [descripción breve]
FECHA:  [DD/MM/AAAA]
PLAZO PARA DECIDIR: [DD/MM/AAAA, HH:MM hs]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. CONTEXTO DEL CONTRATO

Tipo:        [Tipo de contrato]
Partes:      [Parte A] — [Parte B]
Valor:       [Monto y moneda]
Jurisdicción:[AR / UY / Internacional]
Ley aplicable:[CCyCN / CC UY / otra]
Estado:      [En revisión / En negociación / Por firmar / En ejecución]
Fecha límite para firma o respuesta: [DD/MM/AAAA]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. NATURALEZA DEL ISSUE

[Descripción clara y concisa del issue en no más de 5 líneas. Sin jerga innecesaria
— que lo pueda leer el socio en el ascensor.]

Cláusula involucrada: [N° y texto de la cláusula]
Norma aplicable:      [art. X CCyCN / art. Y CC UY]
Nivel de riesgo:      [ALTO / MEDIO]
Regla de escalamiento activada: [Citar la regla del CLAUDE.md o la tabla por defecto]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. OPCIONES RECOMENDADAS

[Tabla de opciones del Paso 3 — máximo 4 opciones]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV. POSICIÓN DEL CLIENTE

[Qué dice o quiere el cliente sobre este issue. Si no hay instrucciones, indicarlo.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
V. DECISIÓN REQUERIDA

Para continuar con la revisión / negociación / firma, necesitamos que:

□ Autorice la opción [N]
□ Nos instruya sobre una opción alternativa
□ Se comunique directamente con [Nombre / Área] sobre este punto

PLAZO: [DD/MM/AAAA] — Si no recibimos instrucciones antes de esa fecha,
[procedemos con la opción X por defecto / suspendemos la firma / informamos a la contraparte].

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ante cualquier consulta, estamos disponibles.

[Firma del abogado revisor]
```

---

## Paso 5 — Registro del escalamiento

Producir un registro interno del escalamiento para que quede en el file del asunto:

```
REGISTRO DE ESCALAMIENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contrato:           [Tipo — Partes]
Fecha del issue:    [DD/MM/AAAA]
Issue:              [Descripción breve]
Nivel:              [ALTO / MEDIO]
Aprobador:          [Nombre / Área]
Fecha de consulta:  [DD/MM/AAAA]
Plazo de respuesta: [DD/MM/AAAA]
Estado:             PENDIENTE DE RESPUESTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESOLUCIÓN (a completar cuando se reciba instrucción):
Fecha:     [DD/MM/AAAA]
Decisión:  [Opción elegida / instrucción recibida]
Resolvió:  [Nombre del aprobador]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Si el issue activa múltiples reglas de escalamiento simultáneamente, escalar siempre al aprobador de mayor jerarquía e informar a los secundarios en copia.
- No recomendar que el abogado revisor resuelva unilateralmente un issue que activa una regla de escalamiento de nivel ALTO, aunque la solución parezca obvia. La regla de escalamiento existe precisamente para que la responsabilidad de la decisión quede en el nivel adecuado.
- El plazo para decidir no debe establecerse después de la fecha de firma prevista o del plazo de respuesta a la contraparte — alertar al usuario si el plazo propuesto es insuficiente.
- Si el aprobador identificado en CLAUDE.md ya no está disponible (por ejemplo, el socio de referencia no figura en el perfil), advertir al usuario que debe identificar al aprobador sustituto antes de enviar el email.
- En issues de nivel ALTO con plazo de respuesta menor a 48 horas, recomendar comunicación telefónica o personal además del email de escalamiento.
- Nunca producir el email de escalamiento sin antes listar las opciones recomendadas — el aprobador necesita ese análisis para decidir con fundamento.
