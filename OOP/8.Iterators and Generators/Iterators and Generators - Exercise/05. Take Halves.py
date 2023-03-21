def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():

        for i in integers():
            yield i/2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)

