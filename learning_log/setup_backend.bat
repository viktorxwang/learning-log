@echo off
REM Run this ONCE to set up the Django backend.
REM Usage: double-click this file, or run setup_backend.bat

cd /d "%~dp0"

if not exist ll_env (
    echo Creating virtual environment ^(ll_env^)...
    python -m venv ll_env
)

echo Activating virtual environment...
call ll_env\Scripts\activate.bat

echo Installing Python packages...
pip install -r requirements.txt

echo Applying database migrations...
python manage.py migrate

echo.
echo Setup complete! Next, double-click run_backend.bat
pause