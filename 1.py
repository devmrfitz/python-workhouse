test_cases=int(raw_input())
for i in range(test_cases):
    n=int(raw_input())
    arr=raw_input().split()
    sum=0
    for j in range(n):
        sum+=arr[j]
    if (sum>=0):
        print('YES')
    else:
        print('NO')
