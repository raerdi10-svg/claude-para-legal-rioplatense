---
name: baremo-ilp
description: >
  Calcula el porcentaje de Incapacidad Laboral Permanente (ILP) y el quantum indemnizatorio
  según el Decreto 549/2025 (Tabla de Evaluación de Incapacidades Laborales, Ley 24.557 ART,
  vigente desde febrero 2026). Acepta informes médicos (EMG, RMI, espirometría, ecocardiograma,
  psicodiagnóstico) o hallazgos ya sistematizados. Aplica la metodología oficial: Suma Aritmética
  (SA) por grupo anatómico con techos sectoriales, Capacidad Restante (CR) entre grupos, Factores
  de Ponderación (actividad + edad), preexistencia y techo normativo. Produce el cálculo paso a
  paso y el quantum (Ley 24.557 art. 14) con el IBM que provea el abogado. Solo para Argentina.
argument-hint: "[subir informe médico PDF] o [listar secuelas con %] [--ibm=MONTO] [--edad=N] [--fp=leve|intermedia|alta]"
user-invocable: true
---

# Skill: Cálculo de Incapacidad Laboral Permanente — Baremo Dto. 549/2025

## Propósito

Asistir al abogado laboralista o al consultor médico-legal en el cálculo del porcentaje de ILP
y el quantum indemnizatorio en causas ART (Ley 24.557), aplicando la metodología exacta del
Decreto 549/2025 (IF-2025-19864352-APN-SRT#MCH), vigente desde febrero 2026.

El output es un cálculo de referencia para el abogado actuante. No reemplaza el dictamen
pericial médico ni el asesoramiento jurídico. Los % estimados desde EMG o imágenes requieren
confirmación por examen físico pericial.

**Solo jurisdicción Argentina.** Uruguay no usa este baremo.

---

## Paso 0 — Lectura del perfil de práctica

Leer `laboral/CLAUDE.md` para incorporar:
- Umbrales de riesgo del estudio
- Convenios colectivos habituales (pueden afectar el IBM)
- Si el estudio trabaja del lado actor o demandado (ART/empleador)

---

## Paso 1 — Recolección de datos

Solicitar antes de calcular:

**Datos del trabajador:**
- Edad al momento de la evaluación médica
- Actividad/ocupación habitual (para el Factor de Ponderación de actividad)
- IBM — Ingreso Base Mensual: promedio de remuneraciones de los últimos 12 meses
  (lo aporta el abogado — no lo estima esta skill)

**Material médico** (una de las dos opciones):
- A) PDF del informe médico / estudios complementarios → extraer secuelas con IA
- B) Lista de secuelas con % de tabla ya asignados → calcular directamente

**Preexistencia** (si existe):
- % de incapacidad preexistente documentada (sin FP)

---

## Paso 2 — Extracción de secuelas desde informes médicos

Si el abogado sube un informe médico, actuar como perito consultor aplicando el baremo.

### Nervio periférico (Tabla 5)

**Fórmula:** ILP = (%total × comp_motor × escalaM) + (%total × comp_sensitivo × escalaS)

Nervios MMSS (%total / motor / sensitivo):
- N. Mediano DISTAL (STC/canal carpo): 25% / 40% / 60%
- N. Mediano PROXIMAL: 40% / 70% / 30%
- N. Cubital DISTAL: 25% / 70% / 30%
- N. Cubital PROXIMAL: 35% / 70% / 30%
- N. Radial: 30% / 90% / 10%
- N. Axilar/Circunflejo: 20% / 98% / 2%

Escala M: M0=100% | M1/M2=80% | M3=50% | M4=20% | M5=0%
Escala S: S0=100% | S1/S2=80% | S3=50% | S4=20% | S5=0%

EMG "leve" → M5/S3 | EMG "moderado" → M4/S3 | EMG "severo" → M3/S2

Ejemplo oficial (N. Mediano distal M4/S3):
25%×40%=10% motor; 25%×60%=15% sensitivo
ILP = 10%×0,20 + 15%×0,50 = 2% + 7,5% = 9%

### Psiquiatría — RVA/DVAN (Tabla 2)

Grado I=5% | I-II=10% | II=15% | II-III=20% | III=25% | III-IV=30% | IV=35%
Si el psicodiagnóstico ya asignó el grado, tomar ese directamente.

### Columna vertebral (SA)

Hernia discal operada: 5% por nivel
Fractura C3-C7 con secuelas: 8% | sin secuelas: 4%
Fractura L2-L5 con secuelas: 10% | sin secuelas: 5%
Techo Cervical: 40% | Techo Dorsolumbar: 60%

### Sistema respiratorio

VEF1/CVF post-BD: ≥80%→10% | 75-80%→15% | 70-75%→20% | 65-70%→25%
60-65%→35% | 55-60%→45% | 50-55%→55% | 35-50%→70% | ≤35%→100%

### Cardiovascular

FEVI: ≥52%+antec.=10% | 41-51%=30% | 31-40%=50% | ≤30%=70%

### Exclusiones

- Dolor sin sustrato objetivo documentado
- Tendinitis/distensión/contractura SIN ruptura completa documentada
- Hallazgos degenerativos sin nexo causal laboral

---

## Paso 3 — Agrupación anatómica

| Grupo | Metodología | Techo |
|---|---|---|
| Columna Cervical | SA | 40% |
| Columna Dorsolumbar | SA | 60% |
| Miembro Superior Der. | SA | 66% |
| Miembro Superior Izq. | SA | 66% |
| Miembro Inferior Der. | SA | 70% |
| Miembro Inferior Izq. | SA | 70% |
| Cicatrices Quemaduras | SA | sin techo |
| Pérdida Piezas Dentarias | SA | sin techo |
| Nervioso, Psiquiatría, Respiratorio, Cardiovascular, ORL, Oftalmología, Piel, etc. | CR | sin techo |

SA: secuelas del mismo miembro y misma lateralidad → suma aritmética con techo.
CR entre grupos: resultados de cada grupo entran al CR global de mayor a menor.

---

## Paso 4 — Cálculo de ILP

### 4.1 SA por grupo
Sumar aritméticamente. Si supera el techo, aplicar el techo.

### 4.2 Capacidad Restante global
Ordenar de mayor a menor. Aplicar iterativamente:
- Primera entrada: aporte directo
- Siguientes: aporte = (% / 100) × CR disponible

### 4.3 Factores de Ponderación
FP = FP_actividad + FP_edad (suma, no multiplicación)

FP actividad:
- Leve (estético, sin reubicación): +5%
- Intermedia (excede estético, sin reubicación): +10%
- Alta (reubicado, ILPT, o recalificación rechazada): +20%

FP edad al momento de evaluación:
- < 21 años: +5% | 21-35: +4% | 36-45: +3% | ≥ 46: +2%

Incremento FP = FP_total% × subtotal_CR
Subtotal con FP = subtotal_CR + incremento_FP

### 4.4 Preexistencia
CR disponible = 100% - preexistencia%
Resultado = subtotal_FP × CR_disponible / 100

### 4.5 Techo normativo
- ILPP: si resultado ≥ 66% → 65,99%
- ILPT: si resultado > 100% → 100%

---

## Paso 5 — Quantum (Ley 24.557 art. 14)

Solo calcular si el abogado proveyó el IBM.

ILPP: Quantum = IBM × (65/edad) × (ILP%/100) × 53
ILPT: Quantum = IBM × (65/edad) × 53

Adicional opcional: +20% Ley 26.773 art. 3 si aplica.

Advertencia: verificar piso mínimo SRT vigente. No incluye intereses ni costas.

---

## Paso 6 — Output estructurado
