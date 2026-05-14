---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del perfil regulatorio del estudio.
  Recopila organismos reguladores relevantes, sectores de clientes, tipo de productos
  habituales, umbrales de riesgo y socio de referencia, y escribe el perfil en CLAUDE.md.
argument-hint: "[nombre del estudio o abogado responsable]"
user-invocable: true
---

# Skill: Configuración Inicial — Perfil Regulatorio

## Propósito

Obtener del usuario la información necesaria para personalizar todos los skills del plugin
`regulatorio` a la práctica concreta del estudio. El resultado queda escrito en el archivo
`CLAUDE.md` del plugin, que cada skill lee al iniciarse. Sin este perfil, las referencias
a organismos, normas y plazos pueden no corresponderse con los sectores y jurisdicciones
del cliente.

---

## Paso 0 — Presentación

Presentarse brevemente y explicar el propósito de la entrevista:

> "Voy a hacerte una serie de preguntas para configurar el asistente de derecho regulatorio
> a la práctica de tu estudio. Con esa información, los skills de revisión de lanzamiento
> de productos y análisis de brechas normativas van a usar los organismos, los plazos y
> los criterios de riesgo correctos para tu contexto. La entrevista dura aproximadamente
> diez minutos."

---

## Paso 1 — Jurisdicción

Preguntar:

1. ¿El estudio opera principalmente en **Uruguay**, en **Argentina**, o en **ambas**
   jurisdicciones?
2. Si opera en ambas: ¿hay una jurisdicción predominante o depende del sector del cliente?
3. ¿Asesoran a clientes con presencia regulatoria en terceros países (Brasil, Chile,
   Paraguay, México, España)?

---

## Paso 2 — Sectores de clientes

Preguntar:

1. ¿En qué sectores regulados se concentra la práctica? (Marcar todos los que apliquen.)
   - Servicios financieros (bancos, cooperativas de crédito, casas de cambio)
   - Fintech (pagos digitales, lending, crowdfunding, criptoactivos)
   - Seguros y reaseguros
   - Mercado de capitales y fondos de inversión
   - Salud y farmacéutico (medicamentos, dispositivos médicos, suplementos)
   - Alimentario (elaboración, importación, distribución)
   - Telecomunicaciones y medios (TV, radio, internet, OTT)
   - Energía (electricidad, gas, combustibles)
   - Servicios públicos (agua, transporte)
   - Comercio electrónico y plataformas digitales
   - Inteligencia artificial y datos masivos
   - Sector público y concesiones
   - Otro: ___

2. ¿Hay algún sector con regulación especialmente activa o en cambio frecuente que el
   estudio monitoree con mayor atención?

---

## Paso 3 — Organismos reguladores habituales

Preguntar:

1. ¿Con qué organismos reguladores interactúa el estudio con más frecuencia?
   (Seleccionar los relevantes de la lista en CLAUDE.md o agregar otros.)
2. ¿El estudio tiene experiencia en procedimientos de autorización o registro ante alguno
   de esos organismos? ¿Cuáles?
3. ¿Hay algún organismo con el que el estudio tenga un canal de consulta informal
   establecido? (No es obligatorio revelarlo, pero ayuda a calibrar el perfil.)

---

## Paso 4 — Tipo de productos y servicios habituales

Preguntar:

1. ¿Cuál es el tipo de producto o servicio que el estudio revisa con más frecuencia
   antes de su lanzamiento?
   - Producto financiero nuevo (cuenta, tarjeta, crédito, inversión)
   - Servicio de pago o transferencia (wallet, PSP, fintech)
   - Plataforma digital o marketplace
   - Medicamento, suplemento o dispositivo médico
   - Alimento o bebida con nueva fórmula o claims de salud
   - Servicio de telecomunicaciones o contenido audiovisual
   - Producto energético o servicio de distribución
   - Producto con recopilación masiva de datos (IoT, IA, biometría)
   - Otro: ___

2. ¿Los lanzamientos suelen ser en etapa temprana (previo a cualquier interacción con el
   regulador) o cuando ya hay un prototipo o producto operativo?

---

## Paso 5 — Umbrales de riesgo y reglas de escalamiento

Preguntar:

1. ¿Cuál es el nombre del socio o área responsable de regulatorio a quien escalar cuando
   un lanzamiento requiere autorización previa del regulador?
2. ¿Cuál es el umbral de complejidad o riesgo a partir del cual el estudio consulta al
   organismo regulador directamente antes de opinar al cliente?
3. ¿Hay algún tipo de producto o sector en el que el estudio no asesora por política interna?
4. ¿El estudio tiene obligaciones propias como sujeto obligado ante la UIF (Argentina) o
   el SENACLAFT (Uruguay)?

---

## Paso 6 — Seguimiento normativo

Preguntar:

1. ¿El estudio realiza monitoring de cambios normativos para algún organismo o sector en
   particular?
2. ¿Tiene una biblioteca de políticas internas de clientes indexada que quiera usar con
   el skill `diff-politica`? (Se puede referenciar como documento semilla en CLAUDE.md.)
3. ¿Hay alguna resolución, comunicación o decreto reciente que esté en análisis y deba
   considerarse en los análisis?

---

## Paso 7 — Estilo y preferencias

Preguntar:

1. ¿El estudio tiene algún modelo de checklist o memo regulatorio que quiera usar como
   punto de partida? (Se puede cargar como documento semilla en CLAUDE.md.)
2. ¿Hay alguna preferencia de formato para los outputs?
   (Checklist / Semáforo / Memo / Tabla de brechas / Combinación)

---

## Paso 8 — Escritura del perfil

Con las respuestas recopiladas, completar el archivo `CLAUDE.md` del plugin `regulatorio`
con los valores concretos del estudio:

- Jurisdicción principal y secundarias
- Organismos reguladores relevantes (con sus normas y sectores)
- Sectores de clientes atendidos
- Tipo de productos y servicios habituales
- Umbrales de riesgo regulatorio (ajustar los criterios del template al contexto del estudio)
- Reglas de escalamiento (nombres de socios y áreas)
- Documentos semilla (si se cargaron)
- Notas adicionales (normas bajo monitoring, preferencias de formato)

Confirmar al usuario que el perfil fue guardado y mencionar que puede editarlo
directamente en `CLAUDE.md` para ajustes posteriores.

---

## Guardrails

- No escribir datos confidenciales de clientes del estudio en CLAUDE.md (nombres de
  clientes específicos, datos de expedientes). Solo información estructural del estudio.
- Si el usuario menciona un producto ya lanzado que podría estar operando sin
  autorización regulatoria, pausar la configuración y derivar al skill `revision-lanzamiento`
  con carácter urgente.
- No recomendar estrategias regulatorias específicas durante la entrevista de configuración:
  ese es el rol de los otros skills y del abogado a cargo.
- No registrar en CLAUDE.md información que pueda identificar a un cliente concreto en
  una situación de riesgo regulatorio activa.
