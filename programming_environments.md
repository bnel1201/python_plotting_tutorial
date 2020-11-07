# Setting up programming environments in Python
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
# Starting up your **IDE** (*I*nteractive *P*rogramming *Environment*)
 - We have chosen Jupyterlab as our IDE as it is the gold standard in *literate programming* that combines code, computation, embedded-figure-plotting, and the ability to write human-readable notes all in the same document. These are all ideal characteristics of [scientific computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745).
 - After activating your environment start a jupyter lab server with the following command: `jupyter-lab`
![](images/jupyterlab_home.png)
 
 - Because this is a *server* you can actually minimize this terminal and leave it running in the background and perform the rest of your work
   - I recommend you bookmark the page because even if you close your browser you can open it back up by selecting that book mark or going to http://localhost:8888/lab

# Conclusions
 - This concludes our discussion of setting up a programming environment in python
 - Next is [plotting](plotting_01.ipynb)
 - Back to [index](README.md)