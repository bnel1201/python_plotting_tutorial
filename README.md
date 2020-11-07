# Plotting in Python: first steps
- this tutorial assumes running on a *Mac*
- windows instructions are slightly different, I'll note where.
# Background

- Just like [Prism](https://www.graphpad.com/scientific-software/prism/) is a program you download and install on your computer, all plotting in Python starts with downloading and installing *packages*, which contain expert-built, publication-quality graph plotting functionality.
- There are *many* plotting packages available in python, here are some of the top choices as of Nov. 2020:
  1. [Matplotlib](https://matplotlib.org/tutorials/introductory/pyplot.html)
    - Matplotlib is kind of the default starting point for most people
  2. [Plotly](https://plotly.com/python/getting-started/)
  3. [Seaborn](https://seaborn.pydata.org/tutorial/function_overview.html)
- Once you learn one plotting package well it's easy to switch and try others, but its best to **pick one** and stick with it for a while rather than hop around

## Before starting
- download and install a fresh copy of Python: https://www.python.org/downloads/
- often times the builtin Python that comes with your computer is used for other things so its best not to mess with it
- open your terminal and enter: `python`, and make sure you get the correct version you expect to confirm that it was installed properly
## Programming environments in Python
- because each of the above programs have similarly named functions (e.g. plot, scatterplot, barchart, etc.) its best practice to make a *virtual environment* for any python project.
  - this is a folder that contains its own version of python and contains only the packages you need for a particular project.

1. Make a new project folder in an easy to find location on your computer, e.g. `/Users/#MYUSERNAME#/Desktop/myproject` or `~/Dev/myproject`
   - this is best done in the terminal:
     - Go home: `cd`
     - make the folder: `mkdir myproject`
     - go into the folder: `cd myproject`
2. Using your new python install make new virtual environment in the folder
   - `python -m venv myproject_env`
     - passing any argument after "`python`" means that you want to start python and give it instructions, which right now is to make a virtual environment for you
     - "`-m`" means you are going to call a command inside a *m*odule, here that module is one that is built into python, **venv**, which stands for *v*irtual *e*nvironment
   - after doing this you should see in your file explorer, (or in your terminal after running `ls`), a new folder labeled `myproject_env` will appear, inside is a new copy of python and will hold your soon-to-be-installed packages
3. Installing packages with `pip` (*p*ython *i*nstall *p*ackage)