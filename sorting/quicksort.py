def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:  # If the element is smaller than the pivot, swap it because we wait it to be on the left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])
