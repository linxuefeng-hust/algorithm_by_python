# 适用于近乎有序的数组中存放数据, 因为可以提前中止循环，所以理论上比选择排序效率高
# 但因为包含大量的交换操作，所以实际上耗时大于选择排序
# 从小到大排序
import numpy as np
def insertion_sort(arr, n):# arr is the list, n is the number of the list
    for i in range(1, n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

# 改进的做法，先比较a[j-1]与temp，若temp小于a[j-1],则说明temp不应该放在当前的位置，应该前移到满足a[j-1]小于temp的位置a[j]
# 减少了交换操作，时间更快
def improve_insertion_sort(arr,n):
    for i in range(1, n):
        temp = arr[i] # 当前的位置
        j = i
        while j > 0 and arr[j-1] >temp:
            arr[j] = arr[j-1] # arr[j-1]太大了，所以要后移
            j -= 1
        arr[j] = temp
    return arr


if __name__=='__main__':
    arr = np.random.randint(-10, 50, 20)
    new_arr= improve_insertion_sort(arr, len(arr))
    print(new_arr)


