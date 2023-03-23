def multiply(times):

    def decorator(function):

        def wrapper(number):
            return times * function(number)

        return wrapper

    return decorator
