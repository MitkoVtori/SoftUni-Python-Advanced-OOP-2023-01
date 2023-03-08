from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums):
        return sum(nums)

    @staticmethod
    def multiply(*nums):
        return reduce(lambda x, y: x * y, nums)

    @staticmethod
    def divide(*nums):
        return reduce(lambda x, y: x / y, nums)

    @staticmethod
    def subtract(*nums):
        return reduce(lambda x, y: x - y, nums)

