# CoppinCS Challenge (Rock, Paper, Scissors)

Problem Statement:
---

Write a program to play the rock-paper-scissor game. The user selects a move: either R, P, or S.  The program then randomly selects the other move and announces the winner as well as the basis for determining the winner (e.g. Paper covers rock, rock breaks scissors, scissors cut paper, or nobody wins).  The program should allow the players to use lowercase as well as uppercase.

The program should allow the player to enter his/her name.  The player’s name is displayed with the winning move.

My Solution
---

* Get the information from the user (name, move)

* The conditions that has to be met are stored in a list

	The list contains a tuple value pair: keyword and message

* From that tuple, a set of all unique moves (ASCII equivalent of R, P, S) are generated

* The program generates a random move based on the choices in the set 

* The inputs are compared, using program flow, with the stored data

* Finally output the result

**Yadav, Anil (Coppin State University)**