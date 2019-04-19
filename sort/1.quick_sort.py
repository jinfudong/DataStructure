'''
1.先从待排序数组中找到一个数，小于这个数的元素放到左边，大于这个数的元素放到右边
2.分别在左右两个数组以此类推此过程，知道子数组大小为1结束
3.拼接数组
4.时间复杂度：
  最好： nlogn
  平均： nlogn
  最坏： n**n
5.空间复杂度：
     nlogn

# 稳定性排序：
     冒泡排序、插入排序、归并排序、桶排序
  不稳定的排序：
     选择排序、希尔排序、快速排序、堆排序

'''




def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    mid_num = arr.pop()
    left_list = []
    right_list = []
    for i in arr:
        if i <= mid_num:
            left_list.append(i)
        else:
            right_list.append(i)
    return quick_sort(left_list)+[mid_num]+quick_sort(right_list)


# list1 = [3, 7, 5, 8, 4, 2, 1]
# list2 = quick_sort(list1)
# print(list2)

print(print(0))


'''
求一个列表连续之和最大值
'''


def summax(arr:list):
    Max, temp = arr[0], 0
    num_list = [Max]
    for i in arr:
        if temp < 0:
            temp = i
            num_list = [i]
        else:
            temp += i
            num_list.append(i)
        Max = max(temp, Max)
    return Max, num_list


list1 = [1, -2, 3, 10, -4, 7, 2, -5]
list1.sort()
#
# a, b = summax(list1)
# print(a)
# print(b)

