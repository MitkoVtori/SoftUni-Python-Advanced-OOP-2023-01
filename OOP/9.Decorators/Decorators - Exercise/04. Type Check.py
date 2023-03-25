def type_check(good_type):
    def decorator(function):
        def wrapper(parameter):
            if type(parameter) is good_type:
                return function(parameter)
            return "Bad Type"

        return wrapper

    return decorator


# @type_check(int)
# def times2(num):
#     return num*2
# print(times2(2))
# print(times2('Not A Number'))
