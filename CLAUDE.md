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
- **Duración estándar**: vigencia del contrato más 3 años; para información que
  constituye secreto comercial o know-how, plazo indefinido o mientras conserve
  el carácter confidencial.
- **Alcance**: toda información marcada como confidencial o que por su naturaleza
  deba entenderse como tal. Incluir expresamente: datos personales de clientes,
  código fuente, fórmulas, estructuras de precios y estrategias comerciales.
- **Excepciones estándar aceptables**: información de dominio público (sin culpa del
  receptor), información ya conocida por el receptor antes de la divulgación,
  información recibida lícitamente de terceros, divulgación requerida por autoridad
  competente (con notificación previa a la parte divulgante si es posible).
- **Riesgo MEDIO**: ausencia de plazo de confidencialidad post-contractual, o alcance
  tan amplio que incluya información generada independientemente por el receptor.
- **Referencia normativa**: Ley 17.616 (UY — derechos de autor y secreto); CCyCN
  art. 1063 (AR — buena fe contractual); Ley 24.766 (AR — confidencialidad).

### Propiedad intelectual
- **Desarrollos bajo encargo**: los derechos patrimoniales sobre las obras creadas
  en ejecución del contrato corresponden al comitente, salvo pacto en contrario.
  Incluir cláusula de cesión expresa de todos los derechos de explotación.
- **Software preexistente del proveedor**: el proveedor retiene la titularidad;
  se otorga al cliente una licencia de uso no exclusiva, intransferible y limitada
  al objeto del contrato. Verificar que la licencia cubra todos los usos previstos.
- **Desarrollos mixtos (preexistente + nuevo)**: distinguir claramente en el contrato
  qué es preexistente (del proveedor) y qué es desarrollo específico (del cliente).
  Evitar cláusulas que confundan ambas categorías.
- **Marcas y nombre comercial**: prohibir expresamente el uso de marcas de la
  contraparte sin autorización escrita. Incluir cláusula de no afectación de marcas.
- **Riesgo ALTO**: cláusulas que transfieran al proveedor derechos sobre datos o
  desarrollos del cliente; licencias de software sin especificar alcance de uso.
- **Referencia normativa**: Ley 9.739 (UY — derechos de autor); Ley 11.723
  (AR — propiedad intelectual); Ley 17.164 (UY — patentes); Ley 24.481 (AR — patentes).

## Reglas de escalamiento

| Condición | Acción |
|---|---|
| Contrato > USD 500.000 | Consultar al socio principal del estudio antes de emitir opinión |
| Contrato > USD 100.000 con cláusulas de responsabilidad inusuales | Revisión por socio del área |
| Arbitraje internacional (fuera de UY/AR) | Consultar área de litigio internacional |
| Cambio de ley aplicable a ley extranjera | Consultar senior y evaluar necesidad de corresponsal |
| Due diligence M&A con valor de deal > USD 1.000.000 | Involucrar socio responsable de M&A |
| Contrato con cláusula penal > 20% del valor total | Revisión por socio antes de aceptar |
| Renuncia a fuero o jurisdicción local | Consultar senior; rechazar salvo caso justificado |

## Estilo de outputs

- Idioma: español rioplatense formal
- Citas: Código primero (ej. "art. 1291 CC" o "art. 1 LSC"), doctrina como respaldo
- Formato de fecha: día/mes/año
- Evitar gerundio al inicio de oración
- Memo: resumen ejecutivo (3 líneas) → issues críticos → observaciones cláusula a cláusula → cláusulas sugeridas

## Documentos semilla

<!-- Reemplazá estas rutas por los documentos reales del estudio una vez disponibles -->

- `docs/modelos/NDA-bilateral-UY-AR-modelo.docx` — NDA bilateral modelo para operaciones trans-fronterizas
- `docs/modelos/MSA-servicios-tecnologicos-modelo.docx` — MSA de servicios tecnológicos con anexo SOW
- `docs/modelos/SPA-cuotas-sociales-UY-modelo.docx` — compraventa de cuotas sociales LSC Ley 16.060
- `docs/playbook/clausulas-criticas-playbook.md` — posiciones del estudio por tipo de cláusula
- `docs/memos/memo-revision-tipo.docx` — memo de revisión contractual con formato estándar del estudio

## Notas adicionales

- **Moneda de referencia**: USD para contratos trans-fronterizos y operaciones M&A;
  UYU o ARS para contratos de servicios locales. En contratos con precio en moneda local,
  incluir cláusula de ajuste si el contrato supera los 12 meses.
- **Notificaciones**: siempre por escrito; correo electrónico con acuse de recibo es
  suficiente para notificaciones ordinarias; carta documento o telegrama colacionado
  para notificaciones de rescisión o recisión.
- **Firma**: admitir firma electrónica avanzada (Ley 18.600 UY; Ley 25.506 AR) para
  todos los contratos salvo los que exijan escritura pública.
- **Revisión de contratos de contraparte**: siempre usar el formato de memo estándar
  del estudio (resumen ejecutivo → issues críticos → observaciones cláusula a cláusula
  → cláusulas sugeridas). No emitir opinión verbal antes de tener el memo redactado.
- **Conflicto de interés**: antes de iniciar cualquier revisión, verificar en el registro
  de clientes del estudio si la contraparte es o fue cliente. En caso afirmativo, escalar
  al socio principal antes de continuar.
