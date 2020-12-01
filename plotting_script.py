# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # 1. Plotting in Python and Jupyter Notebooks
# %% [markdown]
# ## Importing packages
# 
# Once you open up a new python session (called a "kernel" in tech speak), before you can use any packages that you have installed you have to first `import` them.
# 
# Some packages, such as matplotlib, are large so they are organized into *modules* that can seperately imported using a `.` seperator e.g.
# 
# `import package.module`
# 
# packages with longer names are typically imported with the `as` keyword to give them a shorter nickname, called the **namespace**. Note that some packages have standard import conventions like those used by matplotlib and numpy below and its best to follow those. 

# %%
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# In Python namespaces are used to differentiate which functions are from which package. So two packages `pkgA` and `pkgB` could have functions with the same name `func` that do different things, so you can use both in the session by calling them as `pkgA.func` and `pkgB.func`
# %% [markdown]
# ## Familiarizing yourself with the plotting functions available in a package
# 
# - The best place to get started with a new plotting package is checking out their website and gallery page to see what plots look most like what you are looking.
# - Then use their code examples as templates for your own code.
# 
# We will be basing this example off of matplotlib's bar chart demo from [their gallery page](https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py)
# 
# - If you have time I recommend you go through it yourself to get a feel for working with their package.
# %% [markdown]
# ## Our first bar chart using `plt.bar`
# - This is the core bar char function in matplotlib, you can learn more about the specific details of how to use it by using the `?` for help
# %% [markdown]
# ### Getting help with `?`
# %% [markdown]
# To learn more about any function, start by typing out the name of the function followed (or preceded by a `?`), this will give you the most accurate information of your specific version as sometimes the internet can be outdated or contradictory
# 
# `?` is meant more as a reminder of how to use a function, for a full explanation and help consult their [website](https://matplotlib.org/tutorials/index.html) and [other tutorials](https://matplotlib.org/resources/index.html#tutorials)

# %%
get_ipython().run_line_magic('pinfo', 'plt.bar')

# %% [markdown]
# ## Make some random data

# %%
height = np.abs(np.random.randn(8))
height


# %%
x = list(range(len(height)))
x


# %%
get_ipython().run_line_magic('pinfo', 'len')

# %% [markdown]
# You can also have `?` at the start or end of a command and will get the same help result

# %%
get_ipython().run_line_magic('pinfo', 'len')


# %%
get_ipython().run_line_magic('pinfo', 'range')


# %%
get_ipython().run_line_magic('pinfo', 'list')


# %%
plt.bar(list(range(len(x))), height)

# %% [markdown]
# Matplotlib is a *declarative* style library, meaning that you build up your plot sequentially, adding on commands.

# %%
plt.bar(list(range(len(x))), height)
plt.xlabel("proteins")
plt.ylabel("Relative intesity")

# %% [markdown]
# ## Make some random sample labels

# %%
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# %%
get_random_string(3)

# %% [markdown]
# Below we perfom what is called a 'list comprehension' it is one of the most powerful features of Python and is worth taking some time to learn more about: [tutorial on list comprehensions](https://realpython.com/list-comprehension-python/)

# %%
protein_names = [get_random_string(3) for i in range(len(height))]
protein_names

# %% [markdown]
# Adding `plt.show()` or `plt.savefig(...)` signifies the end of your plot building statements for that particular figure.

# %%
fig, ax = plt.subplots()
ax.bar(list(range(len(x))), height)
plt.xlabel("proteins")
plt.ylabel("Relative intesity")
ax.set_xticks(x)
ax.set_xticklabels(protein_names)
plt.show()

# %% [markdown]
# ## Adding Error bars
# 
# if you look back at the results from `plt.bar?`, under 'Other Parameters', you'll find options for x-error and y-error, xerr, and yerr, respectively.
# 
# ```python
# """
# 
# Other Parameters
# ----------------
# color : scalar or array-like, optional
#     The colors of the bar faces.
# 
# edgecolor : scalar or array-like, optional
#     The colors of the bar edges.
# 
# linewidth : scalar or array-like, optional
#     Width of the bar edge(s). If 0, don't draw edges.
# 
# tick_label : str or array-like, optional
#     The tick labels of the bars.
#     Default: None (Use default numeric labels.)
# 
# xerr, yerr : scalar or array-like of shape(N,) or shape(2, N), optional
#     If not *None*, add horizontal / vertical errorbars to the bar tips.
#     The values are +/- sizes relative to the data:
# 
#     - scalar: symmetric +/- values for all bars
#     - shape(N,): symmetric +/- values for each bar
#     - shape(2, N): Separate - and + values for each bar. First row
#       contains the lower errors, the second row contains the upper
#       errors.
#     - *None*: No errorbar. (Default)
# 
#     See :doc:`/gallery/statistics/errorbar_features`
#     for an example on the usage of ``xerr`` and ``yerr``.
# """
# ```

# %%
def make_y_error(): return np.abs(np.random.randn(len(height)))*0.1
y_error = make_y_error()
y_error


# %%
fig, ax = plt.subplots()
ax.bar(list(range(len(x))), height, yerr=y_error)
plt.xlabel("proteins")
plt.ylabel("Relative intesity")
ax.set_xticks(x)
ax.set_xticklabels(protein_names)
plt.show()

# %% [markdown]
# ## Wrap it up into a function
# It's good practice to make functions whenever it makes sense to.
# 
# To do this start with your inputs, here your protein intensities and names, and then put all of the intermediate calculations and values in the function to hide them away

# %%
def make_bar_plot(protein_names, heights, error=make_y_error()):
    x = list(range(len(height)))
    fig, ax = plt.subplots()
    ax.bar(list(range(len(x))), height, yerr=error)
    plt.xlabel("proteins")
    plt.ylabel("Relative intesity")
    ax.set_xticks(x)
    ax.set_xticklabels(protein_names)


# %%
make_bar_plot(protein_names, height)


# %%
make_bar_plot(protein_names, height)
plt.savefig('mybarplot.png')

# %% [markdown]
# Now see that your plot has been saved

# %%
import os
os.listdir()

# %% [markdown]
# ## Save it for later
# 
# Once you make a plotting function you like, its best practice to save it in a `.py` file (e.g. `plot_templates.py`) so you can reuse them later to save time and effort in the future.
# 
# Try this now by making `plot_templates.py` and including all of the necesarry bits above to make your function then call it below as follows...

# %%
import plot_templates

plot_templates.make_bar_plot(protein_names, height)

# %% [markdown]
# ## Making subplots
# 
# Let's copy paste some of our old code into a new function,
# 
# specifically we will remove the `fig, ax = plt.subplots()` statement and move it outside and feed an axis `ax` as a new argument

# %%
def make_bar_subplot(protein_names, heights, error=make_y_error(), ax=1):
    x = list(range(len(height)))
    ax.bar(list(range(len(x))), height, yerr=error)
    plt.xlabel("proteins")
    plt.ylabel("Relative intesity")
    ax.set_xticks(x)
    ax.set_xticklabels(protein_names)


# %%
def random_heights(n=8): return np.abs(np.random.randn(n))


# %%
def random_names(height): return [get_random_string(3) for i in range(len(height))]

# %% [markdown]
# These functions have been moved into `utils.py` to be called from later notebooks

# %%
random_heights()


# %%
random_names(height)


# %%
fig = plt.figure(figsize=(18,6))
for i in range(6):
    ax = plt.subplot(2,3,i+1)
    height = random_heights()
    protein_names = random_names(height)
    make_bar_subplot(protein_names, height, error = make_y_error(), ax=ax)
plt.show()

# %% [markdown]
# # Conclusions
#  - This concludes our discussion of setting up a programming environment in python
#  - Next is [plotting from spread sheet data](02_plotting_from_spreadsheets.ipynb)
#  - Back to [index](README.md)

