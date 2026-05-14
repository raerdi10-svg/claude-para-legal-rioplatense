---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil de privacidad del estudio.
  Recopila jurisdicción, tipo de clientes, sectores, categorías de datos habituales
  y reglas de escalamiento, y escribe el perfil resultante en CLAUDE.md.
argument-hint: "[nombre del estudio o abogado responsable]"
user-invocable: true
---

# Skill: Configuración Inicial — Perfil de Privacidad

## Propósito

Obtener del usuario la información necesaria para personalizar todos los skills del plugin
`privacidad` a la práctica concreta del estudio. El resultado queda escrito en el archivo
`CLAUDE.md` del plugin, que cada skill lee al iniciarse. Sin este perfil, los plazos,
las referencias al organismo regulador y los umbrales de riesgo pueden no corresponderse
con la realidad del cliente.

---

## Paso 0 — Presentación

Presentarse brevemente y explicar el propósito de la entrevista:

> "Voy a hacerte una serie de preguntas para configurar el asistente de privacidad a la
> práctica de tu estudio. Con esa información, los skills de redacción de respuestas ARCO,
> revisión de DPA y generación de EIA van a usar las normas, los plazos y los umbrales
> correctos para tu contexto. La entrevista dura aproximadamente cinco minutos."

---

## Paso 1 — Jurisdicción

Preguntar:

1. ¿El estudio opera principalmente en **Uruguay**, en **Argentina**, o en **ambas** jurisdicciones?
2. Si opera en ambas: ¿existe una jurisdicción predominante o depende del asunto?
3. ¿Atienden clientes que transfieren datos a la Unión Europea o a otros países con régimen
   propio (EE.UU., Brasil — LGPD, Chile — Ley 21.096)? (Esto determina si corresponde
   aplicar análisis de adecuación.)

---

## Paso 2 — Tipo de clientes y rol en el tratamiento

Preguntar:

1. ¿Los clientes habituales son principalmente **responsables del tratamiento** (quienes
   deciden qué datos se tratan y para qué), **encargados del tratamiento** (proveedores
   de servicios que tratan datos por cuenta ajena), o **ambos**?
2. ¿Con qué frecuencia el estudio negocia DPA como encargado vs. como responsable?
3. ¿Hay clientes que actúan como responsables conjuntos (joint controllers)?

---

## Paso 3 — Sectores de industria

Preguntar:

1. ¿En qué sectores se concentra la práctica? (Seleccionar todos los que apliquen.)
   - Tecnología / SaaS / IA
   - Salud y farmacéutico
   - Servicios financieros / fintech / seguros
   - Retail y consumo masivo
   - Recursos humanos / headhunting / ATS
   - Educación
   - Medios y publicidad digital
   - Sector público / organismos del Estado
   - Otro: ___

2. ¿Hay algún sector con régimen sectorial propio que ya manejan frecuentemente?
   (Ejemplo: secreto bancario BCU/BCRA, datos de salud bajo normas del MSP/ANMAT,
   datos de menores bajo protecciones específicas.)

---

## Paso 4 — Categorías de datos habituales

Preguntar:

1. ¿Qué categorías de datos personales aparecen con más frecuencia en los asuntos
   del estudio? (Marcar todas las que apliquen.)
   - Datos de identificación (nombre, CI/DNI, CUIT/RUT)
   - Datos de contacto (teléfono, email, dirección)
   - Datos financieros (cuentas, transacciones, historial crediticio)
   - Datos laborales (legajo, sueldo, evaluaciones de desempeño)
   - Datos de salud (diagnósticos, historias clínicas, cobertura médica)
   - Datos biométricos (huella, reconocimiento facial, voz)
   - Datos de menores de 18 años
   - Datos de geolocalización
   - Datos de origen racial o étnico
   - Datos de creencias religiosas o filosóficas
   - Datos de orientación sexual o identidad de género
   - Datos penales o contravencionales
   - Datos de comportamiento en línea (cookies, tracking, perfiles publicitarios)
   - Otro: ___

2. ¿El estudio asesora a clientes que realizan tratamiento automatizado con perfilado
   o toma de decisiones automatizadas?

---

## Paso 5 — Reglas de escalamiento

Preguntar:

1. ¿Cuál es el nombre del socio o área responsable de privacidad a quien escalar
   cuando hay una brecha de seguridad que requiere notificación regulatoria?
2. ¿A qué área se derivan las solicitudes de habeas data con patrocinio judicial?
3. ¿Existe algún umbral de monto de contrato o de sensibilidad que dispare consulta
   obligatoria antes de emitir una opinión al cliente?

---

## Paso 6 — Estilo y preferencias

Preguntar:

1. ¿El estudio tiene algún modelo de carta o memo de privacidad que quiera usar
   como punto de partida? (Se puede cargar como documento semilla en CLAUDE.md.)
2. ¿Hay alguna preferencia de formato para los outputs?
   (Tabla semáforo / Memo tradicional / Lista de issues / Combinación)
3. ¿Alguna norma o disposición regulatoria reciente que el estudio esté monitoreando
   y deba considerarse en los análisis?

---

## Paso 7 — Escritura del perfil

Con las respuestas recopiladas, completar el archivo `CLAUDE.md` del plugin `privacidad`
con los valores concretos del estudio:

- Jurisdicción principal y jurisdicciones secundarias
- Tipo de clientes (responsable / encargado / ambos)
- Sectores de industria atendidos
- Categorías de datos habituales (con indicación de cuáles son sensibles)
- Reglas de escalamiento (nombres de socios y áreas)
- Documentos semilla (si se cargaron)
- Notas adicionales (normas bajo monitoreo, preferencias de formato)

Confirmar al usuario que el perfil fue guardado y mencionar que puede editarlo
directamente en `CLAUDE.md` para ajustes posteriores.

---

## Guardrails

- No escribir datos de carácter personal de los clientes del estudio en el CLAUDE.md
  (nombres de clientes concretos, datos de expedientes). Solo información estructural
  del estudio.
- Si el usuario menciona una brecha de seguridad activa durante la entrevista, pausar
  y derivar de inmediato a `respuesta-arco` o al protocolo de notificación de brechas —
  la configuración puede esperar.
- No recomendar que el estudio asuma el rol de encargado o responsable: eso es una
  decisión jurídica que corresponde al abogado.
