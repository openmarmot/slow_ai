# make the downloads folder if it doesn't already exist
mkdir -p downloads

# Check if the virtual environment directory exists
if [ ! -d "venv" ]; then
    # Start the venv only if it doesn't exist
    python -m venv venv
    source venv/bin/activate
else
    # If venv already exists, just activate it
    source venv/bin/activate
fi

# install / check requirements
pip install -r requirements.txt

# Run your Python script
python slow_ai.py

# Deactivate the virtual environment
deactivate
