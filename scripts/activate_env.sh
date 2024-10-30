#!/bin/bash

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd )"

# Source the .psyris_env file
source "${SCRIPT_DIR}/../.psyris_env"

# Activate Python virtual environment (if using venv)
# source "${SCRIPT_DIR}/../src/psyris_code/.venv/bin/activate"

# Set any other environment variables or configurations

echo "Psyris environment activated"