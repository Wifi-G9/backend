@echo off

set FILENAME=packages.txt

python.exe -m pip install --upgrade pip

if not exist %FILENAME% (
    echo File '%FILENAME%' not found.
    exit /b
)

pip install -r %FILENAME%