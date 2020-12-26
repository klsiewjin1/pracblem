def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_array = arr[:mid]
    right_array = arr[mid:]
    mergesort(left_array)
    mergesort(right_array)
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    mergesort(arr)
    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])
