# PyTri
This repository is meant to contain interactive Python app for several triangulation methods.

# Installation
Create [Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) environment and activate by
```bash
cd pytri
conda env create -f environment.yml
conda activate pytri
```
This way you ensure that all important packages are installed.

# How to run
To run the window application just run the `main.py` file e.g.,
```bash
cd pytri
python main.py
```

# Testing
Unittests for this repository are in the `tests` folder. You can run them by:
```bash
cd pytri
python -m unittest discover -s tests -p *_test.py
```

# Examples
In the file `examples.py` are couple of runnable examples. Run those any way you see fit, for example by this command:
```bash
cd pytri
python examples.py
```