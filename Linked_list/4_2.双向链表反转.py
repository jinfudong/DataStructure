'''
双向链表反转，
'''
from Linked_list.Base import DLList

mlist1 = DLList()    # 实例化链表

for i in range(10):   # 生成原始数据
    mlist1.append(i)
mlist1.print_all()

mlist1.rev()    # 反转链表
mlist1.print_all()
