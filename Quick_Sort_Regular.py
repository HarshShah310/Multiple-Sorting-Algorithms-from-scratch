import timeit
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:   # Check if the current value from left end is less than pivot then it is in the right place (left side of pivot) and we can move right, to the next element to check.
            i += 1
        while i <= j and arr[j] >= pivot:   # Check if the current value from right end is greater than pivot then it is in the right place (right side of pivot) and we can move left, to the next element to check.
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

# Main Code
arr=[]        
n = int(input("\nEnter number of elements : "))
print ("\nEnter the array : ")
for i in range(0, n):
    element = int(input())    #Input the data into the list
    arr.append(element)
print ("\nGiven array is : ")
print(arr)
start = timeit.default_timer() 

quicksort(arr, 0, len(arr) - 1)  #passing the array to be sorted through function

stop = timeit.default_timer()  
print ("\nSorted array by QuickSort is : ")
print(arr)   
print("\n", len(arr), "Elements Sorted by Regular Quick Sort in", stop-start, "seconds")
