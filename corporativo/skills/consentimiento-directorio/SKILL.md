---
name: consentimiento-directorio
description: >
  Redacción de actas de directorio o resoluciones de socios para sociedades
  anónimas y SRL en Argentina (LGS Ley 19.550) y Uruguay (LSC Ley 16.060).
  Recopila tipo de sociedad, jurisdicción, tipo de acto a aprobar, quórum
  presente y orden del día, y produce el acta completa en formato listo
  para firmar con todas las formalidades legales requeridas.
argument-hint: "[tipo de sociedad] [jurisdicción AR/UY] [acto a aprobar]"
user-invocable: true
---

# Skill: Redacción de Actas de Directorio y Resoluciones de Socios

## Propósito

Redactar el acta de directorio o la resolución de socios / asamblea que aprueba un acto societario determinado, con todas las formalidades legales exigidas por la LGS (Argentina) y la LSC (Uruguay), el quórum y las mayorías requeridas, y la mención expresa de los fundamentos del acto. El documento producido está listo para su revisión por el abogado actuante y para su firma por los miembros del órgano.

---

## Paso 0 — Lectura del perfil

Leer `CLAUDE.md` del plugin para incorporar jurisdicción, tipo de sociedad habitual y estilo de outputs. Si el estudio tiene templates propios de actas mencionados en "Documentos semilla", usarlos como referencia de formato.

---

## Paso 1 — Recolección de datos

Formular las siguientes preguntas en turnos separados:

**Pregunta 1 — Tipo de sociedad y jurisdicción:**
> ¿Qué tipo de sociedad es y en qué jurisdicción?
> (a) SA argentina — LGS Ley 19.550
> (b) SRL argentina — LGS Ley 19.550
> (c) SAS argentina — Ley 27.349
> (d) SA uruguaya — LSC Ley 16.060
> (e) SRL uruguaya — LSC Ley 16.060
> (f) Otra — especificar

**Pregunta 2 — Órgano que actúa:**
> ¿Qué órgano debe aprobar el acto?
> (a) Directorio (SA) / Gerencia (SRL)
> (b) Asamblea ordinaria de accionistas / Reunión de socios
> (c) Asamblea extraordinaria de accionistas
> (d) Directorio y asamblea (acto que requiere ambos)

**Pregunta 3 — Acto a aprobar:**
> ¿Qué acto o actos debe aprobar el órgano?
> Ejemplos:
> - Aprobación de estados contables y distribución de dividendos
> - Nombramiento o remoción de directores / gerentes / síndicos
> - Reforma de estatutos (especificar artículo/s)
> - Aprobación de contrato relevante (especificar)
> - Otorgamiento o revocación de poder (especificar alcance)
> - Emisión de acciones / aumento de capital
> - Aprobación de operación con parte relacionada (art. 272 LGS / art. 191 LSC)
> - Aprobación de fusión, escisión o transformación
> - Disolución de la sociedad
> - Otro — detallar

**Pregunta 4 — Integración del órgano:**
> ¿Quiénes integran el órgano que aprueba el acto?
> Para cada miembro, indicar:
> - Nombre completo
> - DNI/CI/Pasaporte
> - Cargo (director titular / director suplente / síndico / accionista / cuotapartista)
> - Si tiene conflicto de interés con el acto a aprobar (sí / no)
> - Si asiste en persona, por medio de representante, o a distancia (si el estatuto lo permite)

**Pregunta 5 — Quórum:**
> ¿Cuántos miembros del órgano asistieron y con qué participación en el capital / votos?
> (Esto permite verificar si hay quórum suficiente)

**Pregunta 6 — Datos de la convocatoria (solo para asambleas):**
> - ¿Cómo fue convocada la asamblea? (publicación en Boletín Oficial, edictos, citación personal)
> - ¿Con cuántos días de anticipación?
> - ¿El estatuto establece algún requisito especial de convocatoria?
> - ¿Todos los accionistas / socios renunciaron a la convocatoria y consienten la celebración? (asamblea unánime)

**Pregunta 7 — Datos adicionales del acto:**
> Dependiendo del acto a aprobar, solicitar datos específicos:
> - Aprobación de estados contables: ejercicio cerrado al [fecha]; resultado del ejercicio [ganancia/pérdida/monto].
> - Distribución de dividendos: monto; en efectivo o en acciones; fecha de pago.
> - Nombramiento de directores: nombre completo, DNI/CI, cargo, período (inicio y vencimiento del mandato).
> - Reforma estatutaria: artículo vigente y texto de reemplazo.
> - Poder: nombre del apoderado, tipo de poder (general / especial), actos incluidos, vigencia.
> - Operación con parte relacionada: descripción, precio o condiciones, cómo se comparó con valores de mercado.
> - Fusión: sociedades involucradas, tipo de fusión (por absorción / creación de nueva), relación de canje.

**Pregunta 8 — Datos formales:**
> - Ciudad y fecha de celebración de la reunión / asamblea.
> - ¿Quién presidió la reunión?
> - ¿Quién actuó como secretario?
> - ¿Hay un libro de actas donde debe transcribirse? (para el encabezado de folio)

---

## Paso 2 — Verificación de quórum y mayorías

Antes de redactar, verificar si el acto puede ser aprobado con el quórum declarado:

### Argentina — LGS:

**Actas de directorio (arts. 260-263 LGS):**
- Quórum: mayoría absoluta de directores, salvo disposición estatutaria más exigente.
- Mayoría para decidir: mayoría absoluta de presentes, salvo estatuto.
- Director con interés contrario: debe abstenerse (art. 272 LGS) — si no lo hizo, el acto es impugnable.

**Asamblea ordinaria (art. 243 LGS):**
- Primera convocatoria: quórum de accionistas que representen la mayoría de acciones con derecho a voto.
- Segunda convocatoria: con cualquier número de accionistas.
- Decisiones: mayoría absoluta de votos presentes con derecho a voto (salvo disposición especial).
- Competencia (art. 234 LGS): estados contables, dividendos, elección y remoción de directores y síndicos, responsabilidad de directores, aumento de capital dentro del autorizado.

**Asamblea extraordinaria (art. 244 LGS):**
- Primera convocatoria: 60 % del capital.
- Segunda convocatoria: 30 % del capital, salvo disposición estatutaria.
- Mayorías especiales para actos del art. 244 último párrafo: mayoría de todas las acciones con derecho a voto (incluidas las limitadas), sin aplicación de segunda convocatoria.
- Competencia: reforma estatutaria, fusión, escisión, transformación, disolución, aumento fuera del capital autorizado, emisión de debentures, limitación de derecho de preferencia.

### Uruguay — LSC:

**Directorio (arts. 379-388 LSC):**
- Quórum: mayoría de directores, salvo estatuto.
- Decisiones: mayoría de presentes, salvo estatuto.
- Director con interés contrario: debe abstenerse (art. 191 LSC).

**Asamblea ordinaria (arts. 337-340 LSC):**
- Primera convocatoria: accionistas que representen más de la mitad del capital integrado.
- Segunda convocatoria: sin quórum mínimo (sesiona con los presentes).
- Decisiones: mayoría de votos presentes.
- Competencia (art. 337 LSC): estados contables, distribución de ganancias, nombramiento y remuneración de directores y síndicos.

**Asamblea extraordinaria (arts. 337-340 LSC):**
- Primera convocatoria: presencia de más de la mitad del capital integrado y resolución por mayoría de votos presentes.
- Para actos que requieren mayorías especiales (reforma estatutaria, transformación, fusión, escisión, disolución): verificar el estatuto, que no puede establecer mayorías inferiores a las legales.

Si el quórum declarado por el usuario no es suficiente para el acto a aprobar, advertir antes de redactar el acta e indicar qué quórum se requiere.

---

## Paso 3 — Redacción del acta

### Modelo de Acta de Directorio — Argentina (SA)

```
ACTA N° [XXX] DE REUNIÓN DE DIRECTORIO
[DENOMINACIÓN SOCIAL] S.A.
CUIT: [XXXXXXXXXX]

En la Ciudad de [CIUDAD], a los [DD] días del mes de [MES] de [AAAA], siendo las
[HH:MM] horas, se reúnen en [DOMICILIO SOCIAL / domicilio indicado] los miembros
del Directorio de [DENOMINACIÓN SOCIAL] S.A., quienes se identifican a continuación:

[NOMBRE], DNI [XXXXXXXX] — Director [Titular / Presidente / Vicepresidente]
[NOMBRE], DNI [XXXXXXXX] — Director [Titular / Secretario]
[Si aplica: NOMBRE, DNI XXXXXXXX — Síndico titular (solo asiste, sin voto)]

Los presentes representan la [mayoría absoluta / totalidad] del Directorio,
por lo que se declara válidamente constituida la reunión conforme al
artículo [XXX] del Estatuto Social y el artículo 260 de la Ley 19.550.

Se designa presidente de la reunión a [NOMBRE] y secretario a [NOMBRE].

ORDEN DEL DÍA:

[PRIMER PUNTO — TÍTULO DEL PUNTO]

[El presidente somete a consideración del Directorio [descripción del acto].
Descripción del fundamento: por qué se somete a aprobación, contexto relevante,
condiciones del acto aprobado.]

[Si hay director con interés contrario: "El director [NOMBRE] manifiesta tener
interés contrario al de la sociedad en el presente punto del orden del día,
por lo que, en cumplimiento del artículo 272 de la Ley 19.550, se abstiene
de deliberar y votar."]

Puesto el punto a votación, se aprueba [por unanimidad / por mayoría de votos]:

RESOLUCIÓN: El Directorio de [DENOMINACIÓN SOCIAL] S.A. resuelve:
[Texto dispositivo de la resolución, en términos claros y específicos.
Incluir todos los detalles del acto: nombres, montos, plazos, condiciones.]

[SEGUNDO PUNTO — si aplica, repetir estructura]

Siendo las [HH:MM] horas, y no habiendo más asuntos que tratar, se da por
finalizada la reunión, labrándose la presente acta que, leída y hallada
conforme, es firmada por todos los presentes.

_______________________________     _______________________________
[NOMBRE]                            [NOMBRE]
Director [cargo]                    Director [cargo]
DNI [XXXXXXXX]                      DNI [XXXXXXXX]

[Si hay síndico:]
_______________________________
[NOMBRE]
Síndico [Titular / Suplente]
DNI [XXXXXXXX]
```

### Modelo de Resolución Unánime de Socios — SRL Argentina

```
RESOLUCIÓN UNÁNIME DE SOCIOS
[DENOMINACIÓN SOCIAL] S.R.L.
CUIT: [XXXXXXXXXX]

En la Ciudad de [CIUDAD], a los [DD] días del mes de [MES] de [AAAA], los
socios de [DENOMINACIÓN SOCIAL] S.R.L., identificados a continuación, y que
representan el [100 %] del capital social, prescindiendo de toda formalidad
de convocatoria conforme al artículo 159 de la Ley 19.550, resuelven
unánimemente:

[NOMBRE], DNI [XXXXXXXX] — [N] cuotas — [XX %] del capital social
[NOMBRE], DNI [XXXXXXXX] — [N] cuotas — [XX %] del capital social

RESOLUCIÓN PRIMERA:
[Texto dispositivo]

RESOLUCIÓN SEGUNDA (si aplica):
[Texto dispositivo]

En prueba de conformidad, firman la presente resolución.

_______________________________     _______________________________
[NOMBRE]                            [NOMBRE]
Socio                               Socio
DNI [XXXXXXXX]                      DNI [XXXXXXXX]
```

### Modelo de Acta de Asamblea Extraordinaria — Uruguay (SA)

```
ACTA DE ASAMBLEA EXTRAORDINARIA DE ACCIONISTAS
[DENOMINACIÓN SOCIAL] S.A.
RUT: [XXXXXXXXXX]

En la ciudad de Montevideo, el día [DD] de [mes] de [AAAA], a la hora [HH:MM],
se reúne en [DOMICILIO SOCIAL] la Asamblea Extraordinaria de Accionistas de
[DENOMINACIÓN SOCIAL] S.A., convocada conforme al artículo [del estatuto] y
los artículos 337 y siguientes de la Ley N.° 16.060 (Ley de Sociedades Comerciales).

ACCIONISTAS PRESENTES / REPRESENTADOS:

[NOMBRE], C.I. [XXXXXXXX] — [N] acciones ordinarias nominativas — [XX %] del capital
[NOMBRE], C.I. [XXXXXXXX] — [N] acciones — [XX %] del capital
[En caso de representación: NOMBRE representado por NOMBRE APODERADO según poder
notarial de fecha DD/MM/AAAA]

Capital presente y representado: [XX %] del capital integrado.

El capital presente y representado supera la mayoría del capital integrado exigida
en primera convocatoria (art. 337 LSC), por lo que la Asamblea se declara
válidamente constituida.

Preside la Asamblea: [NOMBRE]
Actúa como Secretario/a: [NOMBRE]

ORDEN DEL DÍA:

[PUNTO ÚNICO / PRIMER PUNTO]:
[Descripción del acto. Contexto y fundamentos. Si hay reforma estatutaria:
transcribir el artículo vigente y el texto propuesto.]

[Si el acto requiere abstención: "El accionista [NOMBRE] manifiesta tener
interés contrario en el presente punto y se abstiene de votar (art. 191 LSC)."]

Sometido a votación:
Votos a favor: [N] acciones — [XX %] del capital presente
Votos en contra: [N] acciones — [XX %] del capital presente
Abstenciones: [N] acciones

RESOLUCIÓN: La Asamblea Extraordinaria resuelve:
[Texto dispositivo — preciso, completo, listo para ejecutar.]

Sin más asuntos que tratar, siendo las [HH:MM] horas, se da por finalizada
la Asamblea, labrándose la presente Acta que, leída y aprobada, firman:

_______________________________     _______________________________
[NOMBRE]                            [NOMBRE]
Presidente de la Asamblea           Secretario/a
C.I. [XXXXXXXX]                     C.I. [XXXXXXXX]
```

---

## Paso 4 — Notas de inscripción registral

Al finalizar el acta, incluir un bloque de recordatorio para el abogado actuante:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECORDATORIO DE TRÁMITES REGISTRALES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Indicar según el acto aprobado:]

ARGENTINA — IGJ / DPPJ:
□ Si se reformó el estatuto: inscripción en IGJ/DPPJ — art. 12 LGS.
  Plazo: presentar dentro de los 15 días de la asamblea (Res. IGJ 7/2015).
□ Si se designaron autoridades: inscripción del nombramiento en IGJ/DPPJ.
  Publicar en Boletín Oficial si la ley lo exige (art. 10 LGS).
□ Si se aumentó el capital: inscripción del aumento y de las nuevas acciones.
□ Si se disolvió la sociedad: inscripción y publicación (art. 98 LGS).

URUGUAY — AIN / Registro Nacional de Comercio:
□ Si se reformó el estatuto: inscripción en AIN y publicación en el
  Diario Oficial — art. 16 LSC.
□ Si se designaron autoridades: inscripción del nombramiento.
□ Si se aprobaron estados contables: presentar ante AIN si la sociedad
  está obligada a ello.
□ Si se fusionó, escindió o transformó: seguir el procedimiento de los
  arts. 108-123 LSC, con publicaciones y plazos de oposición de acreedores.

LIBROS SOCIETARIOS:
□ Transcribir el acta al libro de actas del órgano correspondiente.
□ Firmar en el libro: todos los presentes en la reunión.
□ Si hay síndico: su firma acredita la regularidad de la reunión.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- Si el quórum declarado es insuficiente para el acto a aprobar, no redactar el acta — alertar al usuario con el quórum requerido y las alternativas (segunda convocatoria, renuncia a quórum si el estatuto lo permite, etc.).
- Si hay un director con interés contrario que no se abstuvo, advertir que el acto es impugnable (art. 272 LGS / art. 191 LSC) y recomendar que el acta refleje la abstención.
- Nunca incluir en el texto dispositivo términos ambiguos como "aprobar en general" o "facultar ampliamente" — las resoluciones deben ser específicas y cuantificadas.
- Para actos que requieren inscripción registral, siempre incluir el recordatorio de trámites del Paso 4.
- El acta producida es un borrador para revisión del abogado actuante — incluir siempre la advertencia de que debe ser revisada antes de firmarse.
- En Uruguay, verificar si la sociedad tiene acciones nominativas escriturales o títulos físicos — el mecanismo de registro del accionista presente varía.
- Para poderes amplios o generalísimos en Argentina: recordar que desde la reforma de la IGJ, los poderes amplios de disposición y administración otorgados por directorio pueden requerir ratificación asamblearia según el estatuto.
