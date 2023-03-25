def make_bold(function):
    def wrapper(*args):
        return f"<b>{function(*args)}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*args):
        return f"<i>{function(*args)}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*args):
        return f"<u>{function(*args)}</u>"

    return wrapper

