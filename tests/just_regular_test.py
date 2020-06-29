from ci_learn import main


def test_arg_summ():
    args = 1, 5, 20
    expected = 26

    assert main.arg_summ(*args) == expected


def test_decap():
    string = "WooSH"
    expected = "woosh"

    assert main.de_capitalizer(string) != expected


def test_joinstr():
    args = "Wow", " man ", "that's", " cool", "!"
    expected = "Wow man that's cool!"

    assert main.join_strings(*args) == expected
