@echo off
if not exist venv\ (
    echo Setting up virtual environment and installing requirements...
    mkdir venv
    python3 -m venv venv
    call venv/Scripts/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

    echo Running script...
) else (
    echo Environment already set up.
    call venv/Scripts/activate
)

cd app
python3 main.py