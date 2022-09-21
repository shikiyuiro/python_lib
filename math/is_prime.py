def is_prime(upper):
    res = [True] * (upper)
    for i in range(2, upper):
        if(res[i]):
            d = i * 2
            while(d < upper):
                res[d] = False
                d += i
    return res
# upper未満の整数が素数であるか否かのテーブルを返す
