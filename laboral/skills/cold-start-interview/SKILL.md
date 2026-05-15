---
name: cold-start-interview
description: >
  Entrevista guiada para configurar el perfil laboral del estudio. Recopila jurisdicción,
  industrias cliente, tipo de práctica, umbrales de riesgo, CCT habituales y socio de
  referencia, y persiste el resultado en CLAUDE.md del plugin laboral.
argument-hint: "[dejar vacío para iniciar la entrevista]"
user-invocable: true
---

# Skill: Cold-Start Interview — Laboral

## Propósito

Configurar el perfil de práctica laboral del estudio en una única sesión interactiva.
Sin este perfil, los demás skills del plugin utilizan valores genéricos que pueden no
reflejar la realidad del estudio ni la jurisdicción principal de sus clientes.

---

## Paso 0 — Presentación

Presentarse al usuario con el siguiente texto (adaptado al contexto):

> "Voy a hacerte una serie de preguntas para configurar el perfil de práctica laboral
> del estudio. Con esta información, las demás herramientas del plugin laboral responderán
> de forma alineada con tus clientes y jurisdicción. La entrevista toma aproximadamente
> 10 minutos. Podés responder con toda la información disponible o dejar campos en blanco
> para completar después."

---

## Paso 1 — Jurisdicción y geografía

Preguntar:

1. **Jurisdicción principal:** ¿El estudio opera principalmente en Argentina, Uruguay, o ambos?
   - Si Argentina: ¿hay jurisdicciones provinciales de especial relevancia? (ej. CABA, PBA, Córdoba, Mendoza)
   - Si Uruguay: ¿opera en Montevideo, interior, o ambos?
2. **¿Tienen clientes con empleados en ambos países?** (implicancia de doble normativa)

---

## Paso 2 — Perfil de clientes e industrias

Preguntar:

3. **Industrias cliente más frecuentes:** (ej. tecnología, manufactura, retail, banca, salud, agro, construcción)
4. **Tamaño habitual de los empleadores clientes:**
   - PyME (< 50 empleados)
   - Mediana empresa (50–500 empleados)
   - Gran empresa / corporativo (> 500 empleados)
5. **¿Tienen clientes que sean empleadores del sector público?**

---

## Paso 3 — Tipo de práctica

Preguntar:

6. **¿El estudio hace asesoramiento preventivo, litigio laboral, o ambos?**
7. Si hace litigio: ¿actúan generalmente como representantes del empleador, del trabajador, o ambos?
8. **¿Tienen convenios colectivos de trabajo (CCT) que apliquen con frecuencia?** ¿Cuáles?
   - (ej. CCT UOCRA N° 76/75, CCT Comercio N° 130/75, CCT SMATA N° 260/75, convenios de actividad UY)

---

## Paso 4 — Umbrales de riesgo y escalamiento

Preguntar:

9. **¿A partir de qué monto estimado de indemnización escalan el caso al socio?**
   (expresar en USD, ARS o UYU según corresponda)
10. **¿Quién es el socio o referente de práctica laboral?** (nombre o cargo)
11. **¿Tienen protocolo especial para investigaciones internas?** (ej. comité de ética, HR, externo)

---

## Paso 5 — Preferencias de estilo

Preguntar:

12. **¿Prefieren memos en formato ejecutivo (1 página) o análisis extendido?**
13. **¿Citan preferentemente doctrina argentina (Ackerman, Vázquez Vialard, etc.) o uruguaya (Ermida Uriarte, Grzetich)?**

---

## Paso 6 — Escritura del perfil

Con las respuestas recopiladas, escribir el perfil completo en `laboral/CLAUDE.md`,
completando todas las secciones:

- **Jurisdicción principal:** con las jurisdicciones indicadas
- **Industrias cliente típicas:** lista según lo informado
- **Tipo de práctica:** marcar las opciones que correspondan
- **Umbrales de riesgo:** actualizar la tabla con los montos indicados, incorporar reglas específicas del estudio
- **Convenios Colectivos habituales:** lista de CCT mencionados
- **Reglas de escalamiento:** completar con nombre del socio y monto umbral
- **Estilo de outputs:** ajustar según preferencias de formato y doctrina
- **Socio / referente de práctica laboral:** nombre y datos indicados
- **Notas adicionales:** cualquier otra observación relevante

Confirmar al usuario que el perfil fue guardado y que puede editarlo directamente
en `laboral/CLAUDE.md` para ajustes futuros.

---

## Guardrails

- No inventar datos: si el usuario deja un campo en blanco, dejar el campo vacío o con la nota "[a completar]".
- No preguntar más de dos preguntas por mensaje para no abrumar al usuario.
- Si el usuario menciona una situación de conflicto laboral activo durante la entrevista, completar el perfil primero y luego derivar a la skill correspondiente (`revision-despido`, `investigacion-interna`, etc.).
- No guardar datos de empleados identificados: el perfil es del estudio, no del cliente.
