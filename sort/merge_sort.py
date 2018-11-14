# i表示左半部正在进行比较的数字的位置，j表示右半部正在进行比较的数字的位置，
# 而k表示aux中将要进行比较的数字的位置
# 从小到大排序
import numpy as np

def __merge(arr, lf, mid, rt):
    aux = np.zeros((rt-lf+1))
    for i in range(lf,rt+1): # 闭区间，将rt包含在内
        aux[i - lf] = arr[i]
    i = lf, j = mid +1
    for k in range(lf, rt+1):
        if i > mid:
            arr[k] = aux[j -lf]
            j += 1
        elif j >rt:
            arr[k] = aux[i- lf]
            i += 1
        elif aux[i -lf] < aux[j - lf]:
            arr[k] = aux[i -lf]
            i += 1
        else:
            arr[k] = aux[j -lf]
            j += 1
    return arr



def __merge_sort(arr, lf, rt):
    if lf >= rt:
        return
    mid = lf + (rt - lf)//2
    __merge_sort(arr, lf, mid)
    __merge_sort(arr, mid+1, rt)
    __merge(arr, lf, mid, rt)



def merge_sort(arr, n):
    __merge_sort(arr, 0, n-1) # 因为使用的是前闭后闭的情况，所以传入n-1

if __name__=='__main__':
    arr = np.random.randint(-20, 50, 60)
    n = len(arr)
    merge_sort(arr, n)
    print(arr) # 会是浅拷贝吗
'''
# 因为使用了len函数，所以都是开区间；归并排序在面对近乎有序的数组时，效率不如插入排序，
# 对于有序数组，插入排序的时间复杂度可以达到O(n)
def merge(left, right):
    c = []
    i, j =0,0
    while i <len(left) and j <len(right):
        if left[i] < right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1
    if i ==len(left):  # 边界条件
        for  element in right[j:]:
            c.append(element)

    elif j==len(right):
        for  element in left[i:]:
            c.append(element)
    return c

def merge_sort(lists):
    if len(lists)<= 1:
        return lists
    mid = len(lists)//2
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return  merge(left, right)

if __name__=='__main__':
    arr = np.random.randint(-20, 20, 30)
    print(np.array(merge_sort(arr))) # 传入的是array，返回的是list需要转换成array
'''
