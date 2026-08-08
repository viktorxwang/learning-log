@echo off
REM Run this every time you want to start the Django server.
REM Usage: double-click this file, or run run_backend.bat

cd /d "%~dp0"
call ll_env\Scripts\activate.bat
echo Starting Django server at http://127.0.0.1:8000 ...
echo Press CTRL+C to stop.
python manage.py runserver