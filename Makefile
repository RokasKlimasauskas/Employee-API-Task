# Commands for setting up and running the project

# Create and activate the virtual environment, install dependencies
setup:
    python -m venv venv
    venv/bin/pip install -r requirements.txt

# Run the application
run:
    venv/bin/python run.py

# Run tests
test:
    venv/bin/python -m unittest discover -s tests
