def insert(self, alist, index, n):
    currentvalue = alist[index]
    position = index

    while position > 0 and alist[position - 1] > currentvalue:
        alist[position] = alist[position - 1]
        position = position - 1

    alist[position] = currentvalue

def insertionSort(self, alist, n):
    for index in range(1, n):
        self.insert(alist, index, n)