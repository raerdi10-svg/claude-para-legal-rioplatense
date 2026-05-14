---
name: revision-lanzamiento
description: >
  Revisión regulatoria de un producto o servicio antes de su lanzamiento al mercado.
  Identifica el marco normativo aplicable, requisitos de autorización previa, restricciones
  de publicidad y produce un checklist con semáforo de riesgo regulatorio.
argument-hint: "[descripción del producto o servicio a lanzar]"
user-invocable: true
---

# Skill: Revisión Regulatoria de Lanzamiento de Producto

## Propósito

Analizar un producto o servicio antes de su salida al mercado para identificar las
obligaciones regulatorias aplicables, los requisitos de autorización o registro previo,
las restricciones de comunicación comercial y las acciones de compliance necesarias.
El resultado es un checklist estructurado con semáforo de riesgo y lista de pasos previos
al lanzamiento.

---

## Paso 0 — Recolección de datos

Solicitar al abogado:

1. **Descripción del producto o servicio:** ¿Qué hace? ¿Cómo funciona? ¿Cuál es el
   modelo de negocio?
2. **Mercado objetivo:** ¿A quiénes está dirigido? (Consumidores finales / empresas /
   sector público / inversores / pacientes / menores.)
3. **Jurisdicción(es) de lanzamiento:** Uruguay, Argentina, o ambas. ¿Hay planes de
   expansión regional?
4. **Canal de distribución:** ¿Online, presencial, a través de intermediarios, o mixto?
5. **Entidad operadora:** ¿Quién va a operar el producto? ¿Es una sociedad ya existente
   o una nueva?
6. **¿El cliente ya obtuvo alguna habilitación o autorización previa?** ¿Cuál?
7. **Documentación disponible:** ¿Hay términos y condiciones, política de privacidad,
   descripción técnica, material publicitario preparado?
8. **Fecha objetivo de lanzamiento** (si existe).

---

## Paso 1 — Identificación del marco regulatorio aplicable

Analizar el producto descripto y determinar qué marcos sectoriales aplican. Puede
aplicar más de uno simultáneamente.

### 1.1 Sector financiero

**Uruguay — BCU / SSF:**
- ¿El producto implica captación de depósitos del público o intermediación financiera?
  → Requiere licencia bancaria o de institución financiera (Ley 17.613, art. 1-2; Ley 18.401).
- ¿Es un servicio de pago, transferencia o emisión de dinero electrónico?
  → Puede requerir habilitación como institución emisora de dinero electrónico (Circular BCU).
- ¿El producto involucra crédito al consumo?
  → Aplica Ley 17.250 (defensa del consumidor) y normativa BCU sobre tasas de usura.
- ¿Es una actividad de cambio de moneda o remesas?
  → Requiere autorización del BCU (Decreto-Ley 15.322, art. 38).
- ¿Involucra criptoactivos o activos virtuales?
  → Verificar Circular BCU sobre activos de pago virtuales; analizar si es una oferta pública.

**Argentina — BCRA / CNV:**
- ¿Implica captación habitual de fondos del público?
  → Actividad financiera privativa de entidades autorizadas por el BCRA (art. 1 Ley 21.526).
- ¿Es un proveedor de servicios de pago (PSP)?
  → Requiere inscripción ante el BCRA (Com. A 6885 y complementarias).
- ¿Es una plataforma de financiamiento colectivo (crowdfunding)?
  → Requiere inscripción ante la CNV (RG CNV 717/2017).
- ¿Involucra oferta pública de valores negociables?
  → Requiere autorización de la CNV (arts. 2 y 85 Ley 26.831).
- ¿Involucra activos virtuales (criptomonedas)?
  → Verificar normativa BCRA y CNV vigente; el encuadre regulatorio está en evolución.

### 1.2 Sector salud y farmacéutico

**Uruguay — MSP / URSEA:**
- ¿Es un medicamento, producto biológico o vacuna?
  → Requiere registro en el MSP (Decreto 14/999, arts. 1-5).
- ¿Es un dispositivo médico?
  → Requiere habilitación del MSP (Decreto 135/999).
- ¿Es un suplemento dietético o alimento funcional con claims de salud?
  → Verificar normativa del MSP y Decreto 315/994 (alimentos).

**Argentina — ANMAT:**
- ¿Es un medicamento, producto biológico o vacuna?
  → Requiere registro ante la ANMAT (art. 7 Ley 16.463; Disposiciones ANMAT).
- ¿Es un producto médico (dispositivo, equipamiento, reactivo)?
  → Requiere inscripción en el Registro Nacional de Productores y Productos de Tecnología
    Médica (RPPTM) (Disposición ANMAT 2318/2002 y concs.).
- ¿Es un alimento con nueva fórmula o claims nutricionales?
  → Requiere aprobación del Código Alimentario Argentino (ANMAT / SENASA).
- ¿Es un cosmético o producto de higiene?
  → Requiere inscripción ante la ANMAT (Resolución MS 155/1998).

### 1.3 Telecomunicaciones y medios

**Uruguay — URSEC:**
- ¿Es un servicio de telecomunicaciones (telefonía, internet, TV por cable)?
  → Requiere concesión o habilitación de la URSEC (art. 7 Ley 17.614).
- ¿Implica uso del espectro radioeléctrico?
  → Requiere licencia de la URSEC.
- ¿Es un servicio de radiodifusión o contenido audiovisual?
  → Verificar Ley 19.307 (Servicios de Comunicación Audiovisual) y habilitación URSEC.

**Argentina — ENACOM:**
- ¿Es un proveedor de telecomunicaciones o servicio de internet?
  → Requiere inscripción ante el ENACOM (art. 15 Ley 27.078).
- ¿Es un servicio de contenido audiovisual (OTT, streaming)?
  → Verificar alcance de la Ley 27.078 y regulación ENACOM sobre servicios OTT.

### 1.4 Energía

**Uruguay — URSEA:**
- ¿Implica distribución o comercialización de electricidad, gas o agua?
  → Requiere habilitación de la URSEA (art. 6 Ley 17.598).
- ¿Es generación de energía para el mercado?
  → Verificar marco regulatorio del Mercado Eléctrico Mayorista (UTE / ADME).

**Argentina — ENARGAS / ENRE:**
- ¿Implica distribución de gas natural?
  → Requiere licencia del ENARGAS (Ley 24.076).
- ¿Implica distribución o generación de electricidad?
  → Requiere habilitación del ENRE o autoridad provincial (Ley 24.065).

### 1.5 Datos personales y privacidad

Ver plugin `privacidad` para análisis detallado. Verificar aquí:
- ¿El producto recopila o trata datos personales? → Registro de la base de datos:
  - Uruguay: Registro de Bases de Datos de la URCDP (art. 22 Ley 18.331).
  - Argentina: Registro Nacional de Bases de Datos de la AAIP (art. 21 Ley 25.326).
- ¿Hay datos sensibles, biométricos o de menores? → Riesgo ALTO.
- ¿Corresponde realizar una EIA? → Derivar al skill `generacion-eia`.

### 1.6 Defensa del consumidor

**Uruguay — ADC / MIEM:**
- ¿El producto se dirige a consumidores finales? → Aplica Ley 17.250 de defensa del
  consumidor: información precontractual obligatoria (art. 6), contratos de adhesión
  (arts. 29-38), garantías (arts. 33-38), derecho de arrepentimiento en ventas a distancia
  (art. 15 ss.).
- ¿Hay publicidad? → Aplica Ley 17.250, arts. 12-15 (publicidad engañosa).

**Argentina — Secretaría de Comercio:**
- ¿El producto se dirige a consumidores finales? → Aplica Ley 24.240 de defensa del
  consumidor: información (art. 4), garantías (arts. 11-18), servicios a distancia y
  comercio electrónico (art. 33 ss.), botón de baja (Res. SC 424/2020).
- ¿Hay publicidad? → Aplica Ley 22.802 de lealtad comercial (o su sucesor normativo).

### 1.7 Prevención de lavado de activos (AML)

**Uruguay — SENACLAFT:**
- ¿El cliente es sujeto obligado según la Ley 19.574 (instituciones financieras, inmobiliarias,
  notarios, contadores, casinos, comerciantes de metales preciosos)?
  → Verificar obligaciones de debida diligencia, reporte de operaciones sospechosas (ROS)
    e informe de operaciones en efectivo.

**Argentina — UIF:**
- ¿El cliente es sujeto obligado según la Ley 25.246 y la Resolución UIF correspondiente
  al sector?
  → Verificar obligaciones de debida diligencia del cliente (DDC), ROS, Declaraciones
    Juradas ante la UIF y programa interno de AML.

### 1.8 Competencia y concentración económica

**Uruguay — COPRODEC:**
- ¿El lanzamiento implica una concentración económica (fusión, adquisición, joint venture)?
  → Notificación obligatoria si supera los umbrales de facturación de la Ley 18.159 (art. 7).

**Argentina — CNDC / Secretaría de Comercio:**
- ¿El lanzamiento implica una concentración económica?
  → Notificación obligatoria si supera los umbrales de la Ley 27.442, art. 9 (facturación
    conjunta > AR$ 100 millones — verificar actualización del umbral).

---

## Paso 2 — Requisitos de autorización o registro previo al lanzamiento

Conforme al marco identificado en el Paso 1, elaborar la siguiente tabla:

| N.° | Requisito | Organismo | Norma | Estado | Plazo estimado de obtención | Consecuencia de operar sin él |
|---|---|---|---|---|---|---|
| 1 | [Licencia / Registro / Habilitación] | [BCU / ANMAT / URSEC / etc.] | [Art. X Ley Y] | Obtenido / En trámite / No iniciado | [Días / Meses] | [Sanción / Clausura / Multa] |

---

## Paso 3 — Restricciones de publicidad y comunicación comercial

Verificar:

- ¿El sector tiene normas específicas sobre publicidad? (Financiero: advertencias obligatorias
  sobre riesgos; Farmacéutico: prohibición de publicidad directa al consumidor de
  medicamentos de venta bajo receta; Alimentos: regulación de claims nutricionales.)
- ¿El material publicitario preparado incluye todas las advertencias legales exigidas?
- ¿Hay restricciones de canales? (Publicidad de criptoactivos, tabaco, alcohol, juego.)
- ¿Se cumplen las normas de publicidad dirigida a menores?

---

## Paso 4 — Evaluación del riesgo regulatorio

Asignar un nivel de riesgo global al lanzamiento:

| Nivel | Criterio de asignación para este producto |
|---|---|
| **ALTO** | El producto requiere autorización previa que aún no ha sido obtenida, o existe ambigüedad regulatoria relevante sobre si la actividad es lícita sin licencia. |
| **MEDIO** | El producto puede operar mientras tramita el registro, pero hay obligaciones de compliance no implementadas o restricciones de publicidad no cumplidas. |
| **BAJO** | El producto opera bajo el marco habilitado vigente. Los requisitos pendientes son formales y no impiden el lanzamiento. |

Justificar la asignación con referencia a los hallazgos del Paso 1 y Paso 2.

---

## Paso 5 — Checklist de compliance previo al lanzamiento

Producir el checklist final con el siguiente formato:

```
CHECKLIST REGULATORIO — LANZAMIENTO DE [NOMBRE DEL PRODUCTO]
Jurisdicción(es): [UY / AR / Ambas]
Fecha de elaboración: [día/mes/año]
Riesgo regulatorio global: [ALTO / MEDIO / BAJO]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÁREA: AUTORIZACIONES Y REGISTROS

[ ] Ítem 1 — [Descripción]
    Norma: [Art. X Ley Y / Com. A XXXX BCRA]
    Estado: [Obtenido ✓ / En trámite ⏳ / No iniciado ✗]
    Prioridad: [BLOQUEANTE / ALTA / MEDIA / BAJA]
    Responsable: [cliente / abogado / regulador]
    Observación: [detalles adicionales]

[ ] Ítem 2 — ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÁREA: DEFENSA DEL CONSUMIDOR

[ ] Ítem 3 — ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÁREA: PROTECCIÓN DE DATOS PERSONALES

[ ] Ítem 4 — ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÁREA: PUBLICIDAD Y COMUNICACIÓN COMERCIAL

[ ] Ítem 5 — ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÍTEMS BLOQUEANTES (no lanzar hasta resolver):
1. [ítem bloqueante]
2. [ítem bloqueante]

PRÓXIMOS PASOS RECOMENDADOS:
1. [Acción inmediata — responsable — plazo]
2. ...
```

---

## Guardrails

- **No emitir opinión de "apto para lanzar"** sin que el abogado revise el checklist y
  confirme que todos los ítems bloqueantes están resueltos.
- **Si el riesgo es ALTO y el producto ya está operando sin autorización**, alertar
  de inmediato y derivar al socio de práctica: puede haber una infracción regulatoria
  en curso que requiera una estrategia de regularización urgente.
- **No analizar marcos regulatorios extranjeros** (UE, EE.UU., Brasil) como norma de
  aplicación directa: solo referenciarlos si el cliente opera en esos mercados y señalar
  que se requiere asesoramiento local.
- **Si el producto involucra criptoactivos o activos virtuales**, señalar expresamente
  que el marco regulatorio está en evolución en ambas jurisdicciones y que la opinión
  debe revisarse ante cada cambio normativo del BCU o el BCRA.
- **Si el producto requiere opinión de otro plugin** (privacidad, laboral, corporativo),
  indicarlo explícitamente con la referencia al skill correspondiente.
