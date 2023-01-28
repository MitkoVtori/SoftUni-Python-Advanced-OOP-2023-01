def concatenate(*args, **kwargs):
    message = ''.join(args)

    for old_str, new_str in kwargs.items():
        message = message.replace(old_str, new_str)

    return message


''' TESTS '''
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
