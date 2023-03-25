def tags(tag):
    def decorator(function):
        def wrapper(*args):
            return f"<{tag}>{function(*args)}</{tag}>"

        return wrapper

    return decorator

