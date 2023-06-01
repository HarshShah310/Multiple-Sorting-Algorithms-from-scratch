import timeit
def heapify(arr, n, i):
    """
    Function to create a max heap
    """
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
  
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heap_sort(arr):
    """
    Sorts an array using heap sort algorithm
    """
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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

heap_sort(arr)  #passing the array to be sorted through function

stop = timeit.default_timer()  
print ("\nSorted array by HeapSort is : ")
print(arr)   
print("\n", len(arr), "Elements Sorted by Heap Sort in", stop-start, "seconds")