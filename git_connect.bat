@echo off
setlocal

REM === Set your GitHub repo URL below ===
set "REPO_URL=https://github.com/S2K003/Interview-Question-A2Z"

REM Initialize Git and push
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/S2K003/Interview-Question-A2Z
git push -u origin main

echo GitHub connection initialized and pushed.
pause
