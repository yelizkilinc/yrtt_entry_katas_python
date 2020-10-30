# Scenario
# Several people are standing in a row divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

# Task
# Given an array of positive integers (the weights of the people), return a new array of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

# Notes
# Array size is at least 1.
# All numbers will be positive.

def row_weights(array):
    new_weight_array=[0,0]
   
    for i in range(len(array)):
      if i%2==0:#if item in the array exists in 0,2,4,.. places, it will be added to the first element of the new array.
        new_weight_array[0]=new_weight_array[0]+array[i]
      else:
        new_weight_array[1]=new_weight_array[1]+array[i]
    return new_weight_array