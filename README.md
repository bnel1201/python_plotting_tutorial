# Plotting in Python: first steps
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
## Programming environments in Python
- because each of the above programs have similarly named functions (e.g. plot, scatterplot, barchart, etc.) its best practice to make a *virtual environment* for any python project.
  - this is a folder that contains its own version of python and contains only the packages you need for a particular project.

1. Make a new project folder in an easy to find location on your computer, e.g. `/Users/#MYUSERNAME#/Desktop/myproject` or `~/Dev/myproject`
   - this is best done in the terminal:
     - Go home: `cd`
       - other useful commands: `ls` for list
     - make the folder: `mkdir myproject`
     - go into the folder: `cd myproject`
2. Using your new python install make new virtual environment in the folder
   - `python3 -m venv myproject_env`
     - passing any argument after "`python`" means that you want to start python and give it instructions, which right now is to make a virtual environment for you
     - "`-m`" means you are going to call a command inside a *m*odule, here that module is one that is built into python, **venv**, which stands for *v*irtual *e*nvironment
   - after doing this you should see in your file explorer, (or in your terminal after running `ls`), a new folder labeled `myproject_env` will appear, inside is a new copy of python and will hold your soon-to-be-installed packages
3. Installing packages with `pip` (*p*ython *i*nstall *p*ackage)
   - first activate your environment: `. myproject_env/bin/activate`
   - test pip install by installing [numpy](https://numpy.org/), a central package for scientific python: `pip install numpy`
   - install matplotlib: `python3 -mpip install matplotlib`
     - note: this is a bit different on Mac but these are the specific install instructions from the [matplotlib website](https://matplotlib.org/3.3.2/faq/installing_faq.html)
   - Install [Jupyterlab](https://jupyter.org/): `pip install jupyterlab`
     - This will be our first IDE to start with, see next section on IDEs...

### (Optional) Sharing your environment
4. Exporting your environment
    - when you are ready to share your work with others or install it on another computer, you'll also need to export your environment so that all of your code can ge guaranteed to run the same.
    - This is done using the following command: `pip freeze >> requirements.txt`
      - "`pip freeze`" creates a snap shot of your current packages and versions in your environment and "`>> requirements.txt`" means write and save to the file "**requirements.txt**". (It could be names anything, but thats the conventional name)
      - By sharing your source code and `requirements.txt` you should be able to recreate your programming environment in a reproducible way.
5. Reproducing your environment
    - To build a new virtual environment using this "requirements.txt" file, open a fresh terminal and repeat steps 1 and 2 above (with a different project name if you like).
    - copy `requirements.txt` into that new project folder
    - instead of installing each package individually, just enter: `pip install -r requirements.txt`
      - this will install everything from your old environment into the new one
    - you can then activate this environment the usual way as described in step. 2
## Starting up your **IDE** (*I*nteractive *P*rogramming *E*)
 - We have chosen Jupyterlab as our IDE as it is the gold standard in *literate programming* that combines code, computation, embedded-figure-plotting, and the ability to write human-readable notes all in the same document. These are all ideal characteristics of scientific computing. If you share the