---
name: revision-contratos
description: >
  Revisión de contratos comerciales contra el playbook del estudio. Produce memo
  estructurado con resumen ejecutivo, issues clasificados ALTO/MEDIO/BAJO,
  observaciones cláusula a cláusula y cláusulas sugeridas de reemplazo listas
  para copiar. Requiere confirmación de abogado matriculado antes de entregar
  el memo final al cliente.
argument-hint: "[pegar texto del contrato o indicar nombre del archivo adjunto]"
user-invocable: true
---

# Skill: Revisión de Contratos Comerciales

## Propósito

Analizar un contrato comercial contra el playbook del estudio civil y comercial, identificar los issues relevantes con su nivel de riesgo, y producir un memo de revisión completo que el abogado actuante pueda revisar, ajustar y entregar al cliente. La skill no reemplaza el juicio profesional del abogado; es un primer análisis estructurado que ahorra tiempo en la lectura inicial.

---

## Paso 0 — Lectura previa del perfil

Antes de analizar el contrato, leer el archivo `CLAUDE.md` del plugin para incorporar:
- Jurisdicción principal del estudio
- Umbrales de riesgo (ALTO / MEDIO / BAJO)
- Playbook de cláusulas críticas
- Reglas de escalamiento vigentes
- Estilo de outputs preferido

Si CLAUDE.md no está configurado, advertir al usuario que ejecute `/civil-comercial:cold-start-interview` para un análisis más preciso, y continuar con los valores por defecto del plugin.

---

## Paso 1 — Recolección de datos del contrato

Solicitar al usuario:

1. **Texto del contrato:** pegar el texto completo o adjuntar el archivo.
2. **Rol del cliente:** ¿El cliente es (a) el redactor del contrato, (b) la contraparte receptora, o (c) un tercero que interviene?
3. **Jurisdicción declarada en el contrato:** si no figura, indicar jurisdicción presunta.
4. **Tipo de contrato:** identificar automáticamente si es posible; confirmar con el usuario si hay ambigüedad.
5. **Valor del contrato:** monto total o estimado (en la moneda del contrato).
6. **Fecha de firma prevista:** para determinar urgencia del análisis.
7. **Instrucciones especiales:** ¿Hay puntos específicos que el socio quiere que se revisen con más detalle?

---

## Paso 2 — Identificación de datos estructurales

Extraer del contrato:

| Campo | Valor identificado |
|---|---|
| Partes (nombre y rol) | |
| Tipo de contrato | |
| Objeto | |
| Precio / contraprestación | |
| Moneda y forma de pago | |
| Plazo de vigencia | |
| Ley aplicable | |
| Jurisdicción / fuero / arbitraje | |
| Fecha de celebración | |
| Firma electrónica o ológrafa | |

Si algún dato estructural falta en el contrato, marcarlo como **[NO ESPECIFICADO]** — su ausencia es en sí misma una observación.

---

## Paso 3 — Análisis contra el playbook

Para cada cláusula o bloque temático, contrastar con el playbook del estudio. Usar la siguiente estructura de análisis:

### 3.1 — Responsabilidad (arts. 1728, 1743, 1744 CCyCN / art. 1341 CC UY)

- ¿Existe cláusula de limitación de responsabilidad? ¿Establece un cap? ¿El cap equivale al menos al valor del contrato en los últimos 12 meses?
- ¿Hay exoneración total de responsabilidad? Si sí → ALTO.
- ¿La cláusula penal supera el 30 % del valor del contrato? → ALTO. ¿Entre 20 % y 30 %? → MEDIO.
- ¿Se excluye la responsabilidad por dolo o culpa grave? En Argentina, verificar art. 1743 CCyCN (inválido). En Uruguay, art. 1341 CC.
- ¿Se incluye daño emergente y lucro cesante, o solo uno de ellos?

### 3.2 — Rescisión y resolución (arts. 1077-1092 CCyCN / arts. 1431, 1549 CC UY)

- ¿Existen causales de rescisión unilateral sin causa? ¿Solo a favor de una parte?
- ¿Se establece preaviso mínimo? El estudio exige 30 días para rescisión sin causa.
- ¿Existe derecho a subsanar el incumplimiento? El estudio exige 15 días de plazo para subsanar antes de que sea efectiva la rescisión por causa.
- ¿La rescisión unilateral injustificada a favor de solo una parte es una cláusula abusiva? Verificar arts. 988 y 1092 CCyCN.
- ¿Se prevén consecuencias económicas de la rescisión (daños, indemnización por clientela en distribución)?

### 3.3 — Ley aplicable y jurisdicción

- ¿La ley aplicable es Argentina o Uruguay? Si es derecho extranjero → ALTO.
- ¿La jurisdicción corresponde a la sede del cliente o de la contraparte? Si es extranjera sin justificación → ALTO.
- Si hay arbitraje: ¿cuál es la institución? ¿Está en Buenos Aires o Montevideo? Si es fuera de la región → ALTO.
- ¿Se renuncia al fuero ordinario? ¿El cliente puede calificar como consumidor bajo art. 1092 CCyCN o Ley 17.250 UY?

### 3.4 — Confidencialidad

- ¿La definición de "información confidencial" es precisa o es omnicomprensiva?
- ¿Se incluyen las cinco exclusiones mínimas? (dominio público / conocida previamente / recibida de tercero lícito / desarrollada independientemente / exigencia legal)
- ¿El plazo de confidencialidad post-vencimiento es razonable según el sector?
- ¿Hay obligación de destrucción o devolución de soportes? ¿Plazo máximo 30 días?
- ¿El contrato involucra datos personales bajo Ley 25.326 (AR) o Ley 18.331 (UY)? Si sí → verificar cláusula de encargado de tratamiento.

### 3.5 — Propiedad intelectual

- ¿Se distingue entre background IP (preexistente) y foreground IP (creada durante el contrato)?
- ¿La cesión de PI tiene precio diferenciado o está incluida en la contraprestación general?
- ¿La cesión es sin límite geográfico o temporal a favor de una sola parte sin compensación? → ALTO.
- ¿El contrato involucra software? Verificar Ley 11.723 (AR) o Ley 9.739/17.164 (UY).

### 3.6 — Otras cláusulas a revisar

- **Prescripción:** ¿Se modifica el plazo de prescripción? Verificar arts. 2532-2559 CCyCN (modificación dentro de los límites permitidos). Plazos reducidos a menos de 1 año → ALTO. Plazos modificados fuera del rango legal → MEDIO.
- **Exclusividad:** ¿Hay obligaciones de exclusividad? ¿Tienen plazo definido? Sin plazo → MEDIO. Verificar Ley 18.159 UY (defensa de la competencia).
- **No competencia post-contractual:** ¿Tiene límite geográfico y temporal razonables?
- **Auditoría:** ¿Tiene límite temporal y de frecuencia?
- **Indexación:** ¿La moneda de pago o la indexación involucra índices extranjeros? → MEDIO.
- **Garantías:** ¿Se requieren garantías bancarias o seguros de caución? → verificar regla de escalamiento.
- **Anticorrupción:** Si hay contratación pública o cliente de sector regulado, verificar Ley 27.401 (AR) o normativa equivalente UY.

---

## Paso 4 — Clasificación de issues

Construir tabla de issues con el siguiente formato:

| N° | Cláusula | Nivel | Descripción del issue | Recomendación |
|---|---|---|---|---|
| 1 | [Cláusula X] | ALTO | [descripción] | [acción] |
| 2 | [Cláusula Y] | MEDIO | [descripción] | [acción] |
| ... | | | | |

Criterios de nivel según CLAUDE.md del estudio. Si CLAUDE.md no está configurado, usar:
- **ALTO:** responsabilidad ilimitada · arbitraje extranjero · renuncia a fuero · penalidad > 30 % · cesión de PI sin compensación
- **MEDIO:** prescripción modificada · garantías amplias sin límite · penalidad 20-30 % · indexación inusual · exclusividad sin plazo
- **BAJO:** forma y protocolo · dirección · numeración · precisiones de definición

---

## Paso 5 — Redacción del memo

### Estructura obligatoria del memo:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MEMO DE REVISIÓN DE CONTRATO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contrato:       [Tipo — Partes]
Fecha análisis: [DD/MM/AAAA]
Jurisdicción:   [AR / UY / Ambas]
Valor:          [Monto y moneda]
Rol cliente:    [Redactor / Receptor / Tercero]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I. RESUMEN EJECUTIVO
[Tres líneas máximo, redactadas para que las lea el cliente sin formación legal.
Indicar si el contrato es aceptable con ajustes menores, requiere negociación
de puntos críticos o no debe firmarse sin modificaciones sustanciales.]

II. ISSUES CRÍTICOS
[Tabla de issues del Paso 4, ordenada por nivel: ALTO primero, luego MEDIO, luego BAJO.]

III. OBSERVACIONES CLÁUSULA A CLÁUSULA
[Solo las cláusulas que tienen observación. Para cada una:
  - Cláusula N° / Denominación
  - Texto actual (transcribir el fragmento relevante)
  - Observación (citar la norma aplicable)
  - Recomendación
Omitir las cláusulas que están en orden.]

IV. CLÁUSULAS SUGERIDAS DE REEMPLAZO
[Para cada issue ALTO y, cuando sea posible, para los MEDIO, proponer
texto de reemplazo completo, listo para copiar y pegar en el contrato.
Indicar el artículo que reemplaza.]

V. ISSUES QUE REQUIEREN ESCALAMIENTO
[Lista de issues que, según las reglas de CLAUDE.md, deben derivarse a
un socio, área especializada o al cliente para instrucción. Incluir
la razón del escalamiento y el aprobador sugerido.]
```

---

## Paso 6 — Compuerta de aprobación profesional

Antes de entregar el memo al usuario, mostrar:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPUERTA DE REVISIÓN PROFESIONAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Este memo es un análisis preliminar generado con asistencia
de IA. Antes de enviarlo al cliente o usarlo para tomar
decisiones contractuales, confirmar que:

□ Un abogado matriculado en la jurisdicción aplicable
  revisó y validó el contenido del memo.
□ Los issues de nivel ALTO fueron evaluados por el
  socio a cargo o referente designado en CLAUDE.md.
□ Las cláusulas de reemplazo sugeridas fueron adaptadas
  al contexto específico del cliente y la transacción.
□ El valor del contrato fue verificado contra el umbral
  de escalamiento del estudio.
□ Si hay datos personales: el área de privacidad fue
  notificada.

¿Confirma que un abogado matriculado revisará este memo
antes de darlo al cliente? (sí / no)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Si el usuario responde "no", entregar el memo con un banner de advertencia visible al inicio:

```
⚠️  BORRADOR — PENDIENTE DE REVISIÓN POR ABOGADO MATRICULADO
Este documento no ha sido validado por un profesional habilitado.
No puede ser entregado al cliente en este estado.
```

---

## Guardrails

- Nunca afirmar que una cláusula "es inválida" o "no tendrá efecto" en forma absoluta — usar expresiones como "presenta dudas de validez bajo el art. X", "podría ser cuestionada", "es susceptible de reducción judicial".
- Nunca afirmar que el contrato "puede firmarse" o que "no hay problemas" — usar "el análisis preliminar no identifica issues de nivel ALTO" y aclarar que el criterio final es del abogado actuante.
- Si el contrato supera el umbral de monto definido en CLAUDE.md, incluir automáticamente el aviso de escalamiento al socio a cargo.
- Si el contrato contiene cláusulas en idioma extranjero sin traducción, advertir que el análisis de esas cláusulas es parcial y puede requerir asistencia de abogado en esa jurisdicción.
- En contratos de adhesión (arts. 984-989 CCyCN), aplicar el criterio de interpretación favorable a la parte adherente (art. 987 CCyCN) y señalar las cláusulas presumiblemente abusivas (art. 988).
- Citar siempre la norma antes que la doctrina: "art. 1743 CCyCN — las cláusulas de exoneración son inválidas cuando...".
- El memo debe redactarse en español rioplatense formal; evitar gerundios al inicio de oración; formato de fecha: día/mes/año.
