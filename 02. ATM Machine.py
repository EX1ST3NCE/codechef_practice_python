# https://www.codechef.com/problems/ATM2

n = int(input())

for i in range(n):
    a_list = []
    flag = True
    ans = ''
    
    a, b = map(int, input().split())
    a_list = input().split()
    
    money = [int(i) for i in a_list]
    
    for i in range(a):
        if money[i] > b:
            ans += '0'
        else:
            ans += '1'
            b -= money[i]
            
            
    print(ans)