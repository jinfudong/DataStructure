from Linked_list.Base import LNode

'''
循环单链表
最后一个节点的next不是None，而是指向表的第一个节点
'''


class LCList(object):
    def __init__(self):
        self._rear = None
        self.count = 0

    def is_empty(self):
        return self._rear is None

    # 前端插入节点
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
        self.count += 1
        return

    # 尾端插入节点
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    # 前端弹出元素
    def pop(self):
        if self._rear is None:
            raise Exception('链表为空')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        self.count -= 1
        return p.elem

    # 从后端弹出元素
    def pop_last(self):
        p = self._rear
        if p is None:
            raise Exception("链表为空")
        if self._rear.next is p:  # 如果只有一个元素
            self._rear = None
            self.count -= 1
            return p.elem
        while p.next is not self._rear:
            p = p.next
        e = self._rear.elem
        p.next = self._rear.next
        self._rear = p
        self.count -= 1
        return e

    # 指定位置插入元素
    def insert(self, index, elem):
        if index < 0 or index > self.count:
            raise Exception('插入位置无效')
        elif index == 0:
            self.prepend(elem)
        elif index == self.count:
            self.append(elem)
        p = self._rear.next
        for i in range(index - 1):
            p = p.next
        p.next = LNode(elem, p.next)
        self.count += 1

    # 删除元素
    def delete(self, index):
        if index < 0 or index > self.count:
            raise Exception('插入位置无效')
        elif index == 0:
            self.pop()
        elif index == self.count:
            self.pop_last()
        p = self._rear.next
        for i in range(index - 1):
            p = p.next
        p.next = p.next.next
        self.count -= 1

    # 从指定位置输出循环链表
    def print_all(self, index=0):
        temp = self._rear
        if self.is_empty():
            return
        if index == 0:
            p = self._rear.next
        else:
            for i in range(index):
                self._rear = self._rear.next
            p = self._rear.next
        while True:
            print(p.elem, end='')
            if p is self._rear:
                print('')
                break
            print(' --> ', end='')
            p = p.next
        self._rear = temp


# 实例化操作
mlist = LCList()

# 添加元素
mlist.prepend(99)
for i in range(10):
    mlist.append(i)
mlist.print_all()
mlist.print_all(1)
mlist.print_all(2)
mlist.print_all(3)

# 从头部删除
# mlist.pop()
# mlist.print_all()
#
# # 从尾部删除
# mlist.pop_last()
# mlist.print_all()
#
# # 从中间插入
# mlist.insert(2, 'a')
# mlist.print_all()
#
# # 从中间删除
# mlist.delete(3)
# mlist.print_all()
