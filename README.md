# Plotting in Python: first steps (Index)

A tutorial for migrating from Prism, Excel, or other graphical user interface plotting to programmatic plotting using Python.

- this tutorial assumes running on a *Mac*
  - make sure you have Xcode installed if on Mac
- windows instructions are slightly different, I'll note where.

## 0. [Preliminaries](background.md)

## 1. [Setting up a programming environment](programming_environments.md)

- If you have already set up an environment you can pick back up where you left off by doing the following. Recall that your environment contains specific verisions of python and packages specific to your project.

### Making a new environment

- these instructions all you to create a project environment called: `myprojectname` from anywhere on your computer because it uses the path relative to your home path `~`
- this assumes you have made a folder called `.venvs` in your home directory `~`. If you want this folder to *not be invisible* make it: `venvs` or anything without a period `.` at the start of the name.

1. `python3 -m ~/.venvs/myprojectname`
2. `source activate ~/.venvs/myprojectname`

### Re-activating an environment

  1. Navigate back to your project folder
     - e.g. `cd Desktop/myproject` if "myproject" is located on your desktop
  2. re-activate your environment: `. myproject_env/bin/activate`
  3. restart a jupyter server: `jupyter-lab`

## 2. [your first plots in python](notebooks/01_plotting.ipynb)

- This section assumes you have an active virtual environment with jupyter-lab installed. Please see [section 1](programming_environments.md) for more details

## 3. [plotting from spread sheet data (csv or excel)](notebooks/02_plotting_from_spreadsheets.ipynb)

## 4. Using [Python to programmatically work with Excel](Excel/README.md)

- [Excel demo notebook](notebooks/04_plotting_excel_in_python.ipynb)

- [Excel demo script](excel.py)

## 5. Wrap it all up in a [*G*raphical *U*ser *I*nterface](gui/README.md)

- [cytokine GUI demo](cytokine_array.py)

## Basic terminal commands:

1. change directory: `cd target_directory`
2. go to home directory: `cd` or `cd ~`
3. go back a directory: `cd ..`
4. list files in current directory: `ls`
5. make a new directory: `mkdir new_dir_name`
6. remove a file: `rm file_to_be_removed.txt`
7. show contents of a file: `cat filename.txt`
