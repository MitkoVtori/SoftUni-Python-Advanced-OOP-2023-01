def negative_vs_positive(*args):
    global sum_negative
    global sum_positive

    for num in args:
        if num < 0:
            sum_negative += num

        elif num > 0:
            sum_positive += num


sum_negative = 0
sum_positive = 0

numbers = list(map(int, input().split()))

negative_vs_positive(*numbers)

print(sum_negative)
print(sum_positive)

if abs(sum_negative) > sum_positive:
    print("The negatives are stronger than the positives")

elif sum_positive > abs(sum_negative):
    print("The positives are stronger than the negatives")