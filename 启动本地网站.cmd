@echo off
cd /d "%~dp0"
set "PATH=%ProgramFiles%\nodejs;%PATH%"
call npm.cmd run dev
pause
