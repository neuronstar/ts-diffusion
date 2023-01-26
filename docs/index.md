# Documentation for ts_diffusion

## Dev Env

1. This repo has [pre-commit](https://pre-commit.com/) configured. Please run `pre-commit install` before committing code.
2. `ts_diffusion` uses [poetry](https://python-poetry.org/) to manage python env.
   1. Install poetry.
   2. Specify python version, e.g. `poetry env use 3.10.8`.
   3. Install dependencies: `poetry install`
3. If you really hate poetry, please use the `requirements.txt`. This file is automatically updated by poetry though the poetry-export hook. Any manual changes to this `requirements.txt` file will be overwritten by pre-commit.


## Datasets

We can download datasets and load them through `ts-bolt`.

### Download datasets
