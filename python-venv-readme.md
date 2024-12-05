# Setting Up Python Virtual Environments on Raspbian
A beginner-friendly guide to creating and using virtual environments for your Python projects.

## What is a Virtual Environment?
Think of a virtual environment like a clean, isolated workspace for your Python project. It's similar to having a separate toolbox for each project you work on, so the tools (packages) from one project don't get mixed up with another.

## Prerequisites
Before we start, make sure you have:
- Raspbian OS installed on your Raspberry Pi
- Python 3 installed (it comes pre-installed with Raspbian)
- Access to the terminal

## Step-by-Step Guide

### 1. Open the Terminal
Find and open the terminal on your Raspbian desktop, or press `Ctrl + Alt + T`.

### 2. Navigate to Your Project Folder
Create a new project folder and move into it:
```bash
# Create a new folder for your project
mkdir my_project

# Move into that folder
cd my_project
```

### 3. Create a Virtual Environment
Create your virtual environment by running:
```bash
python3 -m venv env
```
This creates a new folder called `env` that contains your isolated Python environment. You can name the folder anything you like, but `env` is a common choice.

### 4. Activate the Virtual Environment
To start using your virtual environment:
```bash
source env/bin/activate
```
You'll know it's working when you see `(env)` at the beginning of your terminal prompt.

### 5. Using Your Virtual Environment
Now that you're in the virtual environment:
- Install packages using `pip install package_name`
- Run your Python scripts as normal
- All packages you install will only exist in this environment

### 6. Deactivate When Done
When you're finished working:
```bash
deactivate
```
This returns you to your normal Python environment.

## Common Tasks

### Installing Required Packages
After activating your environment:
```bash
# Install a single package
pip install numpy

# Install multiple packages
pip install numpy pandas matplotlib
```

### Saving Your Package List
It's good practice to save a list of your project's required packages:
```bash
pip freeze > requirements.txt
```

### Installing from Requirements
When sharing your project, others can install the same packages:
```bash
pip install -r requirements.txt
```

## Important Tips
- Always activate your virtual environment before working on your project
- Each project should have its own virtual environment
- Never edit the `env` folder contents directly
- Add `env/` to your `.gitignore` file if using Git

## Troubleshooting
If you see "command not found":
```bash
sudo apt-get update
sudo apt-get install python3-venv
```

## Need Help?
If you run into problems:
1. Check if your virtual environment is activated (look for `(env)` in terminal)
2. Try deactivating and reactivating the environment
3. Make sure you're in the correct project directory

