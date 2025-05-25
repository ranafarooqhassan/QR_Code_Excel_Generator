#!/bin/bash
APP_NAME="QR Code Excel Generator"
EXEC_PATH=$(pwd)/venv/bin/python3
SCRIPT_PATH=$(pwd)/qr_gui_excel_generator.py
DESKTOP_FILE="$HOME/.local/share/applications/qr_code_excel_generator.desktop"

echo "[Desktop Entry]
Name=$APP_NAME
Exec=$EXEC_PATH $SCRIPT_PATH
Icon=utilities-terminal
Terminal=false
Type=Application
Categories=Utility;" > "$DESKTOP_FILE"

chmod +x "$DESKTOP_FILE"
echo "Shortcut created. Search 'QR Code Excel Generator' in your app menu."
