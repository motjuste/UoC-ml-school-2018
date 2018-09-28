# A Practical Introduction to Automatic Audio Segmentation

_In Proceedings of: [**Late Summer School: Machine Learning for Language Analysis - September, 2018**](http://ml-school.uni-koeln.de/index.html)_ 

## Setup
Please follow the instructions below in sequence.

Install and setup the following:

1. [`git`](https://git-scm.com/downloads)
2. [`miniconda`](https://conda.io/miniconda.html) or [`anaconda`](https://www.anaconda.com/download/) (Python 3.x version)

Clone this repository **WITH SUBMODULES** (in the Terminal on Linux/macOS, or Git Bash on Windows):
```bash
# go to an existing directory where you'd like to clone this repository
cd ~

# clone this repo WITH SUBMODULES!
git clone --recurse-submodules https://github.com/motjuste/UoC-ml-school-2018

# change directory to the clone
cd UoC-ml-school-2018
```

Install the required packages using `conda` (Terminal on Linux/macOS, or **Anaconda Prompt** on Windows):
```bash
# change directory to the clone, if not already
# replace ~ below with where you clones this repository
cd ~/UoC-ml-school-2018

# update conda, just in case
conda update conda

# create a new conda environment with the required packages. May take time.
conda env create --file environment.yml

# activate the environment (also instructed at the end of the last step)
conda activate ml-school
```

Start `jupyter notebook` (Terminal on Linux/macOS, or **Anaconda Prompt** on Windows):
```bash
# change directory to the clone, if not already
# replace ~ below with where you clones this repository
cd ~/UoC-ml-school-2018

# activate the environment
conda activate ml-school

# start jupyter notebook
jupyter notebook

# if not opened automatically, copy the localhost URL and open it in a browser
```

Check setup by opening and following the instructions `00-check-setup.ipynb`.