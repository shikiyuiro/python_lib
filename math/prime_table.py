def prime_table(upper):
    res = []
    is_prime = [True] * (upper)
    for i in range(2, upper):
        if(is_prime[i]):
            res.append(i)
            d = i * 2
            while(d < upper):
                is_prime[d] = False
                d += i
    return res
