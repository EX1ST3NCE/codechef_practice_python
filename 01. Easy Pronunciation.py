# https://www.codechef.com/problems/EZSPEAK

n = int(input())

for i in range(n):
    size = int(input())
    vowels = ['a', 'e', 'i', 'o', 'u']
    flag = 0
    word = input()
    
    if len(word) >= 4:
        for i in range(len(word) - 3):
            if word[i] not in vowels and word[i+1] not in vowels and word[i+2] not in vowels and word[i+3] not in vowels:
                flag =1
                break
            
    if flag == 1:
        print("NO")
    else:
        print("YES")