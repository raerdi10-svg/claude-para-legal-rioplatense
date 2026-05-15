# Perfil de Práctica — Derecho Administrativo Rioplatense

> Este archivo es completado por `/administrativo:cold-start-interview`.
> Editalo directamente para ajustes pequeños. Cada skill de este plugin lo lee.

## Jurisdicción principal

## Organismos habituales

### Uruguay
- Ministerios del Poder Ejecutivo (MEC, MIDES, MEF, MTOP, MSP, MGA, MRREE, MI, MDN)
- Entes Autónomos: BCU, ANCAP, ANTEL, OSE, UTE, ANP, LATU
- Servicios Descentralizados: ASSE, ANEP, UTU, BHU, BPS
- Intendencias departamentales
- Tribunal de lo Contencioso Administrativo (TCA)
- Tribunal Administrativo de Contrataciones Públicas (TACP)

### Argentina
- Organismos del Poder Ejecutivo Nacional (AFIP/ARCA, ANSES, BCRA, CNV, ENARGAS, ENRE, ENACOM)
- Ministerios nacionales
- Entes reguladores sectoriales
- Cámara Nacional en lo Contencioso Administrativo Federal (Cámara CAF)
- Cámara Federal de Apelaciones (según fuero)
- Procuración del Tesoro de la Nación

## Tipo de actos impugnados

- [ ] Actos de alcance individual (resoluciones, disposiciones, habilitaciones)
- [ ] Actos de alcance general (reglamentos, instrucciones)
- [ ] Actos de trámite que causan indefensión
- [ ] Omisiones / silencio administrativo
- [ ] Actos en materia de contratación pública / licitaciones
- [ ] Actos en materia sancionatoria (sumarios, multas)
- [ ] Actos en materia de empleo público
- [ ] Actos en materia impositiva o aduanera

## Umbrales de riesgo

| Nivel | Criterio |
|---|---|
| ALTO | Plazo de recurso con menos de 5 días hábiles · acto que causa lesión irreparable (inhabilitación, clausura, pérdida de licencia) · silencio administrativo que habilita acceso a sede jurisdiccional · acto con vicios de nulidad absoluta · contratación pública con adjudicación inminente |
| MEDIO | Acto sancionatorio con multa entre [MONTO BAJO] y [MONTO ALTO] · exigencia de garantías desproporcionadas · resolución de sumario con posibilidad de impugnación · plazos de recurso entre 6 y 15 días hábiles |
| BAJO | Actos de trámite sin efecto definitivo · pedidos de información o prórroga · ajustes de plazo por fuerza mayor |

## Playbook de vías impugnativas

### Uruguay — Vía administrativa
- Recurso de revocación (art. 317 Constitución; arts. 154-160 Decreto 500/991): 10 días hábiles desde notificación.
- Recurso jerárquico: 10 días hábiles desde resolución o silencio del recurso de revocación.
- Denuncia de mora (Ley 15.869, art. 8): exigir resolución cuando la Administración no responde en plazo legal.

### Uruguay — Vía jurisdiccional
- Acción de nulidad ante el TCA (art. 309 Constitución; Ley 15.869): 60 días corridos desde agotamiento de la vía administrativa.
- Acción reparatoria patrimonial ante Juzgados Civiles: independiente de la anulación; plazo de prescripción general de 4 años (art. 1216 CC).

### Argentina — Vía administrativa
- Recurso de reconsideración (art. 84 RLPA — Decreto 1759/72): 10 días hábiles.
- Recurso jerárquico (arts. 89-93 RLPA): 15 días hábiles.
- Recurso de alzada contra actos de entes descentralizados (arts. 94-98 RLPA): 15 días hábiles.
- Recurso de queja (art. 71 LPA): sin plazo fijo; aconsejable dentro de 5 días de la demora.

### Argentina — Vía jurisdiccional
- Acción contencioso-administrativa federal (Ley 26.944; Código Contencioso Administrativo): ante Cámara CAF, plazo 90 días hábiles judiciales desde agotamiento.
- Acción de amparo (art. 43 CN; Ley 16.986): cuando haya urgencia y violación manifiesta de derechos.

## Reglas de escalamiento

| Condición | Acción |
|---|---|
| Plazo fatal < 5 días hábiles | Escalar de inmediato al socio a cargo; suspender otras tareas del caso |
| Contrato o concesión > [MONTO] | Consultar al socio a cargo antes de presentar |
| Acto con efectos sobre licencias o habilitaciones clave | Evaluar medida cautelar de urgencia; derivar a litigio |
| Arbitraje internacional (CIADI, CNUDMI) | Consultar área especializada en inversiones |
| Acción de amparo potencial | Revisar con socio senior; coordinar con litigio constitucional |

## Estilo de outputs

- Idioma: español rioplatense formal
- Citas normativas: código o norma primero (ej. "art. 317 Constitución UY", "art. 84 RLPA", "art. 7 LPA"), doctrina y jurisprudencia del TCA o Cámara CAF como respaldo
- Formato de fecha: día/mes/año (ej. 14/05/2026)
- Evitar gerundio al inicio de oración
- Estructura de escrito: encabezado → legitimación → acto impugnado → agravios (nulidad primero, mérito después) → petitorio
- Estructura de memo: resumen ejecutivo (3 líneas) → árbol de recurso recomendado → tabla de plazos → escrito base → compuerta de aprobación
- Nunca afirmar que el recurso "va a prosperar"; solo que está correctamente formulado
- Siempre alertar si el plazo fatal está próximo a vencer

## Socio / referente de práctica administrativa

## Notas adicionales

- En Uruguay, los plazos del Decreto 500/991 son de días hábiles administrativos (excluyen sábados, domingos y feriados nacionales y departamentales).
- En Argentina, el Decreto 1759/72 (texto ordenado 2017) es la norma de procedimiento; verificar siempre si el ente tiene reglamento propio más específico.
- La TCA uruguaya solo tiene competencia anulatoria; la acción de reparación patrimonial tramita ante la justicia civil.
- En materia de contratación pública (TOCAF en UY; Ley 13.064 y Decreto Delegado 1023/01 en AR), los plazos de impugnación de pliegos y adjudicaciones son brevísimos — verificar siempre.
