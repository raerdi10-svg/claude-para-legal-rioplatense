---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil administrativo del estudio.
  Recopila jurisdicción, organismos habituales, tipo de actos impugnados, umbrales de riesgo
  y socio de referencia, y actualiza CLAUDE.md con el perfil resultante.
argument-hint: "[ninguno — la skill guía la conversación]"
user-invocable: true
---

# Skill: Cold-Start Interview — Derecho Administrativo

## Propósito

Configurar el perfil de práctica administrativa del estudio antes de usar cualquier otra skill del plugin. Sin este perfil, las skills de recurso y análisis trabajan con placeholders. Con él, producen outputs calibrados a la jurisdicción, los organismos y los umbrales reales del estudio.

---

## Paso 0 — Presentación

Presentarse brevemente:

> "Voy a hacerle algunas preguntas para configurar el perfil de práctica administrativa de su estudio. Las respuestas quedan guardadas en CLAUDE.md y las usan todas las skills de este plugin. El proceso lleva aproximadamente 10 minutos. Puede saltear cualquier pregunta con 'no sé' o 'después' y completarla más adelante editando CLAUDE.md directamente."

---

## Paso 1 — Jurisdicción y sede

Formular las siguientes preguntas, de a una, esperando respuesta antes de continuar:

1. **¿En qué jurisdicción o jurisdicciones ejerce la práctica administrativa?**
   - Opciones orientativas: Uruguay · Argentina · Ambas · Otra (indicar cuál)

2. **¿Cuál es la ciudad/sede principal del estudio?**
   - Relevante para determinar el fuero local en Argentina (federal vs. provincial vs. porteño).

3. **En Uruguay: ¿trabaja principalmente con organismos centralizados (ministerios), entes autónomos (BCU, ANTEL, OSE, UTE, ANCAP, ANP), servicios descentralizados (ASSE, ANEP, BPS) o intendencias departamentales?**

4. **En Argentina: ¿trabaja principalmente con organismos nacionales (AFIP/ARCA, ANSES, BCRA, CNV, ENARGAS, ENRE, ENACOM), ministerios nacionales, entes provinciales o municipales?**

---

## Paso 2 — Tipo de actos y práctica

5. **¿Qué tipos de actos impugna con mayor frecuencia?**
   Pedir que seleccione todos los que apliquen:
   - Resoluciones sancionatorias (multas, inhabilitaciones)
   - Denegatorias de habilitaciones o licencias
   - Actos en materia de contratación pública (pliegos, adjudicaciones)
   - Actos en materia de empleo público (sumarios, cesantías)
   - Omisiones / silencio administrativo
   - Actos reglamentarios (impugnación de normas generales)
   - Otro (indicar cuál)

6. **¿El estudio litigia ante el TCA (Uruguay) o la Cámara CAF / cámaras federales (Argentina)?**
   - Sí, con frecuencia / Ocasionalmente / No, solo vía administrativa / Derivamos esa etapa

7. **¿El estudio interviene en procedimientos de contratación pública (licitaciones, concursos)?**
   - Si la respuesta es afirmativa: ¿como oferente, como organismo contratante o como asesor de ambos?

---

## Paso 3 — Umbrales de riesgo y escalamiento

8. **¿A partir de qué monto de multa o valor económico del acto considera que el asunto es de alto riesgo y requiere intervención del socio a cargo?**

9. **¿A partir de qué monto o impacto considera que un asunto es de riesgo medio?**

10. **¿Tiene un socio o referente designado para la práctica administrativa? (nombre o cargo)**

11. **¿Existe algún organismo regulador con el que trabaje especialmente y tenga criterios particulares de escalamiento?**

---

## Paso 4 — Estilo y preferencias

12. **¿Prefiere que los escritos se redacten en primera persona del singular (me presento y digo) o del plural (nos presentamos)?**

13. **¿Hay alguna convención de estilo interna del estudio para escritos administrativos que deba respetar?** (ej. encabezado particular, numeración de secciones, fuente de citas)

14. **¿El estudio usa algún sistema de gestión de expedientes o calendario de plazos al que deba integrarse el output?**

---

## Paso 5 — Revisión y escritura del perfil

Presentar un resumen de las respuestas en formato tabla y preguntar:

> "Estos son los datos del perfil. ¿Hay algo que quiera ajustar antes de guardarlos?"

Una vez confirmado, actualizar las secciones correspondientes de `CLAUDE.md`:
- "Jurisdicción principal"
- "Organismos habituales" (marcar los relevantes)
- "Tipo de actos impugnados" (marcar los aplicables)
- "Umbrales de riesgo" (completar los montos)
- "Reglas de escalamiento" (completar nombre de socio y organismos)
- "Estilo de outputs" (ajustar si corresponde)
- "Socio / referente de práctica administrativa"
- "Notas adicionales" (cualquier criterio particular mencionado)

Confirmar al usuario:

> "El perfil quedó guardado en CLAUDE.md. A partir de ahora, `/administrativo:recurso-administrativo` y las demás skills del plugin usarán estos datos. Puede editar CLAUDE.md directamente en cualquier momento para actualizarlos."

---

## Guardrails

- No avanzar al Paso 2 sin conocer al menos la jurisdicción principal.
- Si el usuario menciona un plazo que ya está corriendo, interrumpir la entrevista y sugerir correr `/administrativo:recurso-administrativo` de inmediato antes de continuar la configuración.
- No inventar nombres de organismos ni de socios; dejar el campo en blanco si el usuario no lo provee.
- No guardar datos personales de clientes o partes en CLAUDE.md — solo configuración del estudio.
