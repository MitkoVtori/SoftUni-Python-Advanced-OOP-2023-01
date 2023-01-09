def concatenate(*args, **kwargs):
    string = ''.join(args)

    for key in kwargs.keys():
        if key in string:
            string = string.replace(key, kwargs[key])

    return string


''' TESTS '''
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
