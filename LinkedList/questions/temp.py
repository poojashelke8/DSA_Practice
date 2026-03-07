l1 = [2,'s',4]
l2 = ['m','1',10]

print(l1+l2*2**2)


def decorator(prog):
    def func(x):
        result = prog(x)
        print(result)
    return func
@decorator
def program_result(i):
    return i + 1
program_result(10) 


print([1,2,3][::-1])

lst = [2,4,1,3]
print(sorted(lst))
print(lst)

import functools
@functools.lru_cache()
def fibonacci(n):
    if n < 4:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
res = fibonacci(10)
print(res)

def modify(lst):
    lst = [8,9]

lst = [1,2,3,4]
modify(lst)
print(lst)

from collections import Counter

MOD = 1000000007

t =int(input())

for _ in range(t):
    s = input().strip()
    
    freq = Counter(s)
    
    ans = 1
    for f in freq.values():
        ans = (ans * (f + 1)) % MOD
    
    print(ans)