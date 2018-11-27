# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pass

def partition2(a, l, r):
    x = a[l]
    j = l;
# 定义：a[l+1...j] < =x； a[j+1...i) >v, 前闭后开，i表示当前值,一开始这两个数组都为空
    for i in range(l + 1, r + 1):
        if a[i] <= x: # a[i]表示当前值，a[j+1]表示第一个大于value的值
            j += 1 # j= j+1，此时a[j]就变成了第一个大于等于value的数
            a[i], a[j] = a[j], a[i] #a[i]和a[j]交换正好满足定义
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
	# a[l, m-1]< a[m] ; a[m+1, r]>a[m]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
