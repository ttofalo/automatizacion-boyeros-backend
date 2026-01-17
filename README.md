# Backend - Automatización de Boyeros Eléctricos

Backend para el control y monitoreo de boyeros eléctricos mediante ESP32.

## Estructura
- `app/`: Código fuente principal
- `tests/`: Tests automatizados

## Ejecución

1. **Crear entorno virtual (Recomendado):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # En Windows
   # source venv/bin/activate # En Linux/Mac
   ```

2. Instalar dependencias: 
   ```bash
   pip install -r requirements.txt
   ```

3. Correr servidor: 
   ```bash
   uvicorn app.main:app --reload
   ```

## API Docs
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
