import time

# F(n) = F(n-1) + F(n-2)

def fib(n):
    if n < 0: raise ValueError("Fibonnacci can only be calculated for positive numbers.")
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

memo = {0: 0, 1: 1}
def memo_fib(n):
    if n < 0: raise ValueError("Fibonnacci can only be calculated for positive numbers.")
    if n in memo: return memo[n]
    res = fib(n-1) + fib(n-2)
    memo[n] = res
    return res

# start_fib = time.time()
# for i in range(10000):
#     print(fib(i))
# end_fib = time.time()
# print("fib function, elapsed time:",end_fib - start_fib)
# 
# start_memo_fib = time.time()
# for i in range(10000):
#     print(memo_fib(i))
# end_memo_fib = time.time()
# print("memo_fib function, elapsed time:",end_memo_fib - start_memo_fib)

memo_fib(2)