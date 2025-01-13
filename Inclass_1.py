# Question 1
def foo(n):
    result = 0
    for i in range(2, n + 1, 3):
        result += i
    return result

# Question 2
import time

start_time = time.time()
def sum_largest(li):
    largest = float("-inf")
    second_largest = float("-inf")
    for num in li:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return largest + second_largest
example_list = [10, 4, 6, 12, -3, 1, 14, -7, 9]
print(sum_largest(example_list)) 
end_time = time.time()

elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time)

# Question 3
import time

start_time = time.time()
def sum_largest(li):
    sorted_list = sorted(li)
    return sorted_list[-1] + sorted_list[-2]
example_list = [10, 4, 6, 12, -3, 1, 14, -7, 9]
print(sum_largest(example_list))  
end_time = time.time()

elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time)

#Question 4(a)
#Function 2 will be faster since it will take O(n) time will function 3 takes (nlog(n))

#Question 4(b)
#In Python, the key difference between the sort() method and the sorted() function is that 
# sort() modifies the original list in-place, while sorted() creates and returns a new sorted list, 
# leaving the original list unchanged; essentially, sort() alters the existing list, 
# while sorted() generates a new one based on the iterable you provide.

#Question 5
def merge(li1, li2):
    merged_list = []
    i, j = 0, 0
    while i < len(li1) and j < len(li2):
        if li1[i] <= li2[j]:
            merged_list.append(li1[i])
            i += 1
        else:
            merged_list.append(li2[j])
            j += 1
    while i < len(li1):
        merged_list.append(li1[i])
        i += 1
    while j < len(li2):
        merged_list.append(li2[j])
        j += 1
    return merged_list

# Example usage
list1 = [2, 4, 5, 8, 10, 11, 13]
list2 = [3, 6, 7, 8, 10, 12]
print(merge(list1, list2))  

#Question 6
def largest_so_far(li):
    # Initialize variables
    max_so_far = float("-inf")  
    count = 0 
    
    # Iterate through the list
    for num in li:
        if num > max_so_far:
            count += 1  
            max_so_far = num 
    
    return count
example_list = [10, 8, 9, 9, 13, 16, 12]
print(largest_so_far(example_list))  

#Question 7
def evens(li):
    count=0
    length=len(li)
    for num in range(0,length-1,2):
        if l[num]%2==0:
            count+=1
    return count
l = [3, -2, 4, 7, -6, 7, 5]
print(evens(l))

#Question 8
def linear_search(li, num):
    for element in li:
        if element == num:
            return True  
    return False
example_list = [3, -2, 4, 7, -6, 7, 5]
print(linear_search(example_list, 4))  
print(linear_search(example_list, 10))

# Question 9
def binary_search(li, num):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == num:
            return True  
        elif li[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return False
ordered_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(ordered_list, 15))  # Output: True
print(binary_search(ordered_list, 8))  # Output: False

#Question 10
#Worst Case for linear search O(n)
# Worst case for Binary search is O(log(n))