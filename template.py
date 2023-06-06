import os
#this will help in making application OS independece it will automatically find the path
from pathlib import Path 
#for logs
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != "":
        break

#creating log
logging.info(f"Creating the Project by Name: {project_name}")

#list of files:
list_of_files = [
    ".github/workflows/.gitkeep",   #.gitkeep is a dummy file
    f"scr/{project_name}/__init__.py",     #scoure file: where all scripts will present 
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",  # it will help in conda env setup
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"  #this will help in testing the various python env
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    #when we need to re run the file its going to delete the previous files so to stop this we are doing this
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")