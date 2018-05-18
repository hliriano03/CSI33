# This programs has implementation of two algorithms:
# linear search and binary search ...

from time import time

def main():

  numbers = list(range(1000000)) # generate a list of numbers from 0 to 999999
  #print(numbers)

  start = time() #starts time
  linear_search(numbers,10)
  end = time() #ends time

  print("Linear Search for 10, Time:", end - start) #substracts the end time with the start time to get the enlapsed time

  start = time()
  linear_search(numbers,499999)
  end = time()

  print("Linear Search for 499999, Time:", end - start)

  start = time()
  linear_search(numbers,999999)
  end = time()

  print("Linear Search for 999999, Time:", end - start, "\n")

  start = time()
  binary_search(numbers,10)
  end = time()

  print("Binary Search for 10, Time:", end - start)

  start = time()
  binary_search(numbers,499999)
  end = time()

  print("Binary Search for 499999, Time:", end - start)

  start = time()
  binary_search(numbers,999999)
  end = time()

  print("Binary Search for 999999, Time:", end - start)

##  do the same for binary search

def linear_search(items,target):
  """ Checks items one by one until finding target, if it does not find it it
      returns -1 """
  
  for i in range(len(items)): #checks each item on the list

      if items[i] == target: #if the target in the list it returns the item

          return i

  return -1 #if the target not in the list then it returns -1


def binary_search(items,target):
  """ Sorts list and breaks it in half whether the target number is bigger
      or smaller to find target faster"""

  first = 0
  last = len(items) #sets last list number position 

  while first < last:

    middle = (first + last) // 2 #sets middle list number position
    x = items[middle] #sets middle number to x

    if target == x: #if target is the middle number it returns it

      return middle

    elif target > x: #if target bigger than middle number then first is replaced by the middle number position
      if first == middle:
        break
      
      first = middle

    elif target < x: #if target smaller than middle number then last is replaced by the middle number position
      last = middle

  return -1
