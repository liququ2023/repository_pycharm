import random
import time

count = int(input('请输入要生成随机数列的长度：'))


# 归并排序
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


a = [random.randint(0, 100000000) for _ in range(0, count)]
b = a
time_start = time.time()
merge_sort(a)
time_end = time.time()
time_merge_sort = time_end - time_start
print('merge_sort:', time_merge_sort, 's')


# 选择排序
def selection_sort(list):
    length = len(list)
    if length <= 1:
        return list

    for j in range(length):
        # 假设第一个元素为最小元素
        min = j

        # 遍历未排序区域元素，以此和未排序区域的第一个元素做对比
        for i in range(j + 1, length):
            if list[i] < list[min]:
                min = i

        # 交换位置
        list[min], list[j] = list[j], list[min]

    return list


time_start = time.time()
selection_sort(b)
time_end = time.time()
time_selection_sort = time_end - time_start
print('selection_sort:', time_selection_sort, 's')

# 在随机数列长度为1000时，归并排序消耗0.002048秒，选择排序消耗0.017889秒
# 在随机数列长度为10000时，归并排序消耗0.018362秒，选择排序消耗1.334169秒
# 在随机数列长度为100000时，归并排序消耗0.200786秒，选择排序消耗142.833889秒
# 可见在数列随机排列的情况下，归并排序所需的时间短，比选择排序更高效，且数据规模越大，优势更突出
# 这是因为归并排序的时间复杂度为O(NlogN)，而选择排序的时间复杂度为O(N^2)
