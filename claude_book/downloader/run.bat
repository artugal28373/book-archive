@echo off
REM Double-click this to run the interactive downloader.
cd /d "%~dp0"
if not exist "venv\Scripts\python.exe" (
    echo Setting up venv for the first time...
    python -m venv venv
    venv\Scripts\python.exe -m pip install --upgrade pip
    venv\Scripts\python.exe -m pip install -r requirements.txt
)
venv\Scripts\python.exe get.py
echo.
pause
