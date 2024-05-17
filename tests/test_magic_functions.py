import re

from IPython.testing.globalipapp import get_ipython

from llm_jupyter.magic import load_ipython_extension

ipy = get_ipython()


def test_magic_line_function(capsys):
    load_ipython_extension(ipy)

    ipy.run_line_magic("llm", "--help")

    captured = capsys.readouterr()
    assert re.match(
        r"^usage: .* \[-h\] \[--print\] \[--model MODEL\] \[--system SYSTEM\]",
        captured.out,
    )


def test_custom_model():
    load_ipython_extension(ipy)

    ipy.run_line_magic("llm", "--model length-summary 'This has 17 chars'")

    assert ipy.rl_next_input == "System: 331 - Prompt: 17"


def test_print(capsys):
    load_ipython_extension(ipy)

    ipy.run_line_magic("llm", "--print --model length-summary 'This has 17 chars'")

    captured = capsys.readouterr()
    assert captured.out == "System: 331 - Prompt: 17\n"


def test_custom_model_and_system():
    load_ipython_extension(ipy)

    ipy.run_line_magic(
        "llm",
        "--model length-summary --system 'System has 19 chars' 'This has 17 chars'",
    )

    assert ipy.rl_next_input == "System: 19 - Prompt: 17"
