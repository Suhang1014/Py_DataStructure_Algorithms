# 二分查找
def binary_search(nums: list, target: int):
    return bsearch_inner(nums, 0, len(nums) - 1, target)

def bsearch_inner(nums: list, low: int, high: int, target: int):
    if low > high:
        return -1
    
    mid = low + int((high - low) >> 2)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bsearch_inner(nums, mid + 1, high, target)
    elif nums[mid] > target:
        return bsearch_inner(nums, low, mid - 1, target)


if __name__ == "__main__":
    ts = [1,2,3,4,5,6,7]
    target = 4
    ind = binary_search(ts, target)
    print(ind)

