@echo off
REM Run this ONCE to set up the React frontend.
REM Usage: double-click this file, or run setup_frontend.bat

cd /d "%~dp0"
echo Installing Node packages ^(this can take a minute^)...
npm install

echo.
echo Setup complete! Next, double-click run_frontend.bat
pause