from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        letters = [x for x in function() if x.lower() in vowels]
        return letters

    return wrapper
