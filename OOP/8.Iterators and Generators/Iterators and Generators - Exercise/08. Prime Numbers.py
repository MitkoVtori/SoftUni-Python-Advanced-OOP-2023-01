def get_primes(integers):
    for i in integers:
        if i > 1:
            prime = True
            for n in range(2, i):
                if i % n == 0:
                    prime = False
                    break
            if prime:
                yield i

