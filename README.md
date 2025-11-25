# 🤖 PolicyGPT Enterprise – Backend IA (FastAPI)

> **FastAPI • Azure OpenAI • PyPDF • Pydantic**

Este repositorio contiene el **Motor de Inteligencia Artificial** de PolicyGPT Enterprise.
Se encarga de extraer texto de las pólizas PDF, limpiarlo, enviarlo al modelo de Azure OpenAI, y generar un **informe estructurado**.

---

## ⚙️ Arquitectura y Funcionalidades

### 📄 Extracción de texto PDF
- Limpieza y normalización del contenido.
- Eliminación de caracteres especiales.
- Unificación de bloques de texto.

### 🧠 Análisis con Azure OpenAI
- Envío de prompts especializados.
- Recuperación del JSON estructurado generado por gpt-3.5-turbo
- Formato final incluye: Coberturas, Exclusiones, Deducibles y Resumen ejecutivo.

### 🧱 Modelo de Respuesta Estandarizado
Usando Pydantic para validar la salida:

```json
{
  "coverages": [],
  "exclusions": [],
  "deductibles": "",
  "summary": ""
}


