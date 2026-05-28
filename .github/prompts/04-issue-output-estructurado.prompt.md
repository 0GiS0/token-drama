---
name: "04 Issue Output Estructurado"
description: "Demo con formato: issue en tabla comparativa de accion"
argument-hint: "Issue para analizar"
agent: "agent"
---

Analiza el issue y responde SOLO con esta estructura:

Refiere siempre el contenido al issue 1.

| Campo                | Contenido               |
| -------------------- | ----------------------- |
| Problem summary      | Una frase               |
| Suspected root cause | Una frase               |
| Evidence needed      | Maximo 3 bullets cortos |
| Proposed fix         | Maximo 3 bullets cortos |
| Risks                | Maximo 2 bullets        |
| Done when            | Criterio verificable    |

Reglas:

- No agregues secciones fuera de la tabla.
- Si falta informacion, escribe "Unknown" en la celda.
