# Perfil de Práctica — Gobernanza y Regulación de IA

> Este archivo es completado por `/gobernanza-ia:cold-start-interview`.
> Editalo directamente para ajustes pequeños. Cada skill de este plugin lo lee.

## Jurisdicción principal

## Sectores cliente

<!-- Ejemplos: financiero · salud · telecomunicaciones · retail · gobierno · educación · legal tech -->

## Usos de IA en evaluación

<!-- Listar los sistemas o usos de IA que el cliente tiene en evaluación o ya desplegados.
     Ejemplos: scoring crediticio · chatbots de atención · análisis de imágenes médicas ·
     sistemas de selección de personal · modelos de detección de fraude · generación de contenido -->

## Regímenes regulatorios aplicables

### Unión Europea
- Reglamento (UE) 2024/1689 — AI Act (en vigor; aplicación escalonada hasta agosto 2026/2027)
  - Prohibiciones absolutas: art. 5 (usos de IA inaceptables)
  - Sistemas de alto riesgo: Anexo III (listado cerrado con actualización por Comisión)
  - Obligaciones de transparencia: arts. 50-52 (sistemas de interacción con humanos, deepfakes)
  - Gobernanza: autoridades nacionales de supervisión, ENIA, OCEIA

### Argentina
- Ley 27.275 — Acceso a la Información Pública (transparencia algorítmica en sector público)
- Resolución ARCA (ex AFIP) sobre tratamiento automatizado de datos tributarios
- Comunicaciones BCRA sobre uso de IA en entidades financieras (verificar vigencia)
- Ley 25.326 — Protección de Datos Personales: art. 20 (decisiones exclusivamente automatizadas)
- INFOLEG — seguimiento de proyectos de ley sobre IA (pendientes de sanción al 14/05/2026)

### Uruguay
- Ley 18.331 — Protección de Datos Personales: art. 16 (decisiones automatizadas con perfil)
- Decreto 64/020 y normativa AGESIC sobre gobierno digital y ética de IA en sector público
- Circular BCU sobre gestión de riesgos tecnológicos en entidades financieras
- Marco Ético Nacional de IA (MENIA) — documento de principios del MIDES/AGESIC

### Regulación sectorial
- Salud (AR): Disposiciones ANMAT sobre software como dispositivo médico (SaMD); FDA AI/ML SaMD Action Plan como referencia
- Salud (UY): Ministerio de Salud Pública — normativa en desarrollo
- Financiero (AR): BCRA Com. A 7724 sobre gestión de riesgos; CNV sobre robo-advisors
- Financiero (UY): Circular BCU 2407 y normativa de gestión de riesgos tecnológicos
- Telecomunicaciones: ENACOM (AR) / URSEC (UY)

## Umbrales de riesgo

| Nivel | Criterio |
|---|---|
| ALTO | Sistema de IA en Anexo III del AI Act UE · decisión automatizada sin revisión humana que afecte derechos (art. 20 Ley 25.326 AR; art. 16 Ley 18.331 UY) · uso de datos biométricos o sensibles · sistemas de scoring crediticio o de empleo · IA en contexto de salud o seguridad pública · proveedor sin cláusula de opt-out de entrenamiento con datos del cliente |
| MEDIO | Chatbots que no se identifican como IA ante el usuario · modelos generativos con riesgo de alucinación en contexto legal o médico · uso de datos de menores · cláusulas de jurisdicción extranjera en contratos de proveedor IA · sistemas con impacto en grupos vulnerables no evaluado |
| BAJO | Automatización de procesos internos sin impacto en terceros · uso de IA generativa para borrador de documentos internos con revisión humana final · sistemas de recomendación sin efectos vinculantes |

## Playbook de evaluación

### Decisiones automatizadas
- AR: art. 20 Ley 25.326 — derecho a impugnar decisiones adoptadas exclusivamente por medios automatizados que produzcan efectos jurídicos o afecten significativamente al titular.
- UY: art. 16 Ley 18.331 — los titulares tienen derecho a no ser sometidos a decisiones que les afecten significativamente y estén basadas exclusivamente en tratamiento automatizado.
- AI Act UE (si aplica): art. 86 — derecho a explicación en sistemas de alto riesgo.

### Discriminación algorítmica
- Verificar si el modelo usa proxies de categorías protegidas (género, origen étnico, religión).
- Exigir pruebas de equidad (fairness testing) en sistemas de scoring o selección.
- Documentar metodología de detección de sesgos y frecuencia de auditoría.

### Privacidad y minimización de datos
- Verificar que los datos de entrenamiento cumplen con la base jurídica de tratamiento (consentimiento / interés legítimo / contrato).
- Datos sintéticos: verificar que el proceso de síntesis no permite re-identificación.
- Transferencias internacionales: aplicar art. 12 Ley 25.326 (AR) o arts. 23-24 Ley 18.331 (UY).

### Transparencia y explicabilidad
- Exigir documentación técnica del modelo (model card o equivalente).
- Sistemas de alto riesgo (AI Act): obligación de mantener logs técnicos (art. 12).
- Comunicar a los usuarios cuando interactúan con un sistema de IA (art. 50 AI Act; principio de transparencia AGESIC).

## Reglas de escalamiento

| Condición | Acción |
|---|---|
| Sistema clasificado como de alto riesgo bajo AI Act Anexo III | Consultar a [REFERENTE DE PRÁCTICA] antes de emitir opinión final |
| Decisión automatizada sobre empleo, crédito o prestaciones sociales | Derivar análisis a área de privacidad / laboral según corresponda |
| Proveedor de IA con sede exclusiva fuera de AR/UY/UE | Solicitar dictamen sobre transferencias internacionales |
| Cliente del sector salud con IA sobre datos médicos | Coordinar con área regulatoria sanitaria |
| Proyecto con financiamiento público (UY: AGESIC; AR: MTE/MEC) | Verificar requisitos de transparencia y acceso a la información aplicables |

## Estilo de outputs

- Idioma: español rioplatense formal
- Citas normativas: reglamento o ley primero (ej. "art. 5 AI Act UE", "art. 20 Ley 25.326"), doctrina y guías regulatorias como respaldo
- Formato de fecha: día/mes/año (ej. 14/05/2026)
- Evitar gerundio al inicio de oración
- Estructura de ficha de triaje: semáforo → categoría de uso → riesgos identificados → derechos afectados → recomendación → próximos pasos
- Estructura de EIA-IA: descripción del sistema → mapa de partes → inventario de datos → evaluación de riesgos (tabla) → plan de mitigación → cronograma de revisión
- Estructura de revisión de proveedor: tabla de cláusulas con semáforo → issues críticos → cláusulas sugeridas
- Nunca afirmar que un sistema "cumple" la regulación sin reserva; siempre indicar que la opinión está sujeta a revisión por el abogado actuante y a la evolución normativa

## Referente de práctica de gobernanza IA

## Notas adicionales

- El AI Act UE aplica a sistemas de IA que afecten a personas ubicadas en la UE, independientemente del lugar de establecimiento del proveedor u operador — verificar si los clientes tienen presencia o clientes en la UE.
- En Argentina, la regulación de IA es fragmentaria al 14/05/2026; monitorear el avance legislativo y las resoluciones sectoriales (BCRA, CNV, ANMAT, ARCA).
- En Uruguay, el MENIA es un documento de principios sin efecto vinculante; las obligaciones concretas surgen de la Ley 18.331 y la normativa sectorial (BCU, URSEC).
- Los proyectos de IA generativa (LLMs, modelos multimodales) que no son de alto riesgo pueden igualmente generar obligaciones de transparencia bajo art. 50 AI Act si interactúan con personas naturales.
