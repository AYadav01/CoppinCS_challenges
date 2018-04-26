global found
found = False #will be set to True if we find the goal

def makeBrick(available_big_bricks, available_small_bricks, goal):
    #step sizes of the brick
    step_size_big = 5
    step_size_small = 1

    #this will execute only when number of bigger bricks are not zero
    if available_big_bricks != 0:
      required_big_bricks = goal//step_size_big #integer division
      #if required bigger bricks are less than or equal to available bricks
      if required_big_bricks <= available_big_bricks:
        #if length of required bricks, which are currently available, is equal to the goal, return True
        if (step_size_big*required_big_bricks) == goal:
          return not found
        else:
          #if we dont find the goal, find the required distance remaining to reach the goal
          inch_covered_big = goal-(step_size_big*required_big_bricks)
          #if the remaining distance could be covered by smaller bricks, return True/False
          return small_calcualate(inch_covered_big, step_size_small, available_small_bricks)

      #if required bigger bricks are greater than the avaiale greater bricks
      elif required_big_bricks >= available_big_bricks:
        #check how much distance could be covered by the available bricks
        distance_covered_big = goal - (available_big_bricks * step_size_big)
        #check if the remaining distance could be covered by smaller bricks, return True/False
        return small_calcualate(distance_covered_big, step_size_small, available_small_bricks)

    #if no bigger bricks are availabe
    elif available_small_bricks != 0:
      #find the required number of smaller bricks
      required_small_bricks = goal//step_size_small
      #check if required is less than or equal to availabe smaller bricks
      if required_small_bricks <= available_small_bricks:
        if (step_size_small*required_small_bricks) == goal:
          return not found #returns True
        else:
          return found
      else:
        return found
        
    #if both input is zero, such that invalid input
    else:
      return "Enter a valid input!"

#calculates if the required distance could be replace by smaller bricks
def small_calcualate(incoming_distance, step_size_small, available_small_bricks):
  if incoming_distance//step_size_small <= available_small_bricks:
    return not found
  else:
    return found

#paramters
bigBrick_num = 5
smallBrick_num = 2
goal = 3
print(makeBrick(bigBrick_num, smallBrick_num, goal))
#Yadav, Anil