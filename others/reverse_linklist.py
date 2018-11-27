class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next =None

head = ListNode()
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        pre = None
        temp = head
        while temp.next != None:
            next = temp.next
            temp.next = pre   # pre 已经初始化为None了，明白这个很重要

            pre = temp
            temp = next

        temp.next = pre

        return  temp




# 递归版

pre = None
def recurrence_reverse_linklist(head, pre):
    if head == None:
        return  None
    if head.next == None:
        head.next = pre
        return  head
    else:
        next = head.next
        head.next = pre
        pre = head
        head = next
        recurrence_reverse_linklist(head, pre)

# 递归函数什么时候加return， 什么时候不加呢？
# 参看之前的binary_search, quick_sort，有的加了，有的有没有加

