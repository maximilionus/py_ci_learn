def maximilionus_is_god() -> bool:
    return True


def arg_summ(*args):
    """ Summ all numbers """
    result = 0
    for arg in args:
        result += arg
    return result


def de_capitalizer(text: str):
    return text.lower()


def join_strings(*args):
    result = ""
    for string in args:
        result += string
    return result
