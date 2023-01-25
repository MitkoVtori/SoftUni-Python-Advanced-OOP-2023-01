def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)


''' --- Tests --- '''
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))



''' ANOTHER WAY '''
# def recursive_power(number, power):
#     if power == 0:
#         return 1
#     return number * recursive_power(number, power - 1)



# ''' Without recurse '''
# def recursive_power(number, power):
#     return number ** power


# ''' --- Tests --- '''
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))