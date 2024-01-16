# Sucecion Fibonacci con python
N1, N2 = 0, 1

while N2 <= 1597 :
    print(N1, N2, end="-")
    N1 = N1 + N2
    N2 = N1 + N2