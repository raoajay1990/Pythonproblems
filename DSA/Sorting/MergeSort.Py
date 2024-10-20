# sort the below array input using merge sort
#input array [12, 11, 13, 5, 6, 7]

def mergeSort(arr, left, right):
    if (left<right):

        # mid = (left+right)//2

        # Best Approach for calculating Mid
        mid = left + (right-left)//2


        #Divide the first half
        mergeSort(arr, left, mid)
        #Divide the second half
        mergeSort(arr, mid+1, right)

        merge(arr, left, mid, right)


def merge(arr, left:int, mid:int, right:int):
    
    left_size = mid-left + 1
    right_size = right - mid

    left_temp_array = []
    right_temp_array = []

    for i in range(0, left_size):
        left_temp_array.append(arr[i+left])

    for i in range(0, right_size):
        right_temp_array.append(arr[mid+1+i])

    
    # print(f"left_temp_array: {left_temp_array}")
    # print(f"right_temp_array: {right_temp_array}")

    i,j=0,0
    k=left

    while (i<left_size and j<right_size):
        
        if(left_temp_array[i]<=right_temp_array[j]):
            arr[k] = left_temp_array[i]
            i = i+1
        else:
            arr[k] = right_temp_array[j]
            j = j+1
        
        k = k+1


    #copy remaining elements in left array
    while i<left_size:
        arr[k] = left_temp_array[i]
        i=i+1
        k = k+1

    #copy remaining elements in right array
    while j<right_size:
        arr[k] = right_temp_array[j]
        j=j+1
        k = k+1

    



input_array = [12, 11, 13, 5, 6, 7]
arrayLeft : int = 0
arrayRight : int = len(input_array)

for i in range(len(input_array)):
    print(f"{input_array[i]}", end=" ")

mergeSort(input_array, arrayLeft, arrayRight-1)

print("sorting completed using Merge Sort Algorithm")
print("After Sorting")
for i in range(len(input_array)):
    print(f"{input_array[i]}", end=" ")


