from ci_learn import main
from os import getenv


def test_arg_summ():
    args = 1, 5, 20, 1
    expected = 27

    assert main.arg_summ(*args) == expected


def test_decap():
    string = "WooSH"
    expected = "woosh"

    assert main.de_capitalizer(string) == expected


def test_joinstr():
    args = "Wow", " man ", "that's", " cool", "!"
    expected = "Wow man that's cool!"

    assert main.join_strings(*args) == expected


def test_env():
    var_name = "SUPER_PUPER_VAR"
    expected = "cockroach"

    assert getenv(var_name) == expected, f"Env var '{var_name}' doesn't exist or value is wrong"