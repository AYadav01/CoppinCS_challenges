# CoppinCS Challenge (makeBricks)

Problem Statement:
---

We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return true if it is possible to make the goal by choosing from the given bricks. The solution can be implemented without any loops.

My Solution
---

* Testing for two conditions: if there are bigger bricks or there is none

* If bigger bricks are available, find the minimun number of them to get to the goal

* If minimum number of bigger bricks, required to get to goal, is less than or equal to the available bricks, check if we reach the goal with the current bricks; if not, check how much distance is remaining to be covered (test if this distance could be covered by available smaller brick)

* If minimum number of bigger bricks is greater than the availabe bricks, check what is the maximum number of distance that could be covered from the current number of bigger bricks and test if the rest of the distance could be covered by smaller brick

* If no bigger bricks are available, check if the entire distance could be covered by the available number of single bricks

* If both the input bricks are zero, it is an invalid input

**Yadav, Anil (Coppin State University)**