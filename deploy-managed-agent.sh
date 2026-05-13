#!/usr/bin/env bash
# deploy-managed-agent.sh
# Despliega un agente programado del repo claude-para-legal-rioplatense
# vía la Claude Managed Agents API.
#
# Uso:
#   bash scripts/deploy-managed-agent.sh <nombre-agente>
#
# Agentes disponibles:
#   monitor-normas          - Monitor de cambios normativos (BCU, BCRA, AFIP, CNV, URSEA)
#   vencimiento-contratos   - Vigía semanal de vencimientos de contratos
#   seguimiento-expedientes - Monitor de expedientes judiciales (PJN / Poder Judicial UY)
#   diligencia-grilla       - Grilla de diligencia M&A
#   radar-lanzamiento       - Monitor de lanzamientos de productos
#
# Requisitos:
#   - ANTHROPIC_API_KEY seteada en el entorno
#   - curl y jq instalados
#   - Python 3.8+ para el orquestador (opcional)

set -euo pipefail

AGENT_NAME="${1:-}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
API_BASE="https://api.anthropic.com/v1"

if [[ -z "$AGENT_NAME" ]]; then
  echo "Uso: $0 <nombre-agente>"
  echo "Agentes disponibles: monitor-normas | vencimiento-contratos | seguimiento-expedientes | diligencia-grilla | radar-lanzamiento"
  exit 1
fi

if [[ -z "${ANTHROPIC_API_KEY:-}" ]]; then
  echo "Error: ANTHROPIC_API_KEY no está seteada."
  exit 1
fi

COOKBOOK_DIR="$REPO_ROOT/managed-agent-cookbooks/$AGENT_NAME"

if [[ ! -d "$COOKBOOK_DIR" ]]; then
  echo "Error: No se encontró el cookbook para '$AGENT_NAME' en $COOKBOOK_DIR"
  exit 1
fi

AGENT_YAML="$COOKBOOK_DIR/agent.yaml"
if [[ ! -f "$AGENT_YAML" ]]; then
  echo "Error: No se encontró $AGENT_YAML"
  exit 1
fi

echo "▶ Desplegando agente: $AGENT_NAME"
echo "  Cookbook: $COOKBOOK_DIR"
echo ""

# Leer configuración del agent.yaml
AGENT_DISPLAY_NAME=$(grep "^display_name:" "$AGENT_YAML" | awk '{print $2}' | tr -d '"')
AGENT_DESCRIPTION=$(grep "^description:" "$AGENT_YAML" | cut -d: -f2- | xargs)
SCHEDULE=$(grep "^schedule:" "$AGENT_YAML" | awk '{print $2}' | tr -d '"')

echo "  Nombre: $AGENT_DISPLAY_NAME"
echo "  Schedule: $SCHEDULE"
echo ""

# Construir el payload del agente
SYSTEM_PROMPT_FILE="$COOKBOOK_DIR/system-prompt.md"
if [[ ! -f "$SYSTEM_PROMPT_FILE" ]]; then
  echo "Advertencia: No se encontró system-prompt.md — usando descripción como prompt base"
  SYSTEM_PROMPT="$AGENT_DESCRIPTION"
else
  SYSTEM_PROMPT=$(cat "$SYSTEM_PROMPT_FILE")
fi

# POST a la API de Managed Agents
echo "▶ Creando agente en la API..."

RESPONSE=$(curl -s -X POST "$API_BASE/agents" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2025-01-01" \
  -d "{
    \"name\": \"$AGENT_NAME\",
    \"display_name\": \"$AGENT_DISPLAY_NAME\",
    \"description\": \"$AGENT_DESCRIPTION\",
    \"system_prompt\": $(echo "$SYSTEM_PROMPT" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))'),
    \"schedule\": \"$SCHEDULE\"
  }")

if echo "$RESPONSE" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("id",""))' | grep -q "^agt_"; then
  AGENT_ID=$(echo "$RESPONSE" | python3 -c 'import json,sys; print(json.load(sys.stdin)["id"])')
  echo "✅ Agente creado: $AGENT_ID"
  echo ""
  echo "Para ver el estado:"
  echo "  curl -s -H 'x-api-key: \$ANTHROPIC_API_KEY' $API_BASE/agents/$AGENT_ID"
  echo ""
  echo "Para disparar manualmente:"
  echo "  curl -s -X POST -H 'x-api-key: \$ANTHROPIC_API_KEY' $API_BASE/agents/$AGENT_ID/run"
else
  echo "❌ Error al crear el agente:"
  echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
  exit 1
fi
