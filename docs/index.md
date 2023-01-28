# Getting Started

`ts_diffusion` is a [community](https://github.com/neuronstar/ts-diffusion/graphs/contributors) project investigating cutting-edge diffusion models for time series.

## Prepare Dev Environment

### 0. Prerequisites

- [pre-commit](https://pre-commit.com/): set up git commit hooks
- whichever python virtual env management tool, pyenv, conda, ...
- [poetry](https://python-poetry.org/): package and env management

!!! tip "Python Environment"

    [Here is a one-pager](https://dl.leima.is/engineering/python/) about python environment and pre-commit.


### 1. Setup pre-commit

0. Install [pre-commit](https://pre-commit.com/).
1. Clone this repository.
2. Install git hooks using `pre-commit install`.
   1. This has to be done ASAP, before committing any changes.
   2. If one forgets to do this before git commit, run `pre-commit run --all-files` then commit again.


### 2. Setup Python Environment

0. Install [poetry](https://python-poetry.org/).
1. Use your python environment management tool to create a environment with a specific python version,
   1. e.g., `conda create -n ts-diffusion python=3.10 pip` if using conda, or
   2. `pyenv shell 3.10.9` if using pyenv.
2. Tell poetry we want to use this python environment: `poetry env use 3.10.8`.
3. Install dependencies: `poetry install`

!!! note "'I hate poetry!'"

    If you really hate poetry, please use the `requirements.txt` to install dependencies.

    However, please note that this file is automatically updated by poetry though the poetry-export hook.
    Any manual changes to this `requirements.txt` file will be overwritten by our automated pre-commit hooks.


## Datasets

We can download datasets and load them through `ts-bolt`.

!!! warning ""

    All contents in the `datasets` folder is excluded from git.

### Download datasets

This repository ships a datasest downloading tool called "bolt".

```sh
poetry run bolt download --name ecb_exchange_rate --target datasets
```

??? note "List and Inspect Datasets"

    List datasets:

    ```sh
    poetry run bolt list
    ```

    Inspect the details of a dataset:

    ```sh
    poetry run bolt list --name=ecb_exchange_rate
    ```
