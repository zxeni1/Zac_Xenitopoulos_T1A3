#!/bin/bash

# Change to the src directory
cd "$(dirname "$0")"

# Check if python3 is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed."
    
    # Check if python3 needs to be updated
    if python3 -c 'import sys; exit(sys.version_info < (3, 9))'; then
        echo "Python 3 is up to date."
    else
        echo "Updating Python 3..."
        # Update Python 3
        sudo apt-get update
        sudo apt-get install --only-upgrade python3
    fi
else
    # Prompt user to install python3
    echo "Python 3 is not installed. Please install Python 3 before proceeding."
    
    echo "On Ubuntu, you can install Python 3 using: sudo apt-get install python3"
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the specified packages
pip install altgraph==0.17.2 colored==2.2.3 future==0.18.2 macholib==1.15.2 numpy==1.26.2 pandas==2.1.4 prettytable==3.9.0 python-dateutil==2.8.2 pytz==2023.3.post1 six==1.15.0 tzdata==2023.3 wcwidth==0.2.12

# Run your Python script
python3 study_planner.py

# Deactivate the virtual environment
deactivate