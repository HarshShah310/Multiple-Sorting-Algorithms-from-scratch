import timeit
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]      # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            j -= 1
        arr[j + 1] = key

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

insertion_sort(arr)  #passing the array to be sorted through function

stop = timeit.default_timer()  
print ("\nSorted array with Insertion Sort is : ")
print(arr)   
print("\n", len(arr), "Elements Sorted by Insertion Sort in", stop-start, "seconds")