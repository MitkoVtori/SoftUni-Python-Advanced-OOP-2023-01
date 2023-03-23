def even_numbers(function):

    def wrapper(numbers):

        result = [n for n in numbers if n % 2 == 0]
        return function(result)

    return wrapper
