---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil de gobernanza de IA del estudio.
  Recopila sectores cliente, usos de IA en evaluación, regímenes regulatorios aplicables,
  umbrales de riesgo y referente de práctica, y actualiza CLAUDE.md con el perfil resultante.
argument-hint: "[ninguno — la skill guía la conversación]"
user-invocable: true
---

# Skill: Cold-Start Interview — Gobernanza y Regulación de IA

## Propósito

Configurar el perfil de práctica de gobernanza de IA del estudio antes de usar cualquier otra skill del plugin. Sin este perfil, las skills de triaje, evaluación de impacto y revisión de proveedor operan con parámetros genéricos. Con el perfil completo, los análisis reflejan los regímenes regulatorios relevantes, los sectores del cliente y los umbrales reales del estudio.

---

## Paso 0 — Presentación

Al invocar la skill, mostrar el siguiente bloque introductorio:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIGURACIÓN DE PERFIL — GOBERNANZA Y REGULACIÓN DE IA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Esta entrevista toma entre 10 y 15 minutos.
Las respuestas quedan guardadas en CLAUDE.md y pueden
editarse manualmente en cualquier momento.
Responda con la información actual del estudio o cliente;
puede dejar en blanco las preguntas que no apliquen aún.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Paso 1 — Recolección de datos (una pregunta por turno)

### Bloque A — Jurisdicción y alcance geográfico

**Pregunta A1:**
> ¿En qué jurisdicción(es) opera principalmente el estudio o el cliente cuya práctica de IA vamos a configurar?
> (a) Argentina
> (b) Uruguay
> (c) Ambas
> (d) Argentina / Uruguay con alcance hacia la Unión Europea (ej. exporta servicios o datos a UE)
> (e) Otra combinación — indicar cuál

**Pregunta A2 (si eligió UE o combinación con UE):**
> ¿El sistema de IA o el cliente tiene usuarios, clientes o presencia operativa en algún Estado miembro de la Unión Europea?
> Si es así: ¿en qué países? Esto determina si el AI Act (Reglamento UE 2024/1689) aplica directamente.

---

### Bloque B — Sectores cliente

**Pregunta B1:**
> ¿En qué sectores se concentra la práctica del estudio o los clientes que usan IA?
> Seleccionar todos los que apliquen:
> - Financiero y bancario (bancos, aseguradoras, fintech, mercado de capitales)
> - Salud y ciencias de la vida (hospitales, laboratorios, dispositivos médicos, telemedicina)
> - Telecomunicaciones y medios
> - Retail y comercio electrónico
> - Recursos humanos y gestión del talento
> - Sector público (gobierno central, entes autónomos, intendencias)
> - Legal tech y servicios jurídicos
> - Educación
> - Otro — indicar cuál

**Pregunta B2:**
> ¿El estudio asesora principalmente a proveedores de sistemas de IA (empresas que desarrollan o comercializan IA) o a operadores/usuarios finales (empresas que despliegan IA de terceros en sus procesos)?
> (a) Principalmente proveedores
> (b) Principalmente operadores / usuarios finales
> (c) Ambos con igual frecuencia

---

### Bloque C — Usos de IA en evaluación

**Pregunta C1:**
> ¿Cuáles son los usos de IA que el estudio o sus clientes tienen actualmente en evaluación o ya desplegados?
> Describir brevemente cada uno. Ejemplos orientativos:
> - Scoring crediticio o evaluación de riesgo financiero
> - Chatbots de atención al cliente
> - Análisis de imágenes médicas o diagnóstico asistido
> - Sistemas de selección o evaluación de personal
> - Modelos de detección de fraude
> - Herramientas de generación de contenido (LLMs, texto, imagen)
> - Automatización de procesos legales o contractuales
> - Sistemas de vigilancia o reconocimiento facial

**Pregunta C2:**
> ¿Alguno de estos sistemas toma o asiste en decisiones que afectan directamente a personas físicas sin revisión humana final?
> Si es así: ¿qué tipo de decisiones? (ej. aprobación de crédito, contratación laboral, acceso a prestaciones)

---

### Bloque D — Regímenes regulatorios

**Pregunta D1:**
> ¿El AI Act de la Unión Europea (Reglamento 2024/1689) ya fue identificado como aplicable a algún sistema del cliente?
> Si es así: ¿en qué categoría se clasificó provisionalmente? (prohibido / alto riesgo / transparencia / uso general)

**Pregunta D2:**
> ¿Los sistemas de IA en evaluación utilizan datos personales de personas físicas? Si es así:
> - ¿Están bajo la Ley 25.326 (AR) o la Ley 18.331 (UY)?
> - ¿El tratamiento incluye datos sensibles (salud, biometría, origen étnico, afiliación sindical)?

**Pregunta D3:**
> ¿El cliente opera en el sector financiero bajo supervisión del BCRA o el BCU?
> Si es así: ¿se revisaron las comunicaciones del supervisor sobre gestión de riesgos tecnológicos y uso de IA?

---

### Bloque E — Umbrales y escalamiento

**Pregunta E1:**
> ¿Qué tipo de análisis activa una revisión obligatoria del socio o referente de práctica?
> Ejemplos: sistemas que afectan más de X personas / contratos de proveedor IA con valor > USD Y / sistemas en sectores regulados

**Pregunta E2:**
> ¿Tiene un socio o referente designado para la práctica de gobernanza de IA?
> (nombre o cargo)

**Pregunta E3:**
> ¿Existe coordinación con otras áreas del estudio para temas de IA?
> (ej. privacidad/DPO, laboral, regulatorio financiero, PI/tecnología)

---

### Bloque F — Estilo

**Pregunta F1:**
> ¿Prefiere outputs en formato ejecutivo (resumen + tabla de semáforo) o técnico-jurídico detallado (análisis norma por norma)?
> (a) Ejecutivo — para presentar al cliente directamente
> (b) Técnico-jurídico — para uso interno del abogado
> (c) Mixto — ejecutivo primero, técnico en anexo

---

## Paso 2 — Confirmación de perfil

Presentar resumen en formato tabla antes de guardar:

```
RESUMEN DEL PERFIL A GUARDAR — GOBERNANZA IA
═══════════════════════════════════════════════════════
Jurisdicción principal:           [respuesta A1]
Alcance UE:                       [respuesta A2 o N/A]
Sectores cliente:                 [respuesta B1]
Rol en el ecosistema IA:          [respuesta B2]
Usos de IA en evaluación:         [respuesta C1]
Decisiones automatizadas:         [respuesta C2 o N/A]
AI Act aplicable:                 [respuesta D1 o No identificado]
Datos personales / sensibles:     [respuesta D2]
Supervisión BCRA/BCU:             [respuesta D3 o N/A]
Umbral de escalamiento:           [respuesta E1]
Referente de práctica IA:         [respuesta E2]
Coordinación con otras áreas:     [respuesta E3]
Formato de outputs:               [respuesta F1]
═══════════════════════════════════════════════════════
¿Confirmamos y guardamos este perfil en CLAUDE.md? (sí / no / corregir [campo])
```

---

## Paso 3 — Escritura en CLAUDE.md

Una vez confirmado, reescribir las secciones correspondientes del archivo `CLAUDE.md` del plugin gobernanza-ia con los valores recopilados. Mantener intactas las secciones que no fueron respondidas.

Secciones a actualizar:
- `## Jurisdicción principal`
- `## Sectores cliente`
- `## Usos de IA en evaluación`
- `## Regímenes regulatorios aplicables` (activar o desactivar los regímenes según la jurisdicción y sector confirmados)
- `## Umbrales de riesgo` (ajustar umbrales si el usuario proveyó valores específicos)
- `## Reglas de escalamiento` (completar nombre del referente y áreas de coordinación)
- `## Estilo de outputs` (ajustar si el usuario eligió variante)
- `## Referente de práctica de gobernanza IA`
- `## Notas adicionales` (agregar cualquier criterio particular mencionado)

---

## Paso 4 — Mensaje de cierre

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERFIL GUARDADO EXITOSAMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El perfil de práctica de gobernanza de IA fue actualizado
en CLAUDE.md. Todas las skills del plugin leerán este
perfil en cada análisis.

Para ajustes menores, edite CLAUDE.md directamente.
Para reconfigurar el perfil completo, vuelva a invocar
esta skill: /gobernanza-ia:cold-start-interview

Skills disponibles:
  /gobernanza-ia:triaje-uso-ia
  /gobernanza-ia:evaluacion-impacto-ia
  /gobernanza-ia:revision-proveedor-ia
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Guardrails

- No inferir valores no proporcionados; si el usuario deja una pregunta en blanco, dejar el campo como `[a completar]` en CLAUDE.md.
- No sobrescribir el `## Playbook de evaluación` existente en CLAUDE.md — ese contenido lo mantiene el equipo del plugin.
- Si el usuario describe un sistema que parece caer en las prohibiciones absolutas del art. 5 del AI Act (ej. scoring social, manipulación subliminal, identificación biométrica en tiempo real en espacios públicos), interrumpir la entrevista y alertar que ese uso requiere análisis legal urgente antes de cualquier despliegue.
- Nunca omitir el paso de confirmación (Paso 2) antes de escribir en CLAUDE.md.
- Si el cliente opera en el sector salud o financiero, recordar que las regulaciones sectoriales pueden ser más estrictas que las generales — consignar esta nota en `## Notas adicionales`.
