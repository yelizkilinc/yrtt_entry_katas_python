# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# More examples in the test cases below.
# Good luck!
def repeats(arr):
  dict={}
  for item in arr:
    if item in dict:
      dict[item]+=1
    else:
      dict[item]=0
  sum=0
  for num in dict.keys():
    if dict[num]==0:
      sum=sum+int(num)
  return sum