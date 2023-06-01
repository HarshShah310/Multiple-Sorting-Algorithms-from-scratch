import timeit
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]       # Dividing the array elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)       # Sorting the left half
        merge_sort(right_half)      # Sorting the right half

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):   # Check if any element was left in left half, if so then append it to an array
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):  # Check if any element was left in right half, if so then append it to an array
            arr[k] = right_half[j]
            j += 1
            k += 1

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

merge_sort(arr)  #passing the array to be sorted through function

stop = timeit.default_timer()  
print ("\nSorted array by MergeSort is : ")
print(arr)   
print("\n", len(arr), "Elements Sorted by Merge Sort in", stop-start, "seconds")