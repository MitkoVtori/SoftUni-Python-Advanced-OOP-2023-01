def negative_vs_positive(*args):
    sum_negatives = sum([num for num in args if num < 0])
    sum_positives = sum([num for num in args if num >= 0])

    print(sum_negatives)
    print(sum_positives)

    if abs(sum_negatives) > sum_positives:
        print("The negatives are stronger than the positives")

    elif sum_positives > abs(sum_negatives):
        print("The positives are stronger than the negatives")


numbers = [int(num) for num in input().split()]
negative_vs_positive(*numbers)
