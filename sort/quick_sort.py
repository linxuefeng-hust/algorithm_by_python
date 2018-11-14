# Uses python3
import sys
import random

def partition3(a, l, r):
    # write your code here
    lt = l  # 加了分号之后就不会报错
    rt = r    # lt 与 rt 分别是与标致值相等的数的左右两边
    value = a[l]
    i = l
    while i <= rt:
        if value > a[i]:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif value < a[i]:
            a[i], a[rt] = a[rt], a[i]
            rt -=1
        else:
            i +=1
    #return str(lt), str(rt)  # 不加上str就会在第一行 lt = l 那里报错，TypeError: 'int' object is not iterable
    return lt, rt



def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]  # python中对数据进行交换操作都这么秀吗
    a[l], a[j] = a[j], a[l]
    return j                         # j是标志数所对应的数组位置



def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)  # k是在l与r范围内随机取一个数，与那种将整个数据打乱的思路略有差异
    a[l], a[k] = a[k], a[l]
    #use partition3
    left, right = partition3(a, l, r)
    # left = int(left)          # 不加以下两行就会报错 ，因为返回值是str类型
    # right = int(right)
    randomized_quick_sort(a, l, left - 1) # 加了分号之后就不会报错
    randomized_quick_sort(a, right + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
