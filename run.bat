@echo off
setlocal enabledelayedexpansion

:: Define the model and output directories
set input_dir=./input
set output_dir=./output

:: Check workspace folder and clean if necessary
echo Checking workspace folder..
for /r "./workspace" %%G in (*) do (
    if not "%%~nG"=="aaa folder placeholder" (
        echo Cleaning workspace folder...
        del /Q "./workspace/*"
        echo Workspace folder cleaned
        goto :continue
    )
)
echo Workspace folder clean.

:continue

:: Check if the model directory exists
if not exist %input_dir% (
   echo The ./input directory does not exist.
    pause
    exit /b
)

:: Check if the output directory exists
if not exist %output_dir% (
    echo The ./output directory does not exist, creating it...
    mkdir %output_dir%
)

:: Display model directories, get user selection
echo.
echo Select an option:
echo.
set /a i=1
for /d %%G in ("%input_dir%\*") do (
    if exist "%%G/*.bin" (
        echo !i!. %%~nxG
        set "option_!i!=%%~G"
        set /a i+=1
    )
)
echo !i!. Exit
echo.

:: Get user selection
set /p selection=Enter the number of your selection:
if %selection% equ !i! (
    echo Exiting Trans-Onyx...
    pause
    exit /b
)

:: Convert the selected model to ONNX format
set /a selection-=1
call set selected_model_dir=%%option_%selection%%%

:: Update settings.json with model directory and bin file
for /r "%selected_model_dir%" %%G in (*.bin) do (
    set first_bin_file=%%~nG
    goto :continue2
)
:continue2
:: Load max_position_embeddings from config.json
for /f "tokens=2 delims=: " %%a in ('powershell -Command "Get-Content -Path '%input_dir%/%selected_model_dir%/config.json' | Select-String -Pattern 'max_position_embeddings'"') do (
    set max_position_embeddings=%%a
)
set max_position_embeddings=%max_position_embeddings:~0,-1%

:: Merge model files if necessary
wsl python3 merge.py

:: Convert the model to ONNX format
wsl python3 convert.py

:: Move the converted model
move ./workspace/* %output_dir%/
del ./workspace/*

endlocal
