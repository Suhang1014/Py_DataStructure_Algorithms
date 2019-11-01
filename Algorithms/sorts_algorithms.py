"""
    O(n^2)
    1. 冒泡排序
    2. 插入排序
    3. 选择排序

    O(nlogn)
    4. 快速排序
    5. 归并排序

    6. 希尔排序
    7. 堆排序
"""
"""
执行效率分析：
    1. 最好情况、最坏情况、平均情况时间复杂度
    2. 时间复杂度的系数、常数、低阶
    3. 比较次数和交换或移动的次数
"""


#冒泡排序
def bubble_sort(a: list):
    length = len(a)
    if length <= 1:
        return
    
    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                made_swap = True
        if not made_swap:
            break


# 插入排序
def insertion_sort(a: list):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value


# 选择排序
def selection_sort(a: list):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


# 快速排序
def quick_sort(a: list):
    quick_sort_between(a, 0, len(a) - 1)

def quick_sort_between(a: list, low: int, high: int):
    if low < high:
        pos = partition(a, low, high)
        quick_sort_between(a, low, pos - 1)
        quick_sort_between(a, pos + 1, high)

def partition(a: list, low: int, high: int):
    # 选最左边数作为pivot
    pivot, j = a[low], low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[low], a[j] = a[j], a[low]
    return j

# def qsort2(arr, low, high):
#     if low < high:
#         pos = partition2(arr, low, high)
#         qsort2(arr, low, pos - 1)
#         qsort2(arr, pos + 1, high)
#
# def partition2(arr, low, high):
#     pivot = arr[low]
#     left = low
#     right = high
#     while arr[right] > pivot:
#         right -= 1
#     while arr[left] <= pivot:
#         left += 1
#     arr[left], arr[right] = arr[right], arr[left]
#     arr[low], arr[right] = arr[right], arr[low]
#     return right


# 归并排序
def merge_sort(a: list):
    merge_sort_between(a, 0, len(a) - 1)

def merge_sort_between(a: list, low: int, high: int):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort_between(a, low, mid)
        merge_sort_between(a, mid + 1, high)
        merge(a, low, mid, high)

def merge(a: list, low: int, mid: int, high: int):
    l1, l2 = low, mid + 1
    tmp = []
    while l1 <= mid and l2 <= high:
        if a[l1] <= a[l2]:
            tmp.append(a[l1])
            l1 += 1
        else:
            tmp.append(a[l2])
            l2 += 1
    start = l1 if l1 <= mid else l2
    end = mid if l1 <= mid else high
    tmp.extend(a[start : end + 1])
    a[low : high + 1] = tmp


if __name__ == '__main__':
    a = [2, 5, 1, 9, 3, 7, 4, 6, 8]
    bubble_sort(a)
    print(a)

    b = [2, 5, 1, 9, 3, 7, 4, 6, 8]
    insertion_sort(b)
    print(b)

    c = [2, 5, 1, 9, 3, 7, 4, 6, 8]
    selection_sort(c)
    print(c)

    d = [2, 5, 1, 9, 3, 7, 4, 6, 8]
    qsort(d, 0, len(d)-1)
    print(d)

    e = [2, 5, 1, 9, 3, 7, 4, 6, 8]
    merge_sort(e)
    print(e)