# Perfil de Práctica — Civil y Comercial Rioplatense

> Completado por `/civil-comercial:cold-start-interview`. Editá directamente para ajustes menores.
> Cada skill de este plugin lee este archivo antes de actuar.

---

## Jurisdicción principal

Argentina (CCyCN, Ley 26.994) y Uruguay (Código Civil, Ley 18.159).
Para contratos transfronterizos entre ambos países se aplican ambos marcos, con prioridad a la ley elegida por las partes (art. 2651 CCyCN; art. 2399 CC uruguayo).

---

## Tipos de contrato más frecuentes

- Contratos de compraventa de mercaderías (doméstica e internacional)
- Contratos de distribución y agencia comercial
- Contratos de prestación de servicios profesionales y tecnológicos
- Contratos de locación de obra y servicios (arts. 1251-1279 CCyCN)
- Acuerdos de confidencialidad (NDA) unilaterales y bilaterales
- Contratos de licencia de software y propiedad intelectual
- Contratos de joint venture contractual (sin personalidad jurídica)
- Contratos de cesión de créditos y posición contractual (arts. 1614-1623 CCyCN)
- Contratos de franquicia (art. 1512 CCyCN)
- Contratos de suministro (arts. 1176-1186 CCyCN)

---

## Umbrales de riesgo

| Nivel | Criterio |
|---|---|
| ALTO | Cláusulas de responsabilidad ilimitada o exclusión total de responsabilidad · arbitraje en jurisdicción extranjera o CIADI · renuncia a fuero ordinario sin contraprestación · cambio material de objeto contractual no notificado · penalidades > 30 % del valor del contrato · plazos de garantía que exceden el doble del estándar legal |
| MEDIO | Plazos de prescripción modificados fuera del rango CCyCN (arts. 2532-2559) · garantías amplias sin límite de monto · cláusulas penales entre 20 % y 30 % del contrato · moneda de pago inusual o indexación a índice extranjero · obligaciones de exclusividad sin plazo definido · cláusulas de auditoría sin límite temporal |
| BAJO | Modificaciones menores de forma o protocolo · ajustes de dirección o contacto · cambios en numeración de cláusulas sin alteración sustantiva · precisiones de definiciones que no amplían obligaciones |

---

## Playbook de cláusulas críticas

### Responsabilidad

**Argentina (CCyCN):**
- Art. 1728: en contratos celebrados en el marco de actividad profesional, la responsabilidad por consecuencias no previsibles al momento de contratar no puede excluirse cuando existe dolo o culpa grave.
- Art. 1743: las cláusulas de exoneración de responsabilidad son válidas salvo que: (i) afecten derechos de terceros, (ii) atenten contra la buena fe, o (iii) estén prohibidas por ley especial.
- Art. 1744: la cláusula penal excesiva puede ser reducida judicialmente (principio de reducibilidad).
- Posición del estudio: rechazar toda exoneración total de responsabilidad en contratos B2B; aceptar topes razonables (cap de responsabilidad) no inferiores al valor del contrato en los últimos 12 meses.

**Uruguay (Código Civil):**
- Art. 1341 CC: las partes pueden limitar la responsabilidad pero no excluirla por dolo.
- Criterio de cláusulas abusivas: Ley 17.250 (relaciones de consumo) y, por analogía, Ley 18.159 (defensa de la competencia) para contratos entre empresas.
- Posición del estudio: idéntica a Argentina; verificar cláusulas de limitación en contratos de adhesión bajo art. 1291 CC uruguayo.

### Rescisión

**Argentina (CCyCN):**
- Art. 1077: las partes pueden resolver el contrato cuando la otra incumple; requiere constitución en mora (art. 886-888) salvo plazo esencial.
- Art. 1078: resolución extrajudicial mediante declaración recepticia al deudor.
- Art. 1079: la parte que resuelve puede reclamar daños y perjuicios.
- Art. 1091: en contratos de larga duración, imprevisión que altera la ecuación económica habilita revisión o resolución.
- Art. 1092: contratos de adhesión — cláusulas de rescisión unilateral injustificada a favor de solo una parte son presuntamente abusivas.
- Posición del estudio: exigir preaviso mínimo de 30 días para rescisión sin causa; derecho a subsanar incumplimiento en 15 días antes de que sea efectiva la rescisión por causa.

**Uruguay (Código Civil):**
- Art. 1431 CC: pacto comisorio expreso o tácito.
- Art. 1549 CC: resolución por incumplimiento.
- Posición del estudio: igual criterio de preaviso; en contratos de distribución, verificar Ley 17.250 y doctrina sobre agentes.

### Ley aplicable y jurisdicción

- Contratos puramente argentinos: CABA — Tribunales Ordinarios en lo Comercial.
- Contratos puramente uruguayos: Montevideo — Juzgados Letrados de Primera Instancia en lo Civil.
- Contratos transfronterizos: si las partes eligen arbitraje, verificar sede (Buenos Aires vs. Montevideo), reglamento (CNUDMI, CCI, CAM) y ley sustantiva aplicable.
- Alerta ALTO: cualquier cláusula que someta a jurisdicción extranjera fuera de la región (ej. Nueva York, Londres) sin justificación de negocio.
- Alerta ALTO: renuncia a fuero del domicilio del consumidor si alguna parte puede calificar como tal.

### Confidencialidad

- Definición de "información confidencial": debe ser precisa; evitar fórmulas omnicomprensivas como "toda información intercambiada" sin exclusiones razonables.
- Exclusiones mínimas obligatorias: (i) información en dominio público, (ii) conocida previamente por el receptor, (iii) recibida lícitamente de tercero, (iv) desarrollada independientemente, (v) divulgada por exigencia legal o judicial.
- Plazo: razonable según sector; en tecnología, máximo 3 años post-vencimiento; en farma/biotech, hasta 5 años.
- Obligaciones post-vencimiento: destrucción o devolución de soportes; plazo máximo 30 días desde solicitud.
- Datos personales: verificar si la información confidencial incluye datos personales (Ley 25.326 AR; Ley 18.331 UY) y si corresponde incluir cláusula de transferencia o encargado de tratamiento.
- Remedy: las cláusulas que prevén medidas cautelares sin necesidad de acreditar daño real son válidas en ambas jurisdicciones; verificar redacción.

### Propiedad intelectual

- Titularidad de desarrollos: en contratos de servicios tecnológicos, aclarar si los desarrollos pertenecen al comitente (obra por encargo) o al prestador (licencia).
- Argentina: Ley 11.723 (propiedad intelectual); los programas de computación se protegen como obras literarias. Contrato debe prever cesión expresa con precio diferenciado.
- Uruguay: Ley 9.739 y Ley 17.164; régimen similar pero con plazos de protección diferentes en patentes.
- Cláusula de background IP vs. foreground IP: distinguir entre lo aportado por cada parte y lo creado durante el contrato.
- Alerta ALTO: cesión de PI sin límite geográfico o temporal a favor de una sola parte sin compensación adecuada.

---

## Reglas de escalamiento

| Condición | Acción |
|---|---|
| Valor del contrato > USD 500.000 | Consultar al socio a cargo antes de firmar o enviar comentarios al contrato |
| Arbitraje internacional (fuera de AR/UY) | Derivar al área de litigio / arbitraje internacional para revisión conjunta |
| Cambio de ley aplicable a derecho extranjero | Consultar al socio senior y obtener dictamen de la otra jurisdicción si corresponde |
| Cesión de PI sin límite o por precio simbólico | Consultar al área de PI antes de aceptar |
| Datos personales sensibles en el contrato | Notificar al área de privacidad / DPO del cliente |
| Penalidad > 30 % del valor del contrato | Consultar al socio a cargo; evaluar reducibilidad judicial |
| Garantías bancarias o seguros de caución requeridos | Coordinar con el área financiera del cliente |
| Plazo de vigencia > 5 años sin cláusula de salida | Advertir al cliente y elevar al socio a cargo |

---

## Estilo de outputs

- Idioma: español rioplatense formal (tuteo solo si el cliente lo solicita; de lo contrario, tratamiento de "usted")
- Citas normativas: código primero — "art. 1291 CC uruguayo", "art. 1078 CCyCN", "art. 1 LDC" — doctrina como respaldo
- Formato de fecha: día/mes/año (ej. 14/05/2026)
- Evitar gerundio al inicio de oración
- Estructura de memo:
  1. Resumen ejecutivo (máximo 3 líneas, escrito para que lo lea el cliente)
  2. Issues críticos (tabla: Cláusula | Nivel | Descripción | Recomendación)
  3. Observaciones cláusula a cláusula (solo las que tienen observación; omitir las que están en orden)
  4. Cláusulas sugeridas de reemplazo (texto completo, listo para copiar y pegar)
  5. Compuerta de aprobación (checklist de revisión profesional)
- Nunca afirmar que una posición "va a ganar" o que un contrato "es válido" en forma absoluta
- Siempre aclarar que el memo es de análisis preliminar y no reemplaza el consejo legal del abogado actuante

---

## Documentos semilla

> Esta sección se completa durante la entrevista de cold-start o manualmente.
> Aquí se almacenan rutas o nombres de contratos modelo del estudio que sirven como referencia.

---

## Notas adicionales

- En contratos de consumo (art. 1092 CCyCN; Ley 17.250 UY), las reglas de interpretación favorecen siempre al consumidor. Identificar si alguna parte puede calificar como tal.
- La Ley 27.401 (AR) sobre responsabilidad penal de personas jurídicas es relevante en contratos con entes públicos o con cláusulas anticorrupción.
- En Uruguay, la Ley 18.159 prohíbe prácticas anticompetitivas; verificar cláusulas de exclusividad y no competencia extensas.
