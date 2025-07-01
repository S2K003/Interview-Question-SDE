@echo off
setlocal

REM Get current date and time
for /f "tokens=1-5 delims=/: " %%a in ("%date% %time%") do (
    set day=%%a
    set month=%%b
    set year=%%c
    set hour=%%d
    set min=%%e
)

REM Format timestamp as YYYY-MM-DD_HH-MM
set commit_msg=Commit %year%-%month%-%day%_%hour%-%min%

echo Commit message: %commit_msg%

git add .
git commit -m "%commit_msg%"
git push origin main

pause
