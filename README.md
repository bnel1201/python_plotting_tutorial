# Plotting in Python: first steps

A tutorial for migrating from Prism, Excel, or other graphical user interface plotting to programmatic plotting using Python.

- this tutorial assumes running on a *Mac*
- windows instructions are slightly different, I'll note where.
# Background

- Just like [Prism](https://www.graphpad.com/scientific-software/prism/) is a program you download and install on your computer, all plotting in Python starts with downloading and installing *packages*, which contain expert-built, publication-quality graph plotting functionality.
- There are *many* plotting packages available in python, here are some of the top choices as of Nov. 2020:
  1. [matplotlib](https://matplotlib.org/tutorials/introductory/pyplot.html)
    - Matplotlib is kind of the default starting point for most people
  2. [plotly](https://plotly.com/python/getting-started/)
  3. [seaborn](https://seaborn.pydata.org/tutorial/function_overview.html)
- Once you learn one plotting package well it's easy to switch and try others, but its best to **pick one** and stick with it for a while rather than hop around

## Before starting
- download and install a fresh copy of Python: https://www.python.org/downloads/
- often times the builtin Python that comes with your computer is used for other things so its best not to mess with it
- open your terminal and enter: `python`, and make sure you get the correct version you expect to confirm that it was installed properly

- note in Mac, you may have
# Index
## 0. [Setting up a programming environment](programming_environments.md)
 - If you have already set up an environment you can pick back up where you left off by doing the following.
  1. Navigate back to your project folder
     - e.g. `cd Desktop/myproject` if "myproject" is located on your desktop
  2. re-activate your environment: `. myproject_env/bin/activate`
  3. restart a jupyter server: `jupyter-lab`
## 1. [your first plots in python](01_plotting.ipynb)
 - This section assumes you have an active virtual environment with jupyter-lab installed. Please see [section 1](programming_environments.md) for more details
## 2. [plotting from spread sheet data (csv or excel)](02_plotting_from_spreadsheets.ipynb)