# Token Drama

<div align="center">

[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC140iBrEZbOtvxWsJ-Tb0lQ?style=for-the-badge&logo=youtube&logoColor=white&color=red)](https://www.youtube.com/c/GiselaTorres?sub_confirmation=1)
[![GitHub followers](https://img.shields.io/github/followers/0GiS0?style=for-the-badge&logo=github&logoColor=white)](https://github.com/0GiS0)
[![LinkedIn Follow](https://img.shields.io/badge/LinkedIn-S%C3%ADgueme-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/giselatorresbuitrago/)
[![X Follow](https://img.shields.io/badge/X-S%C3%ADgueme-black?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/0GiS0)

</div>

---

¡Hola developer 👋🏻! Este proyecto acompaña el vídeo **"💸 GitHub Copilot: aprovecha mejor tus AI Credits"** y sirve como app de ejemplo para probar cómo pequeños cambios en tus prompts pueden cambiar el resultado de Copilot.

Aquí verás un escenario visual (token drama) ideal para experimentar con prompts en español/inglés, output estructurado, límites de respuesta y restricciones de tools.

<a href="https://youtu.be/6hCjypUW_tY">
 <img src="https://img.youtube.com/vi/6hCjypUW_tY/maxresdefault.jpg" alt="💸 GitHub Copilot: aprovecha mejor tus AI Credits" width="100%" />
</a>

## 📑 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías-utilizadas)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Capítulos del vídeo](#-capítulos-del-vídeo)
- [Sígueme](#-sígueme-en-mis-redes-sociales)

## ✨ Características

- App de ejemplo construida para practicar prompt engineering con GitHub Copilot.
- Interfaz visual con componentes reutilizables en Astro para simular un ranking de "drama de tokens".
- Escenario perfecto para comparar resultados con distintos estilos de prompt.
- Base ligera y rápida, sin dependencias innecesarias.
- Ideal para demos, vídeos y talleres sobre productividad con IA.

## 🛠️ Tecnologías Utilizadas

- [Astro 6](https://astro.build/) como framework principal.
- TypeScript para tipado y soporte en archivos de datos.
- Node.js como entorno de ejecución.
- npm para gestión de dependencias y scripts.
- Despliegue compatible con cualquier hosting estático (Netlify, Vercel, GitHub Pages, etc.).

## 📋 Requisitos Previos

- macOS, Linux o Windows.
- Node.js `22.12.0` o superior.
- npm (incluido con Node.js).
- Git para clonar el repositorio.

## 🚀 Instalación

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/0GiS0/token-drama.git
cd token-drama
```

### Paso 2: Instalar dependencias

```bash
npm install
```

### Paso 3: Configurar variables de entorno

```bash
# Este proyecto no requiere variables de entorno para funcionar.
# Si en el futuro se añaden, podrás usar:
# cp .env.example .env
```

### Paso 4: Ejecutar el proyecto

```bash
npm run dev
```

## 💻 Uso

Una vez arrancado el servidor, abre tu navegador en `http://localhost:4321`.

Puedes usar esta app para repetir los experimentos del vídeo y comparar respuestas de Copilot según el tipo de prompt:

- Español vs inglés.
- Con o sin output estructurado.
- Prompt abierto vs prompt con límites estrictos.
- Pedir implementación + explicación vs solo código.
- Restringir herramientas disponibles en sesión.

### Ejemplo Básico

```bash
# Desarrollo
npm run dev

# Build de producción
npm run build

# Vista previa local del build
npm run preview
```

> Nota importante
> Si estás midiendo consumo de AI Credits, intenta mantener prompts consistentes entre pruebas para comparar resultados de forma justa.

## 📁 Estructura del Proyecto

```text
token-drama/
├── public/
├── src/
│   ├── components/
│   │   ├── ChaosToggle.astro
│   │   ├── InfoCard.astro
│   │   ├── RankingCard.astro
│   │   ├── Sidebar.astro
│   │   └── TokenScore.astro
│   ├── data/
│   │   └── rankings.ts
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       └── index.astro
├── astro.config.mjs
├── package.json
├── tsconfig.json
└── README.md
```

## 🎬 Capítulos del vídeo

- [`00:00`](https://youtu.be/6hCjypUW_tY?t=0) 👋🏻 Introducción
- [`01:20`](https://youtu.be/6hCjypUW_tY?t=80) 🧪 Aplicación de ejemplo
- [`03:44`](https://youtu.be/6hCjypUW_tY?t=224) 🇪🇸 Prompt en español
- [`08:00`](https://youtu.be/6hCjypUW_tY?t=480) 🇬🇧 Prompt en inglés
- [`10:19`](https://youtu.be/6hCjypUW_tY?t=619) 🧾 Sin output estructurado
- [`12:18`](https://youtu.be/6hCjypUW_tY?t=738) 📐 Con output estructurado
- [`15:03`](https://youtu.be/6hCjypUW_tY?t=903) 🤯 Pedir demasiadas cosas sin límites claros
- [`16:58`](https://youtu.be/6hCjypUW_tY?t=1018) 🚧 Pedir muchas cosas con hard limits
- [`18:39`](https://youtu.be/6hCjypUW_tY?t=1119) 🧑🏻‍💻 Pedir implementación y explicación
- [`20:57`](https://youtu.be/6hCjypUW_tY?t=1257) ⚡ Pedir solo el código, sin explicación
- [`22:10`](https://youtu.be/6hCjypUW_tY?t=1330) 🛠️ Restringir las tools de la sesión
- [`26:06`](https://youtu.be/6hCjypUW_tY?t=1566) 🔍 Herramienta rtk

## 🌐 Sígueme en Mis Redes Sociales

Si te ha gustado este proyecto y quieres ver más contenido como este, no olvides suscribirte a mi canal de YouTube y seguirme en mis redes sociales:

<div align="center">

[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC140iBrEZbOtvxWsJ-Tb0lQ?style=for-the-badge&logo=youtube&logoColor=white&color=red)](https://www.youtube.com/c/GiselaTorres?sub_confirmation=1)
[![GitHub followers](https://img.shields.io/github/followers/0GiS0?style=for-the-badge&logo=github&logoColor=white)](https://github.com/0GiS0)
[![LinkedIn Follow](https://img.shields.io/badge/LinkedIn-S%C3%ADgueme-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/giselatorresbuitrago/)
[![X Follow](https://img.shields.io/badge/X-S%C3%ADgueme-black?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/0GiS0)

</div>
