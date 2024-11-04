# main.py
import os
import sys

# Ensure the src directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the run function from app.py
from app import run  

if __name__ == "__main__":
    run() 