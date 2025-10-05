
# extend the max sum subArray if the previous element by adding the current element to it. if th maximums sub array sum ending at previous element is positive else
# start a new sub array from the current element
# maxEnding at index i = max(maxEnding at index (i-1) + arr[i], arr[i])

# Tc = O(n)
# Sc = O(1)

def max_subarray_sum(arr): 
    # Get the length of the input array 
    l=len(arr) 
    # Initialize the running subarray sum and the maximum subarray sum to the first element in the array 
    max_sum = arr[0] 
    current_sum = arr[0] 
    # Select an index of a subarray 
    for i in range(1,l): 
        # Get the sum of previous subarray elements and the current element 
        combined_sum  = current_sum + arr[i] 
 
        # If the current element is greater combined_sum, update current_sum to the current element, otherwise update it to combined_sum 
        if arr[i] > combined_sum : 
            current_sum= arr[i]  
        else: 
            current_sum= combined_sum 
        # Update the maximum subarray sum 
        if current_sum>max_sum: 
            max_sum=current_sum 
             
    return max_sum 
 
arr = [2, 3, -5, 6, -4] 
print("The input array is:",arr) 
result=max_subarray_sum(arr) 
print("The maximum subarray sum is:", result) 



