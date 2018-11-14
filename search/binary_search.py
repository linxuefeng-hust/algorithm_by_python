# recurrence version
# a is sorted by low to high
# x is not in a？
# 两个版本的都没有问题，被注释掉的是非递归的版本
import sys
import math


def re_binary_search(left, right, a, x):
    mid = left + (right - left)//2
    if left > right:
        return -1  # a
    if x > a[mid]:
        left = mid + 1
        return re_binary_search(left, right, a, x)
    elif x < a[mid]:
        right = mid -1
        return re_binary_search(left, right, a, x)
    else:
        return  mid


if __name__=='__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n+1]
    a = data[1 : n+1] # n+1 can't be add in a
    for x in data[n+2:]:
        print(re_binary_search(0, len(a) - 1, a, x), end = '  ')

'''
def binary_search(a, x):
    left, right = 0, len(a)-1
    while left <= right:


        mid = left + (right - left)//2  # floor division
        if x > a[mid]:
            left = mid + 1
        elif x < a[mid]:
            right = mid -1
        else:
            return mid
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]   # the number of test examples
    a = data[1 : n + 1] # n+1 can't be add in a
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')

'''


