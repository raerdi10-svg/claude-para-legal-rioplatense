---
name: cold-start-interview
description: >
  Entrevista guiada para configurar el perfil de litigio del estudio. Recopila
  jurisdicción(es), fuero habitual, tipo de práctica (actor / demandado / ambos),
  conexión con cartera in-house, umbrales de escalamiento y preferencias de estilo,
  y persiste el resultado en CLAUDE.md del plugin litigio.
argument-hint: "[dejar vacío para iniciar la entrevista]"
user-invocable: true
---

# Skill: Cold-Start Interview — Litigio

## Propósito

Configurar el perfil de práctica litigiosa del estudio en una única sesión interactiva.
Sin este perfil, los demás skills del plugin utilizan valores genéricos que pueden no
reflejar el fuero, la jurisdicción ni la estrategia habitual del estudio.

---

## Paso 0 — Presentación

Presentarse al usuario con el siguiente texto:

> "Voy a hacerte una serie de preguntas para configurar el perfil de práctica litigiosa
> del estudio. Con esta información, las demás herramientas del plugin de litigio responderán
> de forma alineada con tu fuero, jurisdicción y estrategia habitual. La entrevista toma
> aproximadamente 10 minutos. Podés responder con toda la información disponible o dejar
> campos en blanco para completar después."

---

## Paso 1 — Jurisdicción y fuero

Preguntar:

1. **Jurisdicción principal:** ¿El estudio litiga principalmente en Argentina, Uruguay, o ambos?
   - Si Argentina: ¿fuero federal, CABA, provincial? ¿Qué provincia(s)?
   - Si Uruguay: ¿Juzgados Letrados Civiles, Juzgados de Paz, TAC?
2. **Fuero habitual:**
   - ¿Civil? ¿Comercial? ¿Laboral? ¿Contencioso-administrativo? ¿Penal (como parte civil)?
   - ¿Litigan en más de un fuero? ¿Cuál es el principal?
3. **¿Hacen arbitraje nacional o internacional?** ¿Bajo qué reglamento? (CAM, CIAC, CCI, CNUDMI)

---

## Paso 2 — Tipo de práctica

Preguntar:

4. **¿Representan habitualmente al actor, al demandado, o a ambos?**
5. **¿Tienen clientes que sean demandados recurrentes** (ej. empresas con litigiosidad alta: banca, salud, aseguradoras, utilities)?
6. **¿Tienen cartera in-house?** ¿Qué tipo de causas les derivan los clientes internamente?
7. **¿Manejan causas colectivas o de clase?** ¿En qué materias?

---

## Paso 3 — Umbrales y escalamiento

Preguntar:

8. **¿A partir de qué monto de demanda escalan el caso al socio?**
   (expresar en USD, ARS o UYU según corresponda)
9. **¿Quién es el socio o referente de litigio?** (nombre o cargo)
10. **¿Tienen protocolo para medidas cautelares urgentes?** (plazos internos de notificación, aprobación)
11. **¿Cómo gestionan causas donde la misma parte es actora y demandada en distintos expedientes** (cross-cartera)?

---

## Paso 4 — Herramientas y sistemas

Preguntar:

12. **¿Utilizan algún sistema de gestión de expedientes?** (ej. Lex Doctor, Thomson Reuters Proview, sistema propio)
13. **¿Tienen acceso a bases de datos de jurisprudencia?** (ej. El Dial, Microjuris, La Ley Online, SIREJ UY)
14. **¿Cómo prefieren que se cite la jurisprudencia?** (tribunal + fecha + carátula / número de fallo / ambos)

---

## Paso 5 — Preferencias de estilo

Preguntar:

15. **¿Prefieren memos en formato ejecutivo (1 página) o análisis extendido?**
16. **¿El resumen ejecutivo está destinado al abogado o también al cliente?**
17. **¿Citan preferentemente doctrina procesal argentina** (Palacio, Falcón, Highton) **o uruguaya** (Véscovi, Couture, Landoni Sosa)**?**

---

## Paso 6 — Escritura del perfil

Con las respuestas recopiladas, escribir el perfil completo en `litigio/CLAUDE.md`,
completando todas las secciones:

- **Jurisdicción principal:** con las jurisdicciones y fueros indicados
- **Fuero habitual:** marcar las opciones que correspondan
- **Tipo de práctica:** marcar actor / demandado / ambos
- **Umbrales de riesgo:** actualizar la tabla con los montos indicados
- **Reglas de escalamiento:** completar con nombre del socio y umbral
- **Conexión con cartera in-house:** describir el tipo de causas derivadas
- **Estilo de outputs:** ajustar según preferencias de formato, cita y doctrina
- **Socio / referente de litigio:** nombre y datos indicados
- **Notas adicionales:** cualquier observación relevante (árbitros habituales, peritos de confianza, etc.)

Confirmar al usuario que el perfil fue guardado y que puede editarlo directamente
en `litigio/CLAUDE.md` para ajustes futuros.

---

## Guardrails

- No inventar datos: si el usuario deja un campo en blanco, dejar el campo vacío o con la nota "[a completar]".
- No preguntar más de dos preguntas por mensaje para no abrumar al usuario.
- Si el usuario menciona un expediente activo o una demanda urgente durante la entrevista, completar el perfil primero y luego derivar a la skill correspondiente (`demanda-recibida`, `cronologia`, etc.).
- No guardar datos de contrapartes identificadas: el perfil es del estudio, no de un caso concreto.
