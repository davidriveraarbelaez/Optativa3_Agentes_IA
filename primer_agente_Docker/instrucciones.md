# Primer agente local

## Instalaciones

- Python.

- UV. Ingresar a la terminar, copiar y pegar la siguiente instrucción. 

```bash
pip install uv
```

## Crear el proyecto.

1. Crear la carpeta del proyecto

2. Inicializar el proyecto con UV
```bash
uv init --name first-agent-gemini
```

3. Añadir todas las dependencias (uv crea el .env automáticamente).
```bash
uv add langchain langchain-google-genai langchain-community fastapi uvicorn python-dotenv
```