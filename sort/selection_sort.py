
# 默认从小到大排序
import sys
def selection_sort(arr, n):
    # arr is the list, n is the number of the list
    for i in range(0,n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__=='__main__':
    arr = ['D', 'C', 'A', 'E', 'H', 'F', 'B'] # has been test with int ,float, string
    n = 7
    newarr = selection_sort(arr, n)
    print(newarr)







   
   
