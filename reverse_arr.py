# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def revers_string(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5, 6]
print(arr)
revers_string(arr, 0, 5)
print(arr)