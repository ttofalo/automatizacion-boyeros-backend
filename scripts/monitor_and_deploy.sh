#!/bin/bash

# Configuración
PROJECT_DIR="/home/admin/automatizacion-boyeros-backend"
DEPLOY_SCRIPT="$PROJECT_DIR/scripts/deploy.sh"

cd "$PROJECT_DIR" || exit 1

# Asegurarse de estar en main
git checkout main > /dev/null 2>&1

# Traer información remota sin fusionar cambios
git remote update > /dev/null 2>&1

# Verificar estado
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "$(date): Detectados cambios en remoto. Iniciando actualización..."
    # Ejecutar script de deploy existente
    if [ -f "$DEPLOY_SCRIPT" ]; then
        "$DEPLOY_SCRIPT" >> "$PROJECT_DIR/deploy.log" 2>&1
    else
        echo "Error: No se encontró el script de deploy en $DEPLOY_SCRIPT"
    fi
fi
