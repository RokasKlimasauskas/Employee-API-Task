@echo off
REM Create virtual environment if it doesn't exist
if not exist "venv\Scripts\python.exe" (
    python -m venv venv
)
REM Activate virtual environment and install dependencies
call venv\Scripts\activate
pip install -r requirements.txt
