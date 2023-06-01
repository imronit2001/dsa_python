class SortingAlgo:
    def __init__(self):
        self.arr = self.randomArray()

    def randomArray(self):
        return [50, 90, 40, 80, 10, 30, 20, 60]

    def bubbleSort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-i-1):
                if self.arr[j] > self.arr[j+1]:
                    x = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = x

    def display(self):
        print()
        for i in range(len(self.arr)):
            print(self.arr[i], end=' ')
        print()
        self.arr = self.randomArray()

    def modifiedBubbleSort(self):
        swap = False
        for i in range(len(self.arr)):
            swap = False
            for j in range(len(self.arr)-i-1):
                if self.arr[j] > self.arr[j+1]:
                    x = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = x
                    swap = True
            if not swap:
                break

    def insertionSort(self):
        for i in range(1, len(self.arr)):
            j = i-1
            key = self.arr[i]
            while j >= 0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key

    def selectionSort(self):
        for i in range(len(self.arr)):
            min_index = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[min_index], self.arr[i] = self.arr[i], self.arr[min_index]

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            leftArray = arr[:mid]
            rightArray = arr[mid:]
            self.mergeSort(leftArray)
            self.mergeSort(rightArray)

            i = j = k = 0
            while i < len(leftArray) and j < len(rightArray):
                if leftArray[i] < rightArray[j]:
                    arr[k] = leftArray[i]
                    i += 1
                else:
                    arr[k] = rightArray[j]
                    j += 1
                k += 1
            while i < len(leftArray):
                arr[k] = leftArray[i]
                i += 1
                k += 1
            while j < len(rightArray):
                arr[k] = rightArray[j]
                j += 1
                k += 1

    def quickSort(self, arr, left, right):
        if left < right:
            loc = quick(arr, left, right)
            if loc > left+1:
                self.quickSort(arr, left, loc-1)
            else:
                self.quickSort(arr, loc+1, right)


def quick(arr, left, right):
    loc = left
    while left < right:
        while left < right and arr[loc] <= arr[right]:
            right -= 1
        if left == right:
            break
        arr[loc], arr[right] = arr[right], arr[loc]
        loc = right

        while left < right and arr[left] <= arr[loc]:
            left += 1
        if left == right:
            break
        arr[loc], arr[left] = arr[left], arr[loc]
        loc = left
    return loc


sort = SortingAlgo()
flag = True
while flag:
    print("1. Display List")
    print("2. Bubble Sort")
    print("3. Modified Bubble Sort")
    print("4. Insertion Sort")
    print("5. Selection Sort")
    print("6. Merge Sort")
    print("7. Quick Sort")
    print("0. Exit")

    ch = int(input("Enter choice : "))
    if ch == 1:
        sort.display()

    elif ch == 2:
        print("Before Sorting : ")
        sort.display()
        sort.bubbleSort()
        print("After Sorting : ")
        sort.display()

    elif ch == 3:
        sort.modifiedBubbleSort()
        sort.display()

    elif ch == 4:
        sort.insertionSort()
        sort.display()

    elif ch == 5:
        sort.selectionSort()
        sort.display()

    elif ch == 6:
        sort.mergeSort(sort.arr)
        sort.display()

    elif ch == 7:
        sort.quickSort(sort.arr, 0, len(sort.arr)-1)
        sort.display()

    elif ch == 0:
        flag = False

    else:
        print("Invalid choice")
