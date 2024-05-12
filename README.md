# llm-jupyter

[![PyPI](https://img.shields.io/pypi/v/llm-jupyter.svg)](https://pypi.org/project/llm-jupyter/)
[![Changelog](https://img.shields.io/github/v/release/lucasrcezimbra/llm-jupyter?include_prereleases&label=changelog)](https://github.com/lucasrcezimbra/llm-jupyter/releases)
[![Tests](https://github.com/lucasrcezimbra/llm-jupyter/workflows/Test/badge.svg)](https://github.com/lucasrcezimbra/llm-jupyter/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/lucasrcezimbra/llm-jupyter/blob/main/LICENSE)

Run a IPython interpreter in the LLM virtual environment

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-jupyter
```
## Usage

This plugin adds a new `ipython` command to LLM. This executes IPython in the same virtual environment as LLM itself.

You can use this to check the Python version

```bash
llm ipython --version
# Should output '8.20.0' or similar
```
Or to start a IPython shell. In that shell you can import `llm` and use it to interact with models:
```bash
llm ipython
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
git clone git@github.com:lucasrcezimbra/llm-jupyter.git
cd llm-jupyter
python -m venv .venv
source .venv/bin/activate
pip install -e .[test]
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
