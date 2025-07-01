@echo off
REM This batch file starts two Node.js applications.

REM --- Command 1: Start node server.js ---
echo Starting E:\StudyCode\node server.js...
start "Node Server 1" cmd /k "pushd E:\StudyCode && node server.js"

REM --- Command 2: Start npm start ---
echo Starting E:\StudyCode\studycode\npm start...
REM The /k switch keeps the command prompt open after the command executes.
start "Node Server 2" cmd /k "pushd E:\StudyCode\studycode && npm start"

echo All applications have been launched. You may close this window.
exit