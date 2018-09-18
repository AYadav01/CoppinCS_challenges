
"""
Problem: create a method SecondGreatLow(arr) that takes the array of
numbers stored in arr and return the second lowest and second greatest
numbers, respectively, separated by a space.

Solution: sort the array (Bubble sort used here) and return the elements by indexing.
"""

def secondGreatLow(array):
  
  #modified bubble sort
  start_index = 0
  
  if len(array) <= 1:
    return array
    
  while start_index < len(array):
    for index in range(start_index+1, len(array)):
      if array[start_index] > array[index]:
        temp = array[start_index]
        array[start_index] = array[index]
        array[index] = temp
      else:
        continue
    start_index += 1
  
  #returning the desired element
  if len(array) <= 3:
    return (array[0],array[1])
  else:
    return (array[1], array[-2])

arg = [4,2,1,0,9]
print(secondGreatLow(arg))






