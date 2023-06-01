import timeit
def quick_sort_3median(arr):
    quicksort_3median(arr,0,len(arr)-1)
    
def median_of_three(arr, i, j, k):      #comparing the 3 pivot values with each other to find out the median of the 3 pivots
  if arr[i] < arr[j]:
    return i if arr[k] < arr[i] else k if arr[k] < arr[j] else j
  else:
    return j if arr[k] < arr[j] else k if arr[k] < arr[i] else i

def quicksort_3median(arr,start,end):
    if start < end:
        divide = partition(arr,start,end)
        quicksort_3median(arr,start,divide-1)
        quicksort_3median(arr,divide+1,end)

def partition(arr,start,end):
    pivot = median_of_three(arr, start, end, (start + end) // 2)
    arr[start], arr[pivot] = arr[pivot], arr[start]
    pivot_value = arr[start]
    l = start+1
    r = end
    done = False
    while not done:
       while l <= r and arr[l] <= pivot_value:
           l = l + 1
       while arr[r] >= pivot_value and r >= l:
           r = r -1
       if r < l:
           done = True
       else:
           arr[l], arr[r] = arr[r], arr[l]
    arr[start], arr[r] = arr[r], arr[start]
    return r

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

quick_sort_3median(arr)  #passing the array to be sorted through function

stop = timeit.default_timer()  
print ("\nSorted array by quicksort 3-median is : ")
print(arr)   
print("\n", len(arr), "Elements Sorted by Quick Sort using 3 medians in", stop-start, "seconds")