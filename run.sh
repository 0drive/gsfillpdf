if [[[ ! -d "/venv" ]]]
then
    echo Setting up virtual environment and installing requirements...
    mkdir venv
    python3 -m venv venv
    pip install -r requirements.txt
else
    echo Environment already set up.

venv/Scripts/activate
cd app
python3 main.py
