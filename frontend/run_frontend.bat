@echo off
REM Run this every time you want to start the React app.
REM Usage: double-click this file, or run run_frontend.bat

cd /d "%~dp0"
echo Starting React dev server, usually at http://localhost:5173 ...
echo Press CTRL+C to stop.
npm run dev