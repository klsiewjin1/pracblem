"""
A min heap implementation
"""


class MinHeap:
    """
    Without having an unused first elem, the properties would like like this
    parent: heapList[i-1]/2
    left child: heapList[(2i)+1]
    right child: heapList[(2i)+2]

    Whereas with the unused first elem,
    parent: heapList[i]
    left child: heapList[2i]
    right child: heapList[2i+1]
    """

    def __init__(self):
        self.heapList = [0]
        self.current_size = 0

    def parent(self, i):
        return self.heapList[i // 2]

    def left_child(self, i):
        return self.heapList[2 * i]

    def right_child(self, i):
        return self.heapList[2 * i + 1]

    def bubble_up(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.parent(i):
                # If current node value is smaller than parent, swap and continue checking
                self.swap(i // 2, i)
            i //= 2  # Move to the parent node and check

    def insert(self, k):
        """
        Add element to the end of the list, and bubble up

        When inserting an element to the list, if the element is smaller than the parent,
        swap the elements with it's parent till no longer true
        :param k:9999
        :return:
        """
        self.heapList.append(k)
        self.current_size += 1
        self.bubble_up(self.current_size)

    def swap(self, i, k):
        self.heapList[i], self.heapList[k] = self.heapList[k], self.heapList[i]

    def bubble_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heapList[i] > self.heapList[mc]:
                self.swap(i, mc)
            i = mc

    def min_child(self, i):
        """
        Returns heapList index of the smaller value
        :param i:
        :return:
        """
        if i * 2 + 1 > self.current_size:
            # If current node does not have a right child, return left child
            return i * 2
        else:
            if self.left_child(i) < self.right_child(i):
                return i * 2
            else:
                return i * 2 + 1

    def remove(self):
        """
        When removing an element, swap the last-placed element to root and bubble down
        :return:
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.current_size]  # Move the last element to root
        self.current_size -= 1
        self.heapList.pop()
        self.bubble_down(1)
        return retval

    def buildHeap(self, arr):
        i = len(arr) // 2
        self.current_size = len(arr)
        self.heapList = [0] + arr[:]
        while i > 0:
            self.bubble_down(i)
            i -= 1


# Driver Code
if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MinHeap()
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)

    print("The Min val is " + str(minHeap.remove()))
