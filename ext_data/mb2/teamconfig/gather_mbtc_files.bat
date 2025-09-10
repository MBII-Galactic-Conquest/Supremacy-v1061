@echo off
setlocal
REM Get the current directory (where the batch file is run from)
set "RWD=%~dp0"
set "GATHER_DIR=%RWD%gather"
REM Create the gather folder if it doesn't exist
if not exist "%GATHER_DIR%" (
	mkdir "%GATHER_DIR%"
)
REM Copy all .mbtc files from subdirectories to the gather folder
for /R "%RWD%" %%F in (*.mbtc) do (
	REM Skip if the file is already in the gather folder
	if /I not "%%~dpF"=="%GATHER_DIR%\" (
		copy "%%F" "%GATHER_DIR%" >nul
	)
)
echo All .mbtc files copied to: "%GATHER_DIR%"
REM Open the gather folder
start "" "%GATHER_DIR%"
pause
