# Scenario
# Several people are standing in a row divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

# Task
# Given an array of positive integers (the weights of the people), return a new array of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

# Notes
# Array size is at least 1.
# All numbers will be positive.

def row_weights(array):
    new_weight_array=[0,0]
   
    for item in array:
      if array.index(item)%2==0:
        new_weight_array[0]=new_weight_array[0]+item
      else:
        new_weight_array[1]=new_weight_array[1]+item
    return new_weight_array