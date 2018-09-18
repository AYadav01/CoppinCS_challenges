"""
Problem: Have the function KaprekarsConstant(num) take the num parameter being passed 
which will be a 4-digit number with at least two distinct digits. Your program should
perform the following routine on the number: Arrange the digits in descending order
and in ascending order (adding zeroes to fit it to a 4-digit number), and subtract the 
smaller number from the bigger number. Then repeat the previous step. Performing this
routine will always cause you to reach a fixed number: 6174. Then performing the routine 
on 6174 will always give you 6174 (7641 – 1467 = 6174). Your program should return the 
number of times this routine must be performed until 6174 is reached. 
For example: if num is 3524 your program should return 3 because of the following steps:
(1) 5432 – 2345 = 3087, (2) 8730 – 0378 = 8352, (3) 8532 – 2358 = 6174.

Solution: Given the input, arrange it in ascending and descending order first. Here, 
sorted() function is used to sort the element accordingly. Then subtract both the 
digits to verify if the result matches the constant. If not, call the recursive function
with the result as the new number. Also, check whether the result is a 4 digit number
before every recursive call.
"""

def kaprekarsConstant(num, tracker):
  
  #checking if the number is a 4 digit num and has at least
  #two distinct numbers
  if len(str(num))<4 or len(set(str(num)))<2:
    return "Provide a 4 digit num with at least two distinct digit!"
  
  constant = 6174 #constant for comparison
  
  #tuple unpacking from the function return value
  high_num, low_num = high_and_low(num)
  result = high_num - low_num

  if result != constant:
    #this check makes sure that the subtracted result a 4 digit number, if not it appends
    #"0" to the result
    if len(str(result))<4:
      result = int(str(result)+"0")
    #recursive case begins here
    return kaprekarsConstant(result, tracker+1)
  else:
    #break case
    return tracker
  

#this function return a tuple of two digits: one arranged in ascending and the other
#in descending order
def high_and_low(num):
  my_list = list(str(num)) #creates a list of character from the input number
  highNum = ""
  lowNum = ""
  
  #arranges number in highest order
  sorted_list = sorted(my_list, reverse=True)
  for num in sorted_list:
    highNum += num
  
  #arranges number in lowest order
  sorted_list = sorted(my_list)
  for num in sorted_list:
    lowNum += num

  return (int(highNum), int(lowNum)) #return the tuple value
 
#main function 
def main(num):
  print(kaprekarsConstant(num,tracker=1))

#main function call (change the num variable to see different result)
num = 5466
main(num)