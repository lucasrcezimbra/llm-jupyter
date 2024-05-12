import click
import llm
import sys
import subprocess


@llm.hookimpl
def register_commands(cli):
    @cli.command(context_settings=dict(ignore_unknown_options=True))
    @click.argument("args", nargs=-1, type=click.UNPROCESSED)
    def ipython(args):
        """
        Run IPython interpreter, passing through any arguments
        """
        subprocess.run(['ipython', *args])

    @cli.command(context_settings=dict(ignore_unknown_options=True))
    @click.argument("args", nargs=-1, type=click.UNPROCESSED)
    def notebook(args):
        """
        Run Jupyter Notebook, passing through any arguments
        """
        subprocess.run(['jupyter', "notebook", *args])
