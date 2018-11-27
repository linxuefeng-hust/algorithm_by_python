# Uses python3
# 三路快排，好处是中间相等的这部分就不用再排序了
import sys
import random

def partition3(a, l, r):
    # write your code here
    lt = l  # 加了分号之后就不会报错
    rt = r    # lt 与 rt 分别是与标致值相等的数的左右两边
    value = a[l]
    i = l
	# a[l+1...lt-1]<v; a[lt...i-1]==v; a[rt+1]>v
    while i <= rt:
        if a[i] < value : # 当前值小于value, 将其和等于value的第一个值交换位置
            a[i], a[lt] = a[lt], a[i] # a[lt]即等于value的第一个值,二者交换
            lt += 1
            i += 1
        elif a[i] > value : # 当前值大于value，将其和a[rt]交换
            a[i], a[rt] = a[rt], a[i] # a[rt]相当于大于v的第一个数的前一个位置的数，这个数未被处理
            rt -=1  # rt=rt-1，减一之前的a[rt]变为大于v的第一个数
			        # 此时i这个索引依然指向一个未被处理的数，所以不用维护
        else: # 当前值等于value,就直接保持在中间不变，i向后移动
            i +=1
    return lt, rt



def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:    # 小于标志数都放到前面去，同时将标志数所对应的位置后移
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
