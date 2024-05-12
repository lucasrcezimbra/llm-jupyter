from llm.cli import cli
from click.testing import CliRunner


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

    result = runner.invoke(cli, ["ipython", "help"])

    captured = capfd.readouterr()
    assert captured.out.startswith("=========\n IPython\n========")


def test_jupyter(capfd):
    runner = CliRunner()

    result = runner.invoke(cli, ["notebook", "--help-all"])

    captured = capfd.readouterr()
    assert captured.out.startswith("Jupyter Notebook - A web-based notebook environment for interactive computing")
