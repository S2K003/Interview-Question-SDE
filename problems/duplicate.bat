@echo off
setlocal enabledelayedexpansion

:: Set source folder path here (folder to duplicate)
set "source=E:\Interview-Question-SDE-main\problems\Question1"

:: Set destination parent folder where duplicates will be created
set "destination=E:\Interview-Question-SDE-main\problems"

:: Loop from 2 to 100
for /L %%i in (2,1,100) do (
    set "target=%destination%\Question%%i"
    echo Copying "%source%" to "!target!"
    xcopy "%source%" "!target!" /E /I /H /C /Y >nul
)

echo Done duplicating folders.
pause
