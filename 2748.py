# BOJ 2748 피보나치 수 2

dict = {0: 0, 1: 1, 2: 1}

def fibo(N):
    if N in dict:
        return dict[N]
    dict[N] = fibo(N - 1) + fibo(N - 2)
    return dict[N]


print(fibo(int(input())))