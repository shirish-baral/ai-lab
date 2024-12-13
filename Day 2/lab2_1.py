array =[]
n =  int(input("Enter number of array elements:"))
print("Enter array elements")
for i in range (n):
  element = int(input())
  array.append(element)
print("Array is:",array)
array.sort()
print("Sorted array is:",array)

