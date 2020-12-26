def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if arr[idx] > arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    selectionsort(arr)
    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])
