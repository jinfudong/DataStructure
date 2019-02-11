'''
双向链表在插入和删除方面比单向列表有优势，
因为单向链表在插入的时候，需要遍历找到他的前驱节点，然后再进行插入数据，
单向链表在删除数据的时候，同样也要遍历找到前驱节点，而双向链表则不需要这些操作
'''
from Linked_list.Base import DLList

mlist1 = DLList()    # 实例化链表

for i in range(10):   # 生成原始数据
    mlist1.append(i)
mlist1.print_all()

mlist1.insert(3, 'a')  # 插入数据
mlist1.print_all()

mlist1.delete(3)  # 删除数据
mlist1.print_all()

mlist1.pop_last()  # 删除末尾数据
mlist1.print_all()
