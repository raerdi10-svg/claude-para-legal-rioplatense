---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil de propiedad intelectual del estudio.
  Recopila jurisdicción, tipos de activos, tipo de clientes (titulares o demandados),
  sectores y reglas de escalamiento, y escribe el perfil resultante en CLAUDE.md.
argument-hint: "[nombre del estudio o abogado responsable de PI]"
user-invocable: true
---

# Skill: Configuración Inicial — Perfil de Propiedad Intelectual

## Propósito

Obtener del usuario la información necesaria para personalizar todos los skills del plugin
`propiedad-intelectual` a la práctica concreta del estudio. El resultado queda escrito en
el archivo `CLAUDE.md` del plugin, que cada skill lee al iniciarse. Sin este perfil, las
referencias al DNPI o al INPI, los plazos de oposición y los criterios de riesgo pueden
no corresponderse con la realidad del estudio.

---

## Paso 0 — Presentación

Presentarse brevemente y explicar el propósito de la entrevista:

> "Voy a hacerte una serie de preguntas para configurar el asistente de propiedad
> intelectual a la práctica de tu estudio. Con esa información, los skills de búsqueda
> de marcas y redacción de cartas de cese van a usar las normas, los registros y los
> criterios de riesgo correctos para tu contexto. La entrevista dura aproximadamente
> diez minutos."

---

## Paso 1 — Jurisdicción

Preguntar:

1. ¿El estudio opera principalmente en **Uruguay** (DNPI), en **Argentina** (INPI), o en
   **ambas** jurisdicciones?
2. Si opera en ambas: ¿hay una jurisdicción predominante en materia de PI o depende del
   tipo de activo o del cliente?
3. ¿El estudio gestiona registros internacionales (Sistema de Madrid para marcas, PCT
   para patentes, Protocolo de La Haya para diseños)?
4. ¿Tienen relacionamiento con agentes de PI en terceros países (Brasil, Chile, Paraguay,
   España, EE.UU.) para casos con extensión territorial?

---

## Paso 2 — Tipo de activos habituales

Preguntar:

1. ¿Con qué tipos de activos de PI trabaja el estudio con más frecuencia?
   (Seleccionar todos los que apliquen.)
   - Marcas (registro y defensa)
   - Patentes de invención
   - Modelos de utilidad
   - Diseños industriales
   - Derechos de autor (obras literarias, artísticas, musicales)
   - Software (protección como obra y/o secreto empresarial)
   - Secretos empresariales y know-how
   - Nombres de dominio
   - Indicaciones geográficas / denominaciones de origen
   - Variedades vegetales

2. ¿La práctica tiene mayor énfasis en el **registro** (obtención de derechos) o en el
   **enforcement** (defensa y litigio)?

---

## Paso 3 — Tipo de clientes

Preguntar:

1. ¿Los clientes son principalmente:
   - **Titulares de derechos** que buscan registrar o defender su PI?
   - **Demandados** que reciben cartas de cese o demandas y buscan asesoramiento defensivo?
   - **Licenciatarios** que utilizan PI ajena y necesitan verificar el alcance de sus licencias?
   - **Mixto** según el asunto?

2. ¿El estudio asesora a empresas, a personas físicas (artistas, inventores, creadores),
   o a ambos?

3. ¿Tienen clientes que sean titulares de marcas notorias o de alta reputación en sus
   respectivos mercados?

---

## Paso 4 — Sectores de industria atendidos

Preguntar:

1. ¿En qué sectores de industria se concentran los activos de PI que el estudio gestiona?
   - Tecnología y software
   - Farmacéutico y biotecnología
   - Alimentos y bebidas
   - Moda, indumentaria y diseño
   - Medios, entretenimiento y contenidos digitales
   - Comercio minorista y marcas de consumo masivo
   - Industria y manufactura
   - Agricultura y agroindustria
   - Sector público (patrimonio cultural, marcas país)
   - Otro: ___

2. ¿Hay algún sector con una dinámica de registros o disputas marcarias especialmente
   activa en la práctica del estudio?

---

## Paso 5 — Reglas de escalamiento y umbrales de riesgo

Preguntar:

1. ¿Cuál es el nombre del socio o área de litigio a quien escalar cuando una infracción
   de PI puede generar una medida cautelar de urgencia o una denuncia penal?
2. ¿Existe algún umbral de valor del activo o de escala de la infracción a partir del
   cual el estudio requiere revisión del socio antes de emitir una opinión?
3. ¿El estudio tiene política sobre si actúa o no como patrocinante en demandas por
   infracción (solo asesoramiento previo vs. litigio completo)?
4. En el caso de cartas de cese, ¿el estudio las envía directamente o siempre a través
   de un escribano o con acuse notarial?

---

## Paso 6 — Herramientas y bases de datos

Preguntar:

1. ¿El estudio tiene acceso a bases de datos de marcas más allá de las búsquedas gratuitas
   en el DNPI y el INPI? (Ej. Marcaria, Saegis, Thomson CompuMark, TMview.)
2. ¿Realizan búsquedas en el Sistema de Madrid (WIPO)?
3. ¿Tienen modelos de cartas de cese que quieran usar como documentos semilla en CLAUDE.md?
4. ¿Hay alguna preferencia de formato para los dictámenes de clearing de marcas?
   (Tabla de knock-outs / análisis narrativo / combinación)

---

## Paso 7 — Escritura del perfil

Con las respuestas recopiladas, completar el archivo `CLAUDE.md` del plugin
`propiedad-intelectual` con los valores concretos del estudio:

- Jurisdicción principal y secundarias
- Tipo de activos habituales (con indicación de los más frecuentes)
- Tipo de clientes (titulares / demandados / licenciatarios)
- Sectores de industria atendidos
- Reglas de escalamiento (nombres de socios y áreas)
- Documentos semilla (si se cargaron modelos de cartas o dictámenes)
- Notas adicionales (bases de datos disponibles, preferencias de formato)

Confirmar al usuario que el perfil fue guardado y mencionar que puede editarlo
directamente en `CLAUDE.md` para ajustes posteriores.

---

## Guardrails

- No escribir datos de clientes concretos ni información de expedientes en CLAUDE.md:
  solo información estructural del estudio.
- Si el usuario menciona una infracción activa y urgente durante la entrevista (ej.
  producto falsificado en el mercado hoy mismo), pausar la configuración y derivar de
  inmediato al skill `cese-desistimiento` y al socio de litigio.
- No opinar sobre la viabilidad de un registro o la fuerza de una marca durante la
  entrevista de configuración: ese es el rol del skill `busqueda-marca`.
- No recomendar si el estudio debe actuar como apoderado ante el DNPI o el INPI: esa
  es una decisión estratégica que corresponde al abogado y al cliente.
