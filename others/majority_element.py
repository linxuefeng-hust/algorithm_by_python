# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    result=a[0]
    cnt=1
    for i in range(1,right):
        if a[i] == result:
            cnt += 1
        elif cnt == 1:
            result = a[i]
        else:
            cnt = cnt-1
    cnt = 0
    for j in range(0, right):
        if a[j] == result:
            cnt += 1
    if cnt > right/2 :
        return result
    else:
        return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
