
# 默认从小到大排序
import sys
def selection_sort(arr, n):
    # arr is the list, n is the number of the list
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
		if min_index != i：# 其实这个if不要也行，相等的话，交不交换都无所谓，不相等，则说明最小值改变，所以交换一下
		   arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

if __name__=='__main__':
    arr = ['D', 'C', 'A', 'E', 'H', 'F', 'B'] # has been test with int ,float, string
    n = 7
    newarr = selection_sort(arr, n)
    print(newarr)







   
   
