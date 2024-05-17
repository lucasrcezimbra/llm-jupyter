import re
import sys

from click.testing import CliRunner
from llm.cli import cli


def test_ipython_execute(tmpdir):
    runner = CliRunner()

    # tmpdir should be empty
    assert len(tmpdir.listdir()) == 0

    filepath = tmpdir / "test.txt"

    result = runner.invoke(
        cli, ["ipython", "-c", f"open('{filepath}', 'w').write('Hello World!')"]
    )

    assert result.exit_code == 0
    assert len(tmpdir.listdir()) == 1
    assert filepath.read() == "Hello World!"


def test_ipython_help(capfd):
    runner = CliRunner()

    runner.invoke(cli, ["ipython", "help"])

    captured = capfd.readouterr()
    assert captured.out.startswith("=========\n IPython\n========")


def test_ipython_auto_load_extension(capfd):
    runner = CliRunner()

    runner.invoke(cli, ["ipython", "-c", "%llm --help"])

    captured = capfd.readouterr()
    assert re.match(
        r"^usage: .* \[-h\] \[--print\] \[--model MODEL\] \[--system SYSTEM\]",
        captured.out,
    )


def test_jupyter(capfd):
    runner = CliRunner()

    runner.invoke(cli, ["notebook", "--help-all"])

    captured = capfd.readouterr()
    assert captured.out.startswith(
        "Jupyter Notebook - A web-based notebook environment for interactive computing"
    )


def test_jupyter_auto_load_extension(mocker):
    run_mock = mocker.patch("llm_jupyter.commands.subprocess.run")
    runner = CliRunner()

    result = runner.invoke(cli, ["notebook", "--help-all"])

    assert result.exit_code == 0
    assert run_mock.call_args.args[0] == [
        sys.executable,
        "-m",
        "notebook",
        "--help-all",
        "--ext",
        "llm_jupyter.magic",
    ]
