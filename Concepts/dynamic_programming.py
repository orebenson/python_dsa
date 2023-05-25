'''
Top-down dynamic prog (memoization):
- recursive
- create a hashmap memo[] and store values for lookup as they are calculated
- reduces number of calls by only needing to visit each once

Bottom-up dynamic prog:
- iterative
= create a hashmap and compute all values before returning

'''


# Top down using recusion
def fibonacci1(n):
    return fibonacci(n, [0]*(n+1))

def fibonacci(i, memo):
    if i == 0 or i == 1: return i
    if memo[i] == 0:
        memo[i] = fibonacci(i-1, memo) + fibonacci(i-2, memo)
    return memo[i]

# Bottom up using iteration
def fibonacci2(n):
    if n == 0: return n
    a = 0
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return a + b

print(fibonacci1(4))
print(fibonacci2(4))