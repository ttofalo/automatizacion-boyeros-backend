#!/bin/bash
set -e

# Directorio de trabajo definido
PROJECT_DIR="/home/admin/automatizacion-boyeros-backend"

echo "Iniciando despliegue el $(date)..."
cd "$PROJECT_DIR"

echo "Obteniendo últimos cambios..."
git pull origin main

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Reiniciando servicio..."
sudo systemctl restart boyeros-backend

echo "¡Despliegue finalizado con éxito!"
