#!/bin/bash
cd "$HOME/MissionAcademy" || exit 1
git pull --ff-only origin develop
python3 app/main.py
