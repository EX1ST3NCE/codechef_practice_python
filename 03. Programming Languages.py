# https://www.codechef.com/problems/PROGLANG

n = int(input())

for i in range(n):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    
    if (A == A1 or A== B1) and (B == A1 or B == B1):
        print(1)
    elif (A == A2 or A== B2) and (B == A2 or B == B2):
        print(2)
    else:
        print(0)