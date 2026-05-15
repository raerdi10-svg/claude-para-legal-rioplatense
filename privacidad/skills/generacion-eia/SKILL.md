---
name: generacion-eia
description: >
  Conducción paso a paso de una Evaluación de Impacto en la Privacidad (EIA/PIA).
  Recopila descripción del tratamiento, finalidad, datos, partes y medidas de seguridad,
  y produce un informe con análisis de riesgos, mitigaciones y conclusión sobre procedencia.
argument-hint: "[nombre o descripción del proyecto o tratamiento a evaluar]"
user-invocable: true
---

# Skill: Generación de Evaluación de Impacto en la Privacidad (EIA / PIA)

## Propósito

Asistir al abogado en la elaboración de una Evaluación de Impacto en la Privacidad
(EIA, también denominada PIA — Privacy Impact Assessment) para un nuevo proyecto,
producto, sistema o tratamiento de datos personales que presente riesgos elevados para
los derechos de los titulares. El skill conduce una entrevista estructurada y produce
un informe completo listo para revisión.

La EIA no es aún obligatoria de forma general en Uruguay ni en Argentina, pero es una
buena práctica respaldada por la URCDP (Resolución 26/021) y la AAIP (Resolución
AAIP 47/2018), y puede ser exigida contractualmente o en procesos de auditoría.
En tratamientos que involucren datos sensibles, tecnologías de reconocimiento biométrico,
perfilado automatizado o monitoreo sistemático, su realización es altamente recomendable.

---

## Paso 0 — Presentación y alcance

Presentar al usuario el propósito del proceso:

> "Voy a guiarte en la elaboración de una Evaluación de Impacto en la Privacidad para
> el tratamiento que querés analizar. La entrevista tiene nueve secciones. Al finalizar,
> voy a generar el informe completo con el análisis de riesgos y la conclusión sobre
> procedencia. El proceso dura entre 20 y 40 minutos según la complejidad del tratamiento."

Preguntar si ya existe documentación del proyecto (brief, especificación técnica, términos
de servicio, política de privacidad borrador). Si existe, solicitarla para incorporarla.

---

## Paso 1 — Identificación del tratamiento

Recopilar:

1. **Nombre del proyecto o sistema:** denominación interna del tratamiento.
2. **Descripción general:** ¿En qué consiste el tratamiento? ¿Qué problema resuelve o
   qué función cumple?
3. **Estado del proyecto:** ¿Es nuevo (diseño) / en implementación / ya operativo?
   (Una EIA es más valiosa en fase de diseño — privacy by design.)
4. **Responsable del tratamiento:** nombre de la organización y su domicilio.
5. **Encargado(s) del tratamiento:** ¿Hay proveedores externos que traten los datos?
   (Nombre, domicilio, rol en el tratamiento.)
6. **Delegado de Protección de Datos (DPO):** ¿Existe? ¿Fue consultado?
7. **Jurisdicción(es) aplicable(s):** Uruguay, Argentina, o ambas. ¿Hay titulares
   en otros países?

---

## Paso 2 — Finalidad del tratamiento

Recopilar:

1. **Finalidad principal:** ¿Para qué se tratan los datos? (Ej.: prestación del servicio,
   facturación, prevención de fraude, personalización, analítica, recursos humanos.)
2. **Finalidades secundarias:** ¿Se usarán los datos para fines adicionales?
   (Ej.: marketing, desarrollo de modelos de IA, cesión a terceros, investigación.)
3. **¿Las finalidades secundarias son compatibles** con la finalidad original?
   Analizar compatibilidad conforme al principio de finalidad (art. 6 inc. 3 Ley 18.331;
   art. 4 inc. 3 Ley 25.326).
4. **Base legal para cada finalidad:**

   | Finalidad | Base legal UY (art. 9 Ley 18.331) | Base legal AR (art. 5 Ley 25.326) |
   |---|---|---|
   | [Finalidad 1] | Consentimiento / Contrato / Interés legítimo / Ley | Consentimiento / Contrato / Interés legítimo / Ley |

---

## Paso 3 — Datos involucrados

Recopilar:

1. **Categorías de datos personales** que se tratarán:
   - Identificación (nombre, CI/DNI, CUIT/RUT, pasaporte)
   - Contacto (email, teléfono, dirección)
   - Financieros (cuentas bancarias, tarjetas, historial crediticio)
   - Laborales (legajo, salario, evaluaciones)
   - Salud (diagnósticos, historia clínica, cobertura)
   - Biométricos (huella dactilar, reconocimiento facial, voz)
   - Geolocalización (tiempo real o histórico)
   - Comportamiento en línea (cookies, tracking, perfiles)
   - Origen racial o étnico
   - Creencias religiosas o filosóficas
   - Orientación sexual o identidad de género
   - Datos penales o contravencionales
   - Menores de 18 años
   - Otro: ___

2. **¿Qué datos son estrictamente necesarios** para la finalidad declarada? (Principio
   de minimización — art. 6 inc. 4 Ley 18.331; art. 4 inc. 1 Ley 25.326.)
3. **Volumen aproximado de titulares** cuyos datos serán tratados.
4. **Plazo de conservación** de los datos. ¿Está justificado? (Principio de limitación
   del plazo — art. 6 inc. 5 Ley 18.331; art. 4 inc. 7 Ley 25.326.)

---

## Paso 4 — Colectivo de titulares y partes

Recopilar:

1. **¿Quiénes son los titulares** de los datos? (Clientes, empleados, usuarios, pacientes,
   niños/adolescentes, público general, personas en situación de vulnerabilidad.)
2. **¿Tienen los titulares la posibilidad real de negarse** al tratamiento? ¿Existe una
   relación de desequilibrio de poder (empleado/empleador, paciente/médico, cliente
   cautivo)?
3. **Destinatarios de los datos:** ¿A quiénes se comunicarán o cederán los datos?
   (Otros responsables, encargados, autoridades públicas, socios comerciales.)
4. **¿Se realizarán transferencias internacionales?** ¿A qué países? ¿Con qué garantías?
   (Nivel de adecuación URCDP/AAIP o garantías contractuales — art. 23-25 Ley 18.331;
   art. 12 Ley 25.326.)

---

## Paso 5 — Tecnología y sistemas

Recopilar:

1. **Sistemas o plataformas** que intervendrán en el tratamiento (bases de datos, CRM,
   plataformas cloud, APIs, dispositivos IoT, cámaras, etc.).
2. **¿Hay toma de decisiones automatizada o perfilado** con efectos jurídicos o
   significativos sobre los titulares? (Scoring crediticio, evaluación de candidatos,
   personalización de precios.) (art. 16 inc. 3 Ley 18.331; art. 20 Ley 25.326.)
3. **¿Se usan tecnologías de reconocimiento biométrico**, geolocalización en tiempo real,
   o monitoreo sistemático?
4. **Arquitectura general del flujo de datos:** ¿Desde dónde se recopilan, cómo se almacenan,
   cómo se procesan, cómo se eliminan?

---

## Paso 6 — Medidas técnicas y organizativas existentes

Recopilar las medidas ya previstas o en implementación:

**Técnicas:**
- Cifrado de datos en tránsito y en reposo
- Seudonimización o anonimización
- Control de acceso basado en roles
- Registro de auditoría (logs)
- Pruebas de penetración / vulnerability assessment
- Backup y recuperación ante desastres
- Otras: ___

**Organizativas:**
- Política de privacidad y protección de datos
- Capacitación del personal en protección de datos
- Registro de actividades de tratamiento
- Procedimiento de gestión de brechas de seguridad
- Procedimiento de gestión de solicitudes ARCO
- Cláusulas de confidencialidad en contratos con personal y proveedores
- Otras: ___

---

## Paso 7 — Identificación de riesgos

Para cada categoría de riesgo, evaluar:
- **Probabilidad:** Alta / Media / Baja
- **Impacto sobre los titulares:** Alto / Medio / Bajo
- **Nivel de riesgo residual** (combinación de probabilidad × impacto):
  Alta × Alto = CRÍTICO; Alta × Medio o Media × Alto = ALTO; Media × Medio = MEDIO; Baja o Bajo = BAJO.

| N.° | Riesgo | Descripción | Prob. | Impacto | Nivel | Medidas existentes | Riesgo residual |
|---|---|---|---|---|---|---|---|
| R1 | Acceso no autorizado a datos | Brecha por ataque externo o error interno | | | | | |
| R2 | Uso excesivo o incompatible de datos | Datos usados más allá de la finalidad declarada | | | | | |
| R3 | Conservación más allá del plazo necesario | Datos retenidos sin justificación tras fin de la finalidad | | | | | |
| R4 | Transferencia a terceros no autorizados | Cesión o acceso por destinatarios no contemplados | | | | | |
| R5 | Toma de decisiones automatizada discriminatoria | Algoritmo produce resultados sesgados con efectos sobre titulares | | | | | |
| R6 | Vulneración de derechos ARCO | Imposibilidad de ejercer acceso, rectificación, cancelación u oposición | | | | | |
| R7 | Falta de transparencia | Los titulares no saben qué datos se tratan ni para qué | | | | | |
| R8 | Transferencia internacional sin garantías | Datos enviados a países sin nivel de protección adecuado | | | | | |
| R9 | [Riesgo específico del tratamiento] | [Descripción] | | | | | |

Completar la tabla con los datos aportados por el usuario y el análisis del contexto.

---

## Paso 8 — Plan de mitigación de riesgos

Para cada riesgo con nivel CRÍTICO, ALTO o MEDIO, proponer medidas de mitigación
adicionales:

| N.° Riesgo | Riesgo | Medida de mitigación | Responsable | Plazo | Riesgo residual esperado |
|---|---|---|---|---|---|
| R1 | Acceso no autorizado | Implementar MFA; segmentar red; cifrar BD en reposo | CISO / IT | [Fecha] | BAJO |
| ... | ... | ... | ... | ... | ... |

Las medidas deben ser concretas, asignadas a un responsable y con plazo definido.

---

## Paso 9 — Consulta a partes interesadas

Verificar si se realizó o debe realizarse consulta previa a:

- Los propios titulares de datos (o sus representantes), especialmente si son personas
  en situación de vulnerabilidad o menores.
- El DPO (Delegado de Protección de Datos) si existe.
- La URCDP o la AAIP, en los casos en que la normativa lo recomiende o exija.
- Otras áreas del cliente (legal, IT, seguridad, compliance).

---

## Paso 10 — Informe de EIA

Producir el informe completo con la siguiente estructura:

```
EVALUACIÓN DE IMPACTO EN LA PRIVACIDAD (EIA)

Proyecto / Tratamiento: [Nombre]
Responsable del tratamiento: [Nombre y domicilio]
Fecha de elaboración: [día/mes/año]
Elaborado por: [Abogado / Estudio]
Versión: 1.0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESUMEN EJECUTIVO
[Tres párrafos: (1) descripción del tratamiento, (2) riesgos principales identificados,
(3) conclusión y condiciones para proceder.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DESCRIPCIÓN DEL TRATAMIENTO
   1.1 Identificación y contexto
   1.2 Finalidad y base legal
   1.3 Datos involucrados y titulares
   1.4 Partes y flujo de datos
   1.5 Tecnología y sistemas

2. ANÁLISIS DE NECESIDAD Y PROPORCIONALIDAD
   [¿El tratamiento es necesario para la finalidad? ¿Los datos recabados son los mínimos
   necesarios? ¿El plazo de conservación es proporcional?]

3. ANÁLISIS DE RIESGOS
   [Tabla de riesgos del Paso 7 completada]

4. MEDIDAS DE MITIGACIÓN
   [Tabla del Paso 8]

5. CONSULTA A PARTES INTERESADAS
   [Resultado del Paso 9]

6. CONCLUSIÓN

   □ PROCEDER: El tratamiento es conforme con la normativa aplicable. Los riesgos
     identificados son bajos y las medidas existentes son suficientes.

   □ PROCEDER CON MEDIDAS: El tratamiento puede iniciarse una vez implementadas
     las siguientes medidas adicionales: [lista]. El responsable debe verificar
     el cumplimiento antes del lanzamiento.

   □ NO PROCEDER: El tratamiento presenta riesgos altos que no pueden mitigarse
     adecuadamente en las condiciones actuales. Se recomienda rediseñar el proyecto
     antes de retomarlo.

7. COMPUERTA DE APROBACIÓN
   [Firmante responsable / DPO / Socio del estudio — campo para completar]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANEXOS
A. Documentación del proyecto aportada
B. Listado de sub-encargados
C. Garantías de transferencias internacionales
D. Otros documentos de soporte
```

---

## Guardrails

- **No emitir la conclusión "PROCEDER"** automáticamente. La conclusión final requiere
  revisión del abogado, quien debe aprobarla antes de comunicarla al cliente.
- **Si el tratamiento involucra datos de menores**, elevar el nivel de riesgo de todos
  los ítems en al menos un nivel y alertar que puede requerirse consulta a la URCDP o AAIP.
- **Si hay toma de decisiones automatizada con efectos jurídicos**, señalar que en Uruguay
  el art. 16 inc. 3 Ley 18.331 otorga derecho a impugnar esas decisiones, y que el
  tratamiento requiere transparencia sobre la lógica aplicada.
- **Si el resultado es "NO PROCEDER"**, escalar al socio de práctica antes de comunicar
  al cliente (ver regla de escalamiento en CLAUDE.md).
- **La EIA es un documento confidencial** del cliente: no compartir su contenido más
  allá del análisis solicitado.
- **No sustituir la consulta con la URCDP o la AAIP** cuando corresponda legalmente
  o sea aconsejable por el nivel de riesgo del tratamiento.
