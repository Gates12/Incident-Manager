#!/usr/bin/env bash
set -euo pipefail

if [ ! -f "app/main.py" ]; then
  echo "Error: run this from the incident-management project root."
  exit 1
fi

mkdir -p app/api app/schemas app/services app/repositories

move_if_empty() {
  source_file="$1"
  target_file="$2"

  if [ ! -f "$source_file" ]; then
    echo "Skipped: $source_file does not exist"
    return
  fi

  if [ ! -e "$target_file" ] || [ ! -s "$target_file" ]; then
    mv "$source_file" "$target_file"
    echo "Moved: $source_file → $target_file"
  else
    echo "Skipped: $target_file already has content"
  fi
}

move_if_empty "app/app/api/incidents.py" "app/api/incidents.py"
move_if_empty "app/app/schemas/incident.py" "app/schemas/incident.py"
move_if_empty "app/app/services/incident_service.py" "app/services/incident_service.py"
move_if_empty "app/app/repositories/incident_repository.py" "app/repositories/incident_repository.py"

echo
echo "Correct project files:"
find app -maxdepth 2 -type f | sort