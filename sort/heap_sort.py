# 堆排序在从0开始排序和从1开始排序的规律略有不同
# 从1开始， 左子节点 i= 2*k, 右子节点j = 2*k +1, 根节点k/2
# 从0开始， 左子节点 i = 2*k+1, 右子节点j = 2*k+2, 根节点（k-1）/2
# 最大堆的实现
'''
def shift_down(lists):
    i = 1 # 堆从数组1开始计数
    cur_value =lists[len(lists)-1]
    # 最后一个子节点取得到， len(lists)=堆元素个数+1
    while 2*i < len(lists):
        if cur_value < lists[i]:
            i = i*2
        else:
            lists[i] ,cur_value= cur_value, lists[i]
            lists.append(cur_value)
            shift_down(lists)
'''

import numpy as np

def shift_down(heaplist,i, cur_size):
    temp = heaplist[i]
    j = 2*i
    while j <= cur_size:
        if j+1<=cur_size and heaplist[j]<heaplist[j+1]: #heaplist[j+1]可能会数组越界吗？
            # 不会，因为j等于2*i，因为堆的性质，只会小于或等于cur_size
            j = j+1
        if temp < heaplist[j]:
            heaplist[i] = heaplist[j]
            i = j  #i代表根节点下滑到的位置，i=j则表示根节点下换到其子节点
            j = 2*i
        else:
            break
    heaplist[i] =temp # 使用依次赋值覆盖避免每次swap带来的时间消耗



def swap(heaplist, i, j):
    heaplist[i], heaplist[j] = heaplist[j] ,heaplist[i]

def heap_sort(alist):
    alist=list(alist) # 将传入的数据类型转换成list类型
    heaplist=[0] + alist[:]
    cur_size=len(alist) # 堆排序从1开始存储数据
    i = cur_size//2
    while i>=1 :  # 1是根节点
        shift_down(heaplist,i, cur_size)
        i -= 1     # 到这步为止都是在构建最大堆

    h = cur_size
    while h>=1 :
        swap(heaplist, 1, h)  #将堆的最后一个元素和头节点进行交换
        h -= 1 # 最大堆长度减1，因为最后一个元素作为最大值已经移除
        shift_down(heaplist,1,h) #因为除了头节点都是有序的，所以只对头节点1进行shift_down

    return [heaplist[i] for i in range(1, len(heaplist))]

if __name__=='__main__':
    alist= np.random.randint(-100,100,85)
    print(alist)
    print(heap_sort(alist))





