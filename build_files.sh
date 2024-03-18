# Specify the absolute path to Python 3.10 executable
PYTHON_EXECUTABLE="C:\Users\achar\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10"

# Check if Python 3.10 executable exists
if [ ! -x "$PYTHON_EXECUTABLE" ]; then
    echo "Python 3.10 executable not found at specified path: $PYTHON_EXECUTABLE"
    exit 1
fi

echo "BUILD START"

# Use the specified Python executable to install dependencies and run manage.py
"$PYTHON_EXECUTABLE" -m pip install -r requirements.txt
"$PYTHON_EXECUTABLE" manage.py collectstatic --noinput --clear

echo "BUILD END"