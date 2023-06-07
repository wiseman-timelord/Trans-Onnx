@echo off
setlocal EnableDelayedExpansion


:: Starting message
echo Installing Requirements...
for /L %%i in (2,-1,1) do (
    echo.
    timeout /t 1 /nobreak >nul
)


:: Install requirements.txt
for /F "delims=#" %%i in (requirements.txt) do (
    echo Installing %%i...
    wsl pip install %%i
    if errorlevel 1 (
        echo An error occurred during the installation of %%i.
        echo Please make sure you have pip installed and try again.
    ) else (
        echo Successfully installed %%i.
    )
)
echo.
echo.


:: Ending message
echo Exiting Installer...
echo Installation process completed.
for /L %%i in (2,-1,1) do (
    echo.
    timeout /t 1 /nobreak >nul
)


pause