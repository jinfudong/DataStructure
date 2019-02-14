
# 单链表的基本操作


class LNode(object):   # 定义节点类

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList(object):

    def __init__(self):
        self._head = None
        self.count = 0

    # 判断链表是否为空
    def is_empty(self):
        return self._head is None

    # 在表头插入数据
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        self.count += 1
        return

    # 删除表头节点并返回该数据
    def pop(self):
        if self._head is None:
            raise Exception('链表为空')
        e = self._head.elem
        self._head = self._head.next
        self.count -= 1
        return e

    # 在链表尾部插入元素
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self.count += 1
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        self.count += 1
        return

    # 在链表尾部删除元素
    def pop_last(self):
        if self._head is None:  # 如果链表为空
            raise Exception('链表为空')
        p = self._head
        if p.next is None:  # 如果链表只有一个元素
            e = p.elem
            self._head = None
            self.count -= 1
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self.count -= 1
        return e

    # 在指定位置插入数据
    def insert(self, index, elem):
        if index < 0 or index > self.count:
            raise Exception('插入位置无效')
        elif index == 0:
            self.prepend(elem)
        elif index == self.count:
            self.append(elem)
        p = self._head
        for i in range(index-1):
            p = p.next
        p.next = LNode(elem, p.next)
        self.count += 1

    # 在指定位置删除数据
    def delete(self, index):
        if index < 0 or index > self.count:
            raise Exception('插入位置无效')
        elif index == 0:
            self.pop()
        elif index == self.count:
            self.pop_last()
        p = self._head
        for i in range(index-1):
            p = p.next
        p.next = p.next.next
        self.count -= 1

    # 输出链表
    def print_all(self):
        p = self._head
        if p is None:
            raise Exception('链表为空')
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(' --> ', end='')
            p = p.next
        print('')

    # 单链表反转
    def rev(self):
        if self._head is None:
            return
        pre = self._head
        cur = pre.next
        pre.next = None
        while cur.next:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        self._head = cur
        cur.next = pre


# 双向链表基本操作

class DLNode(LNode):

    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

class DLList(LList):

    def __init__(self):
        LList.__init__(self)
        self._rear = None

    # 从前端插入节点
    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:  # 空表
            self._rear = p
        else:
            p.next.prev = p
        self._head = p
        self.count += 1

    # 从后端插入节点
    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:  # 空表插入
            self._head = p
        else:
            p.prev.next = p
        self._rear = p
        self.count += 1

    # 从前端删除节点
    def pop(self):
        if self._head is None:
            raise Exception('链表为空')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        self.count -= 1
        return e

    # 从后端删除节点
    def pop_last(self):
        if self._head is None:
            raise Exception('链表为空')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None  # 设置_head，保证is_empty正常工作
        else:
            self._rear.next = None
        self.count -= 1
        return e

    # 插入节点
    def insert(self, index, elem):
        if index < 0 or index > self.count:
            raise Exception('插入位置无效')
        elif index == 0:
            self.prepend(elem)
        elif index == self.count:
            self.append(elem)
        p = self._head
        for i in range(index-1):
            p = p.next
        new_node = DLNode(elem, p, p.next)
        p.next.prev = new_node
        p.next = new_node
        self.count += 1

    # 删除节点
    def delete(self, index):
        if index < 0 or index > self.count:
            raise Exception('插入位置无效')
        elif index == 0:
            self.pop()
        elif index == self.count:
            self.pop_last()
        p = self._head
        for i in range(index - 1):
            p = p.next
        p.next.next.prev = p
        p.next = p.next.next
        self.count -= 1

    # 双向链表反转
    def rev(self):
        if self._head is None:
            return
        p = self._head
        while p.next:
            temp = p.next
            p.next = p.prev
            p.prev = temp
            p = p.prev

        p.next = p.prev  # 最后一个p节点
        p.prev = None
        self._head.prev = self._head.next
        self._rear = self._head
        self._head = p



