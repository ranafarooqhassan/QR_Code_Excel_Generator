@echo off
echo Creating Windows .exe using PyInstaller...
python -m pip install pyinstaller
pyinstaller --onefile --noconsole qr_gui_excel_generator.py
echo Build complete. Find your .exe in the /dist folder.
pause
