# https://www.codechef.com/problems/SLOWSOLN

n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    
    sum = 0
    
    while b <= c and a > 0:
        sum += b ** 2
        c -= b
        a -= 1
    
    
    if c  > 0 and a > 0:
        sum += c ** 2
    print(sum)