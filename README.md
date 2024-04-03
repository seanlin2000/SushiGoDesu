# SushiGoDesu

# Virtual Environment Instructions
SushiGo Project stores all package dependencies in `conda_env.yml`. To get the latest updates, run `conda env update --file conda_env.yml  --prune`. Verify that your environment is working by running `venv_test.py`.

If you make new changes to the virtual environment and wish to export them to the YAML file, run `conda env export > conda_env.yml`. 

### Installing new Packages
If possible, use conda to install new packages. If a package does not exist in conda, such as `pettingzoo`, install it with pip. Make sure that it is pip installed into the conda python directory using `python -m pip install pettingzoo`

### Absolute imports
pyproject.toml sets up the absolute import structure of the project. After creating pyproject.toml, we run `python -m pip install -e .` to make `sushigo` a `pypi` package. See https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder for details. 