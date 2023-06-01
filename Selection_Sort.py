import timeit
def selection_sort(arr):
    """
    Sorts an array in ascending order using selection sort.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j            # Find the minimum element in remaining unsorted array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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

selection_sort(arr)  #passing the array to be sorted through function

stop = timeit.default_timer()  
print ("\nSorted array with Selection Sort is : ")
print(arr)   
print("\n", len(arr), "Elements Sorted by Selection Sort in", stop-start, "seconds")