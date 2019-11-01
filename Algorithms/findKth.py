# _*_ coding:utf-8 _*_
def partition(num, low, high):
    pivot = num[low]
    while low < high:
        while low < high and num[high] > pivot:
            high -= 1
        while low < high and num[low] < pivot:
            low += 1
        num[low], num[high] = num[high], num[low]
        num[high] = pivot
        return high, num


def findKth(num, low, high, k):
    index = partition(num, low, high)[0]
    print(partition(num, low, high)[1])
    if index == k:
        return num[index]
    elif index < k:
        return findKth(num, index + 1, high, k)
    else:
        return findKth(num, low, index - 1, k)


if __name__ == '__main__':
    arr = [2, 5, 1, 9, 3, 7, 4, 6, 8]
    k = 4
    tar = findKth(arr, 0, len(arr) - 1, k)
    print(tar)