---
name: evaluacion-impacto-ia
description: >
  Conduce una Evaluación de Impacto de IA (EIA-IA) completa. Recopila descripción del sistema,
  finalidad, datos de entrenamiento e inferencia, partes involucradas, supervisión humana y
  mecanismos de impugnación. Evalúa riesgos de discriminación algorítmica, privacidad,
  seguridad y responsabilidad. Produce informe con plan de mitigación y cronograma de revisión.
argument-hint: "[nombre o descripción del sistema de IA a evaluar] [--sector=financiero|salud|rrhh|publico|otro]"
user-invocable: true
---

# Skill: Evaluación de Impacto de IA (EIA-IA)

## Propósito

Conducir una evaluación estructurada del impacto regulatorio, de derechos y de riesgos de un sistema de IA antes de su despliegue o durante su operación. La EIA-IA es la herramienta de debida diligencia central para sistemas de alto riesgo bajo el AI Act (Anexo III) y para cualquier sistema que adopte decisiones automatizadas con efectos sobre personas físicas en el marco de las leyes de protección de datos de Argentina (Ley 25.326) y Uruguay (Ley 18.331).

---

## Paso 0 — Verificación de prerrequisitos

1. Verificar si se realizó previamente el triaje con `/gobernanza-ia:triaje-uso-ia`. Si el resultado fue ROJO (prohibido), detener la EIA-IA y remitir al referente de práctica.
2. Confirmar que el abogado actuante está presente para supervisar el proceso.
3. Informar al usuario que la EIA-IA se conduce en módulos; puede pausarse y retomarse en sesiones sucesivas.

---

## Paso 1 — Descripción del sistema

Recopilar la siguiente información:

**1.1 Identificación del sistema**
- Nombre del sistema o proyecto
- Versión o estado de desarrollo (prototipo / piloto / producción)
- Nombre del proveedor o equipo de desarrollo
- Fecha prevista de despliegue o fecha en que ya está en operación

**1.2 Finalidad y contexto**
- ¿Cuál es el propósito del sistema? ¿Qué problema resuelve?
- ¿En qué contexto organizacional se desplegará? (proceso de negocio afectado)
- ¿Existe algún sistema previo que reemplace o complemente?

**1.3 Funcionamiento técnico (nivel de detalle accesible)**
- Tipo de modelo: clasificación / regresión / generación / reconocimiento / agrupamiento / otro
- ¿El modelo aprende continuamente (online learning) o es estático (batch training)?
- ¿El sistema puede explicar sus outputs? ¿Qué nivel de explicabilidad provee?

---

## Paso 2 — Mapa de partes y flujo de datos

**2.1 Partes involucradas**

| Rol | Nombre/descripción | Obligaciones bajo AI Act | Obligaciones bajo Ley 25.326/18.331 |
|---|---|---|---|
| Proveedor del sistema IA | | | |
| Operador / deployer | | | |
| Importador (si aplica) | | | |
| Distribuidores | | | |
| Personas afectadas (sujetos) | | | |
| Autoridad supervisora | | | |

**2.2 Flujo de datos**
- ¿De dónde provienen los datos de entrenamiento? (fuentes, datasets, origen)
- ¿Los datos de entrenamiento incluyen datos personales? ¿Cuál fue la base jurídica del tratamiento?
- ¿De dónde provienen los datos de inferencia (datos de entrada en producción)?
- ¿Dónde se almacenan los datos? (ubicación geográfica de los servidores)
- ¿Existen transferencias internacionales de datos? ¿A qué países?
- ¿Cuánto tiempo se retienen los datos y los logs del sistema?

---

## Paso 3 — Evaluación de riesgos

Completar la siguiente tabla de riesgos. Para cada riesgo: describir el escenario, evaluar la probabilidad (Alta/Media/Baja), el impacto (Alto/Medio/Bajo) y la calificación resultante.

### 3.1 Discriminación algorítmica

| Escenario de riesgo | Probabilidad | Impacto | Calificación | Evidencia o indicios |
|---|---|---|---|---|
| El modelo replica sesgos presentes en los datos de entrenamiento (ej. datos históricos con subrepresentación de grupos) | | | | |
| El modelo usa proxies de categorías protegidas (ej. código postal como proxy de origen étnico) | | | | |
| El modelo produce tasas de error diferenciadas entre grupos demográficos (disparate impact) | | | | |
| Los datos de entrenamiento provienen de períodos o contextos con prácticas discriminatorias | | | | |

**Base normativa:** art. 16 Constitución Nacional (AR); art. 8 Constitución UY; art. 21 Carta Derechos Fundamentales UE; OCDE — Principios de IA (pilar de equidad); AI Act Anexo III aplica para empleo, acceso a crédito, educación.

### 3.2 Privacidad y protección de datos

| Escenario de riesgo | Probabilidad | Impacto | Calificación | Norma aplicable |
|---|---|---|---|---|
| Tratamiento sin base jurídica válida (falta de consentimiento o habilitación legal) | | | | Ley 25.326 art. 5 / Ley 18.331 art. 9 |
| Recolección de más datos de los necesarios (exceso del principio de minimización) | | | | Ley 25.326 art. 4 / Ley 18.331 art. 8 |
| Uso de datos sensibles sin consentimiento expreso o excepción legal habilitante | | | | Ley 25.326 art. 7 / Ley 18.331 art. 18 |
| Re-identificación de datos supuestamente anonimizados | | | | Aplica a ambas jurisdicciones |
| Transferencia internacional sin garantías adecuadas | | | | Ley 25.326 art. 12 / Ley 18.331 arts. 23-24 |
| Retención de datos más allá del plazo necesario | | | | Principio de limitación del plazo, ambas leyes |
| Brecha de seguridad sin plan de respuesta ni notificación a titulares | | | | Ley 25.326 art. 9 / Ley 18.331 art. 10 |

### 3.3 Seguridad y robustez

| Escenario de riesgo | Probabilidad | Impacto | Calificación | Medida técnica disponible |
|---|---|---|---|---|
| Ataques adversariales (manipulación deliberada del input para engañar al modelo) | | | | |
| Model poisoning durante el entrenamiento | | | | |
| Extracción de datos de entrenamiento mediante consultas (model inversion) | | | | |
| Dependencia de proveedor externo sin continuidad garantizada (single point of failure) | | | | |
| Degradación no detectada del rendimiento del modelo (model drift) | | | | |

**Base normativa:** AI Act arts. 9 y 15 (robustez, seguridad y exactitud para sistemas de alto riesgo); Ley 25.326 art. 9 / Ley 18.331 art. 10 (medidas de seguridad).

### 3.4 Responsabilidad por errores

| Escenario de riesgo | Probabilidad | Impacto | Calificación | Observaciones |
|---|---|---|---|---|
| El sistema produce un output erróneo que causa daño a una persona física | | | | |
| El contrato con el proveedor excluye o limita la responsabilidad por outputs incorrectos | | | | |
| No existe mecanismo para que el afectado impugne o solicite revisión de la decisión automatizada | | | | |
| Los logs no permiten reconstruir qué input produjo qué output (falta de auditabilidad) | | | | |
| Responsabilidad civil no está asignada claramente entre proveedor y operador | | | | |

**Base normativa:** AI Act arts. 9, 12 y 17 (sistema de gestión de riesgos, logs, documentación técnica); CCyCN art. 1757 (responsabilidad por riesgo de la cosa / actividad riesgosa); Ley 18.331 art. 16 (derecho de impugnación de decisiones automatizadas).

### 3.5 Impacto en derechos laborales (si el sistema involucra a empleados)

| Escenario de riesgo | Probabilidad | Impacto | Calificación | Norma |
|---|---|---|---|---|
| Monitoreo de empleados sin información previa ni consentimiento | | | | Ley 20.744 LCT art. 75 (AR); Código del Trabajo (UY) |
| Decisiones de despido, calificación o ascenso basadas exclusivamente en IA sin revisión humana | | | | AI Act Anexo III, punto 4 |
| Uso de IA en negociaciones colectivas o control de actividad sindical | | | | Art. 14 bis CN (AR); Convenios OIT 87 y 98 |

---

## Paso 4 — Supervisión humana y mecanismos de impugnación

**4.1 Nivel de autonomía del sistema**

| Nivel | Descripción | Clasificación del sistema |
|---|---|---|
| Automatización total | El sistema actúa sin intervención humana en ningún caso | |
| Supervisión humana en la excepción | Revisión humana solo cuando el sistema lo solicita o falla | |
| Supervisión humana siempre | Cada output es revisado por una persona antes de tener efecto | |
| Asistencia al humano | El sistema provee información, la decisión siempre la toma el humano | |

**4.2 Mecanismos de impugnación existentes o proyectados**

- ¿Puede el afectado solicitar revisión humana de una decisión automatizada?
- ¿Existe un canal de reclamo identificado y accesible?
- ¿El plazo para impugnar es razonable y está comunicado al afectado?
- ¿Qué ocurre con los efectos de la decisión automatizada mientras tramita la impugnación?

**Base normativa:** art. 20 Ley 25.326 (AR) — derecho a impugnar y obtener revisión; art. 16 Ley 18.331 (UY) — ídem; art. 86 AI Act (derecho a explicación para sistemas de alto riesgo).

---

## Paso 5 — Plan de mitigación

Para cada riesgo calificado como ALTO o MEDIO, definir:

| Riesgo | Medida de mitigación | Responsable | Plazo | Indicador de cumplimiento |
|---|---|---|---|---|
| [Riesgo identificado] | [Medida concreta: técnica / organizacional / contractual / comunicacional] | [Área o persona] | [Fecha o período] | [Cómo se verifica] |

**Medidas típicas por categoría:**

- Discriminación: auditoría de sesgos antes del despliegue; pruebas de equidad (accuracy parity, equal opportunity); diversificación del dataset; revisión humana para casos límite (near-threshold cases)
- Privacidad: seudonimización o anonimización de datos de entrenamiento; contrato de encargado de tratamiento con el proveedor; registro de actividades de tratamiento; DPIA si corresponde
- Seguridad: penetration testing del modelo; monitoreo de model drift; plan de respuesta a incidentes; SLA de continuidad con el proveedor
- Responsabilidad: cláusulas contractuales de asignación de responsabilidad; seguro de responsabilidad civil; mecanismo de impugnación operativo y comunicado
- Transparencia: aviso claro al usuario de que interactúa con IA; documentación del modelo (model card); logs técnicos con retención mínima de 6 meses para sistemas de alto riesgo (AI Act art. 12)

---

## Paso 6 — Output: informe EIA-IA

Producir el siguiente informe:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORME — EVALUACIÓN DE IMPACTO DE IA (EIA-IA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fecha del informe:         [DD/MM/AAAA]
Sistema evaluado:          [nombre y versión]
Cliente / Organización:    [nombre]
Abogado actuante:          [nombre — a completar]
Revisión próxima:          [fecha sugerida, máx. 12 meses o ante cambio material del sistema]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESUMEN EJECUTIVO
[3-5 líneas: descripción del sistema, clasificación de riesgo general y recomendación principal]

CLASIFICACIÓN REGULATORIA
[AI Act: prohibido / alto riesgo / transparencia / uso general / no aplica]
[Ley 25.326 / Ley 18.331: decisión automatizada con efectos sí/no; datos sensibles sí/no]

MAPA DE RIESGOS (resumen)
| Categoría | Calificación | Issues principales |
|---|---|---|
| Discriminación algorítmica | ALTO / MEDIO / BAJO / N/E | |
| Privacidad y datos personales | ALTO / MEDIO / BAJO / N/E | |
| Seguridad y robustez | ALTO / MEDIO / BAJO / N/E | |
| Responsabilidad por errores | ALTO / MEDIO / BAJO / N/E | |
| Derechos laborales | ALTO / MEDIO / BAJO / N/A | |

ISSUES CRÍTICOS (calificación ALTO)
[Lista de issues con referencia normativa y medida de mitigación requerida]

PLAN DE MITIGACIÓN
[Tabla del Paso 5 con responsables y plazos]

MECANISMOS DE IMPUGNACIÓN
[Descripción del mecanismo existente o propuesto; gaps identificados]

CRONOGRAMA DE REVISIÓN
- Primera revisión post-despliegue: [fecha]
- Revisión periódica: [cada X meses]
- Revisión extraordinaria: ante cambio material del modelo, del dataset o del marco regulatorio

ADVERTENCIA
Este informe es de análisis preliminar y no reemplaza la opinión legal del abogado
actuante. La evaluación se basa en la información provista por el cliente; hallazgos
adicionales pueden surgir de una auditoría técnica del modelo. El marco regulatorio de
IA está en evolución — verificar actualizaciones al momento de implementar las medidas.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- No emitir el informe final sin que el abogado actuante haya confirmado la revisión — incluir siempre la compuerta de aprobación profesional.
- Si el sistema cae en la categoría prohibida del AI Act art. 5: detener la evaluación, emitir resultado ROJO y escalar al referente de práctica configurado en CLAUDE.md.
- No acceder a código fuente, modelos descargados ni datos de entrenamiento del cliente a través de esta skill — el análisis se basa en la información que el usuario provee.
- Si el cliente no puede proveer información sobre los datos de entrenamiento (ej. modelo de tercero como caja negra): consignar la brecha de información en el informe y recomendar solicitar documentación técnica al proveedor antes de desplegar.
- Nunca afirmar que el sistema "cumple" el AI Act o la Ley 25.326/18.331 — siempre indicar que el análisis es preliminar y sujeto a revisión por la autoridad competente.
- Si el riesgo de discriminación es ALTO y el sistema ya está en producción: recomendar suspensión preventiva hasta implementar las medidas de mitigación.
