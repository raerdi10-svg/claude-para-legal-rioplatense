# Perfil de Práctica — Civil y Comercial Rioplatense

> Este archivo es completado por `/civil-comercial:cold-start-interview`.
> Editalo directamente para ajustes pequeños. Cada skill de este plugin lo lee.

## Jurisdicción principal
Ambas — operaciones trans-fronterizas Uruguay / Argentina.

- **Uruguay:** CC (Código Civil), CGP (Código General del Proceso), LSC Ley 16.060,
  Ley 18.331 (datos personales), Ley 17.250 (relaciones de consumo).
- **Argentina:** CCyCN (Código Civil y Comercial de la Nación), LGS Ley 19.550,
  CPCCN, Ley 25.326 (datos personales), Ley 24.240 (defensa del consumidor).

Sede del estudio: Montevideo. Foro preferido: tribunales locales de cada jurisdicción;
arbitraje nacional ante el CAM (UY) o el CEMARC (AR) para disputas comerciales de
cuantía superior a USD 200.000.

## Tipos de contrato más frecuentes
- Acuerdos de confidencialidad (NDAs) — operaciones M&A y joint ventures
- Contratos de servicios tecnológicos (MSAs, SOWs, SaaS)
- Acuerdos de distribución y representación comercial (UY y AR)
- Contratos de compraventa de participaciones sociales (SPAs)
- Contratos de obra y servicios de construcción
- Contratos de licencia de propiedad intelectual y software
- Acuerdos de accionistas y pactos parasociales
- Contratos de arrendamiento comercial e industrial

## Umbrales de riesgo

| Nivel | Criterio |
|---|---|
| ALTO | Cláusulas de responsabilidad ilimitada · arbitraje en jurisdicción extranjera · renuncia a fuero · cambio material no notificado |
| MEDIO | Plazos de prescripción modificados · garantías amplias · cláusulas penales > 20% del contrato · moneda de pago inusual |
| BAJO | Modificaciones menores de forma · ajustes de protocolo de notificación · cambios de dirección |

## Playbook de cláusulas críticas

### Responsabilidad
Posición predeterminada del estudio para contratos de servicios:

- **Cap de responsabilidad**: limitar la responsabilidad total de nuestro cliente al monto
  pagado en los últimos 12 meses bajo el contrato, o al valor del contrato si es de suma fija.
- **Exclusiones obligatorias**: excluir daños indirectos, lucro cesante, pérdida de datos y
  daño a la reputación, salvo dolo o culpa grave.
- **Indemnización**: cláusula recíproca; rechazar indemnización unilateral a favor de la
  contraparte sin cap ni exclusiones. Si se acepta, exigir que esté sujeta al mismo cap
  de responsabilidad general.
- **Riesgo ALTO**: cualquier cláusula de responsabilidad ilimitada o que excluya el cap
  para categorías amplias (ej. "toda violación al contrato"). Escalar siempre.

### Rescisión
- **Preaviso mínimo para rescisión sin causa**: 30 días para contratos de hasta 1 año;
  60 días para contratos de más de 1 año; 90 días para contratos de más de 3 años.
- **Rescisión inmediata (justa causa)**: incumplimiento material no subsanado en 15 días
  tras notificación fehaciente; insolvencia, concurso o quiebra de la contraparte;
  cambio de control sin consentimiento (si el contrato lo prevé).
- **Consecuencias de rescisión sin causa**: pago de servicios devengados hasta la fecha;
  no procede indemnización adicional salvo pacto expreso. Rechazar cláusulas de
  "break-up fee" superiores al 5% del valor total del contrato sin justificación.
- **Referencia normativa**: CC art. 1291 (UY — rescisión bilateral); CCyCN art. 1078
  (AR — extinción del contrato); CCyCN art. 1011 (AR — contratos de duración).

### Ley aplicable y jurisdicción
- **Preferencia de ley**: ley del domicilio del cliente; en contratos trans-fronterizos
  UY/AR, negociar ley uruguaya como primera opción (mayor certeza para el estudio),
  ley argentina como alternativa aceptable.
- **Preferencia de foro**: juzgados ordinarios del domicilio del cliente para contratos
  de mediana cuantía (hasta USD 200.000). Para contratos de mayor cuantía, arbitraje
  ante CAM (Montevideo) o CEMARC (Buenos Aires) según la sede de la contraparte.
- **Riesgo ALTO**: sumisión a jurisdicción extranjera (fuera de UY/AR), arbitraje en
  sede internacional (ICC, AAA, LCIA) sin consulta previa al área de litigio del estudio.
- **Renuncia al fuero**: rechazar sistemáticamente; si la contraparte insiste, escalar.
- **Referencia normativa**: Ley 19.920 (DIPr UY); CCyCN arts. 2594 y ss. (DIPr AR).

### Confidencialidad
<!-- Duración, alcance, excepciones estándar -->

### Propiedad intelectual
<!-- Titularidad de desarrollos, licencias, obras por encargo -->

## Reglas de escalamiento

| Condición | Acción |
|---|---|
| Contrato > USD [MONTO] | Consultar a [NOMBRE SOCIO/ÁREA] |
| Arbitraje internacional | Consultar área de litigio |
| Cambio de ley aplicable | Consultar senior |

## Estilo de outputs

- Idioma: español rioplatense formal
- Citas: Código primero (ej. "art. 1291 CC" o "art. 1 LSC"), doctrina como respaldo
- Formato de fecha: día/mes/año
- Evitar gerundio al inicio de oración
- Memo: resumen ejecutivo (3 líneas) → issues críticos → observaciones cláusula a cláusula → cláusulas sugeridas

## Documentos semilla

<!-- Rutas a contratos firmados de referencia, playbook de cláusulas, memos de revisión anteriores -->

## Notas adicionales

<!-- Cualquier otra instrucción específica para tu práctica -->
