option = int(input("\nEnter you choice : \n1. Merge Sort \n2. Heap Sort \n3. Regular Quick Sort \n4. Quick Sort using 3 Medians \n5. Insertion Sort \n6. Selection Sort \n7. Bubble Sort \n8. Exit Main Menu\n"))
if option == 1:
    exec(open('Merge_Sort.py').read())
    exec(open('MainMenu.py').read())
elif option == 2:
    exec(open('Heap_Sort.py').read())
    exec(open('MainMenu.py').read())
elif option == 3:
    exec(open('Quick_Sort_Regular.py').read())
    exec(open('MainMenu.py').read())
elif option == 4:
    exec(open('Quick_Sort_3_Median.py').read())
    exec(open('MainMenu.py').read())
elif option == 5:
    exec(open('Insertion_Sort.py').read())
    exec(open('MainMenu.py').read())
elif option == 6:
    exec(open('Selection_Sort.py').read())
    exec(open('MainMenu.py').read())
elif option == 7:
    exec(open('Bubble_Sort.py').read())
    exec(open('MainMenu.py').read())
elif option == 8:
    exit()
else:
    print("Invalid option, Please select correct option and Try again")
    exec(open('MainMenu.py').read())
