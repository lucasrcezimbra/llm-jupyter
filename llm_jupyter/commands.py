import subprocess
import sys

import click
import llm


@llm.hookimpl
def register_commands(cli):
    @cli.command(context_settings={"ignore_unknown_options": True})
    @click.argument("args", nargs=-1, type=click.UNPROCESSED)
    def ipython(args):
        """
        Run IPython interpreter, passing through any arguments
        """
        subprocess.run(
            [sys.executable, "-m", "IPython", *args, "--ext", "llm_jupyter.magic"]
        )

    @cli.command(context_settings={"ignore_unknown_options": True})
    @click.argument("args", nargs=-1, type=click.UNPROCESSED)
    def notebook(args):
        """
        Run Jupyter Notebook, passing through any arguments
        """
        subprocess.run([sys.executable, "-m", "notebook", *args])
