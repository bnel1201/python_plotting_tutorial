# A tldr in Scientific Computing

## Benefits

- learn to code and automate your work
- these programs are free compared to paid programs like Excel, Prism or Matlab


## Goal

This post is inspired by a podcast episode:
- [Talk Python to Me: Maintainable data science tips for non-developers](https://talkpython.fm/episodes/show/227/maintainable-data-science-tips-for-non-developers)

as well as from three papers also cited in the podcast:
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

- [Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
- [A Quick Guide to Organizing Computation Biology Projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)
- [Best Practices for Scientific Computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)

While there is an abundance of excellent information out there online, it can be intimidating to know where to start. The purpose of this post is introduce the core concepts that I find valuable and point to more extensive references. The main goal is simply to make you aware of what is out there, what is possible, and how it can help you.

For a scientist, regardless of background or specialization, [Software Carpentry](https://software-carpentry.org/) is an excellent starting point to gather more extensive information on all topics cover, so consider this blog-series a too long, didn't read tldr, so we aim to keep it brief.