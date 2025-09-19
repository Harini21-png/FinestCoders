def maximum_iteration(n, k):
    count = 0
    orig = str(n)
    rev = str(n)[::-1]
    max_num = int(orig)+ int(rev)
    for i in range(k):
        if str(max_num) == str(max_num)[::-1]:
            count += 1
            return([count, max_num])
        else:
            orig = str(max_num)
            rev = str(orig)[::-1]
            max_num = int(orig) + int(rev)
            count += 1
    return([count, max_num])
n = int(input())
k = int(input())
print(maximum_iteration(n, k))