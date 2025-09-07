
# Time Complexities of Array Ops 
# Initial List
arr = [4, 6, 9, 3, 7, 2]

# Access & Update 
print(f"First element is: {arr[0]}")   # Access by index → O(1)

arr[3] = 88                            # Update value at index → O(1)
print(f"Modified list (insert 88 at index 3): {arr}")

# Adding / Removing Elements 
arr.append(5)                          # Add at end → O(1)
print(f"Insert 5 at end: {arr}")

arr.insert(3, 23)                      # Insert at specific index → O(n)
print(f"Insert 23 at index 3: {arr}")

arr.pop()                              # Remove last element → O(1)
print(f"Popped last element: {arr}")

arr.pop(3)                             # Remove at specific index → O(n)
print(f"Popped element at index 3: {arr}")

arr.append(88)                         
print(f"Added 88 at the end: {arr}")

arr.remove(88)                         # Remove by value (first occurrence) → O(n)
print(f"Removed first occurrence of 88: {arr}")

#  Searching 
if 4 in arr:                           # Membership check → O(n)
    print("4 is present ✅")

#  Slicing 
print(f"Slice [2:5]: {arr[2:5]}")      # Slice → O(k), where k = slice size

# Reverse 
print(f"Reversed: {arr[::-1]}")        # Reverse via slicing → O(n)

# Extending 
arr.extend([58, 99])                   # Extend with another list → O(k)
print(f"Extended with [58, 99]: {arr}")

# Sorting 
arr.sort()                             # Python uses Timsort → O(n log n) average
print(f"Sorted list: {arr}")