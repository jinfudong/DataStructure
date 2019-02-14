from Linked_list.Base import LList


mlist1 = LList()    # 实例化链表

for i in range(10):   # 生成原始数据
    mlist1.append(i)
mlist1.print_all()

mlist1.rev()
mlist1.print_all()

# mlist1.insert(3, 'a')  # 插入数据
# mlist1.print_all()
#
# mlist1.delete(3)  # 删除数据
# mlist1.print_all()
#
# mlist1.pop_last()  # 删除末尾数据
# mlist1.print_all()



