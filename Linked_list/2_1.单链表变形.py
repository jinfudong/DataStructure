# 1.普通链表在结尾插入数据的时候，复杂度为O(n),为此，可以变形，让Head再定义一个_rear属性指向末尾的节点，
# 当从末尾插入一个节点的时候，直接让head._rear.next = 这个节点，然后head.rear也等于这个节点，就完成了插入操作，
from Linked_list.Base import LList, LNode


class LListRear(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    # 重写在表头插入节点方法
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
        self.count += 1
        return

    # 重写在表尾添加节点方法
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
        self.count += 1
        return

    # 重写在表尾删除元素的方法
    def pop_last(self):
        if self._head is None:
            raise Exception('链表为空')
        p = self._head
        if p.next is None:  # 链表中只有一个元素
            e = p.elem
            self._head = None
            self.count -= 1
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        self.count -= 1
        return e


# 实例操作
list_rear = LListRear()
list_rear.prepend(99)
for i in range(10):
    list_rear.append(i)

list_rear.print_all()
