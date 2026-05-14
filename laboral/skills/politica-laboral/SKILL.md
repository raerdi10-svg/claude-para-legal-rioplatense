---
name: politica-laboral
description: >
  Dada la materia (trabajo remoto, acoso, uso de IA, privacidad, etc.) y jurisdicción(es),
  redacta una política de empleo completa con objeto, alcance, definiciones, obligaciones,
  procedimiento, sanciones, vigencia y suplementos jurisdiccionales específicos para
  Argentina y Uruguay. El borrador requiere revisión del abogado antes de su implementación.
argument-hint: "[materia de la política] [--jurisdiccion=AR|UY|ambas]"
user-invocable: true
---

# Skill: Política Laboral

## Propósito

Redactar el borrador de políticas de empleo corporativas, adaptadas a la normativa
laboral de Argentina y/o Uruguay, con suplementos jurisdiccionales donde la regulación
difiere. Las políticas producidas son borradores para revisión profesional — no
deben implementarse sin aprobación del abogado actuante y del cliente.

---

## Paso 0 — Recolección de datos

1. **Materia de la política:** (ej. trabajo remoto / teletrabajo, prevención de acoso y violencia, uso de inteligencia artificial, privacidad y protección de datos, uso de dispositivos y redes, conflicto de interés, capacitación, licencias especiales)
2. **Jurisdicción(es):** Argentina / Uruguay / Ambas
3. **Industria y tamaño de la empresa:** (influye en la aplicabilidad de convenios colectivos)
4. **¿Hay CCT aplicable?** Si el CCT tiene disposiciones sobre la materia, deben integrarse.
5. **¿Es una política nueva o actualización de una existente?** Si es actualización, solicitar el texto vigente.
6. **¿Requiere suplemento específico para alguna provincia argentina?** (ej. CABA, PBA, Córdoba tienen normativa adicional en algunas materias)
7. **Tono:** ¿Formal-corporativo o claro-accesible (para empleados en general)?
8. **¿Incluye procedimiento de denuncia?** (necesario para acoso, privacidad, conflicto de interés)

---

## Paso 1 — Encuadre normativo por materia

### Trabajo remoto / teletrabajo

**Argentina:**
- Ley 27.555 (Teletrabajo) — vigente desde 01/04/2021.
- Puntos obligatorios: (a) reversibilidad del teletrabajo a pedido del trabajador (art. 8); (b) derecho a la desconexión digital (art. 4 — no requerido responder fuera de horario pactado); (c) provisión de herramientas y conectividad por el empleador (art. 9); (d) igualdad de trato con empleados presenciales (art. 6); (e) protección de la privacidad del domicilio del teletrabajador.
- CCT pueden establecer condiciones adicionales — verificar.

**Uruguay:**
- No existe ley específica de teletrabajo equivalente a la argentina (al 2026).
- Se aplica la normativa general de la LRT (Ley 17.828 — responsabilidad laboral en accidentes), el Código General del Proceso y la jurisprudencia del MTSS.
- El MTSS emitió orientaciones sobre teletrabajo; aplicar por analogía el marco de la Ley 27.555 como buena práctica es recomendable aunque no obligatorio.

### Prevención de acoso y violencia laboral

**Argentina:**
- No hay ley nacional unificada de acoso laboral; sí hay normativa provincial (Ley 1225 CABA, Ley 13.168 PBA).
- La Resolución MTSS 05/2007 establece orientaciones sobre acoso psicológico laboral.
- Para acoso sexual: Ley 26.485 (violencia de género) y reglamentaciones sectoriales.
- El empleador tiene deber de prevención (art. 75 LCT) y puede ser responsable solidario si no investigó.

**Uruguay:**
- Ley 18.561 (Acoso Sexual en el Ámbito Laboral) — obliga a toda empresa a tener un protocolo de prevención.
- Ley 19.196 (Acoso Laboral en General) — establece definiciones, obligaciones y sanciones.
- El MTSS puede inspeccionar y sancionar ante incumplimiento.

### Uso de inteligencia artificial

**Argentina y Uruguay:**
- No existe ley específica de IA laboral al momento (2026); se aplica el marco general de:
  - Protección de datos personales (Ley 25.326 AR / Ley 18.331 UY) — decisiones automatizadas que afecten al trabajador.
  - LCT art. 66 (ius variandi) — el empleador puede cambiar métodos de trabajo dentro de límites.
  - CCT: algunos acuerdos colectivos comienzan a incluir cláusulas sobre IA — verificar.
- La política debe abordar: uso de IA generativa con datos confidenciales del cliente / empleador, propiedad de los outputs, no discriminación algorítmica, trazabilidad de decisiones de RRHH con IA.

### Privacidad y protección de datos

**Argentina:**
- Ley 25.326 (LPDP) y su reglamentación (Decreto 1558/2001).
- Resolución AAIP 47/2018 (medidas de seguridad).
- En el ámbito laboral: el monitoreo de comunicaciones del empleado tiene límites — la CSJN ha resuelto que el correo corporativo puede ser monitoreado con aviso previo.

**Uruguay:**
- Ley 18.331 (Protección de Datos Personales) y Decreto 64/020.
- La URCDP (Unidad Reguladora) emite resoluciones vinculantes.
- El empleador puede tratar datos del empleado solo en la medida necesaria para la relación laboral.

---

## Paso 2 — Estructura estándar de la política

### Estructura obligatoria

```
POLÍTICA DE [MATERIA]
[NOMBRE DE LA EMPRESA]
Versión: 1.0  |  Fecha: [DD/MM/AAAA]  |  Vigente desde: [DD/MM/AAAA]

I. OBJETO
[Qué busca lograr esta política y por qué existe]

II. ALCANCE
[A quiénes aplica: empleados, contratistas, pasantes, directores, etc.]
[Jurisdicciones cubiertas]

III. DEFINICIONES
[Términos clave con definición precisa — evitar ambigüedad]

IV. PRINCIPIOS GENERALES
[Marco de valores sobre el cual se apoya la política]

V. OBLIGACIONES DE LA EMPRESA
[Qué debe hacer el empleador]

VI. OBLIGACIONES DE LOS EMPLEADOS
[Qué deben y qué no deben hacer los empleados]

VII. PROCEDIMIENTO
[Pasos a seguir para ejercer derechos, formular denuncias, solicitar excepciones, etc.]

VIII. SANCIONES
[Consecuencias del incumplimiento — remisión al régimen disciplinario general]

IX. DISPOSICIONES JURISDICCIONALES
IX.A Argentina
[Reglas específicas de AR que difieren de las generales o las complementan]
IX.B Uruguay
[Reglas específicas de UY que difieren de las generales o las complementan]

X. VIGENCIA Y REVISIÓN
[Cuándo entra en vigor; con qué frecuencia se revisa; quién es el responsable]

XI. CONTACTO Y CONSULTAS
[Área responsable: RRHH / Legal / DPO / Canal de denuncias]
```

---

## Paso 3 — Redacción de la política

Con los datos recopilados y el encuadre normativo correspondiente, redactar el borrador
completo siguiendo la estructura del Paso 2.

**Criterios de redacción:**
- Lenguaje claro y accesible para el empleado promedio (a menos que el cliente solicite tono técnico-legal).
- Cláusulas concretas, no declarativas: "el empleado no debe compartir información confidencial de clientes con herramientas de IA generativa externas sin aprobación previa de [ÁREA]" en lugar de "se protegerá la confidencialidad".
- Suplementos jurisdiccionales: cuando Argentina y Uruguay tengan reglas distintas, presentarlas en secciones separadas (IX.A y IX.B) para facilitar la implementación diferenciada.
- Las sanciones deben remitir al régimen disciplinario general del empleador — no inventar sanciones nuevas en la política.

---

## Paso 4 — Checklist de implementación

Una vez aprobada la política por el abogado actuante y el cliente:

- [ ] Traducir o adaptar si hay empleados en idioma diferente (en UY: español estándar; en AR: español rioplatense formal)
- [ ] Distribuir a todos los alcanzados y obtener acuse de recibo firmado (físico o digital)
- [ ] Incorporar al proceso de inducción de nuevos empleados
- [ ] Si aplica CCT: verificar que la política no contradiga disposiciones convencionales
- [ ] Si hay comité sindical: evaluar necesidad de consulta previa (art. 25 Ley 14.250 AR; Ley 18.566 UY)
- [ ] Registrar la política en el sistema de gestión documental del cliente con número de versión
- [ ] Calendarizar la próxima revisión (recomendado: anual o ante cambio normativo)
- [ ] Si incluye tratamiento de datos personales: verificar con el DPO o responsable de protección de datos

---

## Guardrails

- Las políticas no pueden establecer condiciones por debajo de los mínimos legales o convencionales: una cláusula que restrinja derechos del empleado por debajo de la LCT o de la Ley 18.566 UY es nula de pleno derecho (art. 12 LCT).
- En Argentina, la Ley 27.555 es de orden público: las cláusulas de teletrabajo que contravengan sus disposiciones (ej. negar la reversibilidad, cargar al empleado con el costo de la conectividad) son inválidas.
- En Uruguay, la Ley 18.561 obliga a toda empresa a contar con protocolo de prevención de acoso sexual — si el cliente no lo tiene, la política debe suplir ese vacío con urgencia.
- Si la política incluye monitoreo de comunicaciones o dispositivos del empleado: advertir que requiere notificación previa por escrito y puede tener límites constitucionales de privacidad (art. 19 Constitución AR; art. 28 Constitución UY).
- El borrador es un insumo — no implementar sin revisión del abogado actuante y aprobación del cliente.
- Si hay CCT aplicable con comisión paritaria: algunas materias requieren negociación previa con el sindicato antes de implementar la política (art. 25 Ley 14.250 AR).
