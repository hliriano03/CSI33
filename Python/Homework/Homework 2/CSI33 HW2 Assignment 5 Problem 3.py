def SelectionSort(items):

    print("Unsorted List: ", items)
    Sorted = 0
    n = len(items)

    while Sorted < n-1:
        m = FindSmallest(items[Sorted:])
        tmp = items[Sorted]
        items[Sorted] = items[m+Sorted]
        items[m+Sorted] = tmp

        Sorted += 1

    print("\nSorted List: ", items)

def FindSmallest(items):

    s = 0 # index of smallest element
    i = 0 # index/counter

    while i < len(items): # check all the elements in the list

        if items[s] > items[i]:
            s = i
        i += 1
    return s

SelectionSort([1,48,29,12,69,0,38,6,5,7,8,9,110])
