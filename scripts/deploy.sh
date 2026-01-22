#!/bin/bash
set -e

# Directorio de trabajo definido
PROJECT_DIR="/home/admin/automatizacion-boyeros-backend"

echo "Iniciando despliegue el $(date)..."
cd "$PROJECT_DIR"

echo "Obteniendo últimos cambios..."
git pull origin main


# Validar/Crear entorno virtual
if [ ! -d "venv" ]; then
    echo "⚠️ venv no encontrado. Creando..."
    python3 -m venv venv
fi

echo "Activando entorno virtual..."
source venv/bin/activate

echo "Instalando dependencias..."
python -m pip install -r requirements.txt

echo "Reiniciando servicio..."
sudo systemctl restart boyeros-backend

echo "¡Despliegue finalizado con éxito!"
