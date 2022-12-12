import sys
from cx_Freeze import setup, Executable

# Set up the build options
build_options = {
    'build_exe': {
        'include_files': ['my_file.txt'],
        'includes': ['my_module'],
    }
}

# Create the executables
executables = [
    Executable('Chatgpt.py')
]

# Run the setup
setup(
    name='My Program',
    version='1.0',
    options=build_options,
    executables=executables
)