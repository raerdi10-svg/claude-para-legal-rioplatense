#!/usr/bin/env python3
"""
validate.py — Validador de estructura del repo claude-para-legal-rioplatense.

Uso:
  python scripts/validate.py --check manifests
  python scripts/validate.py --check skills
  python scripts/validate.py --check description-length
  python scripts/validate.py --check agents
  python scripts/validate.py  # corre todas las validaciones
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).parent.parent
PLUGINS = [
    "civil-comercial", "corporativo", "laboral", "litigio",
    "regulatorio", "privacidad", "propiedad-intelectual", "administrativo",
    "gobernanza-ia", "clinica-juridica", "estudiante-derecho", "hub-constructor"
]
MAX_DESCRIPTION_LENGTH = 1024

errors = []
warnings = []


def check_manifests():
    """Verifica que cada plugin tenga un plugin.json válido."""
    print("▶ Validando manifests de plugins...")
    required_fields = ["name", "display_name", "description", "version", "license", "skills"]

    for plugin in PLUGINS:
        manifest_path = REPO_ROOT / plugin / ".claude-plugin" / "plugin.json"
        if not manifest_path.exists():
            errors.append(f"[{plugin}] Falta .claude-plugin/plugin.json")
            continue

        try:
            with open(manifest_path) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"[{plugin}] JSON inválido en plugin.json: {e}")
            continue

        for field in required_fields:
            if field not in data:
                errors.append(f"[{plugin}] Campo faltante en plugin.json: '{field}'")

        if "skills" in data:
            for skill in data["skills"]:
                for sf in ["name", "description", "user-invocable"]:
                    if sf not in skill:
                        errors.append(f"[{plugin}] Skill '{skill.get('name', '?')}' en plugin.json le falta campo '{sf}'")

    if not any("[manifest]" in e for e in errors):
        print("  ✅ Manifests OK")


def check_skills():
    """Verifica que las skills tengan frontmatter correcto."""
    print("▶ Validando frontmatter de skills...")
    required_frontmatter = ["name", "description", "user-invocable"]

    for plugin in PLUGINS:
        skills_dir = REPO_ROOT / plugin / "skills"
        if not skills_dir.exists():
            continue

        for skill_dir in skills_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"[{plugin}/{skill_dir.name}] Falta SKILL.md")
                continue

            content = skill_md.read_text()
            if not content.startswith("---"):
                errors.append(f"[{plugin}/{skill_dir.name}] SKILL.md no tiene frontmatter YAML")
                continue

            # Extraer frontmatter
            parts = content.split("---", 2)
            if len(parts) < 3:
                errors.append(f"[{plugin}/{skill_dir.name}] Frontmatter YAML malformado")
                continue

            try:
                frontmatter = yaml.safe_load(parts[1])
            except yaml.YAMLError as e:
                errors.append(f"[{plugin}/{skill_dir.name}] Error en YAML frontmatter: {e}")
                continue

            for field in required_frontmatter:
                if field not in (frontmatter or {}):
                    errors.append(f"[{plugin}/{skill_dir.name}] Campo faltante en frontmatter: '{field}'")

    print("  ✅ Skills OK" if not errors else "  ❌ Hay errores en skills")


def check_description_length():
    """Verifica que las descripciones de skills no superen 1024 caracteres."""
    print(f"▶ Verificando límite de descripción ({MAX_DESCRIPTION_LENGTH} chars)...")

    for plugin in PLUGINS:
        skills_dir = REPO_ROOT / plugin / "skills"
        if not skills_dir.exists():
            continue

        for skill_dir in skills_dir.iterdir():
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue

            content = skill_md.read_text()
            parts = content.split("---", 2)
            if len(parts) < 3:
                continue

            try:
                frontmatter = yaml.safe_load(parts[1])
                if frontmatter and "description" in frontmatter:
                    desc = str(frontmatter["description"])
                    if len(desc) > MAX_DESCRIPTION_LENGTH:
                        errors.append(
                            f"[{plugin}/{skill_dir.name}] Descripción excede {MAX_DESCRIPTION_LENGTH} chars "
                            f"({len(desc)} chars)"
                        )
            except yaml.YAMLError:
                pass

    print("  ✅ Longitudes OK" if not errors else "  ❌ Hay descripciones demasiado largas")


def check_agents():
    """Verifica que los cookbooks de managed agents tengan agent.yaml."""
    print("▶ Validando cookbooks de agentes...")
    cookbooks_dir = REPO_ROOT / "managed-agent-cookbooks"
    if not cookbooks_dir.exists():
        warnings.append("No se encontró managed-agent-cookbooks/ — omitiendo validación de agentes")
        return

    required_yaml_fields = ["name", "display_name", "description", "schedule"]

    for cookbook_dir in cookbooks_dir.iterdir():
        if not cookbook_dir.is_dir():
            continue
        agent_yaml = cookbook_dir / "agent.yaml"
        if not agent_yaml.exists():
            errors.append(f"[cookbooks/{cookbook_dir.name}] Falta agent.yaml")
            continue

        try:
            with open(agent_yaml) as f:
                content = f.read()
            # Parsear solo la sección YAML (ignorar el system prompt después de ---)
            yaml_content = content.split("---\n")[0] + content.split("---")[1] if "---\n---" not in content else content
            # Intentar parsear el primer bloque YAML
            data = yaml.safe_load(content.split("---")[1] if content.startswith("---") else content)
        except yaml.YAMLError as e:
            errors.append(f"[cookbooks/{cookbook_dir.name}] YAML inválido en agent.yaml: {e}")
            continue

        if data:
            for field in required_yaml_fields:
                if field not in data:
                    warnings.append(f"[cookbooks/{cookbook_dir.name}] Campo sugerido faltante en agent.yaml: '{field}'")

    print("  ✅ Cookbooks OK" if not any("cookbooks" in e for e in errors) else "  ❌ Hay errores en cookbooks")


def main():
    parser = argparse.ArgumentParser(description="Validador del repo claude-para-legal-rioplatense")
    parser.add_argument("--check", choices=["manifests", "skills", "description-length", "agents"],
                        help="Validación específica a ejecutar")
    args = parser.parse_args()

    print("Claude para Legal Rioplatense — Validador\n")

    if args.check == "manifests" or not args.check:
        check_manifests()
    if args.check == "skills" or not args.check:
        check_skills()
    if args.check == "description-length" or not args.check:
        check_description_length()
    if args.check == "agents" or not args.check:
        check_agents()

    print()
    if warnings:
        print(f"⚠️  Advertencias ({len(warnings)}):")
        for w in warnings:
            print(f"   {w}")

    if errors:
        print(f"\n❌ Errores ({len(errors)}):")
        for e in errors:
            print(f"   {e}")
        print()
        sys.exit(1)
    else:
        print("✅ Validación completada — sin errores.")


if __name__ == "__main__":
    main()
