import argparse
import shlex

from IPython.core.getipython import get_ipython
from llm import get_key, get_model
from llm.cli import get_default_model

SYSTEM_PROMPT = """\
You are a Python programmer using Jupyter Notebook. Your output will be passed
to the next cell directly.

Return only the Python code to be executed as a raw string, no string delimiters
wrapping it, no yapping, no markdown, no fenced code blocks.

For example, if the user asks: print the variable `x`

You return only: print(x)
"""


def llm(line):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--print",
        "-p",
        action="store_true",
        default=False,
        help="Only print the output",
    )
    parser.add_argument(
        "--model", "-m", default=get_default_model(), help="Model to use"
    )
    parser.add_argument(
        "--system", "-s", default=SYSTEM_PROMPT, help="System prompt to use"
    )
    parser.add_argument("prompt", nargs="*", help="Prompt to use")
    try:
        args = parser.parse_args(shlex.split(line))
    except SystemExit:
        return

    model = get_model(args.model)
    if model.needs_key:
        model.key = get_key(None, model.needs_key, model.key_env_var)

    prompt = " ".join(args.prompt)
    response = model.prompt(prompt, system=args.system).text()

    if args.print:
        print(response)
    else:
        get_ipython().set_next_input(response, replace=True)


def load_ipython_extension(ipython):
    ipython.register_magic_function(llm, "line")
