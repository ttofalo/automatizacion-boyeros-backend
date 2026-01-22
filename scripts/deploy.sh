#!/bin/bash
set -e

# Directorio de trabajo definido
PROJECT_DIR="/home/admin/automatizacion-boyeros-backend"

echo "Iniciando despliegue el $(date)..."
cd "$PROJECT_DIR"

echo "Obteniendo últimos cambios..."
git pull origin main


# Asegurar que el PATH incluye los binarios locales del usuario (pip, uvicorn)
export PATH=$PATH:/home/admin/.local/bin

echo "Instalando dependencias..."
# Usar el pip del usuario (sin venv, coincide con el servicio systemd)
# Se agrega --break-system-packages porque estamos en un entorno gestionado
pip install -r requirements.txt --break-system-packages

echo "Reiniciando servicio..." 
sudo systemctl restart boyeros-backend

echo "¡Despliegue finalizado con éxito!"
