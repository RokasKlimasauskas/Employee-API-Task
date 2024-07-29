@echo off
REM Activate virtual environment and run tests
call venv\Scripts\activate
python -m unittest discover -s tests
