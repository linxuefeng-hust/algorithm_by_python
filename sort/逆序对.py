# 与归并排序的思路一致。分治法，保证子序列有序，再合并的过程中，一遍比较子序列的大小
# 一边记录逆序对的个数。即，只是在归并的过程中多加了计数器而已。

import numpy as np


def merge_count(left, right, count1, count2):
    count = count1 + count2
    i,j = 0,0
    alist = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # 加不加‘=’？相等的 算逆序吗，不算
            alist.append(left[i])
            i += 1
        else:
            alist.append(right[j])
            count += len(left[i:])
            j += 1
    if i == len(left):
            alist.extend(right[j:])
    elif j == len(right):
            alist.extend(left[i:])

    return alist, count



def number_of_inversions(alist,count):

    if len(alist) <= 1:
        count = 0 # 应该以0的形式传入，而非在此处初始化?
        return alist, count
    mid = len(alist)//2
    #count += count
    left, count1 = number_of_inversions(alist[:mid], count)
    right, count2 = number_of_inversions(alist[mid:], count)
    return merge_count(left, right, count1, count2)

if __name__=='__main__':
    alist = np.random.randint(-100000,300000 ,300000 ) # 实际中不可能用python实现算法，因为效率太低了，30万的数据就吃不消了
    alist = list(alist) # 这个的空间和时间的复杂度考虑了吗?
    count = 0
    #print(alist)
    alist ,count = number_of_inversions(alist, count)
    #print(alist)
    print('number of inversions:',count)
