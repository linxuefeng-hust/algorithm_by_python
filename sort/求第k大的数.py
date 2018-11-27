# 思路与快排很类似，在快排中，当我们根据快排中的标志位求得分割点m时，在分割点左边的m-l位都是小于标志位的
# 而分割点右边的r-m都是大于标志位的，即前（r-m)大的数都在分割点右边，
# 因为要求第k大的数，所以如果k<=r-m，则下一步对分割点右边的数组再分割，寻早第k大的数，反之，则再左边的数组寻早第k大的数
# 如果数组全部排好序了，那么最后一位（r)，则是第1大的数,
# 像上面的思路那样就很难想清楚，第k大，这个说法和从小到大的排序方式很不匹配，因为是反着来的，不如从改成大到小排序，就很合适了，
# 此时，第k大的数，就在从大到小排好序的数组的第k-1位
#https://blog.csdn.net/wenqiwenqi123/article/details/81669899
import random
import numpy as np

def partion(alist,l, r):
    value=alist[l]
    j=l
    # 定义：a[l+1...j] >=x； a[j+1...i) <v, 前闭后开，i表示当前值,一开始这两个数组都为空
    for i in range(l+1, r+1):
        if alist[i] >= value:
            j += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[l], alist[j] = alist[j], alist[l]
    return j


def max_k(alist,k, l, r):
    #l, r=0, len(alist)-1 # 这个r的取法似乎有点问题，得到不是一个在alsit中的绝对位置
    if l >= r:
        return
    h = random.randint(l,r) # 记住是randint
    alist[h], alist[l] = alist[l], alist[h]
    m = partion(alist, l, r) # 按大于l的在左边，小于l的在右边
    if k-1 < m:
        return max_k(alist, k, l, m-1) # 不加return，最后输出的m就等于none，
        # 按照师兄的说法，将递归看作树形结构，如果需要回到上面继续查找，就得用return，
        # 之前快排不用return是因为不需要返回值，因为传入的list本身会被改变

    elif k-1 > m:
        return max_k(alist, k, m+1, r)
    else: # k-1=m
        return alist[m] # 怎么把找到的数传出去呢？

if __name__=='__main__':
    alist = np.random.randint(-20,10, 15)
    print(alist)
    alist=list(alist)
    k=2
    l,r =0, len(alist)-1
    m=max_k(alist,k,l,r)
    print(alist)
    print(m)